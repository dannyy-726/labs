with open('customers-100.csv', 'r') as f:
    headers = f.readline().strip().split(sep=',')
    print(headers)

    for line in f:
        data = f.readline().strip().split(sep=',')
        print(data)


#part 2
import csv
with open('customers-100.csv', 'r') as f:
    reader = csv.reader(f)
    rows = [row[0:2] for row in reader]
    print(rows)

#part 3
import csv
with open('customers-100.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

