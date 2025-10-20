class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self,value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    
    def print_all(self):
        cur = self.head
        while cur is not None:
            if cur.next is None:
                print(f"마지막입니다:{cur.data}")
            else : print(cur.data)
            cur = cur.next

linked_list = LinkedList(5)
linked_list.append(6)
linked_list.append(10)
linked_list.print_all()
