class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.top is None:
            raise IndexError('Stack is empty')
        result = self.top
        self.top = result.next
        self.size -= 1
        return result.data
    
    def __len__(self):
        return self.size

    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return f"Stack:[{" -> ".join(items)}] "

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push("안녕")
    stack.push("push")
    print(stack.pop())
    print(stack)