---
layout: default
title: Downloads
---

# Design Downloads

CAD files for all boat configurations in FreeCAD (`.FCStd`) and STEP (`.step`) formats.

- **FreeCAD files** can be opened in [FreeCAD](https://www.freecadweb.org/) for parametric editing
- **STEP files** are compatible with most CAD software (Fusion 360, SolidWorks, Onshape, etc.)

## FreeCAD Files

{% assign fcstd_files = site.static_files | where_exp: "file", "file.path contains '/downloads/'" | where_exp: "file", "file.extname == '.FCStd'" | sort: "path" %}

<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr style="background: #f0f0f0;">
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Boat</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Configuration</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">File</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Download</th>
    </tr>
  </thead>
  <tbody>
{% for file in fcstd_files %}
  {% assign parts = file.name | split: "." %}
  {% assign boat = parts[0] %}
  {% assign config = parts[1] %}
  <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><strong>{{ boat | upcase }}</strong></td>
    <td style="padding: 10px; border: 1px solid #ddd;">{{ config | capitalize }}</td>
    <td style="padding: 10px; border: 1px solid #ddd; font-family: monospace; font-size: 0.9em;">{{ file.name }}</td>
    <td style="padding: 10px; border: 1px solid #ddd;">
      <a href="{{ file.path }}" download style="background: #28a745; color: white; padding: 5px 15px; border-radius: 3px; text-decoration: none;">📐 FreeCAD</a>
    </td>
  </tr>
{% endfor %}
  </tbody>
</table>

## STEP Files

{% assign step_files = site.static_files | where_exp: "file", "file.path contains '/downloads/'" | where_exp: "file", "file.extname == '.step'" | sort: "path" %}

{% if step_files.size > 0 %}
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr style="background: #f0f0f0;">
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Boat</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Configuration</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">File</th>
      <th style="padding: 10px; text-align: left; border: 1px solid #ddd;">Download</th>
    </tr>
  </thead>
  <tbody>
{% for file in step_files %}
  {% assign parts = file.name | split: "." %}
  {% assign boat = parts[0] %}
  {% assign config = parts[1] %}
  <tr>
    <td style="padding: 10px; border: 1px solid #ddd;"><strong>{{ boat | upcase }}</strong></td>
    <td style="padding: 10px; border: 1px solid #ddd;">{{ config | capitalize }}</td>
    <td style="padding: 10px; border: 1px solid #ddd; font-family: monospace; font-size: 0.9em;">{{ file.name }}</td>
    <td style="padding: 10px; border: 1px solid #ddd;">
      <a href="{{ file.path }}" download style="background: #007bff; color: white; padding: 5px 15px; border-radius: 3px; text-decoration: none;">📦 STEP</a>
    </td>
  </tr>
{% endfor %}
  </tbody>
</table>
{% else %}
<p><em>STEP files are being generated...</em></p>
{% endif %}

## How to Use

### FreeCAD Files
1. **Install FreeCAD**: Download from [freecadweb.org](https://www.freecadweb.org/)
2. **Download a file**: Click the FreeCAD download button above
3. **Open in FreeCAD**: File → Open → Select the downloaded `.FCStd` file
4. **Explore**: All components should be visible and editable

### STEP Files
1. **Open in your preferred CAD software**: Fusion 360, SolidWorks, Onshape, FreeCAD, etc.
2. **Import the STEP file**: Most CAD software supports STEP import natively
3. **Note**: STEP files contain geometry only (no parametric history)

## File Naming Convention

- **FreeCAD**: `{boat}.{configuration}.color.FCStd`
- **STEP**: `{boat}.{configuration}.step.step`

Where:
- **boat**: `rp1`, `rp2`, `rp3` (Roti Proa models 1, 2, 3)
- **configuration**: Sailing configuration (closehaul, beamreach, etc.)

---

[← Back to Home](/)
