#!/usr/bin/env python3
"""
Generate downloads.yml for Jekyll from available configurations
"""

import os
import sys

def generate_downloads_yaml(boat, config_dir, output_path):
    """Generate YAML file listing available configurations"""
    
    # Get all configuration files
    configs = []
    
    for f in os.listdir(config_dir):
        if f.endswith('.py') and f != 'default.py' and not f.startswith('__'):
            config_name = f.replace('.py', '')
            configs.append(config_name)
    
    # Sort configs
    configs.sort()
    
    # Generate YAML
    yaml_lines = [
        f"# Auto-generated download links for {boat}",
        f"boat: {boat}",
        "configurations:"
    ]
    
    for config in configs:
        yaml_lines.append(f"  - name: {config}")
        yaml_lines.append(f"    filename: SolarProa_{boat}_{config}.FCStd")
        # Add friendly description
        descriptions = {
            'Beaching': 'Rigging stowed, solar deployed',
            'BeamReach': 'Crosswind, optimal speed',
            'BroadReach': 'Downwind angle',
            'CloseHaul': 'Upwind sailing, tight angle',
            'CloseHaulReefed': 'Reduced sail in strong winds',
            'GooseWing': 'Running downwind'
        }
        if config in descriptions:
            yaml_lines.append(f"    description: {descriptions[config]}")
    
    # Write file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write('\n'.join(yaml_lines))
    
    print(f"✓ Generated {output_path} ({len(configs)} configurations)")

if __name__ == "__main__":
    # Determine script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(script_dir, 'configurations')
    
    # Check if config directory exists
    if not os.path.exists(config_dir):
        print(f"ERROR: Configuration directory not found: {config_dir}")
        sys.exit(1)
    
    # Generate for all boats
    boats = ['RP1', 'RP2', 'RP3']
    
    for boat in boats:
        output = os.path.join(script_dir, '..', 'docs', '_data', f'{boat.lower()}_downloads.yml')
        generate_downloads_yaml(boat, config_dir, output)
    
    print("All downloads YAML files generated!")
