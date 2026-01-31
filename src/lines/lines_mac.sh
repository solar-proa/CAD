#!/bin/bash
# Lines plan generation wrapper for macOS
# Usage: lines_mac.sh <design.FCStd> <parameter.json> <output_dir> <freecad_app>

DESIGN_FILE="$1"
PARAMETER_FILE="$2"
OUTPUT_DIR="$3"
FREECAD_APP="$4"

if [ -z "$DESIGN_FILE" ] || [ -z "$PARAMETER_FILE" ] || [ -z "$OUTPUT_DIR" ] || [ -z "$FREECAD_APP" ]; then
    echo "Usage: lines_mac.sh <design.FCStd> <parameter.json> <output_dir> <freecad_app>"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
# FREECAD_APP is /Applications/FreeCAD.app/Contents/MacOS/FreeCAD
# We need /Applications/FreeCAD.app
FREECAD_BUNDLE="$(dirname "$(dirname "$(dirname "$FREECAD_APP")")")"
FREECAD_PYTHON="$FREECAD_BUNDLE/Contents/Resources/bin/python"

echo "Lines plan generation (macOS)"
echo "  Design: $DESIGN_FILE"
echo "  Parameters: $PARAMETER_FILE"
echo "  Output: $OUTPUT_DIR"
echo "  FreeCAD: $FREECAD_APP"

# Set environment for FreeCAD Python
export PYTHONPATH="$FREECAD_BUNDLE/Contents/Resources/lib:$FREECAD_BUNDLE/Contents/Resources/Mod:$REPO_ROOT"
export DYLD_LIBRARY_PATH="$FREECAD_BUNDLE/Contents/Frameworks:$FREECAD_BUNDLE/Contents/Resources/lib"

# Set environment variables for the script
export DESIGN_FILE
export PARAMETER_FILE
export OUTPUT_DIR

# Run the lines plan script
"$FREECAD_PYTHON" -m src.lines

exit $?
