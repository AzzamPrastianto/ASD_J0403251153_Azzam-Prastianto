# ==========================================================================
# Nama: Azzam Prastianto
# NIM: J0403251153
# Kelas: A2
# ==========================================================================
# Implementasi dasar: Stack
# ==========================================================================

class Node:
    # Konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil/diinstalisasi
    def __init__(self,data):
        self.data = data # Menyimpan nilai atau data pada list
        self.next = None # Pointer ini menunjuk ke note berikutnya (awal = none)

# Stack ada operasi push (memasukkan head baru) dan pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None # Menunjuk ke node paling atas (awalnya kosong)

    def push(self,data): # Memasukkan data baru pada stack
        #1 Membuat node baru
        nodeBaru = Node(data) # Instantiasi/memanggil konsruktor pada class Node

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 Geser top dan pindah ke node baru
        self.top = nodeBaru

        # B -> A -> None
    
    def is_empty(self):
        return self.top is None # Stack kosong jika Top = None

    def pop(self): # Mengambil atau menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack Kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data # Soroti bagian top dan simpan di variabel
        self.top = self.top.next # Geser top ke node berikutnya
        return data_terhapus 
    
    def peek(self):
        # Melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        # Top -> A -> B
        current = self.top
        print("Top", end=' -> ')
        while current is not None:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Instantiasi class
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print(f"Lihat Top: {s.peek()}")
s.pop()
s.tampilkan()
print(f"Lihat Top: {s.peek()}")
s.pop()
s.tampilkan()
print(f"Lihat Top: {s.peek()}")