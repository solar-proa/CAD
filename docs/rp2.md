---
layout: default
title: Roti Proa II - 9m Day Tourism Vessel
---

<div style="display: flex; align-items: center; gap: 2em; margin-bottom: 2em; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 300px;">
    <h1 style="margin: 0;">Roti Proa II</h1>
    <h2 style="margin-top: 0.5em; font-weight: 300;">9-Meter Solar-Electric Day Tourism Vessel</h2>
  </div>
  <div style="flex: 1; min-width: 300px; max-width: 500px;">
    <img src="{{ '/renders/rp2.closehaul.render.isometric.png' | relative_url }}" alt="Roti Proa II" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  </div>
</div>

[← Back to Home]({{ '/' | relative_url }})

---

## Specifications

**Overall Length:** {{ site.data.rp2_closehaul_parameter.vaka_length }} mm  
**Beam:** {{ site.data.rp2_closehaul_parameter.beam }} mm (with outrigger)  
**Total mass (unloaded):** {{ site.data.rp2_beaching_mass.total_mass_kg }} kg  
**Total unsinkable volume:** {{ site.data.rp2_beaching_mass.total_unsinkable_volume_liters }} liters  
**Displacement of unsinkable volume in saltwater:** {{ site.data.rp2_beaching_mass.total_unsinkable_displacement_saltwater_kg }} kg  
**Capacity:** 4 passengers + 2 crew  
**Solar Power:** 4 kW peak (8 panels)  
**Motor Power:** 4 kW electric  
**Cruising Speed:** 10 knots  
**Daily Range:** 50 nautical miles (solar-electric only)  
**Battery Type:** LiFePO₄  
**Motor Runtime:** 5 hours (battery only)  
**Masts:** Two unstayed rotatable masts, cylindrical aluminium pipes with diameter {{ site.data.rp2_broadreach_parameter.mast_diameter }} mm and wall thickness {{ site.data.rp2_broadreach_parameter.mast_thickness }} mm; mast height from vaka sole: {{ site.data.rp2_broadreach_parameter.mast_height }} mm  
**Rig:** Each mast carries one tanja sail, each rectangular-shaped {{ site.data.rp2_broadreach_parameter.sail_width }} mm x {{ site.data.rp2_broadreach_parameter.sail_height }} mm; total sail area: {{ site.data.rp2_broadreach_parameter.sail_area_m2 }} square meters

---

## Design Features

**Hull Construction:**
- Professional fiberglass construction by Singapore boat maker
- Optimized for electric propulsion efficiency
- Delivery scheduled mid-February 2026

**Solar-Electric System:**
- 8 x 500W solar panels (4kW total)
- 48V electrical system
- Sponsored 4kW electric motor
- Integrated battery management

**Sailing Rig:**
- Dual aluminum stay-less masts
- Traditional tanja-inspired rectangular sails
- Shunting configuration for tropical conditions
- Backup propulsion capability

**Outrigger (Ama):**
- Aluminum crossbeam (aka) construction
- PVC pipe float construction  
- Optimized solar panel mounting
- Enhanced stability for passenger comfort

---

## Stability & Buoyancy

The vessel's stability has been analyzed using automated buoyancy equilibrium and GZ curve calculations.

**[View Full Stability & Buoyancy Analysis →]({{ '/stability_rp2.html' | relative_url }})**

| Parameter | Value | Description |
|-----------|-------|-------------|
| Draft | {{ site.data.rp2_beaching_buoyancy.equilibrium.z_offset_mm }} mm | Depth below waterline at equilibrium |
| Max righting arm | {{ site.data.rp2_beaching_gz.summary.max_gz_m | times: 100 | round: 0 }} cm | At {{ site.data.rp2_beaching_gz.summary.max_gz_angle_deg }}° heel |
| Capsize angle | {{ site.data.rp2_beaching_gz.summary.capsize_angle_deg }}° | Away from ama |
| Turtle angle | {{ site.data.rp2_beaching_gz.summary.turtle_angle_deg }}° | Towards ama |
| Roll period | {{ site.data.rp2_beaching_gz.natural_periods.roll_period_s }} s | Rough estimate |
| Pitch period | {{ site.data.rp2_beaching_gz.natural_periods.pitch_period_s }} s | Rough estimate |
| Heave period | {{ site.data.rp2_beaching_gz.natural_periods.heave_period_s }} s | Rough estimate |

---

## Structural Validation

The vessel's structural integrity has been validated under multiple load scenarios including static loads, wave impacts, wind forces, and crane operations. All tests pass with safety factors exceeding the required minimum of 2.0.

**[View Full Structural Safety Report →]({{ '/validation_rp2.html' | relative_url }})**

