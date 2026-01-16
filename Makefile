# Makefile-Based Staged Framework for Solar Proa
# Three-tier architecture:
# Boat + Configuration constants (JSON)
# → Parameters (Make + Python)
# → Design generation (Make + Python)

# ==============================================================================
# PLATFORM DETECTION AND FREECAD CONFIGURATION
# ==============================================================================

UNAME := $(shell uname)

# Detect FreeCAD command (different on different systems)
FREECAD_APP := /Applications/FreeCAD.app/Contents/MacOS/FreeCAD
FREECAD_BUNDLE := /Applications/FreeCAD.app
FREECAD := $(shell which freecad 2>/dev/null || \
                   which freecadcmd 2>/dev/null || \
                   (test -f $(FREECAD_APP) && echo $(FREECAD_APP)) || \
                   echo "freecad")

# On macOS use GUI app, on Linux use headless
ifeq ($(UNAME),Darwin)
	FREECAD_CMD := $(FREECAD_APP) --console
	FREECAD_PYTHON := $(FREECAD_BUNDLE)/Contents/Resources/bin/python
else
	FREECAD_CMD := xvfb-run -a freecadcmd
	FREECAD_PYTHON := freecad-python
endif

# ==============================================================================
# DIRECTORY STRUCTURE
# ==============================================================================

CONST_DIR := constants
BOATS_DIR := $(CONST_DIR)/boats
CONFIGURATIONS_DIR := $(CONST_DIR)/configurations
MATERIALS_DIR := $(CONST_DIR)/materials
SRC_DIR := src
ARTIFACTS_DIR := artifacts
DOCS_DATA_DIR := docs/_data

# Source directories
PARAMETERS_DIR := $(SRC_DIR)/parameters
DESIGN_DIR := $(SRC_DIR)/design
COLOR_DIR := $(SRC_DIR)/color
MASS_DIR := $(SRC_DIR)/mass
RENDER_DIR := $(SRC_DIR)/render
STEP_DIR := $(SRC_DIR)/step

