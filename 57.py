import sqlite3

conn = sqlite3.connect('employe.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS employes
            (id INTEGER PRIMARY KEY,
            name TEXT,
            salary REAL)''')


c.execute("INSERT INTO employes (id, name, salary) VALUES (1, 'John Smith', 50000.00)")
c.execute("INSERT INTO employes (id, name, salary) VALUES (2, 'Jane Doe', 60000.00)")
c.execute("INSERT INTO employes (id, name, salary) VALUES (3, 'Bob Johnson', 70000.00)")
c.execute("INSERT INTO employes (id, name, salary) VALUES (4, 'Alice Williams', 80000.00)")

conn.commit()

print("all employees: ")
c.execute("SELECT * FROM employes")
for row in c:
    print(row)


did = input("enter to del")
c.execute("DELETE FROM employes WHERE id=?",(did,))
print(c.rowcount)
conn.commit()

print("all employees: ")
c.execute("SELECT * FROM employes")
for row in c:
    print(row)


c.close()
conn.close()