import streamlit as st
import pandas as pd
from joblib import load

# Memuat model yang telah dilatih
model = load('/content/drive/MyDrive/Skripsi 2/trained_model.joblib')

st.title("Prediksi Harga Emas")

# Membuat form untuk input data
with st.form("prediction_form"):
    st.write("Silakan masukkan informasi berikut:")
    ihsg = st.number_input("Nilai IHSG", value=6000.0)
    usd_rate = st.number_input("Nilai Kurs USD", value=14000.0)
    inflation = st.number_input("Tingkat Inflasi", value=3.0)
    
    # Tombol untuk melakukan prediksi
    submit_button = st.form_submit_button("Prediksi")

if submit_button:
    # Menyiapkan data untuk prediksi
    input_data = pd.DataFrame([[ihsg, usd_rate, inflation]], columns=['IHSG', 'Kurs Jual', 'Data Inflasi'])
    
    # Melakukan prediksi menggunakan model
    prediction = model.predict(input_data)
    
    # Menampilkan hasil prediksi
    st.write(f"Prediksi harga emas: Rp{prediction[0]:,.2f}")
