import csv

ifile = input("enter input file name")
ofile = input("enter output file name")

rows = set()

with open(ifile, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        rows.add(tuple(row))

with open(ofile, 'w') as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow(row)

print("Duplicate values removed and saved to", ofile)