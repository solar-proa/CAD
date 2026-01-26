import Part
import FreeCAD
from FreeCAD import Base


#TODO: Avoid using object names ("panel"), calculate placements directly from parameters

def create_sweep(group, profile, radius, vertices, name="SweepObject"):
    """Creates a swept solid given a profile (cross section) and list of vertices representing the bends""" 
    edges: list[tuple[Part.Edge, str]] = []
    for i in range(len(vertices) - 1):
        start = vertices[i]
        end = vertices[i+1]
        line = Part.makeLine(start, end)
        edges.append((line, f"Edge_{i+1}"))
        print(f"Created edge {i} from {start} to {end}")

    path_obj = group.addObject("Part::Feature", f"{name}Path")
    path_obj.Shape = Part.Wire([edge[0] for edge in edges])

    if profile.lower() == "circle":
        # creating a profile for every sweep is inefficient, add functionality for reusing profile?
        direction = edges[0][0].tangentAt(0)
        # print(f"Sweep direction: {direction}")
        profile_shape = Part.makeCircle(radius, edges[0][0].valueAt(0), direction)
        profile_obj = group.addObject("Part::Feature", f"{name}Profile")
        profile_obj.Shape = Part.Wire(profile_shape)
        # print(f"Created circular profile with radius {radius}")
    
    else:
        raise ValueError(f"Profile type '{profile}' is not supported.")

    sweep = group.addObject("Part::Sweep", name)
    sweep.Sections = [profile_obj]
    sweep.Spine = (path_obj, [edge[1] for edge in edges])
    sweep.Solid = True
    sweep.Frenet = True
    sweep.Transition = 'Round corner'

    return sweep

def wire_solar_panels(group, radius=5, transverse_offset=10, central_extension=10, params={}):
    """
    Extracts all solar panels from the group and draws a wire sweep along their length.
    
    Args:
        group: The FreeCAD Document or Group object containing the panels.
        radius: Radius of the wire sweep.
        transverse_offset: Offset factor for colinear wires.
    """
    panels = []
    
    # Handle both Document and Group objects
    objects = group.Group if hasattr(group, "Group") else group.Objects
    
    for obj in objects:
        # Assume that all solar panels have 'solar' in their label
        # Check for 'solar' in label (ignoring case)
        # Using getattr for safety, defaulting to Name if Label not present/empty
        label = getattr(obj, "Label", getattr(obj, "Name", ""))
        if "solar" in label.lower():
            panels.append(obj)
            
    print(f"Found {len(panels)} solar panels to wire.")

    # Group panels by their approximate Y-center to handle colinear placements
    y_groups = {}
    for panel in panels:
        bbox = panel.Shape.BoundBox
        mid_y = (bbox.YMin + bbox.YMax) / 2
        # Round to avoid floating point precision issues when grouping
        key = round(mid_y, 4)
        if key not in y_groups:
            y_groups[key] = []
        y_groups[key].append(panel)
    
    print(f"groups {y_groups.items()}")

    # Compute z-level of panels
    panel_z = params['panel_base_level'] + params['panel_height']

    # Compute where the connecting wire should be
    connecting_wire_z = params['deck_base_level'] / 2

    for group_y, group_panels in y_groups.items():
        # Sort by X to ensure consistent ordering
        group_panels.sort(key=lambda p: p.Shape.BoundBox.XMin)

        # Get the x position of the end of the wire, should be the same for each transverse panel group
        panel_end_x = max(p.Shape.BoundBox.XMax for p in group_panels)
        connecting_wire_x = panel_end_x + params['deck_width'] / 3

        for i, panel in enumerate(group_panels):
            # Get global bounding box of the panel
            # panel.Shape returns the shape with Placement applied (global coords)
            bbox = panel.Shape.BoundBox
            
            # Calculate start and end points for the wire
            # Running along the length (X-axis), centered on Width (Y-axis), on Top (Z-axis)
            
            mid_y = group_y
            # top_z = bbox.ZMax
            
            # Apply offset to prevent colinear wires within the group
            offset = i * (radius * transverse_offset)
            wire_y = mid_y + offset
            
            # Start at min X, End at central hull
            start_point = Base.Vector(bbox.XMin, wire_y, panel_z)
            end_point = Base.Vector(panel_end_x, wire_y, panel_z)

            # Assuming deck level param is the top of the hull, go a third into the deck width
            connecting_wire_point = Base.Vector(connecting_wire_x, wire_y, connecting_wire_z)
            
            primary_wire_name = f"{panel.Name}_Wire"
            
            try:
                create_sweep(group, "circle", radius, [start_point, end_point, connecting_wire_point], name=primary_wire_name)
            except Exception as e:
                print(f"Failed to wire panel {panel.Name}: {e}")

    # Add Central Connecting Wire

    min_y, max_y = min(y_groups.keys()), max(y_groups.keys())
    central_start_point = Base.Vector(connecting_wire_x, min_y - central_extension , connecting_wire_z) # type: ignore
    central_end_point = Base.Vector(connecting_wire_x, max_y + central_extension, connecting_wire_z) # type: ignore

    try:
        create_sweep(group, "circle", radius, [central_start_point, central_end_point], name="Central_Connecting_Wire")
    except Exception as e:
        print(f"Failed to create central connecting wire: {e}")