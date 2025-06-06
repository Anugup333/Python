# Step -1
import csv

colnames=["EMPNO","NAME","SAL"] # Step-2
# Step -3
records=[[111,"SrinuSri79",1.2],
        [222,"Pavan",1.2],
        [333,"Charan",1.5],
        [444,"KVR",0.0],
        [555,"Sharshad",1.3]]

# Step -4
with open('employee.csv' ,'a') as fp:
    # Step -5
    csvwrobj = csv.writer(fp)
    # Step -6  This is used to write the field row in the csv file
    csvwrobj.writerow(colnames)
    # Step -7
    csvwrobj.writerows(records)
    print("Csv File is Creted Successfully bu using the csv Writer ")
    
