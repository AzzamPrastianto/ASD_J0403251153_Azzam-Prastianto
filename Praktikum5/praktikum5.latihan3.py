# ==========================================================
# Nama : Azzam Prastianto
# NIM : J0403251153
# Kelas : A2
# ==========================================================
# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0): # Definisikan fungsi cari_maks() dengan parameter data dan index = 0
 
    # Base case 
    if index == len(data) - 1: # Jika index sama dengan panjang data
        return data[index] # kembalikan data[index]
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) # maks sisa sama dengan funsi itu sendiri
 
    if data[index] > maks_sisa: # Jika isi dari index data lebih dari maks_sisa
        return data[index] # Kembalikan isi dari index data
    else: 
        return maks_sisa # Kembalikan maks_sisa
 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) 

# Base Case: Berhenti ketika index = len(data) - 1
# Recursive Call: Memanggil fungsi itu lagi dalam bentuk variabel bernama maks_sisa
 