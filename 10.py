#import shutil

#shutil.copyfile("input.txt", "output.txt")


with open("input.txt","r") as ip:
    with open("output.txt","w") as op:
        op.write(ip.read())