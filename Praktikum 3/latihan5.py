# Latihan 5: Tambahkan metode untuk membalik (reverse) tanpa membuat linked list baru
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertattheend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("null")

ll = LinkedList()

input_string = input("Masukkan elemen untuk Linked List (Kalau mau multiple pake koma): ")
data_list = [int(x.strip()) for x in input_string.split(',')]

for item in data_list:
    ll.insertattheend(item)

print("Linked List sebelum dibalik: ", end="")
ll.display()

ll.reverse()

print("Linked List setelah dibalik: ", end="")
ll.display()