# ========================================================== 
# Latihan 5: Studi Kasus dengan Program Shortest Path 
# Algoritma: Dijkstra 
# ========================================================== 
import heapq 
# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
'Bogor': {'Jakarta': 5, 'Depok': 2}, 
'Jakarta': {'Bandung': 7}, 
'Depok': {'Jakarta': 2, 'Bandung': 6}, 
'Bandung': {}
} 
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
    priority_queue = [(0, start)] 
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
        if current_distance > distances[current_node]: 
            continue 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
    return distances 
hasil = dijkstra(graph, 'Bogor') 
print("Jarak terpendek dari Bogor:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "jam") 

# Jawaban Analisis: 
# 1. Node awal yang digunakan apa? 
# Jawaban: Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal? 
# Jawaban: Depok

# 3. Node mana yang memiliki jarak paling besar dari node awal? 
# Jawaban: Bandung

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat. 
# Jawaban:
# Algoritma mencari rute tercepat secara bertahap (greedy) dari node Bogor:
# 1. Mulai dari Bogor (0), rute langsung ke Depok (2) dan Jakarta (5).
# 2. Karena Depok (2) lebih kecil, algoritma memproses Depok terlebih dahulu.
# 3. Dari Depok, rute ke Jakarta butuh +2 (total 2+2=4), dan ke Bandung butuh +6 (total 2+6=8).
# 4. Jarak ke Jakarta yang awalnya 5 (langsung dari Bogor) diperbarui menjadi 4 karena melewati Depok ternyata lebih cepat.
# 5. Algoritma kemudian memproses Jakarta (jarak 4). Dari Jakarta ke Bandung butuh +7 (total 4+7=11). Karena rute ini lebih lambat dari rute sebelumnya (8), maka diabaikan.
# 6. Hasil akhir: Depok terdekat (2), disusul Jakarta (4, lewat Depok), dan Bandung terjauh (8, lewat Depok).