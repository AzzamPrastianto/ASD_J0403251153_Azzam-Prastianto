# -----------------------------------------------------
# Nama  : Azzam Prastianto
# NIM   : J0403251153
# Kelas : A2
# -----------------------------------------------------

# Latihan 1: Implementasikan fungsi untuk menghapus node dengan nilai tertentu.	
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

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next  
            temp = None            
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        print("List saat ini: ", end="")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
        
dll = DoublyLinkedList() 

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.display() 

dll.delete_node(20)
dll.display()
