#!/bin/bash
# Export FreeCAD design to STEP format (macOS)
#
# STEP (Standard for the Exchange of Product Data) is an ISO standard
# for CAD data exchange, widely supported by CAD software.

if [ $# -lt 3 ]; then
    echo "Usage: $0 <input.FCStd> <output.step> [freecad_path]"
    exit 1
fi

INPUT_FCSTD="$1"
OUTPUT_STEP="$2"
FREECAD="${3:-/Applications/FreeCAD.app/Contents/MacOS/FreeCAD}"

if [ ! -f "$INPUT_FCSTD" ]; then
    echo "ERROR: Input file not found: $INPUT_FCSTD"
    exit 1
fi

# Create temporary Python script
TEMP_SCRIPT=$(mktemp /tmp/freecad_step_XXXXXX.py)

cat > "$TEMP_SCRIPT" << 'EOFPYTHON'
import FreeCAD
import FreeCADGui
import sys
import os
import Import

# Get arguments
input_fcstd = sys.argv[-2]
output_step = sys.argv[-1]

print(f"Loading FreeCAD document: {input_fcstd}")
doc = FreeCAD.openDocument(input_fcstd)

# Collect all shapes to export
shapes_to_export = []

def collect_shapes(obj_list):
    """Recursively collect all objects with shapes"""
    for obj in obj_list:
        # Skip objects without shapes
        if not hasattr(obj, 'Shape'):
            continue

        # Skip empty shapes
        if obj.Shape.isNull():
            continue

        shapes_to_export.append(obj)

        # Recurse into groups
        if hasattr(obj, 'Group'):
            collect_shapes(obj.Group)

collect_shapes(doc.Objects)

print(f"Found {len(shapes_to_export)} objects to export")

if shapes_to_export:
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_step) or '.', exist_ok=True)

    # Export to STEP
    print(f"Exporting to STEP: {output_step}")
    Import.export(shapes_to_export, output_step)
    print(f"STEP export complete!")
else:
    print("Warning: No shapes found to export")

# Close and quit
FreeCAD.closeDocument(doc.Name)
os._exit(0)
EOFPYTHON

# Run FreeCAD with the script
echo "Running FreeCAD to export STEP..."
"$FREECAD" "$TEMP_SCRIPT" "$INPUT_FCSTD" "$OUTPUT_STEP" &
FREECAD_PID=$!

# Wait up to 60 seconds for completion
for i in {1..120}; do
    if ! kill -0 $FREECAD_PID 2>/dev/null; then
        break
    fi
    sleep 0.5
done

# Force kill if still running
if kill -0 $FREECAD_PID 2>/dev/null; then
    echo "Warning: FreeCAD did not exit cleanly, forcing..."
    kill -9 $FREECAD_PID 2>/dev/null
fi

# Clean up
rm -f "$TEMP_SCRIPT"

# Verify output was created
if [ ! -f "$OUTPUT_STEP" ]; then
    echo "ERROR: STEP file was not created"
    exit 1
fi

echo "STEP export complete: $OUTPUT_STEP"
