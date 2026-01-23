#!/usr/bin/env python3
"""
Generate configurations.yml for Jekyll from configuration JSON files.
Auto-discovers all configurations and extracts display names and descriptions.
"""

import os
import sys
import json
import glob


def main():
    # Determine paths relative to repository root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.join(script_dir, '..')
    config_dir = os.path.join(repo_root, 'constant', 'configuration')
    output_path = os.path.join(repo_root, 'docs', '_data', 'configurations.yml')

    if not os.path.exists(config_dir):
        print(f"ERROR: Configuration directory not found: {config_dir}")
        sys.exit(1)

    # Read all configuration files
    configs = []
    for config_file in sorted(glob.glob(os.path.join(config_dir, '*.json'))):
        if os.path.basename(config_file).startswith('_'):
            continue

        with open(config_file) as f:
            data = json.load(f)
            configs.append({
                'name': data.get('configuration_name', os.path.basename(config_file).replace('.json', '')),
                'display_name': data.get('display_name', data.get('configuration_name', '')),
                'display_name_id': data.get('display_name_id', data.get('display_name', '')),
                'description': data.get('configuration_description', ''),
                'description_id': data.get('configuration_description_id', data.get('configuration_description', ''))
            })

    if not configs:
        print("ERROR: No configurations found")
        sys.exit(1)

    # Generate YAML
    yaml_lines = [
        "# Auto-generated from constant/configuration/*.json",
        "# Do not edit manually - run: python3 docs/generate_configurations_yaml.py",
        ""
    ]

    for config in configs:
        yaml_lines.append(f"- name: {config['name']}")
        yaml_lines.append(f"  display_name: \"{config['display_name']}\"")
        yaml_lines.append(f"  display_name_id: \"{config['display_name_id']}\"")
        yaml_lines.append(f"  description: \"{config['description']}\"")
        yaml_lines.append(f"  description_id: \"{config['description_id']}\"")
        yaml_lines.append("")

    # Write file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write('\n'.join(yaml_lines))

    print(f"✓ Generated {output_path} ({len(configs)} configurations)")


if __name__ == '__main__':
    main()
