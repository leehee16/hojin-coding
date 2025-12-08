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
    def get_index(self,index):
        cur = self.head
        cur_index = 0
        while cur_index < index:
            cur = cur.next
            cur_index += 1
            if cur is None:
                return print("인덱스 범위를 초과하였습니다.")
        return cur
    
    def add_node(self,value,index):
        new_node = Node(value)
        prev_node = self.get_index(index-1)
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node




link_list=LinkedList(5)
link_list.append(3)
link_list.append(2)
#link_list.print_all()
link_list.add_node(11, 1)
link_list.print_all()
