# ==========================================================
# Nama : Azzam Prastianto
# NIM : J0403251153
# Kelas : A2
# ==========================================================
# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 
def pangkat(a, n): # Mendefinisikan fungsi pangkat(a,n)
    # Base case 
    if n == 0: # Jika n = 0
        return 1 # Kembalikan 1
    # Recursive case 
    return a * pangkat(a, n - 1) # Sama saja tetapi fungsi tersebut dipanggil lagi di dalam fungsinya 
print(pangkat(2, 4))  # Output: 16

# Base case: Berhenti ketika n = 0
# Recursive call: Memanggilkan fungsi itu sendiri di return a * pangkat(a, n - 1)