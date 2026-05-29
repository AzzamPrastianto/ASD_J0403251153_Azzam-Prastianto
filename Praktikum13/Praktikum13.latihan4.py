# Nama : Azzam Prastianto 
# NIM : J0403251153
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree 

import heapq # Menggunakan Priority Queue (heap)

# Representasi graf (gedung dan jalur beserta harganya)
graph = { 
    'Gedung_A': {'Gedung_B': 4, 'Gedung_C': 2, 'Gedung_D': 5}, 
    'Gedung_B': {'Gedung_D': 3}, 
    'Gedung_C': {'Gedung_D': 1}, 
    'Gedung_D': {} 
} 

def prim(graph, start):
    visited = set([start]) # Catat gedung yang sudah dikunjungi
    edges = [] # List untuk antrean jalur (edge)
    
    # Masukkan semua jalur dari gedung awal ke dalam antrean
    for gedung, harga in graph[start].items(): 
        heapq.heappush(edges, (harga, start, gedung)) # Format antrean: (harga, asal, tujuan)
        
    mst = []          # Simpan jalur-jalur yang terpilih masuk MST
    total_harga = 0   # Total akumulasi harga pembangunan jalur
    
    while edges: # Selama masih ada jalur dalam antrean
        harga, u, v = heapq.heappop(edges) # Ambil jalur dengan harga termurah
        
        if v not in visited: # Pastikan gedung tujuan belum dikunjungi (mencegah siklus)
            visited.add(v) # Tandai gedung sebagai sudah dikunjungi
            mst.append((u, v, harga)) # Tambahkan jalur ini ke hasil MST
            total_harga += harga # Tambahkan harganya ke total pengeluaran
            
            # Cek gedung tetangga dari gedung yang baru saja dikunjungi
            for gedung, w in graph[v].items():
                if gedung not in visited: # Jika gedung tetangga belum dikunjungi
                    heapq.heappush(edges, (w, v, gedung)) # Masukkan ke antrean jalur

    return mst, total_harga # Kembalikan daftar jalur dan total harganya

# Jalankan fungsi dimulai dari Gedung_A
mst, total = prim(graph, 'Gedung_A') 

# Cetak hasil akhir
print("Minimum Spanning Tree:") 
for edge in mst:
    print(edge) 
print("Total biaya =", total)

# 1. Algoritma apa yang digunakan? 
'''
Algoritma Prim karena jumlah edgenya tidak banyak sehingga
lebih efisien untuk menggunakan Algoritma Prim.
'''
# 2. Edge mana saja yang dipilih? 
'''
~ Gedung_A - Gedung_C
~ Gedung_C - Gedung_D
~ Gedung_A - Gedung_B
'''
# 3. Berapa total biaya minimum? 
'''
7
'''
# 4. Mengapa MST cocok digunakan pada kasus ini? 
'''
Dikarenakan efisiensi budaya dan mencegah cycle.
'''