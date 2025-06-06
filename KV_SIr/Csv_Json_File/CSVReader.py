import csv
try:
    with open("citizen.csv",'r') as fp:
        csvr = csv.reader(fp)
        for record in csvr:
            for val in record:
                print(f"\t{val}",end="")
            print()
except FileNotFoundError:
    print("CSV File Does not Exist")
