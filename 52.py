string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

common_letters = set(string1) & set(string2)

print("Common letters:", ', '.join(common_letters))
