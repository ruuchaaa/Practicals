class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("NAME: ",self.name)
        print("AGE: ",self.age)


class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks=marks

    def display(self):
        super().display()
        print("MARKS: ",self.marks)


name=input("ENTER NAME: ")
age=input("ENTER AGE: ")
marks=input("ENTER MARKS: ")

s=Student(name,age,marks)
s.display()