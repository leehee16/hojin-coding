# python object oriented programming practice

#class Person:
#    pass
#p = Person()
#print(p)
# 출력 : <__main__.Person object at 0x105649ca0>

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

p1 = Person("Hojin", 30)
p1.say_hello()