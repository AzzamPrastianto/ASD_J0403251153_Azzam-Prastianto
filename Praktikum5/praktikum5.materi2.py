# ==========================================================
# Nama : Azzam Prastianto
# NIM : J0403251153
# Kelas : A2
# ==========================================================
# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 
def hitung(n): # Mendefinisikan hitung()
    # Base case 
    if n == 0: # Jika n = 0
        print("Selesai") # print selesai 
        return 
    
    print("Masuk:", n)   # Dia akan mengoutput "Masuk: 3" 
    hitung(n - 1) # Memanggil fungsi dan mengoutput "Masuk: 2" hingga mengoutput "Selesai"           
    print("Keluar:", n) # Setelah itu, dia akan mengoutput "Keluar: 1" hingga "Keluar: 3"
     
hitung(3) # Memanggil fungsi hitung(3)
