#!/usr/bin/env python3
"""
Export FreeCAD model to DXF format.
DXF (Drawing Exchange Format) is Autodesk's CAD data file format,
widely supported for 2D drawings and 3D wireframes.
"""

import sys
import os
import argparse

# FreeCAD imports
import FreeCAD
import Part
import importDXF

def export_to_dxf(input_path: str, output_path: str) -> None:
    """
    Export all visible solid shapes from a FreeCAD document to DXF format.

    Args:
        input_path: Path to input .FCStd file
        output_path: Path to output .dxf file
    """
    print(f"Loading FreeCAD document: {input_path}")
    doc = FreeCAD.open(input_path)

    # Collect all shapes to export
    shapes_to_export = []

    for obj in doc.Objects:
        # Skip objects without shapes
        if not hasattr(obj, 'Shape'):
            continue

        # Skip invisible objects
        if hasattr(obj, 'Visibility') and not obj.Visibility:
            continue

        # Skip empty shapes
        if obj.Shape.isNull():
            continue

        shapes_to_export.append(obj)

    print(f"Found {len(shapes_to_export)} objects to export")

    if not shapes_to_export:
        print("Warning: No shapes found to export")
        return

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)

    # Export to DXF
    print(f"Exporting to DXF: {output_path}")
    importDXF.export(shapes_to_export, output_path)

    print(f"DXF export complete: {output_path}")

    FreeCAD.closeDocument(doc.Name)

def main():
    parser = argparse.ArgumentParser(description='Export FreeCAD model to DXF format')
    parser.add_argument('--input', required=True, help='Input FreeCAD file (.FCStd)')
    parser.add_argument('--output', required=True, help='Output DXF file (.dxf)')

    args = parser.parse_args()

    export_to_dxf(args.input, args.output)
    print("Done!")

if __name__ == "__main__":
    main()
