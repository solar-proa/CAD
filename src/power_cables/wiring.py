import Part
import FreeCAD
from FreeCAD import Base


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

def wire_solar_panels(group, radius=5):
    """
    Extracts all solar panels from the group and draws a wire sweep along their length.
    
    Args:
        group: The FreeCAD Document or Group object containing the panels.
        radius: Radius of the wire sweep.
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

    for panel in panels:
        # Get global bounding box of the panel
        # panel.Shape returns the shape with Placement applied (global coords)
        bbox = panel.Shape.BoundBox
        
        # Calculate start and end points for the wire
        # Running along the length (X-axis), centered on Width (Y-axis), on Top (Z-axis)
        
        mid_y = (bbox.YMin + bbox.YMax) / 2
        top_z = bbox.ZMax
        
        # Start at min X, End at max X

        # TODO: Draw until the central hull and offset the wires for transverse panels, currently draws along the length of panel
        start_point = Base.Vector(bbox.XMin, mid_y, top_z)
        end_point = Base.Vector(bbox.XMax, mid_y, top_z)
        
        wire_name = f"{panel.Name}_Wire"
        
        try:
            create_sweep(group, "circle", radius, [start_point, end_point], name=wire_name)
        except Exception as e:
            print(f"Failed to wire panel {panel.Name}: {e}")
