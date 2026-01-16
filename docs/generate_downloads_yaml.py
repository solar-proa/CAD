#!/usr/bin/env python3
"""
Generate downloads.yml for Jekyll from available color artifacts
"""

import os
import sys
import json
import glob

def discover_boats(boats_dir):
    """Auto-discover boats from constants/boats/*.json"""
    boats = []
    for boat_file in glob.glob(os.path.join(boats_dir, '*.json')):
        if not os.path.basename(boat_file).startswith('_'):
            with open(boat_file) as f:
                boat_data = json.load(f)
                boat_name = boat_data.get('boat_name')
                if boat_name:
                    boats.append(boat_name)
    return sorted(boats)

def get_configuration_description(config_dir, config_name):
    """Read configuration description from JSON file"""
    config_file = os.path.join(config_dir, f'{config_name}.json')
    if os.path.exists(config_file):
        with open(config_file) as f:
            config_data = json.load(f)
            return config_data.get('configuration_description', '')
    return ''

def generate_downloads_yaml(boat, config_dir, artifacts_dir, output_path):
    """Generate YAML file listing available configurations for this boat"""

    # Find all .color.FCStd files for this boat in artifacts/
    pattern = os.path.join(artifacts_dir, f'{boat}.*.color.FCStd')
    color_files = glob.glob(pattern)

    if not color_files:
        print(f"⚠ No color artifacts found for {boat} (searched: {pattern})")
        return

    # Extract configuration names from filenames
    configs = []
    for color_file in color_files:
        basename = os.path.basename(color_file)
        # Parse: boat.config.color.FCStd
        parts = basename.replace('.color.FCStd', '').split('.')
        if len(parts) >= 2 and parts[0] == boat:
            config_name = parts[1]
            description = get_configuration_description(config_dir, config_name)

            # Check if STEP file exists
            step_filename = f'{boat}.{config_name}.step.step'
            step_path = os.path.join(artifacts_dir, step_filename)
            has_step = os.path.exists(step_path)

            configs.append({
                'name': config_name,
                'filename': f'{boat}.{config_name}.color.FCStd',
                'step_filename': step_filename if has_step else None,
                'description': description
            })

    # Sort configs by name
    configs.sort(key=lambda x: x['name'])

    # Generate YAML
    yaml_lines = [
        f"# Auto-generated download links for {boat}",
        f"boat: {boat}",
        "configurations:"
    ]

    for config in configs:
        yaml_lines.append(f"  - name: {config['name']}")
        yaml_lines.append(f"    filename: {config['filename']}")
        if config['step_filename']:
            yaml_lines.append(f"    step_filename: {config['step_filename']}")
        if config['description']:
            yaml_lines.append(f"    description: {config['description']}")

    # Write file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write('\n'.join(yaml_lines))

    print(f"✓ Generated {output_path} ({len(configs)} configurations)")

if __name__ == "__main__":
    # Determine paths relative to repository root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.join(script_dir, '..')
    boats_dir = os.path.join(repo_root, 'constants', 'boats')
    config_dir = os.path.join(repo_root, 'constants', 'configurations')
    artifacts_dir = os.path.join(repo_root, 'artifacts')

    # Check if directories exist
    if not os.path.exists(boats_dir):
        print(f"ERROR: Boats directory not found: {boats_dir}")
        sys.exit(1)

    if not os.path.exists(config_dir):
        print(f"ERROR: Configuration directory not found: {config_dir}")
        sys.exit(1)

    if not os.path.exists(artifacts_dir):
        print(f"WARNING: Artifacts directory not found: {artifacts_dir}")
        print("Run 'make required-all' to generate artifacts first")
        sys.exit(0)

    # Auto-discover boats
    boats = discover_boats(boats_dir)
    if not boats:
        print("ERROR: No boats found in constants/boats/")
        sys.exit(1)

    print(f"Discovered boats: {', '.join(boats)}")

    # Generate downloads YAML for each boat
    for boat in boats:
        output = os.path.join(repo_root, 'docs', '_data', f'{boat}_downloads.yml')
        generate_downloads_yaml(boat, config_dir, artifacts_dir, output)

    print("✓ All downloads YAML files generated!")
