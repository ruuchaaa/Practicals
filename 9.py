try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    result = a/b
    print("RESULT:",result)
except ValueError:
    print("wrong value")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print("theres an error",e)