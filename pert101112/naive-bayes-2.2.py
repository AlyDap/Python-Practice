import streamlit as st

# 1. Membuat Header Web
# menambahkan gambar
from PIL import Image
img1 = Image.open("halaman.jpg")
st.image(img1)

st.write("""
         # Aplikasi Klasifikasi Kelulusan Mahasiswa
         ## Berbasis Web Menggunakan Streamlit       
""")

# 2. Membuat side bar
img2 = Image.open("header.png")
st.sidebar.image(img2, width=150)
st.sidebar.header("Inputan Atribut :")

# membuat inputan
nama = st.sidebar.text_input('Ketikkan Nama :', placeholder="ketikkan nama yang akan diprediksi")
jurusan = st.sidebar.selectbox("Pilih Jurusan",('0-Bahasa', '1-IPA', '2-IPS'), placeholder="pilih jurusan", index=None)
gender = st.sidebar.selectbox("Pilih Gender", ('0-PRIA', '1-WANITA'), placeholder="pilih gender", index=None)
sekolah = st.sidebar.selectbox("Pilih Asal Sekolah", ('0-LUAR', '1-PEKALONGAN'), placeholder="pilih asal kota sekolah", index=None)
sks = st.sidebar.selectbox("Pilih Jumlah SKS", ('0-Kurang18', '1-Lebih18'), placeholder="pilih jumlah sks", index=None)
asisten = st.sidebar.selectbox("Jadi Asisten", ('0-TIDAK', '1-YA'), placeholder="pernah jadi asisten", index=None)

st.sidebar.button("Prediksi", type="primary")

