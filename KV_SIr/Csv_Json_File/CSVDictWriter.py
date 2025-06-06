# Step 1
import csv
# Step - 2
colnames=["CID","CNAME","ADDR"] # Step-2
# Step - 3
records=[{"CID":100,"CNAME":"Mansi","ADDR":"MH"},
         {"CID":200,"CNAME":"Uma","ADDR":"TS"},
         {"CID":300,"CNAME":"Prajwala","ADDR":"MH"},
         {"CID":400,"CNAME":"Sneha","ADDR":"AP"}]

# Step - 4
with open("citizen.csv",'a') as fp:
    # Step -5
    csvdwrobj = csv.DictWriter(fp,fieldnames=colnames)
    # Step -6 used to write the header of the file
    csvdwrobj.writeheader()
    # Step -7 Write the rows in the csv file 
    csvdwrobj.writerows(records)
    print("CSV File Created With Dict Data ")