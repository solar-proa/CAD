#!/usr/bin/env python3
"""
Electrical simulation for solar proa power system.

Supports multiple simulation types:
  operating_point  - Single operating point analysis
  sweep_throttle   - Sweep throttle from 0-100%
  sweep_panel_power - Sweep panel power from 100-0%
  voyage           - Multi-segment voyage simulation
"""

import argparse
import json

from .cable_sizing import parse_current_to_sizing

from .circuit_constructor import build_circuit_from_json
from .pyspice_simulator import begin_simulation
from .result_saver import save_to_file
from .simulation_over_time import start_voyage
from .simulation_sweeper import sweep_panel_power, sweep_throttle

def check_ngspice():
    try:
        from PySpice.Spice.NgSpice.Shared import NgSpiceShared
        NgSpiceShared.new_instance()
        
        print("NgSpice is available.")
        return True
    except Exception as e:
        print(f"NgSpice initialization failed: {e}")
        print("Follow steps indicated in wiki to install NgSpice.")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Run electrical simulation for solar proa power system')
    parser.add_argument('--circuit', required=True,
                        help='Path to circuit setup JSON (e.g. constant/electrical/circuit_setup.json)')
    parser.add_argument('--constants', required=True,
                        help='Path to constants JSON (e.g. constant/electrical/constants.json)')
    parser.add_argument('--components', required=True,
                        help='Path to components JSON (e.g. constant/electrical/components.json)')
    parser.add_argument('--boat', required=True,
                        help='Boat name to select circuit configuration (e.g. rp1)')
    parser.add_argument('--boat-params', default=None,
                        help='Path to boat parameters JSON (e.g. constant/boat/rp2.json)')
    parser.add_argument('--voyage', default=None,
                        help='Path to voyage setup JSON (required for voyage simulation type)')
    parser.add_argument('--output', required=True,
                        help='Path to output artifact directory or file')
    parser.add_argument('--simulation-type', required=True,
                        choices=['operating_point', 'cable_sizing', 'sweep_throttle', 'sweep_panel_power', 'voyage', 'all'],
                        help='Type of simulation to run')
    parser.add_argument('--verbose', action='store_true',
                        help='Enable simulation logging')
    parser.add_argument('--show-plot', action='store_true',
                        help='Display plots interactively')
    parser.add_argument('--propeller-load-factor', type=float, default=None,
                        help='Propeller load factor (0-1). 1.0=startup/bollard, 0.3-0.6=cruise. Overrides config value.')

    args = parser.parse_args()

    # Load constants from JSON
    constants = json.load(open(args.constants))
    components = json.load(open(args.components))
    circuit_setup = json.load(open(args.circuit))
    combine_config_setup(circuit_setup, components)
    if args.boat_params:
        boat_params = json.load(open(args.boat_params))
        apply_boat_panel_config(circuit_setup, boat_params)
    ngspice_available = check_ngspice()

    output_dir = args.output

    if args.simulation_type == 'all':
        run_operating_point_simulation(args, circuit_setup, ngspice_available, output_dir, constants)
        #run_max_operating_point_simulation(args, circuit_setup, ngspice_available, output_dir, constants)
        run_sweep_throttle(args, circuit_setup, ngspice_available, output_dir, constants)
        run_sweep_panel_power(args, circuit_setup, ngspice_available, output_dir, constants)
        run_voyage_simulation(args, circuit_setup, ngspice_available, output_dir, constants)

    elif args.simulation_type == 'operating_point':
        run_operating_point_simulation(args, circuit_setup, ngspice_available, output_dir, constants)

    elif args.simulation_type == 'cable_sizing':
        result = run_max_operating_point_simulation(args, circuit_setup, ngspice_available, output_dir, constants)
        parse_current_to_sizing(result)
        
    elif args.simulation_type == 'sweep_throttle':
        run_sweep_throttle(args, circuit_setup, ngspice_available, output_dir, constants)

    elif args.simulation_type == 'sweep_panel_power':
        run_sweep_panel_power(args, circuit_setup, ngspice_available, output_dir, constants)

    elif args.simulation_type == 'voyage':
        run_voyage_simulation(args, circuit_setup, ngspice_available, output_dir, constants)

def run_operating_point_simulation(args, circuit_setup, ngspice_available, output_dir, constants):
    modifications = {}
    result = run_operating_point(args, circuit_setup, ngspice_available, output_dir, constants, modifications)

    save_to_file(result, save_path=output_dir + ".operating_point.json", constants=constants)
    print(f"✓ Operating point simulation complete: {output_dir}.operating_point.json")

def run_max_operating_point_simulation(args, circuit_setup, ngspice_available, output_dir, constants):
    modifications={'propeller_load_factor': 1.0, 'throttle_setting': 1.0, 'panel_power_setting': 1.0}
    result = run_operating_point(args, circuit_setup, ngspice_available, output_dir, constants, modifications)

    save_to_file(result, save_path=output_dir + ".max_operating_point.json", constants=constants)
    print(f"✓ Maximum operating point simulation complete: {output_dir}.max_operating_point.json")
    return result

