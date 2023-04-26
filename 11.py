def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

num = int(input("ENTER A NUMBER: "))
if num < 0:
    print("factorial doesnt exist")
elif num == 0:
    print("factorial is 1")
else:
    print("Factorial is: ",fact(num))