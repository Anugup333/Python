import csv
try:
    with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\citizen.csv","r") as fp:
        csvr=csv.reader(fp)
        for record in csvr:
            for val in record:
                print("{}".format(val),end="\t")
            print()
except FileNotFoundError:
    print("CSV File Does Not Exist")


#Program for Creating CSV File Dynamically
#DynamicCSVFileEx1.py
import csv
noc=int(input("Enter How Many Columns u have:"))
if(noc<=0):
    print("Invalid Number of Coluns")
else:
    colnames=[]
    for i in range(1,noc+1):
        colname=input("Enter {} Column Name:".format(i))
        colnames.append(colname)
    #colnames=['ENO', 'ENAME', 'SAL']
    nor=int(input("Enter How Many Records u have:"))
    if(nor<=0):
        print("Invalid Number of Records")
    else:
        records=[]
        for i in range(1,nor+1):
            print("-------------------------------")
            print("Enter {} Record Details".format(i))
            print("-------------------------------")
            record=[]
            for col in colnames:
                colval=input("Enter for Value for '{}'=".format(col))
                record.append(colval)
            records.append(record)
            print("-------------------------------")
        else:
            while(True):
                csvfilename=input("Enter File Name with an extension .csv :")
                if(csvfilename.endswith(".csv")):
                    with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\"+csvfilename,"w") as fp:
                        csvwr=csv.writer(fp)
                        csvwr.writerow(colnames)
                        csvwr.writerows(records)
                        print("CSV File Created Dynamically")
                        break
                else:
                    print("Invalid File Extension-try again")

