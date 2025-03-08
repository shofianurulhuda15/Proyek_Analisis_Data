# Proyek_Analisis_Data
# 🚴‍♀️ Bike Sharing Dashboard

Dashboard interaktif untuk menganalisis tren peminjaman sepeda berdasarkan dataset Bike Sharing. Proyek ini dikembangkan sebagai bagian dari submission Dicoding.

## 📦 Persiapan Lingkungan
Sebelum menjalankan dashboard, pastikan Python sudah terinstall di sistem kamu.

### 🔹 Menggunakan Anaconda
```bash
conda create --name bike-sharing python=3.9
conda activate bike-sharing
pip install -r requirements.txt
```

### 🔹 Menggunakan Virtual Environment (venv)
```bash
python -m venv env
source env/bin/activate  # Untuk macOS/Linux
env\Scripts\activate    # Untuk Windows
pip install -r requirements.txt
```

## 🚀 Menjalankan Dashboard
Setelah mengatur lingkungan, jalankan perintah berikut untuk membuka dashboard:
```bash
streamlit run dashboard.py
```

Dashboard akan berjalan di browser dengan alamat default:
```
http://localhost:8501
```

## 📑 Struktur Proyek
```
proyek_analisis_data/
│-- dashboard/
│   │-- dashboard.py  # File utama Streamlit
│   │-- main_data.csv # Dataset utama
│   │-- requirements.txt # Dependencies untuk Streamlit
│
│-- data/
│   │-- day.csv  # Data harian
│   │-- hour.csv # Data per jam
│   │-- Readme.txt  # Keterangan tambahan
│
│-- notebook.ipynb  # Notebook untuk eksplorasi & analisis data
│-- README.md  # Dokumentasi proyek
│-- requirements.txt  # Daftar dependensi
```

## 🛠️ Dependencies
Beberapa pustaka utama yang digunakan dalam proyek ini:
- pandas
- numpy
- seaborn
- matplotlib
- streamlit

Semua pustaka dapat diinstal menggunakan perintah:
```bash
pip install -r requirements.txt
```

## 🎯 Fitur Dashboard
- **Analisis jam peminjaman sepeda** 📊
- **Perbandingan peminjaman berdasarkan kondisi cuaca** ☀️🌧️
- **Perbedaan tren peminjaman pada hari kerja vs. akhir pekan** 🗓️

Selamat mencoba! 🚀

