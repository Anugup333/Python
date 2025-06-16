import csv
try:
    with open("citizen.csv",'r') as fp:
        csvr = csv.reader(fp)
        print(type(csvr))
        for record in csvr:
            print(type(record))
            for val in record:
                print(f"\t{val}",end="")
            print()
except FileNotFoundError:
    print("CSV File Does not Exist")
