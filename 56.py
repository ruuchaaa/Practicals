import sqlite3

# Create a connection to the database
conn = sqlite3.connect('employee.db')

# Create a cursor to execute SQL commands
c = conn.cursor()

# Create the employees table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INTEGER PRIMARY KEY,
              name TEXT,
              salary REAL)''')

# Insert some initial records
c.execute("INSERT INTO employees (id, name, salary) VALUES (1, 'John Smith', 50000.00)")
c.execute("INSERT INTO employees (id, name, salary) VALUES (2, 'Jane Doe', 60000.00)")
c.execute("INSERT INTO employees (id, name, salary) VALUES (3, 'Bob Johnson', 70000.00)")
c.execute("INSERT INTO employees (id, name, salary) VALUES (4, 'Alice Williams', 80000.00)")

# Commit the changes to the database
conn.commit()

# Display all the records in the employees table
print("All employees:")
c.execute("SELECT * FROM employees")
for row in c:
    print(row)

# Allow the user to delete a record by ID
delete_id = input("Enter the ID of the employee to delete: ")
c.execute("DELETE FROM employees WHERE id=?", (delete_id,))
if c.rowcount == 0:
    print("No employee with ID", delete_id, "found.")
else:
    print(c.rowcount, "employee(s) deleted.")

# Commit the changes to the database
conn.commit()

# Display all the records in the employees table again
print("\nRemaining employees:")
c.execute("SELECT * FROM employees")
for row in c:
    print(row)

# Close the cursor and connection
c.close()
conn.close()
