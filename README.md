g```markdown
# 📍 Google Maps Scraper Pro (MVP & Prototype Architecture)

Select Language / Pilih Bahasa:
- [Bahasa Indonesia](#bahasa-indonesia)
- [English](#english)

---

## Bahasa Indonesia

Sebuah prototip aplikasi web mandiri (*Minimum Viable Product*) berbasis Python Flask dan Selenium yang dirancang untuk melakukan ekstraksi data entitas bisnis secara dinamis dari Google Maps berdasarkan filter wilayah bertingkat (Provinsi/Kota).

Aplikasi ini dibangun dengan fokus pada arsitektur kode yang bersih (*clean-code boilerplate*) serta aman untuk kebutuhan demonstrasi, riset pasar, maupun pengembangan lanjutan (*Proof of Concept*).

### ✨ Fitur Utama
- **Keyword Objek Dinamis:** Memungkinkan pencarian entitas apa pun (contoh: Masjid, Toko Sembako, Apotek) secara langsung.
- **Filter Wilayah Bertingkat:** Mekanisme pencarian terarah berdasarkan cakupan Provinsi hingga Kota/Kabupaten.
- **Automated Infinite Scroll:** Simulasi otomatisasi browser untuk memicu *lazy loading* Google Maps guna menarik puluhan data secara *real-time*.
- **Admin Panel Dashboard:** Antarmuka berbasis Bootstrap yang bersih dan intuitif untuk pengelolaan aktivitas scraping.
- **Ekspor Data Excel:** Fitur instan untuk mengunduh hasil ekstraksi data ke format spreadsheet (.xlsx) untuk kebutuhan analisis lanjutan.

### 🛠️ Spesifikasi Teknologi
- **Backend Framework:** Python Flask
- **Otomatisasi Browser:** Selenium WebDriver (Headless Mode)
- **Manajemen Driver:** WebDriver Manager (Chrome)
- **Pengolahan Data & Ekspor:** Pandas & OpenPyXL
- **Frontend Interface:** HTML5, Jinja2 Templates, Bootstrap 5 (via CDN)

### 📁 Struktur Proyek
```text
gmaps-scraper/
│
├── app.py                 # Backend utama & Routing Flask
├── scraper.py             # Logika inti pengikis & Otomatisasi Browser
├── requirements.txt       # Dependensi pustaka proyek
└── templates/
    ├── base.html          # Master Layout (Kerangka Induk Global)
    └── index.html         # Dashboard Panel Utama Admin

```

### 🚀 Panduan Instalasi & Menjalankan Lokal

#### Prasyarat Sistem

Pastikan perangkat Anda sudah terinstal Google Chrome dan Python versi 3.8 ke atas.

1. **Klon Repositori ini:**
```bash
git clone [https://github.com/username-kamu/gmaps-scraper.git](https://github.com/username-kamu/gmaps-scraper.git)
cd gmaps-scraper

```


2. **Instal Seluruh Dependensi:**
```bash
pip install -r requirements.txt

```


3. **Jalankan Aplikasi Server:**
```bash
python3 app.py

```


4. **Akses Dashboard:**
Buka browser Anda dan akses tautan `http://127.0.0.1:5000`

### ⚠️ Batasan Sistem Prototip (Disclaimer)

Aplikasi ini dikembangkan dalam skala **MVP (Minimum Viable Product)**. Untuk menjaga stabilitas server dan menghindari pemblokiran IP oleh proteksi anti-bot Google (*Anti-Scraping Mechanisms*), batasan pencarian bawaan dikunci pada **50 hasil teratas per sesi**. Pengembangan ke skala produksi massal disarankan bermigrasi ke arsitektur *Asynchronous Background Job* (seperti Celery/Redis) dan integrasi database persisten.

---

## English

A standalone web application prototype (*Minimum Viable Product*) built with Python Flask and Selenium, designed to dynamically extract business entity data from Google Maps using multi-level location filters (Province/City).

This application is developed with a strict focus on clean-code architecture (*boilerplate*) and safe practices for demonstration, market research, or further development projects (*Proof of Concept*).

### ✨ Key Features

* **Dynamic Keyword Object:** Allows direct searching for any entity (e.g., Mosque, Grocery Store, Pharmacy).
* **Multi-Level Location Filter:** Target-oriented search mechanism filtered by Province down to City/Regency.
* **Automated Infinite Scroll:** Simulates browser automation to trigger Google Maps' lazy loading to capture dozens of data in real-time.
* **Admin Panel Dashboard:** Clean and intuitive Bootstrap-based interface for managing scraping operations.
* **Excel Data Export:** Instant feature to download extracted data results into a spreadsheet format (.xlsx) for deeper analysis.

### 🛠️ Tech Stack

* **Backend Framework:** Python Flask
* **Browser Automation:** Selenium WebDriver (Headless Mode)
* **Driver Management:** WebDriver Manager (Chrome)
* **Data Processing & Export:** Pandas & OpenPyXL
* **Frontend Interface:** HTML5, Jinja2 Templates, Bootstrap 5 (via CDN)

### 📁 Project Structure

```text
gmaps-scraper/
│
├── app.py                 # Main backend & Flask routing
├── scraper.py             # Core scraper logic & Browser automation
├── requirements.txt       # Project library dependencies
└── templates/
    ├── base.html          # Master Layout (Global Parent Framework)
    └── index.html         # Main Admin Dashboard Panel

```

### 🚀 Installation & Local Setup Guide

#### Prerequisites

Ensure your machine has Google Chrome and Python version 3.8 or above installed.

1. **Clone this Repository:**
```bash
git clone [https://github.com/your-username/gmaps-scraper.git](https://github.com/your-username/gmaps-scraper.git)
cd gmaps-scraper

```


2. **Install All Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the Server Application:**
```bash
python3 app.py

```


4. **Access the Dashboard:**
Open your browser and navigate to `http://127.0.0.1:5000`

### ⚠️ Prototype System Limitations (Disclaimer)

This application is developed strictly as an **MVP (Minimum Viable Product)**. To maintain server stability and prevent IP blocking by Google's anti-bot protection (*Anti-Scraping Mechanisms*), the default search limit is locked at the **top 50 results per session**. Upscaling to mass production architecture requires migrating to an *Asynchronous Background Job* workflow (such as Celery/Redis) paired with persistent database storage.

```

```