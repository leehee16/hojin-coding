class Dict:
    def __init__(self) -> None:
        self.items = [None]*8

    def put(self,key,value):
        index = hash(key)%len(self.items)
        self.items[index] = value
    
    def get(self,key):
        index = hash(key)%len(self.items)
        return self.items[index]

my_dict = Dict()
my_dict.put('호진','13세')
my_dict.put('세영','12세')
print(my_dict.get('세영'))