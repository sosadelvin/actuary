import streamlit as st

# Judul aplikasi
st.title("Aplikasi Streamlit Pertama Saya")

# Menambahkan teks dan input
st.write("Halo, selamat datang di aplikasi Streamlit!")
name = st.text_input("Masukkan nama Anda:")

# Menampilkan inputan
if name:
    st.write(f"Selamat datang, {name}!")