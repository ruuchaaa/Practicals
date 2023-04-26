#Write a program to Catch exception in a function.
def divide():
    try:
        a = float(input("enter a"))
        b = float(input("enter b"))
        result = a / b
    except ZeroDivisionError:
        print("Error: division by zero")
        result = None
    except ValueError:
        print("Error: Invalid input")
        result = None
    except:
        print("An unknown error occurred.")

    return result

# Test the divide() function

print(divide())