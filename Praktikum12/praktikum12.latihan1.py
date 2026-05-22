# ========================================================== 
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ========================================================== 
# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
'A': {'B': 4, 'C': 2}, 
'B': {'D': 5}, 
'C': {'D': 1}, 
'D': {} 
} 
# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D'] 
jalur_2 = graph['A']['C'] + graph['C']['D'] 
print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 
  # A -> B -> D 
  # A -> C -> D 

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis:
 
# 1. Berapa total bobot jalur A -> B -> D?  
# Jawaban: 4 + 5 = 9

# 2. Berapa total bobot jalur A -> C -> D? 
# Jawaban: 2 + 1 = 3

# 3. Jalur mana yang dipilih sebagai jalur terpendek? 
# Jawaban: A -> C -> D

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
"""
Jawaban: Karena jika misalnya total bobot dari graph A dengan jumlah edge lebih sedikit
lebih besar dari dari bobot graph B yang memiliki edge lebih banyak, itu menandakan
bahwa graph B memiliki jalur terpendek meskipun dengan jumlah edge yang lebih sedikit.
"""