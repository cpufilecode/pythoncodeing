import csv
from email import header

f=open("filecsv.csv")
data.csv.reader(f)
header=next(data)
print(header) 
for row in data:
    print(row)
f.close()