class Person:
    def __init__(self):
        pass
    def display(self,name,age):
        print("name: ",name)
        print("age: ",age)
    def inp(self):
        name=input("enter name: ")
        age=input("enter age: ")
        return name,age
p=Person()
name,age= p.inp()
p.display(name,age)