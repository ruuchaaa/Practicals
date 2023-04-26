import sqlite3

conn = sqlite3.connect('student.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY,
            name,TEXT,
            marks,REAL)''')

c.execute("INSERT INTO students (id,name,marks) VALUES (1,'ru',100)")

c.execute("INSERT INTO students (id,name,marks) VALUES (2,'rru',90)")

c.execute("INSERT INTO students (id,name,marks) VALUES (3,'tu',60)")

c.execute("INSERT INTO students (id,name,marks) VALUES (4,'vu',80)")

conn.commit()

print("ALL EMPLOYEES: ")
c.execute("SELECT * FROM students")
for row in c:
    print(row)


did = input("enter id to delete")
c.execute("DELETE FROM students where id=?",(did,))
print(c.rowcount)

conn.commit()

print("ALL EMPLOYEES: ")
c.execute("SELECT * FROM students")
for row in c:
    print(row)