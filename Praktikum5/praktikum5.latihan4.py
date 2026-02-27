# ==========================================================
# Nama : Azzam Prastianto
# NIM : J0403251153
# Kelas : A2
# ==========================================================
# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
 # Base case: Jika panjang dari hasil sama dengan n, print hasil
    if len(hasil) == n: 
        print(hasil) 
        return 
 
    kombinasi(n, hasil + "A") # Memanggil fungsi itu sendiri dan ditambahkan A
    kombinasi(n, hasil + "B") # Memanggil fungsi itu sendiri dan ditambahkan B
 
 
kombinasi(2)  # Memanggil fungsi kombinasi dengan n = 3

# Jumlah kombinasi dihasilkan dengan cara memanggil fungsi kombinasi() yang ada di dalamnya hingga panjang dari hasil sama dengan n