import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Model Antrian M/M/1", layout="centered")

st.title("📈 MODEL ANTRIAN – M/M/1")

st.markdown("""
**Fitur:**
- Input: rata-rata kedatangan (λ) dan layanan (μ)
- Output: nilai ρ (utilisasi), L, Lq, W, Wq
- Visualisasi diagram antrian

**Konsep:** Model Antrian M/M/1 – Sistem satu server dengan distribusi eksponensial
""")

# Input
col1, col2 = st.columns(2)
with col1:
    lambda_ = st.number_input("Rata-rata Kedatangan (λ pelanggan/jam)", value=9.0, step=0.1)
with col2:
    mu = st.number_input("Rata-rata Layanan (μ pelanggan/jam)", value=12.0, step=0.1)

# Fungsi bantu untuk format waktu
def format_waktu(w):
    if w < 1:
        return f"{w * 60:.2f} menit"
    else:
        return f"{w:.2f} jam"

# Validasi dan Perhitungan
if mu > lambda_:
    rho = lambda_ / mu                  # Utilisasi sistem
    L = rho / (1 - rho)                 # Rata-rata pelanggan dalam sistem
    Lq = rho**2 / (1 - rho)             # Rata-rata pelanggan dalam antrean
    W = 1 / (mu - lambda_)              # Waktu rata-rata dalam sistem
    Wq = lambda_ / (mu * (mu - lambda_))# Waktu rata-rata dalam antrean

    # Output
    st.subheader("📊 Hasil Perhitungan")
    st.write(f"**ρ (Utilisasi Sistem):** {rho:.2f}")
    st.write(f"**L (Pelanggan dalam Sistem):** {L:.2f}")
    st.write(f"**Lq (Pelanggan dalam Antrean):** {Lq:.2f}")
    st.write(f"**W (Waktu di Sistem):** {format_waktu(W)}")
    st.write(f"**Wq (Waktu Tunggu dalam Antrean):** {format_waktu(Wq)}")

    # Visualisasi
    st.subheader("📉 Diagram Antrian (W dan Wq)")

    # Tentukan satuan dan ubah nilai jika perlu
    if max(W, Wq) < 1:
        satuan = "menit"
        W_plot = W * 60
        Wq_plot = Wq * 60
    else:
        satuan = "jam"
        W_plot = W
        Wq_plot = Wq

    # Buat diagram batang
    fig, ax = plt.subplots()
    ax.bar(["W (Sistem)", "Wq (Antrean)"], [W_plot, Wq_plot], color=["skyblue", "salmon"])
    ax.set_ylabel(f"Waktu ({satuan})")  # Ini kini dinamis
    ax.set_title(f"Visualisasi Waktu Antrian dalam {satuan.capitalize()}")
    ax.set_ylim(bottom=0)
    st.pyplot(fig)


else:
    st.error("❌ Nilai μ harus lebih besar dari λ agar sistem stabil (ρ < 1)")
