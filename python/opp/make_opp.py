class Person :
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def print_name(self) :
        print(self.name)

hojin = Person('호진',30)
hojin.print_name()