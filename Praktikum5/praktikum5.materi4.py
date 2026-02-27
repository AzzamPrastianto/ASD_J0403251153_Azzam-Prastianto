# ==========================================================
# Nama : Azzam Prastianto
# NIM : J0403251153
# Kelas : A2
# ==========================================================
# ========================================================== 
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ========================================================== 
def biner(n, hasil=""): # Kita definisikan fungsi biner(), parameter hasil menampung fungsi sementara
    # Base case: jika panjang string sudah n, cetak hasil 
    if len(hasil) == n: # Jika panjang hasil sama dengan n
        print(hasil) # Kita print hasil
        return
    # Choose + Explore: tambah '0' 
    biner(n, hasil + "0") # Memanggil fungsi itu sendiri dan ditambahkan 0
 
    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1") # Memanggil fungsi itu sendiri dan ditambahkan 1
 
biner(3) # Memanggil fungsi biner dengan n = 3

# Kode ini akan berjalan sampai panjang hasil sama dengan n