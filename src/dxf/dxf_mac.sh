#!/bin/bash
# Export FreeCAD design to DXF format (macOS)
#
# DXF (Drawing Exchange Format) is Autodesk's CAD data file format,
# widely supported for 2D drawings and 3D wireframes.

if [ $# -lt 3 ]; then
    echo "Usage: $0 <input.FCStd> <output.dxf> [freecad_path]"
    exit 1
fi

INPUT_FCSTD="$1"
OUTPUT_DXF="$2"
FREECAD="${3:-/Applications/FreeCAD.app/Contents/MacOS/FreeCAD}"

if [ ! -f "$INPUT_FCSTD" ]; then
    echo "ERROR: Input file not found: $INPUT_FCSTD"
    exit 1
fi

# Create temporary Python script
TEMP_SCRIPT=$(mktemp /tmp/freecad_dxf_XXXXXX.py)

cat > "$TEMP_SCRIPT" << 'EOFPYTHON'
import FreeCAD
import FreeCADGui
import sys
import os
import importDXF

# Get arguments
input_fcstd = sys.argv[-2]
output_dxf = sys.argv[-1]

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
    os.makedirs(os.path.dirname(output_dxf) or '.', exist_ok=True)

    # Export to DXF
    print(f"Exporting to DXF: {output_dxf}")
    importDXF.export(shapes_to_export, output_dxf)
    print(f"DXF export complete!")
else:
    print("Warning: No shapes found to export")

# Close and quit
FreeCAD.closeDocument(doc.Name)
os._exit(0)
EOFPYTHON

# Run FreeCAD with the script
echo "Running FreeCAD to export DXF..."
"$FREECAD" "$TEMP_SCRIPT" "$INPUT_FCSTD" "$OUTPUT_DXF" &
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
if [ ! -f "$OUTPUT_DXF" ]; then
    echo "ERROR: DXF file was not created"
    exit 1
fi

echo "DXF export complete: $OUTPUT_DXF"
