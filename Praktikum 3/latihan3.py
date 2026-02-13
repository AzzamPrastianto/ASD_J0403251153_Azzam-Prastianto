# Latihan 3: Implementasikan pencarian pada node tertentu Double Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
            
        last.next = new_node
        new_node.prev = last

    def search(self, key):
        temp = self.head 
        while temp: 
            if temp.data == key: 
                return True 
            temp = temp.next 
        return False  

dll = DoublyLinkedList()
input_data = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")
data_list = [int(x.strip()) for x in input_data.split(',')]

for angka in data_list:
    dll.append(angka)
key = int(input("Masukkan elemen yang ingin dicari: "))

if dll.search(key):
    print(f"Elemen {key} ditemukan dalam Doubly Linked List")
else:
    print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List")     

