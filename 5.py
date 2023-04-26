#Python Program to check if a Substring is Present in a Given String.
def is_sub_present(s,sub):
    if sub in s:
        return True
    else:
        return False

s = input("enter a string")
sub = input("enter a substring")

if is_sub_present(s,sub):
    print(sub,"present in string",s)

else:
    print(sub,"not present in string",s)