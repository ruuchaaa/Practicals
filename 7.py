class Calculator:
    def __init__(self):
        pass

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        if b == 0:
            raise ValueError("WRONG VALUE")
        return a/b

    def inp(self):
        a=float(input("Enter 1st numbeer: "))
        b = float(input("Enter 2nd numbeer: "))
        return a,b

    def calc(self):
        choice=input("Enter your choice of operation +,-,*,/: ")

        if choice == '+':
            a,b = self.inp()
            result = self.add(a,b)

        elif choice == '-':
            a,b = self.inp()
            result = self.sub(a,b)

        elif choice == '*':
            a,b = self.inp()
            result = self.mul(a,b)

        elif choice == '/':
            a,b = self.inp()
            result = self.div(a,b)

        else:
            print("INVALID CHOICE")

        print("THE RESULT IS:",result)

calculator=Calculator()
calculator.calc()