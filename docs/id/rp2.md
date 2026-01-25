---
layout: default
title: Roti Proa II - Kapal Wisata Harian 9m
description: Kapal Hibrida Bertenaga Angin-Surya untuk Daerah Tropis
lang: id
---

<div style="display: flex; align-items: center; gap: 2em; margin-bottom: 2em; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 300px;">
    <h1 style="margin: 0;">Roti Proa II</h1>
    <h2 style="margin-top: 0.5em; font-weight: 300;">Kapal Wisata Harian Surya-Listrik 9 Meter</h2>
  </div>
  <div style="flex: 1; min-width: 300px; max-width: 500px;">
    <img src="{{ '/renders/rp2.closehaul.render.isometric.png' | relative_url }}" alt="Roti Proa II" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  </div>
</div>

[← Kembali ke Beranda]({{ '/id/' | relative_url }})

---

## Spesifikasi

**Panjang Keseluruhan:** {{ site.data.rp2_closehaul_parameter.vaka_length }} mm  
**Lebar:** {{ site.data.rp2_closehaul_parameter.beam }} mm (dengan cadik)  
**Massa total (tanpa muatan):** {{ site.data.rp2_beaching_mass.total_mass_kg }} kg  
**Volume total tidak tenggelam:** {{ site.data.rp2_beaching_mass.total_unsinkable_volume_liters }} liter  
**Perpindahan volume tidak tenggelam di air asin:** {{ site.data.rp2_beaching_mass.total_unsinkable_displacement_saltwater_kg }} kg  
**Kapasitas:** 4 penumpang + 2 kru  
**Daya Surya:** 4 kW puncak (8 panel)  
**Daya Motor:** 4 kW listrik  
**Kecepatan Jelajah:** 10 knot  
**Jangkauan Harian:** 50 mil laut (surya-listrik saja)  
**Tipe Baterai:** LiFePO₄  
**Waktu Operasi Motor:** 5 jam (baterai saja)  
**Tiang:** Dua tiang tanpa stay yang dapat diputar, pipa aluminium silinder dengan diameter {{ site.data.rp2_broadreach_parameter.mast_diameter }} mm dan ketebalan dinding {{ site.data.rp2_broadreach_parameter.mast_thickness }} mm; tinggi tiang dari sole vaka: {{ site.data.rp2_broadreach_parameter.mast_height }} mm  
**Rig:** Setiap tiang membawa satu layar tanja, masing-masing berbentuk persegi panjang {{ site.data.rp2_broadreach_parameter.sail_width }} mm x {{ site.data.rp2_broadreach_parameter.sail_height }} mm; total luas layar: {{ site.data.rp2_broadreach_parameter.sail_area_m2 }} meter persegi  

---

## Fitur Desain

**Konstruksi Lambung:**
- Konstruksi fiberglass profesional oleh pembuat kapal Singapura
- Dioptimalkan untuk efisiensi propulsi listrik
- Pengiriman dijadwalkan pertengahan Februari 2026

**Sistem Surya-Listrik:**
- 8 x panel surya 500W (total 4kW)
- Sistem listrik 48V
- Motor listrik 4kW yang disponsori
- Manajemen baterai terintegrasi

**Rig Layar:**
- Dua tiang aluminium tanpa stay
- Layar persegi panjang terinspirasi tanja tradisional
- Konfigurasi shunting untuk kondisi tropis
- Kemampuan propulsi cadangan

**Cadik (Ama):**
- Konstruksi balok silang aluminium (aka)
- Konstruksi pelampung pipa PVC
- Pemasangan panel surya yang dioptimalkan
- Stabilitas yang ditingkatkan untuk kenyamanan penumpang

---

## Stabilitas & Daya Apung

Stabilitas kapal telah dianalisis menggunakan perhitungan kesetimbangan daya apung otomatis dan kurva GZ.

**[Lihat Analisis Stabilitas & Daya Apung Lengkap →]({{ '/id/stability_rp2.html' | relative_url }})**

| Parameter | Nilai | Deskripsi |
|-----------|-------|-----------|
| Sarat | {{ site.data.rp2_beaching_buoyancy.equilibrium.z_offset_mm }} mm | Kedalaman di bawah garis air pada kesetimbangan |
| Lengan penegak maks | {{ site.data.rp2_beaching_gz.summary.max_gz_m | times: 100 | round: 0 }} cm | Pada kemiringan {{ site.data.rp2_beaching_gz.summary.max_gz_angle_deg }}° |
| Sudut capsize | {{ site.data.rp2_beaching_gz.summary.capsize_angle_deg }}° | Menjauhi ama |
| Sudut turtle | {{ site.data.rp2_beaching_gz.summary.turtle_angle_deg }}° | Menuju ama |
| Periode roll | {{ site.data.rp2_beaching_gz.natural_periods.roll_period_s }} s | Perkiraan kasar |
| Periode pitch | {{ site.data.rp2_beaching_gz.natural_periods.pitch_period_s }} s | Perkiraan kasar |
| Periode heave | {{ site.data.rp2_beaching_gz.natural_periods.heave_period_s }} s | Perkiraan kasar |

---

## Validasi Struktural

Integritas struktural kapal telah divalidasi di bawah beberapa skenario beban termasuk beban statis, dampak gelombang, gaya angin, dan operasi crane. Semua tes lulus dengan faktor keamanan melebihi minimum yang diperlukan yaitu 2,0.

