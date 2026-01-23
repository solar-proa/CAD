---
layout: default
title: Roti Proa III - Kapal Multi-Hari 13m
description: Kapal Hibrida Bertenaga Angin-Surya untuk Daerah Tropis
lang: id
---

<div style="display: flex; align-items: center; gap: 2em; margin-bottom: 2em; flex-wrap: wrap;">
  <div style="flex: 1; min-width: 300px;">
    <h1 style="margin: 0;">Roti Proa III</h1>
    <h2 style="margin-top: 0.5em; font-weight: 300;">Kapal Jelajah Multi-Hari Surya-Listrik 13 Meter</h2>
  </div>
  <div style="flex: 1; min-width: 300px; max-width: 500px;">
    <img src="{{ '/renders/rp3.closehaul.render.isometric.png' | relative_url }}" alt="Roti Proa III" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  </div>
</div>

[← Kembali ke Beranda]({{ '/id/' | relative_url }})

---

## Visi: Meningkatkan Skala untuk Pelayaran Multi-Hari

**Status:** 🔵 Fase Desain | **Target:** Validasi pertengahan 2027

Roti Proa III mewakili visi kami untuk pelayaran pesisir multi-hari bebas karbon di Asia Tenggara tropis. Berdasarkan pelajaran dari RP1 (prototipe) dan RP2 (wisata harian), RP3 akan mendemonstrasikan bahwa propulsi surya-listrik dapat mendukung pelayaran jarak jauh dengan akomodasi bermalam.

---

## Konsep Desain

Roti Proa III akan berbasis pada **lambung Dragon Boat DB22** - desain tradisional yang terbukti yang menawarkan:

- **Rasio panjang-ke-lebar optimal** untuk propulsi listrik yang efisien
- **Kelayakan laut yang terbukti** di perairan Asia Tenggara
- **Signifikansi budaya** yang terhubung dengan warisan maritim regional
- **Volume interior yang luas** untuk akomodasi penumpang
- **Metode konstruksi yang mapan** untuk pembangunan yang andal

### Mengapa Warisan Dragon Boat?

Dragon boat telah digunakan di seluruh Asia selama lebih dari 2.000 tahun. Desain DB22 mewakili penyempurnaan berabad-abad untuk perairan pesisir tropis - tepatnya lingkungan operasional kami. Dengan mengadaptasi lambung tradisional ini ke propulsi surya-listrik modern, kami menghormati tradisi maritim sambil merintis teknologi berkelanjutan.

---

## Spesifikasi Awal

| Spesifikasi | Nilai Estimasi |
|-------------|----------------|
| Panjang Keseluruhan (LOA) | {{ site.data.rp3_closehaul_parameter.vaka_length }} mm |
| Lebar (lambung) | ~1,2m (proporsi dragon boat tradisional) |
| Lebar (dengan cadik) | {{ site.data.rp3_closehaul_parameter.beam }} mm |
| Kapasitas | 5-6 penumpang + 2 kru |
| Daya Surya | 6-8kW puncak (estimasi) |
| Daya Motor | 5-6kW listrik (estimasi) |
| Kecepatan Jelajah | 8-10 knot |
| Jangkauan | Multi-hari (100+ mil laut) |
| Akomodasi | Kamar tidur untuk penumpang |
| Dapur | Memasak listrik dari kelebihan surya |
| Air | Kemampuan desalinasi terintegrasi |

*Catatan: Spesifikasi bersifat awal dan dapat disempurnakan selama fase desain detail*

---

## Analisis Daya Apung

