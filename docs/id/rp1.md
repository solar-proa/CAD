---
layout: default
title: Roti Proa I - Prototipe 4,2m
description: Kapal Hibrida Bertenaga Angin-Surya untuk Daerah Tropis
lang: id
---

<div style="display: flex; align-items: center; gap: 2em; margin-bottom: 2em; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 300px;">
    <h1 style="margin: 0;">Roti Proa I</h1>
    <h2 style="margin-top: 0.5em; font-weight: 300;">Prototipe Bukti-Konsep 4,2 Meter</h2>
  </div>
  <div style="flex: 1; min-width: 300px; max-width: 500px;">
    <img src="{{ '/renders/rp1.closehaul.render.isometric.png' | relative_url }}" alt="Roti Proa I" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  </div>
</div>

[← Kembali ke Beranda]({{ '/id/' | relative_url }})

---

## Ringkasan

**Status:** ✅ Selesai dan teruji (Desember 2024 - Juni 2025)

Roti Proa I adalah prototipe bukti-konsep kami yang memvalidasi kelayakan menggabungkan desain cadik tradisional dengan propulsi surya-listrik modern di perairan tropis. Kapal 4,2 meter ini berhasil mendemonstrasikan prinsip-prinsip inti yang menginformasikan desain komersial kami yang lebih besar.

**Pencapaian Utama:**
- **Uji coba laut tervalidasi** di perairan Singapura dekat Changi
- **Kecepatan tertinggi:** 6,5 knot (12 km/jam) dengan tenaga listrik
- **Kapasitas surya:** 1kW puncak (2 panel)
- **Propulsi:** Motor tempel listrik 2kW
- **Baterai:** Sistem LiFePO₄
- **Rig layar:** Dua rig sport independen untuk konfigurasi eksperimental

Prototipe ini membuktikan bahwa proa surya layak untuk perairan Asia Tenggara tropis dan memberikan data penting untuk peningkatan skala ke desain Roti Proa II 9 meter.

---

## Publikasi Unggulan

Untuk laporan detail tentang pengembangan, pengujian, dan pelajaran yang dipetik dari Roti Proa I, baca artikel lengkap yang diterbitkan oleh Changi Sailing Club di Singapura:

