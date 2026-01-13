# TODOs for this repo

- add targets/artifacts for buoyancy and stability
- generate_downloads_yaml.py needs refactoring: do not hardwire "rp1-3"
  generate_downloads_yaml.py should look at the generated files, not
  just the list of configurations
- add a parameter: akas_per_panel: the number of akas under each panel,
  currently 1, but with 2+ meter long panels arranged going in longitudinal
  direction, it makes sense to have 2 akas under each panel. That way,
  when we have 1 panel in longitudinal direction on each side, there would
  be 2 akas on each side, which will be better for the rudder mounting and
  overall design.

