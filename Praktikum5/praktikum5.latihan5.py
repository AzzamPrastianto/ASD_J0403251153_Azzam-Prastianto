# ==========================================================
# Nama : Azzam Prastianto
# NIM : J0403251153
# Kelas : A2
# ==========================================================
# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""): # Kita definisikan fungsi buat_pin()
 
    if len(hasil) == panjang: # Jika panjang hasil sama dengan "panjang"
        print("PIN:", hasil)  # Print "PIN:", hasil
        return 
 
    for angka in ["0", "1", "2"]: # Loop pilihan digit yang boleh dipakai
        buat_pin(panjang, hasil + angka) 
        # Memanggil fungsi lagi dengan menambahkan digit (0/1/2) ke string hasil saat ini
 
buat_pin(3) 

# base case: panjang string sudah = panjang pin
# rekursi: menambahkan digit 0,1,2
# banyak kombinasinya 3 pangkat panjang maka 3 pangkat 3 = 27 PIN

# Kita bisa mencegah angka yang sama muncul berulang dengan cara menambahkan pengecekan kondisi if angka not in hasil: di dalam perulangan for persis sebelum melakukan pemanggilan rekursif.