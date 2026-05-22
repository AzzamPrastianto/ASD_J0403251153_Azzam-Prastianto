# Mengimpor modul bawaan heapq untuk membuat priority queue (antrean prioritas).
# Ini memastikan kita selalu memproses node dengan jarak terpendek lebih dulu.
import heapq 

# Mendefinisikan graf dalam bentuk dictionary bersarang (adjacency list).
# A' terhubung ke 'B' dengan bobot/jarak 4, dan ke 'C' dengan jarak 2.
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} # 'D' tidak memiliki tujuan ke mana pun
}

# Mendefinisikan fungsi Dijkstra yang menerima graf dan node awal (start)
def dijkstra(graph, start): 
    # Membuat dictionary untuk menyimpan jarak minimum dari titik awal ke setiap node.
    # Awalnya, semua jarak diatur menjadi float('inf') (tak terhingga) karena belum diketahui.
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari node awal ke dirinya sendiri 0.
    distances[start] = 0 
 
    # Membuat priority queue (pq) berisi daftar tuple (jarak, node).
    # 0 diletakkan di indeks pertama agar otomatis diurutkan dari jarak terkecil.
    pq = [(0, start)] 
 
    # Perulangan ini akan terus berjalan selama priority queue (pq) belum kosong.
    while pq: 
        # Mengambil dan menghapus node dengan jarak terkecil dari antrean pq.
        current_distance, current_node = heapq.heappop(pq) 
 
        # Melakukan iterasi untuk memeriksa semua tetangga dari node yang sedang diproses.
        for neighbor, weight in graph[current_node].items(): 
 
            # Menghitung total jarak dari titik awal ke node tetangga ini 
            # (jarak ke node saat ini + bobot jalan ke tetangganya).
            distance = current_distance + weight 
 
            # Jika total jarak yang baru saja dihitung lebih kecil (lebih cepat)
            # daripada jarak yang sudah tersimpan di dictionary distances:
            if distance < distances[neighbor]: 
 
                # Perbarui dictionary dengan jarak yang lebih kecil/baru tersebut.
                distances[neighbor] = distance 
 
                # Masukkan tetangga beserta jarak barunya ke dalam priority queue 
                # agar nantinya bisa ditelusuri lebih lanjut.
                heapq.heappush(pq, (distance, neighbor)) 
 
    # Setelah semua rute diperiksa dan antrean kosong, kembalikan hasil jarak terpendeknya.
    return distances 
 
# Menjalankan fungsi dijkstra menggunakan graf di atas dengan titik awal 'A'
hasil = dijkstra(graph, 'A') 

# Mencetak hasil akhirnya.
# Output yang diharapkan: {'A': 0, 'B': 4, 'C': 2, 'D': 3}
print(hasil)