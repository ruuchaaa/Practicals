fname=input("enter file: ")
num=0

with open(fname,'r') as file:
    for line in file:
        words = line.split()
        num+=len(words)
print("NUMBER OF WORDS: ",num)