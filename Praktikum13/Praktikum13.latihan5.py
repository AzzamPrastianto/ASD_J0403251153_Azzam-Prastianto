# Nama : Azzam Prastianto 
# NIM : J0403251153
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree 

import heapq # Menggunakan Priority Queue (heap)

# Representasi graf (kota dan jalur beserta jaraknya)
graph = { 
    'Bogor': {'Jakarta': 5, 'Depok': 2}, 
    'Depok': {'Jakarta': 3, 'Bandung': 4}, 
    'Jakarta': {'Bandung': 6}, 
    'Bandung': {} 
} 

def prim(graph, start):
    visited = set([start]) # Catat kota yang sudah dikunjungi
    edges = [] # List untuk antrean jalur (edge)
    
    # Masukkan semua jalur dari kota awal ke dalam antrean
    for kota, jarak in graph[start].items(): 
        heapq.heappush(edges, (jarak, start, kota)) # Format antrean: (jarak, asal, tujuan)
        
    mst = []          # Simpan jalur-jalur yang terpilih masuk MST
    jarak_total = 0   # Total akumulasi jarak dari rute terpilih
    
    while edges: # Selama masih ada jalur dalam antrean
        jarak, u, v = heapq.heappop(edges) # Ambil jalur dengan jarak terpendek 
        
        if v not in visited: # Pastikan kota tujuan belum dikunjungi (mencegah siklus)
            visited.add(v) # Tandai kota sebagai sudah dikunjungi
            mst.append((u, v, jarak)) # Tambahkan jalur ini ke hasil rute MST
            jarak_total += jarak # Tambahkan jaraknya ke total keseluruhan
            
            # Cek kota tetangga dari kota yang baru saja dikunjungi
            for kota, jarak_baru in graph[v].items():
                if kota not in visited: # Jika kota tetangga belum dikunjungi
                    heapq.heappush(edges, (jarak_baru, v, kota)) # Masukkan ke antrean jalur

    return mst, jarak_total # Kembalikan daftar rute dan total jaraknya

# Jalankan fungsi dimulai dari kota Bogor
mst, total = prim(graph, 'Bogor') 

# Cetak hasil akhir
print("Minimum Spanning Tree:") 
for edge in mst:
    print(edge) 
print("Total jarak =", total)

# 1. Kasus apa yang dipilih? 
'''
Jaringan Jalan Antar Kota
'''
# 2. Algoritma apa yang digunakan? 
'''
Algoritma Prim karena jumlah edgenya tidak banyak sehingga
lebih efisien untuk menggunakan Algoritma Prim.
'''
# 3. Edge mana saja yang dipilih dalam MST? 
'''
~ Bogor - Depok
~ Depok - Jakarta
~ Depok - Bandung
'''
# 4. Berapa total bobot MST? 
'''
9
'''
# 5. Mengapa edge tertentu tidak dipilih? 
'''
Edge Bogor - Jakarta dan Jakarta - Bandung tidak dipilih karena 
kota tujuannya sudah dikunjungi melalui jalur lain yang harganya 
lebih murah.
'''