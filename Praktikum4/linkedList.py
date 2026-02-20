# ==========================================================================
# Nama: Azzam Prastianto
# NIM: J0403251153
# Kelas: A2
# ==========================================================================
# Implementasi dasar: Nama pada Linked List
# ==========================================================================
class Node:
    # Konstruktor yg dijalankan secara otomatis ketika class Node dipanggil/diinstantiasi
    def __init__(self,data):
        self.data = data # Menyimpan nilai atau data pada list
        self.next = None # Pointer ini menunjuk ke note berikutnya (awal = none)

# Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# Menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC
# Traversal: Menelusuri Node dari head sampai ke None
current = head
while current is not None:
    print(current.data) # Menampillkan data pada node saat ini
    current = current.next # Pindah ke node berikutnya

