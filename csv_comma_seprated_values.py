import csv
from statistics import mean

with open('grades.csv') as f:
    reader = csv.reader(f)
    print(reader)
    for row in reader:
        #print(row)
        name = row[0]
        grades= list()

        for i in row[1:]:
            grades.append(int(i))

        print('average of %10s is %5.2f ' %(name,mean(grades)))
