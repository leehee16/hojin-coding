class LinkedTuple:
    def __init__(self) -> None:
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v
        return None

class Dict:
    def __init__(self) -> None:
        self.items = [None] * 8

class LinkedDict:
    def __init__(self) -> None:
        self.items = []
        for _ in range(8):
            self.items.append(LinkedTuple())
    
    def put(self,key,value) -> None:
        """
        값 삽입
        """
        index = hash(key)%len(self.items)
        self.items[index].add(key,value)
    
    def get(self,key):
        index = hash(key)%len(self.items)
        return self.items[index].get(key)
    
if __name__ == "__main__":
    ld = LinkedDict()
    ld.put('호진','33세')
    ld.put('4326','서대문구')
    print(ld.items)