**[Lihat Laporan Keselamatan Struktural Lengkap →]({{ '/id/validation_rp2.html' | relative_url }})**

| Tes | Faktor Keamanan | Hasil |
|-----|-----------------|-------|
| Ama tergantung (lentur aka) | {{ site.data.rp2_beaching_validate_structure.tests[0].summary.strong_axis.safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[0].summary.strong_axis.result }} |
| Beban titik aka (kru berdiri) | {{ site.data.rp2_beaching_validate_structure.tests[1].summary.safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[1].summary.result }} |
| Satu ujung ditopang (lentur spine) | {{ site.data.rp2_beaching_validate_structure.tests[2].summary.safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[2].summary.result }} |
| Beban angin tiang (25 knot) | {{ site.data.rp2_beaching_validate_structure.tests[3].summary.safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[3].summary.result }} |
| Penopang diagonal (lateral) | {{ site.data.rp2_beaching_validate_structure.tests[4].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[4].summary.result }} |
| Hantaman gelombang (vertikal) | {{ site.data.rp2_beaching_validate_structure.tests[5].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[5].summary.result }} |
| Hantaman gelombang frontal | {{ site.data.rp2_beaching_validate_structure.tests[6].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[6].summary.result }} |
| Hantaman gelombang samping | {{ site.data.rp2_beaching_validate_structure.tests[7].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[7].summary.result }} |
| Sling pengangkat (crane) | {{ site.data.rp2_beaching_validate_structure.tests[8].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[8].summary.result }} |
| Beban gunwale | {{ site.data.rp2_beaching_validate_structure.tests[9].summary.min_safety_factor }} | {{ site.data.rp2_beaching_validate_structure.tests[9].summary.result }} |
| Kecepatan angin angkat ama | {{ site.data.rp2_beaching_validate_structure.tests[10].summary.ama_lift_windspeed_knots }} knot | INFO |

---

## Konfigurasi

Kapal dapat dikonfigurasi untuk berbagai kondisi pelayaran dan kasus penggunaan:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1em; margin: 2em 0;">
{% for config in site.data.configurations %}
  <div style="border: 1px solid #ddd; padding: 1em; border-radius: 4px;">
    <h4>{{ config.display_name_id }}</h4>
    <p style="font-size: 0.9em; color: #666;">{{ config.description_id }}</p>
  </div>
{% endfor %}
</div>

---

## Render 3D

*Dihasilkan secara otomatis dari model CAD parametrik*

{% assign render_files = site.static_files | where_exp: "file", "file.path contains 'renders'" | where_exp: "file", "file.path contains 'rp2'" | where_exp: "file", "file.extname == '.png'" %}

{% for config in site.data.configurations %}
  {% assign config_pattern = config.name | append: ".render" %}
  <h3>{{ config.display_name_id }}</h3>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1em; margin: 2em 0;">
  {% assign config_files = render_files | where_exp: "file", "file.basename contains config_pattern" | sort: "basename" %}
  {% for file in config_files %}
    {% assign view_name = file.basename | split: ".render." | last %}
    <div>
      <img src="{{ file.path | relative_url }}" alt="{{ file.basename }}" style="width: 100%; border: 1px solid #ddd; border-radius: 4px;">
      <p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 0.5em;">
        {{ site.data.views[view_name].display_name }}
      </p>
    </div>
  {% endfor %}
  </div>
{% endfor %}

---

## Status Proyek

**Fase Saat Ini:** Dalam Konstruksi

**Selesai:**
- ✅ Desain CAD detail dan optimasi
- ✅ Pesanan lambung ditempatkan ke pembuat kapal
- ✅ Struktur cadik sedang berlangsung
- ✅ Desain sistem listrik
- ✅ Pengadaan komponen

**Langkah Selanjutnya:**
- Pengiriman lambung (Februari 2026)
- Perakitan akhir (Maret-April 2026)
- Uji coba laut (Mei-Juni 2026)
- Validasi komersial dengan mitra (Q3 2026)

---

## Unduh Model CAD

Akses model CAD untuk semua konfigurasi layar dalam format FreeCAD (.FCStd) dan STEP (.step).
File-file ini mencakup geometri 3D lengkap dan dapat dimodifikasi untuk kebutuhan spesifik Anda.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1em; margin: 2em 0;">
{% for config in site.data.rp2_downloads.configuration %}
  {% assign config_trans = site.data.configurations | where: "name", config.name | first %}
  <div style="padding: 1em; border: 1px solid #ddd; border-radius: 4px;">
    <div style="font-weight: bold; margin-bottom: 0.5em;">
      {{ config_trans.display_name_id | default: config.name }}
    </div>
    {% if config_trans.description_id %}
    <div style="font-size: 0.85em; color: #666; margin-bottom: 0.75em;">
      {{ config_trans.description_id }}
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

**Format:**
- **FreeCAD (.FCStd):** Model parametrik untuk [FreeCAD](https://www.freecad.org/) (gratis dan sumber terbuka)
- **STEP (.step):** Format CAD universal yang kompatibel dengan sebagian besar perangkat lunak CAD

**Lisensi:** Model dibagikan di bawah [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) - bebas digunakan, dimodifikasi, dan dibagikan dengan atribusi.

---

[← Kembali ke Beranda]({{ '/id/' | relative_url }}) | [Lihat RP1 →]({{ '/id/rp1.html' | relative_url }}) | [Lihat RP3 →]({{ '/id/rp3.html' | relative_url }})
