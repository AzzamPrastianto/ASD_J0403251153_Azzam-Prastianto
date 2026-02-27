# ==========================================================
# Nama : Azzam Prastianto
# NIM : J0403251153
# Kelas : A2
# ==========================================================

# ========================================================== 
# Contoh Rekursi 1: Faktorial 
# ========================================================== 
def faktorial(n): 
# Base case: berhenti ketika n = 0 
    if n == 0: 
        return 1 
# Recursive case: masalah diperkecil menjadi faktorial(n-1) 
    return n * faktorial(n - 1) 
print(faktorial(5))  # Output: 120 

'''
Disini dijelaskan bahwa base case atau patokan dari n
adalah 0, dan jika n = 0, maka akan mengembalikan 1. 
Sementara itu, Recursive casenya akan mengembalikan n * faktorial(n-1)
yang artinya dia akan mengembalikan 4 * 3 * ..... hingga n sama dengan 0.
'''
