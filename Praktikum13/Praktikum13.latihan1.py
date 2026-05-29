# Nama : Azzam Prastianto 
# NIM : J0403251153
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree 

# Daftar edge graph 
edges = [ 
('A', 'B'), 
('A', 'C'), 
('A', 'D'), 
('C', 'D'), 
('B', 'D') 
] 
# Spanning tree 
spanning_tree = [ 
('A', 'C'), 
('C', 'D'), 
('D', 'B') 
] 
print("Edge pada graph:") 
for edge in edges:
    print(edge) 
print("\nSpanning Tree:") 
for edge in spanning_tree: 
    print(edge) 
print("\nJumlah edge graph =", len(edges)) 
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis: 
# 1. Apa perbedaan graph awal dan spanning tree? 
'''
Graph memiliki 5 edge sedangkan spanning tree memiliki 3.
'''
# 2. Mengapa spanning tree tidak boleh memiliki cycle? 
'''
Karena tree hanya boleh mempunyai satu arah. 
'''
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
'''
Karena hanya memiliki satu arah (tidak memiliki cycle).
''' 