Kami menurunkan karakteristik daya apung berikut dari analisis otomatis kami menggunakan metode Newton, secara iteratif menyesuaikan roll/pitch/z-offset kapal sesuai dengan perbedaan antara pusat/jumlah daya apung dan pusat/jumlah massa. Angka-angka menunjukkan kesetimbangan yang dicapai setelah
{{ site.data.rp3_beaching_buoyancy.iterations }} iterasi menggunakan konfigurasi beaching (tanpa layar dan kemudi diangkat), lihat [implementasi](https://github.com/solar-proa/CAD/blob/main/src/buoyancy/__main__.py).

**Z-offset (penurunan kapal ke air):** {{ site.data.rp3_beaching_buoyancy.equilibrium.z_offset_mm }} mm
**Derajat pitch:** {{ site.data.rp3_beaching_buoyancy.equilibrium.pitch_deg }} derajat busur
**Derajat roll:** {{ site.data.rp3_beaching_buoyancy.equilibrium.roll_deg }} derajat busur
**Volume vaka terendam:** {{ site.data.rp3_beaching_buoyancy.vaka.submerged_volume_liters }} liter
**Volume total vaka:** {{ site.data.rp3_beaching_buoyancy.vaka.total_volume_liters }} liter
**Persentase vaka terendam:** {{ site.data.rp3_beaching_buoyancy.vaka.submerged_percent }} %
**Z-offset vaka:** {{ site.data.rp3_beaching_buoyancy.vaka.z_world_mm }} mm
**Volume ama terendam:** {{ site.data.rp3_beaching_buoyancy.ama.submerged_volume_liters }} liter
**Volume total ama:** {{ site.data.rp3_beaching_buoyancy.ama.total_volume_liters }} liter
**Persentase ama terendam:** {{ site.data.rp3_beaching_buoyancy.ama.submerged_percent }} %
**Z-offset ama:** {{ site.data.rp3_beaching_buoyancy.ama.z_world_mm }} mm
**Pusat gravitasi (koordinat dunia x, y, z):** {{ site.data.rp3_beaching_buoyancy.center_of_gravity_world.x }}, {{ site.data.rp3_beaching_buoyancy.center_of_gravity_world.y }}, {{ site.data.rp3_beaching_buoyancy.center_of_gravity_world.z }} mm
**Pusat daya apung (koordinat dunia x, y, z):** {{ site.data.rp3_beaching_buoyancy.center_of_buoyancy.x }}, {{ site.data.rp3_beaching_buoyancy.center_of_buoyancy.y }}, {{ site.data.rp3_beaching_buoyancy.center_of_buoyancy.z }} mm

---

## Inovasi Kunci untuk Operasi Multi-Hari

**Kapasitas Surya yang Diperluas:**
- Array surya lebih besar (6-8kW) untuk pengisian baterai semalam
- Daya berlebih untuk memasak di kapal dan desalinasi air
- Kompatibilitas daya darat untuk pengisian di dermaga

**Desain Akomodasi:**
- Tempat tidur untuk 5-6 penumpang
- Area dek tertutup untuk perlindungan cuaca
- Dapur dengan fasilitas memasak listrik
- Penyimpanan air tawar dan desalinasi
- Fasilitas toilet laut

**Rig Layar yang Ditingkatkan:**
- Versi yang diperbesar dari desain shunting RP2 yang terbukti
- Luas layar yang ditingkatkan untuk perjalanan jarak jauh
- Kemampuan rig badai untuk keselamatan

**Sistem Redundan:**
- Opsi konfigurasi motor ganda
- Kemampuan berlayar cadangan
- Kapasitas baterai yang ditingkatkan untuk operasi semalam

---

## Linimasa Pengembangan

**2026 Q4:** Finalisasi desain lambung berdasarkan platform DB22
**2027 Q1-Q2:** Konstruksi dan integrasi sistem
**2027 Q2-Q3:** Uji coba laut dan sertifikasi
**2027 Q4:** Validasi komersial dengan mitra strategis

---

## Aplikasi Target

**Eko-Wisata Multi-Hari:**
- Ekspedisi wisata pulau (3-5 hari)
- Wisata pengamatan satwa liar laut
- Tur pesisir warisan budaya
- Pengalaman pelayaran edukatif
- Pengalaman perjalanan lambat menghubungkan komunitas pesisir

**Keunggulan Operasional:**
- Nol biaya bahan bakar pada pelayaran multi-hari
- Operasi tenang untuk pengamatan satwa liar
- Memasak di kapal tanpa generator diesel
- Pembangkitan air tawar dari kelebihan surya
- Posisi eko-wisata premium

---

## Filosofi Desain

Roti Proa III mewujudkan prinsip inti kami: **menggabungkan tradisi maritim Asia Tenggara dengan teknologi berkelanjutan mutakhir.**

Lambung dragon boat mewakili 2.000+ tahun rekayasa maritim Asia. Kontribusi kami adalah mengadaptasi desain yang terbukti ini untuk abad ke-21 - mengganti pendayung manusia dengan propulsi surya-listrik sambil mempertahankan efisiensi dan kelayakan laut fundamental lambung.

Ini bukan hanya tentang transfer teknologi; ini tentang **kesinambungan budaya** - menunjukkan bahwa desain tradisional tetap relevan ketika dipasangkan dengan solusi keberlanjutan modern.

---

## Render 3D

*Dihasilkan secara otomatis dari model CAD parametrik*

{% assign render_files = site.static_files | where_exp: "file", "file.path contains 'renders'" | where_exp: "file", "file.path contains 'rp3'" | where_exp: "file", "file.extname == '.png'" %}

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

## Peluang Kemitraan

Pengembangan RP3 menghadirkan peluang unik bagi mitra strategis yang tertarik dalam:

- **Kolaborasi desain tahap awal** pada kapal eko-wisata multi-hari
- **Partisipasi uji lapangan** dalam fase validasi 2027
- **Validasi pasar** untuk pengalaman wisata berkelanjutan premium
- **Demonstrasi teknologi** untuk inisiatif keberlanjutan korporat

Linimasa 2027 memungkinkan mitra untuk mempengaruhi keputusan desain sambil mempertahankan eksposur ke segmen pasar yang baru.

---

## Dari Prototipe ke Produksi

**RP1 (2025):** Membuktikan konsep
**RP2 (2026):** Memvalidasi operasi wisata harian komersial
**RP3 (2027):** Mendemonstrasikan kemampuan pelayaran multi-hari

Perkembangan ini mengurangi risiko teknologi sambil membangun menuju visi akhir kami: armada kapal bebas karbon yang melayani pasar eko-wisata pesisir Asia Tenggara.

---

## Unduh Model CAD

Akses model CAD untuk semua konfigurasi layar dalam format FreeCAD (.FCStd) dan STEP (.step).
File-file ini mencakup geometri 3D lengkap dan dapat dimodifikasi untuk kebutuhan spesifik Anda.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1em; margin: 2em 0;">
{% for config in site.data.rp3_downloads.configuration %}
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

[← Kembali ke Beranda]({{ '/id/' | relative_url }}) | [Lihat RP1 →]({{ '/id/rp1.html' | relative_url }}) | [Lihat RP2 →]({{ '/id/rp2.html' | relative_url }})
