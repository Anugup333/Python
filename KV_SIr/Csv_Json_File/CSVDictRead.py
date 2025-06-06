# Step -1
import csv
# Step -2
try:
    # Step -3
    with open("citizen.csv",'r') as fp:
        # Step -4
        csvdr = csv.DictReader(fp)
        print("Type of the csvdr = ",type(csvdr))
        # Step -5
        for records in csvdr:
            for key,val in records.items():
                print(f"\t{key} -----> {val}",end="")
            print()
except FileNotFoundError:
    print("CSV File Not Exist Error")