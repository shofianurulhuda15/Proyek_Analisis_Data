import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
def load_data():
    df = pd.read_csv('dashboard/main_data.csv')
    return df

df = load_data()

# Dashboard Title
st.title("Dashboard Interaktif Analisis Data Bike Sharing")

# Sidebar untuk Filter
day_filter = st.sidebar.selectbox("Pilih Hari:", ['Semua'] + sorted(df['dteday'].unique().tolist()))
hour_range = st.sidebar.slider("Pilih Rentang Jam:", 0, 23, (0, 23))
show_summary = st.sidebar.checkbox("Tampilkan Ringkasan Data")

# Filter Data
if day_filter != 'Semua':
    df = df[df['dteday'] == day_filter]
df = df[(df['hr'] >= hour_range[0]) & (df['hr'] <= hour_range[1])]

# Menampilkan Data
st.header("Ringkasan Data")
if show_summary:
    st.write(df.describe())

# Visualisasi Peminjaman Sepeda Berdasarkan Jam
st.header("Peminjaman Sepeda Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='hr', y='cnt', data=df, estimator='sum', ci=None, ax=ax)
ax.set_title('Peminjaman Sepeda Berdasarkan Jam')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Peminjaman')
ax.set_xticks(range(0, 24))
ax.grid()
st.pyplot(fig)

# Pengaruh Kondisi Cuaca terhadap Peminjaman
st.header("Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda")
selected_weather = st.selectbox("Pilih Kondisi Cuaca:", ['Semua'] + sorted(df['weathersit'].unique().tolist()))
if selected_weather != 'Semua':
    df = df[df['weathersit'] == selected_weather]
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='weathersit', y='cnt', data=df, ax=ax)
ax.set_title('Pengaruh Kondisi Cuaca terhadap Peminjaman Sepeda')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Jumlah Peminjaman')
ax.set_xticklabels(['1: Clear', '2: Mist', '3: Light Rain/Snow', '4: Heavy Rain/Snow'])
st.pyplot(fig)

# Perbandingan Peminjaman di Hari Kerja vs Akhir Pekan
st.header("Perbandingan Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='workingday', y='cnt', data=df, ax=ax)
ax.set_title('Perbedaan Peminjaman Sepeda di Hari Kerja vs. Akhir Pekan')
ax.set_xlabel('Hari (0: Akhir Pekan, 1: Hari Kerja)')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

st.write("Dashboard ini menyajikan analisis interaktif mengenai peminjaman sepeda berdasarkan berbagai faktor.")
