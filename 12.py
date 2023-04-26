class Cal:
    def __init__(self):
        pass
    def area(self,r):
        return 3.14*r*r

    def peri(self,r):
        return 2*3.14*r

r=int(input("enter r: "))


cal = Cal()

print("AREA IS: ",cal.area(r))
print("PERIMETER IS: ",cal.peri(r))
