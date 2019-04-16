import csv

f = open('laboratorium.csv','r')
reader = csv.reader(f)

for row in reader:
    print (row)

f.close()