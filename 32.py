class Student:
    def __init__(self):
        pass

    def display(self,name,age,marks):
        print("NAME: ",name)
        print("AGE: ",age)
        print("MARKS: ",marks)

    def inp(self):
        name = input("ENTER NAME: ")
        age = input("ENTER AGE: ")
        marks = input("ENTER MARKS: ")
        return name,age,marks
s=Student()
name,age,marks=s.inp()
s.display(name,age,marks)
