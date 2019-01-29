import csv
#with open('grades.csv') as f:
f = open('grades.csv')
reader = csv.reader(f)
print(reader)
for row in reader :
    numbers = int(row[1:])
    name = row[0]
    print(numbers,name)
        