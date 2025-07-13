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
    lambda_ = st.number_input("Rata-rata Kedatangan (λ pelanggan/jam)", value=8.0, step=0.1)
with col2:
    mu = st.number_input("Rata-rata Layanan (μ pelanggan/jam)", value=11.0, step=0.1)

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
    st.write(f"**W (Waktu di Sistem):** {W:.2f} jam")
    st.write(f"**Wq (Waktu Tunggu dalam Antrean):** {Wq:.2f} jam")

    # Visualisasi
    st.subheader("📉 Diagram Antrian (W dan Wq)")
    fig, ax = plt.subplots()
    ax.bar(["W (Sistem)", "Wq (Antrean)"], [W, Wq], color=["skyblue", "salmon"])
    ax.set_ylabel("Waktu (jam)")
    ax.set_title("Visualisasi Waktu Antrian")
    st.pyplot(fig)

else:
    st.error("❌ Nilai μ harus lebih besar dari λ agar sistem stabil (ρ < 1)")
