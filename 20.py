fname=input("enter file: ")
dname=input("enter file: ")

with open(fname,'r') as f:
    with open(dname, 'w') as d:
       d.write(f.read())
