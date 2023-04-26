m1=int(input("ENTER MARKS FOR SUB 1: "))
m2=int(input("ENTER MARKS FOR SUB 2: "))
m3=int(input("ENTER MARKS FOR SUB 3: "))
m4=int(input("ENTER MARKS FOR SUB 4: "))
m5=int(input("ENTER MARKS FOR SUB 5: "))
t=m1+m2+m3+m4+m5
p=(t/500)*100

if p>=90:
    print("STUDENT SCORED",p,"GRADE A")

elif p>=80:
    print("STUDENT SCORED",p,"GRADE B")

elif p >= 70:
    print("STUDENT SCORED",p,"GRADE C")

elif p>=60:
    print("STUDENT SCORED",p,"GRADE D")

elif p>=50:
    print("STUDENT SCORED",p,"GRADE E")

else:
    print("STUDENT SCORED",p,"FAIL")