# Source files (for dependency tracking)
PARAMETERS_SOURCES := $(wildcard $(PARAMETERS_DIR)/*.py)
DESIGN_SOURCES := $(wildcard $(DESIGN_DIR)/*.py)
COLOR_SOURCES := $(wildcard $(COLOR_DIR)/*.py)
MASS_SOURCES := $(wildcard $(MASS_DIR)/*.py)
RENDER_SOURCES := $(wildcard $(RENDER_DIR)/*.py)
STEP_SOURCES := $(wildcard $(STEP_DIR)/*.py) $(wildcard $(STEP_DIR)/*.sh)

# ==============================================================================
# AUTO-DISCOVERY: Find all boats and configurations
# ==============================================================================

BOATS := $(basename $(notdir $(wildcard $(BOATS_DIR)/*.json)))
CONFIGURATIONS := $(basename $(notdir $(wildcard $(CONFIGURATIONS_DIR)/*.json)))

# Filter out any backup or temp files
BOATS := $(filter-out %~,$(BOATS))
CONFIGURATIONS := $(filter-out %~,$(CONFIGURATIONS))

# ==============================================================================
# DEFAULTS AND VARIABLES
# ==============================================================================

# Default boat and configuration (can be overridden: make design BOAT=rp2 CONFIGURATION=closehaul)
BOAT ?= rp2
CONFIGURATION ?= closehaul
MATERIALS ?= proa

# Computed file paths using dot-separated naming convention
BOAT_FILE := $(BOATS_DIR)/$(BOAT).json
CONFIGURATION_FILE := $(CONFIGURATIONS_DIR)/$(CONFIGURATION).json
MATERIALS_FILE := $(MATERIALS_DIR)/$(MATERIALS).json

# Artifact paths
PARAMETERS_ARTIFACT := $(ARTIFACTS_DIR)/$(BOAT).$(CONFIGURATION).parameters.json
DESIGN_ARTIFACT := $(ARTIFACTS_DIR)/$(BOAT).$(CONFIGURATION).design.FCStd
COLOR_ARTIFACT := $(ARTIFACTS_DIR)/$(BOAT).$(CONFIGURATION).color.FCStd
MASS_ARTIFACT := $(ARTIFACTS_DIR)/$(BOAT).$(CONFIGURATION).mass.json
STEP_ARTIFACT := $(ARTIFACTS_DIR)/$(BOAT).$(CONFIGURATION).step.step
JEKYLL_DATA := $(DOCS_DATA_DIR)/$(BOAT).$(CONFIGURATION).json

# ==============================================================================
# PHONY TARGETS
# ==============================================================================

.PHONY: all help clean check jekyll 

# ==============================================================================
# MAIN TARGETS
# ==============================================================================

all: required-all

help:
	@echo "Solar Proa Makefile-Based Staged Framework"
	@echo ""
	@echo "Platform: $(UNAME)"
	@echo "Discovered boats: $(BOATS)"
	@echo "Discovered configurations: $(CONFIGURATIONS)"
	@echo ""
	@echo "Main Targets:"
	@echo "  make                        - Same as 'make all' and 'make required-all'"
	@echo "  make required-all           - Run all required stages for all boats and configurations"
	@echo "                                Required stages are specified in constants/configurations"
	@echo "  make design                 - Generate single design (BOAT=$(BOAT) CONFIGURATION=$(CONFIGURATION))"
	@echo "  make color                  - Apply color scheme to design (MATERIALS=$(MATERIALS))"
	@echo "  make step                   - Export design to STEP format (geometry only)"
	@echo "  make render                 - Render images (applies colors then renders)"
	@echo ""
	@echo "Parameter Targets:"
	@echo "  make parameters             - Compute and save parameters to artifacts/"
	@echo ""
	@echo "Utility Targets:"
	@echo "  make clean                  - Remove all generated files"
	@echo "  make check                  - Check FreeCAD installation"
	@echo "  make help                   - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make parameters BOAT=rp1"
	@echo "  make design BOAT=rp2 CONFIGURATION=closehaul"
	@echo "  make color BOAT=rp3 CONFIGURATION=closehaul MATERIALS=proa"
	@echo "  make render BOAT=rp2 CONFIGURATION=closehaul"
	@echo ""
	@echo "FreeCAD: $(FREECAD)"

# ==============================================================================
# PARAMETER COMPUTATION
# ==============================================================================

# Compute and save parameters to artifacts directory
$(PARAMETERS_ARTIFACT): $(BOAT_FILE) $(CONFIGURATION_FILE) $(PARAMETERS_SOURCES)
	@echo "Computing parameters for $(BOAT) and $(CONFIGURATION)..."
	@mkdir -p $(ARTIFACTS_DIR)
	@python3 $(PARAMETERS_DIR)/parameters.py \
		--boat $(BOAT_FILE) \
		--configuration $(CONFIGURATION_FILE) \
		--output $@
	@echo "✓ Computed parameters saved to $@"

parameters: $(PARAMETERS_ARTIFACT)

# ==============================================================================
# DESIGN GENERATION
# ==============================================================================

# Create output directories
$(ARTIFACTS_DIR) $(DOCS_DATA_DIR):
	@mkdir -p $@

# Generate a single design
$(DESIGN_ARTIFACT): $(PARAMETERS_ARTIFACT) $(DESIGN_SOURCES) | $(DESIGN_DIR)
	@echo "Generating design: $(BOAT).$(CONFIGURATION)"
	@echo "  Parameters: $(PARAMETERS_ARTIFACT)"
	@$(FREECAD_CMD) $(DESIGN_DIR)/design.py $(PARAMETERS_ARTIFACT) $(DESIGN_ARTIFACT) || true
	@if [ -f "$(DESIGN_ARTIFACT)" ]; then \
		echo "✓ Design complete: $(DESIGN_ARTIFACT)"; \
		if [ "$(UNAME)" = "Darwin" ]; then \
			echo "Fixing visibility on macOS..."; \
			bash $(DESIGN_DIR)/fix_visibility.sh "$(DESIGN_ARTIFACT)" "$(FREECAD_APP)"; \
		fi; \
	else \
		echo "ERROR: Design failed - no design file created"; \
		exit 1; \
	fi

design: $(DESIGN_ARTIFACT)

# Apply color scheme to design
$(COLOR_ARTIFACT): $(DESIGN_ARTIFACT) $(MATERIALS_FILE) $(COLOR_SOURCES) | $(COLOR_DIR)
	@echo "Applying color scheme '$(MATERIALS)' to $(BOAT).$(CONFIGURATION)..."
	@if [ ! -f "$(MATERIALS_FILE)" ]; then \
		echo "ERROR: Color scheme not found: $(MATERIALS_FILE)"; \
		echo "Available schemes: $(notdir $(wildcard $(MATERIALS_DIR)/*.json))"; \
		exit 1; \
	fi
	@if [ "$(UNAME)" = "Darwin" ]; then \
		bash $(COLOR_DIR)/color_mac.sh \
			"$(DESIGN_ARTIFACT)" \
			"$(MATERIALS_FILE)" \
			"$(COLOR_ARTIFACT)" \
			"$(FREECAD_APP)"; \
	else \
		freecad-python $(COLOR_DIR)/color.py \
			--design "$(DESIGN_ARTIFACT)" \
			--color "$(MATERIALS_FILE)" \
			--outputdesign "$(COLOR_ARTIFACT)"; \
	fi
	@echo "✓ Colored design: $(COLOR_ARTIFACT)"

# Convenience target: apply colors to a single design
.PHONY: color
color: $(COLOR_ARTIFACT)
	@echo "✓ Color scheme '$(MATERIALS)' applied to $(BOAT).$(CONFIGURATION)"

# Mass analysis (depends on design, not colors - mass is geometry-based)
$(MASS_ARTIFACT): $(DESIGN_ARTIFACT) $(MATERIALS_FILE) $(MASS_SOURCES) | $(ARTIFACTS_DIR)
	@echo "Running mass analysis: $(BOAT).$(CONFIGURATION)"
	@if [ "$(UNAME)" = "Darwin" ]; then \
		PYTHONPATH=$(FREECAD_BUNDLE)/Contents/Resources/lib:$(FREECAD_BUNDLE)/Contents/Resources/Mod:$(PWD) \
		DYLD_LIBRARY_PATH=$(FREECAD_BUNDLE)/Contents/Frameworks:$(FREECAD_BUNDLE)/Contents/Resources/lib \
		$(FREECAD_PYTHON) $(MASS_DIR)/mass.py --design $(DESIGN_ARTIFACT) --materials $(MATERIALS_FILE) --output $@; \
	else \
		PYTHONPATH=$(PWD):$(PWD)/src/design $(FREECAD_PYTHON) $(MASS_DIR)/mass.py --design $(DESIGN_ARTIFACT) --materials $(MATERIALS_FILE) --output $@; \
	fi

# Convenience target: apply mass to a single design
.PHONY: mass
mass: $(MASS_ARTIFACT)
	@echo "✓ mass calculation applied to $(BOAT).$(CONFIGURATION)"

# Render images from colored FCStd file
.PHONY: render
render: $(COLOR_ARTIFACT) $(RENDER_SOURCES)
	@echo "Rendering images from $(COLOR_ARTIFACT)..."
	@if [ "$(UNAME)" = "Darwin" ]; then \
		$(RENDER_DIR)/render_mac.sh "$(COLOR_ARTIFACT)" "$(ARTIFACTS_DIR)" "$(FREECAD_APP)"; \
	else \
		FCSTD_FILE="$(COLOR_ARTIFACT)" IMAGE_DIR="$(ARTIFACTS_DIR)" freecad-python $(RENDER_DIR)/render_linux.py; \
	fi
	@echo "Cropping images with ImageMagick..."
	@if command -v convert >/dev/null 2>&1; then \
		for img in $(ARTIFACTS_DIR)/*.png; do \
			if [ -f "$$img" ]; then \
				convert "$$img" -fuzz 1% -trim +repage -bordercolor \#C6D2FF -border 25 "$$img" || true; \
			fi \
		done; \
		echo "Cropping complete!"; \
	else \
		echo "ImageMagick not found, skipping crop"; \
	fi
	@echo "Render complete!"

# Export to STEP format (geometry only, no colors)
$(STEP_ARTIFACT): $(DESIGN_ARTIFACT) $(STEP_SOURCES) | $(ARTIFACTS_DIR)
	@echo "Exporting STEP: $(BOAT).$(CONFIGURATION)"
	@if [ "$(UNAME)" = "Darwin" ]; then \
		bash $(STEP_DIR)/step_mac.sh \
			"$(DESIGN_ARTIFACT)" \
			"$(STEP_ARTIFACT)" \
			"$(FREECAD_APP)"; \
	else \
		$(FREECAD_PYTHON) $(STEP_DIR)/step.py \
			--input "$(DESIGN_ARTIFACT)" \
			--output "$(STEP_ARTIFACT)"; \
	fi
	@echo "✓ STEP export: $(STEP_ARTIFACT)"

# Convenience target: export single design to STEP
.PHONY: step
step: $(STEP_ARTIFACT)
	@echo "✓ STEP export complete for $(BOAT).$(CONFIGURATION)"

# "Required" target: look in the appropriate configuration file what stages need to run and run them
.PHONY: required
required:
	@echo "Running required stages for $(BOAT).$(CONFIGURATION)..."
	@required_stages=$$(python3 -c "import json; config = json.load(open('$(CONFIGURATION_FILE)')); print(' '.join(config.get('required', [])))"); \
	for stage in $$required_stages; do \
		echo "Running stage: $$stage"; \
		$(MAKE) $$stage BOAT=$(BOAT) CONFIGURATION=$(CONFIGURATION) MATERIALS=$(MATERIALS) || true; \
	done; \
	echo "✓ Required stages complete for $(BOAT).$(CONFIGURATION)"

# Apply "required" stages to all designs
.PHONY: required-all
required-all:
	@echo "run required stages..."
	@for boat in $(BOATS); do \
		for configuration in $(CONFIGURATIONS); do \
			echo ""; \
			$(MAKE) required BOAT=$$boat CONFIGURATION=$$configuration || true; \
		done \
	done
	@echo ""
	@echo "✓ All required stages complete!"

# ==============================================================================
# MISCELLANEOUS
# ==============================================================================

clean:
	@echo "Cleaning generated files..."
	@rm -rf $(ARTIFACTS_DIR)
	@rm -rf $(DOCS_DATA_DIR)
	@echo "Removing backup files..."
	@find . -name '*~' -delete
	@echo "Removing Python cache..."
	@find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
	@find . -name '*.pyc' -delete
	@find . -name '*.pyo' -delete
	@echo "✓ Clean complete!"

check:
	@echo "Checking for FreeCAD..."
	@$(FREECAD) --version || (echo "FreeCAD not found!" && exit 1)
	@echo "✓ FreeCAD found: $(FREECAD)"
	@echo ""
	@echo "Checking Python..."
	@python3 --version
	@echo ""
	@echo "Discovered boats: $(BOATS)"
	@echo "Discovered configurations: $(CONFIGURATIONS)"
	@echo ""
	@echo "System ready!"

# Serve website locally
.PHONY: localhost
localhost:
	@echo "Serving website in localhost..."
	cd docs; bundle exec jekyll serve

# Make zip file with just the newest versions of the git files
.PHONY: zip
zip:	clean
	@echo "Make zip file with current working directory"
	@rm -f ../CAD-clean.zip
	git ls-files | zip -@ ../CAD-clean.zip
