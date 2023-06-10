import pandas as pd
# Membaca data set pH air dari file CSV
data_air = pd.read_csv("data_air.csv")
# Membaca data set pH tanah dari file CSV
data_tanah = pd.read_csv("data_tanah.csv")

def rekomendasi_tanaman(ph_air_input, ph_tanah_input):
    rekomendasi = []
    for index, row in data_air.iterrows():
        tanaman = row["Nama Tanaman"] 
        ph_air_min, ph_air_max = row["pH Air Optimal Min"], row["pH Air Optimal Max"]
        ph_tanah_min, ph_tanah_max = data_tanah.loc[index, "pH Tanah Optimal Min"], data_tanah.loc[index, "pH Tanah Optimal Max"]
        if ph_air_input >= float(ph_air_min) and ph_air_input <= float(ph_air_max) and \
           ph_tanah_input >= float(ph_tanah_min) and ph_tanah_input <= float(ph_tanah_max):
            rekomendasi.append(tanaman)
    
    return rekomendasi

# Loop input pengguna
while True:
    # Input pH air dan pH tanah
    ph_air_input = float(input("Masukkan pH air: "))
    ph_tanah_input = float(input("Masukkan pH tanah: "))

    # Mendapatkan rekomendasi tanaman
    rekomendasi = rekomendasi_tanaman(ph_air_input, ph_tanah_input)

    # Menampilkan rekomendasi
    if len(rekomendasi) > 0:
        print("Tanaman yang direkomendasikan untuk pH air", ph_air_input, "dan pH tanah", ph_tanah_input, ":")
        for tanaman in rekomendasi:
            print("-", tanaman)
    else:
        print("Tidak ada tanaman yang direkomendasikan untuk pH air", ph_air_input, "dan pH tanah", ph_tanah_input)
    
    berhenti = input("ENTER untuk rekomendasi lain STOP untuk berhenti :")
    if berhenti.lower() == "stop":
        break
