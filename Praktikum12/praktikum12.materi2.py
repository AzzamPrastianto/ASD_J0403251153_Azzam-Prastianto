# Mendefinisikan fungsi bellman_ford yang menerima graf dan node awal (start).
# Algoritma ini bisa menangani graf dengan bobot negatif (berbeda dengan Dijkstra).
def bellman_ford(graph, start): 
 
    # Membuat dictionary untuk menyimpan jarak minimum dari titik awal ke setiap node.
    # Semua jarak diinisialisasi dengan float('inf') (tak terhingga).
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari node awal ke dirinya sendiri diatur menjadi 0.
    distances[start] = 0 
 
    # Jalur terpendek pada graf tanpa siklus akan melewati maksimal (V - 1) edge/garis.
    # V adalah jumlah total node dalam graf (len(graph)).
    for _ in range(len(graph) - 1): 
 
        # Memeriksa setiap node yang ada di dalam graf satu per satu.
        for node in graph: 
 
            # Untuk setiap node, kita periksa semua tetangganya beserta bobot (jarak) ke tetangga tersebut.
            for neighbor, weight in graph[node].items(): 
 
                # Mengecek apakah jarak ke node saat ini (distances[node]) ditambah bobot ke tetangganya
                # lebih kecil (lebih singkat) daripada jarak ke tetangga yang tersimpan saat ini.
                if distances[node] + weight < distances[neighbor]: 
 
                    # Jika ditemukan jalur yang lebih singkat, perbarui jarak untuk node tetangga tersebut
                    # dengan total jarak yang baru (distances[node] + weight).
                    distances[neighbor] = distances[node] + weight 
 
    # Setelah perulangan relaksasi selesai sebanyak (V - 1) kali, 
    # kembalikan dictionary yang berisi jarak terpendek dari titik awal ke semua node.
    return distances