| Test | Safety Factor | Result |
|------|---------------|--------|
| Suspended ama (aka bending) | {{ site.data.rp2_beaching_validate_structure.tests[0].summary.strong_axis.safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[0].summary.strong_axis.result }} |
| Aka point load (crew standing) | {{ site.data.rp2_beaching_validate_structure.tests[1].summary.safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[1].summary.result }} |
| One end supported (spine bending) | {{ site.data.rp2_beaching_validate_structure.tests[2].summary.safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[2].summary.result }} |
| Mast wind loading (25 knots) | {{ site.data.rp2_beaching_validate_structure.tests[3].summary.safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[3].summary.result }} |
| Diagonal braces (lateral) | {{ site.data.rp2_beaching_validate_structure.tests[4].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[4].summary.result }} |
| Wave slam (vertical) | {{ site.data.rp2_beaching_validate_structure.tests[5].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[5].summary.result }} |
| Frontal wave slam | {{ site.data.rp2_beaching_validate_structure.tests[6].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[6].summary.result }} |
| Sideways wave slam | {{ site.data.rp2_beaching_validate_structure.tests[7].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[7].summary.result }} |
| Lifting sling (crane) | {{ site.data.rp2_beaching_validate_structure.tests[8].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[8].summary.result }} |
| Gunwale loads | {{ site.data.rp2_beaching_validate_structure.tests[9].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[9].summary.result }} |
| Ama lift wind speed | {{ site.data.rp2_beaching_validate_structure.tests[10].summary.ama_lift_windspeed_knots }} knots | INFO |

---

## Configurations

The vessel can be configured for different sailing conditions and use cases:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1em; margin: 2em 0;">
{% for config in site.data.configurations %}
  <div style="border: 1px solid #ddd; padding: 1em; border-radius: 4px;">
    <h4>{{ config.display_name }}</h4>
    <p style="font-size: 0.9em; color: #666;">{{ config.description }}</p>
  </div>
{% endfor %}
</div>

---

## 3D Renders

*Automatically generated from parametric CAD models*

{% assign render_files = site.static_files | where_exp: "file", "file.path contains 'renders'" | where_exp: "file", "file.path contains 'rp2'" | where_exp: "file", "file.extname == '.png'" %}

{% for config in site.data.configurations %}
<<<<<<< HEAD
  {% assign config_pattern = config.name | append: ".render" %}
  <h3>{{ config.display_name }}</h3>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1em; margin: 2em 0;">
  {% assign config_files = render_files | where_exp: "file", "file.basename contains config_pattern" | sort: "basename" %}
=======
  <h3>{{ config.display_name }}</h3>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1em; margin: 2em 0;">
  {% assign config_files = render_files | where_exp: "file", "file.basename contains config.name" | sort: "basename" %}
>>>>>>> 5ec7cc0 (Add technical page and systematic configuration display names)
  {% for file in config_files %}
    {% assign view_name = file.basename | split: ".render." | last %}
    <div>
      <img src="{{ file.path | relative_url }}" alt="{{ file.basename }}" style="width: 100%; border: 1px solid #ddd; border-radius: 4px;">
      <p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 0.5em;">
<<<<<<< HEAD
        {{ site.data.views[view_name].display_name }}
=======
        {{ file.basename | remove: "rp2." | remove: config.name | remove: ".render." | remove: "_" | replace: "front", "Back View" | replace: "isometric", "Isometric View" | replace: "right", "Right View" | replace: "top", "Top View" }}
>>>>>>> 5ec7cc0 (Add technical page and systematic configuration display names)
      </p>
    </div>
  {% endfor %}
  </div>
{% endfor %}

---

## Project Status

**Current Phase:** Under Construction

**Completed:**
- ✅ Detailed CAD design and optimization
- ✅ Hull order placed with boat maker
- ✅ Outrigger structure in progress
- ✅ Electrical system design
- ✅ Component procurement

**Next Steps:**
- Hull delivery (February 2026)
- Final assembly (March-April 2026)
- Sea trials (May-June 2026)
- Commercial validation with partners (Q3 2026)

---

## Download CAD Models

Access CAD models for all sail configurations in FreeCAD (.FCStd) and STEP (.step) formats.
These files include the complete 3D geometry and can be modified for your specific requirements.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1em; margin: 2em 0;">
{% for config in site.data.rp2_downloads.configuration %}
  <div style="padding: 1em; border: 1px solid #ddd; border-radius: 4px;">
    <div style="font-weight: bold; margin-bottom: 0.5em; text-transform: capitalize;">
      {{ config.name | replace: "_", " " }}
    </div>
    {% if config.description %}
    <div style="font-size: 0.85em; color: #666; margin-bottom: 0.75em;">
      {{ config.description }}
    </div>
    {% endif %}
    <div style="display: flex; gap: 0.5em; flex-wrap: wrap;">
      <a href="{{ '/downloads/' | append: config.filename | relative_url }}" style="background: #28a745; color: white; padding: 0.4em 0.8em; border-radius: 4px; text-decoration: none; font-size: 0.9em;">
        📐 FreeCAD
      </a>
      {% if config.step_filename %}
      <a href="{{ '/downloads/' | append: config.step_filename | relative_url }}" style="background: #007bff; color: white; padding: 0.4em 0.8em; border-radius: 4px; text-decoration: none; font-size: 0.9em;">
        📦 STEP
      </a>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

**Formats:**
- **FreeCAD (.FCStd):** Parametric model for [FreeCAD](https://www.freecad.org/) (free and open-source)
- **STEP (.step):** Universal CAD format compatible with most CAD software

**License:** Models are shared under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) - free to use, modify, and share with attribution.

---

[← Back to Home]({{ '/' | relative_url }}) | [View RP1 →]({{ '/rp1.html' | relative_url }}) | [View RP3 →]({{ '/rp3.html' | relative_url }})