def run_operating_point(args, circuit_setup, ngspice_available, output_dir, constants, modifications = {}):
    if args.propeller_load_factor is not None:
        modifications['propeller_load_factor'] = args.propeller_load_factor
    circuit, component_object, errors = build_circuit_from_json(circuit_setup=circuit_setup, modifications=modifications, constants=constants)
    analysis, result = begin_simulation(
        circuit=circuit,
        component_object=component_object, 
        errors=errors,
        ngspice_available=ngspice_available,
        simulation_logging=args.verbose, show_errors=args.verbose,
        show_warnings=args.verbose,
        constants=constants)
    return result

def run_sweep_throttle(args, circuit_setup, ngspice_available, output_dir, constants):
    sweep_throttle(
        circuit_setup=circuit_setup,
        save_path=output_dir + ".sweep_throttle",
        ngspice_available=ngspice_available,
        simulation_logging=args.verbose,
        save_output=True,
        constants=constants,
        propeller_load_factor=args.propeller_load_factor) 
    print(f"✓ Sweep throttle simulation complete: {output_dir}.sweep_throttle")
    
def run_sweep_panel_power(args, circuit_setup, ngspice_available, output_dir, constants):
    sweep_panel_power(
        circuit_setup=circuit_setup,
        save_path=output_dir + ".sweep_panel_power",
        ngspice_available=ngspice_available,
        simulation_logging=args.verbose,
        save_output=True,
        constants=constants,
        propeller_load_factor=args.propeller_load_factor)
    print(f"✓ Sweep panel power simulation complete: {output_dir}.sweep_panel_power")

def run_voyage_simulation(args, circuit_setup, ngspice_available, output_dir, constants):
    start_voyage(
        circuit_setup=circuit_setup,
        voyage_config_loc=args.voyage,
        save_path=output_dir + ".voyage",
        ngspice_available=ngspice_available,
        constants=constants) 
    print(f"✓ Voyage simulation complete: {output_dir}.voyage")

def combine_config_setup(circuit_config, component_config):
    if circuit_config.get("mppt_panel") is not None:
        for key, config in circuit_config["mppt_panel"].items():
            panel_choice = config["panel_info"]["choice"]
            mppt_choice = config["mppt_info"]["choice"]
            config["panel_info"].update(component_config["Panel"][panel_choice])
            config["mppt_info"].update(component_config["MPPT"][mppt_choice])
            
    if circuit_config.get("load") is not None:
        for key, load in circuit_config["load"].items():
            load_choice = load["choice"]
            load.update(component_config["Load"][load_choice])
            
    if circuit_config.get("battery") is not None:
        battery_choice = circuit_config["battery"]["choice"]
        circuit_config["battery"].update(component_config["Battery"][battery_choice])

def apply_boat_panel_config(circuit_config, boat_params):
    """Update panel in_series and in_parallel from boat parameters."""
    print("Reading boat config file and circuit config file for panel arrangement...")
    
    panels_per_string = boat_params.get("panels_per_string")
    panels_longitudinal = boat_params.get("panels_longitudinal")
    panels_transversal = boat_params.get("panels_transversal")
    boat_has_panel_config = panels_per_string is not None and panels_longitudinal is not None and panels_transversal is not None
    if boat_has_panel_config:
        in_series = panels_per_string
        in_parallel = panels_longitudinal // panels_transversal
        
    mppt_panel = circuit_config.get("mppt_panel")
    panels_per_string
    for _, config in mppt_panel.items():
        panel_info = config.get("panel_info", {})
        if not panel_info.get("in_series") or not panel_info.get("in_parallel"):
            print("Using boat panel config for mppt_panel config")
            if len(mppt_panel) != 1:
                print("Cannot use boat panel config if there are different config for panel arrangement")
                return
            else:
                if panels_transversal != config.get('count'):
                    print(f"Warning: panels_transversal from boat config ({panels_transversal}) does not match panel count in circuit config ({config.get('count')}). \nUsing panels_per_string {in_series} and panels_longitudinal / panels_transversal {in_parallel} for config_count {config.get('count')} number of panel arrays instead.")
                panel_info["in_series"] = in_series
                panel_info["in_parallel"] = in_parallel
                break
        else:
            print("Panel arrangement already specified in circuit config, not using boat panel config.")
            if panel_info.get("in_series") != in_series or panel_info.get("in_parallel") != in_parallel:
                print(f"Warning: Boat panel config does not match circuit config for {__file__}. Boat config (in_series={in_series}, in_parallel={in_parallel}) vs circuit config (in_series={panel_info.get('in_series')}, in_parallel={panel_info.get('in_parallel')}). \nUsing circuit config values.")
     
if __name__ == "__main__":
    main()