#Python Program to check if a Number is an Armstrong Number
def is_armstrong_num(n):
    num_digits = len(str(n))

    sum = 0
    for digit in str(n):
        sum += int(digit) ** num_digits

    if sum == n:
        return True
    else:
        return False

num = int(input("enter a number"))
if is_armstrong_num(num):
    print(num,"is an armstrong number")
else:
    print(num, "is not an armstrong number")