**[Roti Proa: Perahu Eksperimental Bertenaga Angin dan Surya](https://www.csc.org.sg/2025/07/11/roti-proa-an-experimental-wind-and-solar-powered-boat/)**

Artikel komprehensif ini mencakup:
- Filosofi desain dan pengaruh tradisional
- Proses konstruksi dan pilihan material
- Hasil uji coba laut dan data performa
- Pelajaran yang dipetik untuk pengembangan masa depan
- Tantangan teknis dan solusinya

---

## Spesifikasi Ringkas

| Spesifikasi | Nilai |
|-------------|-------|
| Panjang Keseluruhan (LOA) | 4,2m |
| Lebar | 2,5m |
| Daya Surya | 1kW puncak |
| Daya Motor | Motor tempel listrik 2kW |
| Tipe Baterai | LiFePO₄ |
| Kecepatan Tertinggi | 6,5 knot |
| Kru | 1-2 orang |
| Status | Pengujian selesai Juni 2025 |

---

## Analisis Daya Apung

Kami menurunkan karakteristik daya apung berikut dari analisis otomatis kami menggunakan metode Newton, secara iteratif menyesuaikan roll/pitch/z-offset kapal sesuai dengan perbedaan antara pusat/jumlah daya apung dan pusat/jumlah massa. Angka-angka menunjukkan kesetimbangan yang dicapai setelah
{{ site.data.rp1_beaching_buoyancy.iterations }} iterasi menggunakan konfigurasi beaching (tanpa layar dan kemudi diangkat), lihat [implementasi](https://github.com/solar-proa/CAD/blob/main/src/buoyancy/__main__.py).

**Z-offset (penurunan kapal ke air):** {{ site.data.rp1_beaching_buoyancy.equilibrium.z_offset_mm }} mm
**Derajat pitch:** {{ site.data.rp1_beaching_buoyancy.equilibrium.pitch_deg }} derajat busur
**Derajat roll:** {{ site.data.rp1_beaching_buoyancy.equilibrium.roll_deg }} derajat busur
**Volume vaka terendam:** {{ site.data.rp1_beaching_buoyancy.vaka.submerged_volume_liters }} liter
**Volume total vaka:** {{ site.data.rp1_beaching_buoyancy.vaka.total_volume_liters }} liter
**Persentase vaka terendam:** {{ site.data.rp1_beaching_buoyancy.vaka.submerged_percent }} %
**Z-offset vaka:** {{ site.data.rp1_beaching_buoyancy.vaka.z_world_mm }} mm
**Volume ama terendam:** {{ site.data.rp1_beaching_buoyancy.ama.submerged_volume_liters }} liter
**Volume total ama:** {{ site.data.rp1_beaching_buoyancy.ama.total_volume_liters }} liter
**Persentase ama terendam:** {{ site.data.rp1_beaching_buoyancy.ama.submerged_percent }} %
**Z-offset ama:** {{ site.data.rp1_beaching_buoyancy.ama.z_world_mm }} mm
**Pusat gravitasi (koordinat dunia x, y, z):** {{ site.data.rp1_beaching_buoyancy.center_of_gravity_world.x }}, {{ site.data.rp1_beaching_buoyancy.center_of_gravity_world.y }}, {{ site.data.rp1_beaching_buoyancy.center_of_gravity_world.z }} mm
**Pusat daya apung (koordinat dunia x, y, z):** {{ site.data.rp1_beaching_buoyancy.center_of_buoyancy.x }}, {{ site.data.rp1_beaching_buoyancy.center_of_buoyancy.y }}, {{ site.data.rp1_beaching_buoyancy.center_of_buoyancy.z }} mm

---

## Render 3D

*Dihasilkan secara otomatis dari model CAD parametrik*

{% assign render_files = site.static_files | where_exp: "file", "file.path contains 'renders'" | where_exp: "file", "file.path contains 'rp1'" | where_exp: "file", "file.extname == '.png'" %}

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

## Warisan & Dampak

Uji coba Roti Proa I yang sukses memberikan kepercayaan dan data empiris yang diperlukan untuk mengejar pengembangan skala komersial. Prototipe ini mendemonstrasikan bahwa:

✅ Propulsi surya-listrik layak di perairan tropis
✅ Desain cadik tradisional beradaptasi dengan baik terhadap sistem listrik modern
✅ Proa shunting dapat mengintegrasikan panel surya secara efektif
✅ Kombinasi ini menciptakan pengalaman eko-wisata yang menarik

Wawasan ini secara langsung menginformasikan desain Roti Proa II dan memvalidasi pendekatan kami untuk Roti Proa III 13 meter.

---

## Pendanaan & Dukungan

Roti Proa I didanai melalui:
- **Maybank Green Fund:** S$5.000 (melalui NUS Office of Student Affairs)
- **Donasi dan sponsor swasta:** S$7.000
- **Total biaya proyek:** S$12.000

---

## Dari Prototipe ke Produk

Keberhasilan Roti Proa I mendemonstrasikan bahwa visi kami secara teknis layak. Sekarang, dengan Roti Proa II dalam konstruksi, kami mengambil langkah berikutnya menuju kelayakan komersial—sebuah kapal yang dirancang tidak hanya untuk membuktikan konsep, tetapi untuk melayani operasi eko-wisata nyata di Asia Tenggara tropis.

**Baca cerita lengkapnya:** [Artikel Changi Sailing Club →](https://www.csc.org.sg/2025/07/11/roti-proa-an-experimental-wind-and-solar-powered-boat/)

---

## Unduh Model CAD

Akses model CAD untuk semua konfigurasi layar dalam format FreeCAD (.FCStd) dan STEP (.step).
File-file ini mencakup geometri 3D lengkap dan dapat dimodifikasi untuk kebutuhan spesifik Anda.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1em; margin: 2em 0;">
{% for config in site.data.rp1_downloads.configuration %}
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

[← Kembali ke Beranda]({{ '/id/' | relative_url }}) | [Lihat RP2 →]({{ '/id/rp2.html' | relative_url }}) | [Lihat RP3 →]({{ '/id/rp3.html' | relative_url }})
