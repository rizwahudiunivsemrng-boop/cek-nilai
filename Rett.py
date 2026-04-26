import streamlit as st
st.set_page_config(layout="wide")

# Ini buat nampilin teks Sambutan & Logo ASCII kamu biar tetep ada di web
# Header & Tulisan Sambutan di Tengah
st.markdown("<h1 style='text-align: center;'>########## SELAMAT DATANG ##########</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>###### DI PROGRAM ANALISIS NILAI UAS ######</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>HALO! Selamat, Hasil UAS sudah keluar.</p>", unsafe_allow_html=True)

# Input Data lewat Sidebar (biar rapi di samping)
with st.sidebar:
    st.header("Input Identitas")
    Nama = st.text_input("Nama:")
    Umur = st.number_input("Umur:", min_value=0, step=1)
    Sekolah = st.text_input("Asal sekolah:")
    Mapel = st.text_input("Mapel:")
    Nilai = st.number_input("Nilai:", min_value=0.0, max_value=100.0)
    proses = st.button("Analisis Sekarang")

# Logika muncul setelah tombol diklik
if proses:
    st.markdown("---")
    st.subheader("=== DATA ===")
    st.write(f"**Nama:** {Nama}")
    st.write(f"**Sekolah:** {Sekolah}")
    st.write(f"**Mapel:** {Mapel}")

    st.subheader("=== Hasil Analisis ===")
    
    # Cek Umur
    if Umur >= 18:
        st.info("Status Umur: Dewasa")
    else:
        st.info("Status Umur: Remaja")

    # Cek Grade
    if Nilai >= 90.0:
        st.success("Grade: A Genius")
    elif Nilai >= 80.0:
        st.success("Grade: B Baik")
    elif Nilai >= 75.0:
        st.warning("Grade: C Cukup")
    else:
        st.error("Grade: D Tidak lulus")

    st.subheader("=== Kesimpulan ===")
    if Umur >= 18 and Nilai >= 75:
        st.write("✅ Kamu memenuhi syarat")
    elif Umur < 18 and Nilai >= 75:
        st.write("⚠️ Belum cukup umur")
    elif Umur >= 18 and Nilai < 75:
        st.write("📚 Perlu belajar lagi")
    else:
        st.write("⏳ Masih perlu waktu lagi ya")