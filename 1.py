#Python Program to Calculate the Average of Numbers in a Given List.
def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total/count
    return avg

numbers = input("Enter numbers seperarted by commas")
numbers_list = [float(num) for num in numbers.split(",")]
avg = average(numbers_list)
print("average is :",avg)