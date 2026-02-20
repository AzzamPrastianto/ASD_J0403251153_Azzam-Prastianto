# ==========================================================================
# Nama: Azzam Prastianto
# NIM: J0403251153
# Kelas: A2
# ==========================================================================
# Implementasi dasar: Queue
# ==========================================================================

# Konsep queue: First in First out

class Node:
    # Konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil/diinstalisasi
    def __init__(self,data):
        self.data = data # Menyimpan nilai atau data pada list
        self.next = None # Pointer ini menunjuk ke note berikutnya (awal = none)

class queue:
    # Buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None # Node paling depan
        self.rear = None # Node paling belakang
    
    def is_empty(self):
        return self.front is None 

    # Membuat fungsi untuk menambahkan data baru pada bagian paling belakang (rear)
    def enqueue(self,data):
        nodeBaru = Node(data)
        # Jika queue kosong, front dan rear merujuk pada node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # Jika queue tidak kosong, maka letakkan data baru setelah rear, dan jadikan
        self.rear.next = nodeBaru # Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru # Jadikan data baru sebagai rear

    def dequeue(self):
        # Menghapus data dari depan / front
        data_terhapus = self.front.data # Lihat data paling depan
        self.front = self.front.next # Geser front ke data berikutnya
        
        # Jika setelah geser front menjadi none, maka queue kosong
        # rear juga jadi none
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("front ->", end=' ')
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

# Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()