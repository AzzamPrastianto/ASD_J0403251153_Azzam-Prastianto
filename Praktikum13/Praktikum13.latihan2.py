# Nama : Azzam Prastianto 
# NIM : J0403251153
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree 

# ========================================================== 
# Implementasi Sederhana Algoritma Kruskal 
# ========================================================== 
# Daftar edge: (bobot, node1, node2) 
edges = [ 
(1, 'C', 'D'), 
(2, 'A', 'C'), 
(3, 'B', 'D'), 
(4, 'A', 'B'), 
(5, 'A', 'D') 
] 

# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 
mst = [] 
total_weight = 0 
connected = set() 

for weight, u, v in edges: 
# Memilih edge yang tidak membentuk cycle sederhana 
   if u not in connected or v not in connected:
     mst.append((u, v, weight)) 
     total_weight += weight 
     connected.add(u) 
     connected.add(v) 
print("Minimum Spanning Tree:") 

for edge in mst: 
   print(edge) 
print("Total bobot =", total_weight) 
 

# 1. Edge mana yang dipilih pertama kali? 
'''
CD
'''
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
'''
Karena kita ingin mendapatkan hasil se-minimum mungkin dan
se-efisien mungkin.
'''
# 3. Berapa total bobot MST yang dihasilkan? 
'''
6
'''
# 4. Mengapa edge tertentu tidak dipilih? 
'''
Karena ada beberapa edge yang nodenya sudah terhubung (kedua nodenya).
'''