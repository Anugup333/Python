import mysql.connector as mysql 

##------------------ Connecting MySQl ---------------------##

def connect_mysql():
    mysqlobj = mysql.connect(host='localhost',
                             port='3306',
                             user='root',
                             password='Ramgup9393@')
    print("Connected Successfully!")
    return mysqlobj

##------------------ Create Database -------------------##

def create_database(mysqlobj):
    cursor = mysqlobj.cursor()
    cursor.execute("Create Database IF NOT EXISTS Software_Industry")
    cursor.execute("Show databases")
    records = cursor.fetchall()
    print("List of Databases Present: ")
    print("-"*20)
    for r in records:
        print(r)
    print("-"*20)
    cursor.close()
    
##--------------- Close MySQl Connection -----------------##

def close_connection(mysqlobj):
    print("Closing Connection")
    mysqlobj.close()
    print("Connection Closed Successfully!")
    
##------------------ Create Table --------------------##

def create_table(mysqlobj, db = ' '):
    cursor = mysqlobj.cursor()
    cursor.execute("Use " + db)
    print("Using Database ",db)
    cursor.execute("Create table IF NOT EXISTS Employee_db(Id int(100) \
        NOT NULL AUTO_INCREMENT PRIMARY KEY, Emp_Name varchar(200),\
        Designation varchar(200), Salary decimal(20,2), Location varchar(120))")
    cursor.close()
    
##---------- Show List of Tables present in Database ---------##

def list_table(mysqlobj, db = ' '):
    cursor = mysqlobj.cursor()
    cursor.execute("Use " + db)
    cursor.execute("Show Tables")
    records = cursor.fetchall()
    print("List of Tables present in " + db)
    print("-"*20)
    for r in records:
        print(r)
    print("-"*20)
    cursor.close()
    
##----------------- Insert Record ------------------##

def insert_record(mysqlobj, db = ' ',table = ' '):
    cursor = mysqlobj.cursor()
    cursor.execute("Use " + db)
    
    Name = input("Please Enter Name of Employee: ")
    Designation = input("Please Enter Designation: ")
    Salary = float(input("Please Enter Salary: "))
    Loc = input("Please Enter Location: ")
    query = "INSERT INTO " + table + "\
            (Emp_Name, Designation, Salary, Location)\
            values (%s, %s, %s, %s)"
    values = [(Name, Designation, Salary, Loc)]
    cursor.executemany(query,values)
    mysqlobj.commit()
    cursor.close()
    
##----------------- Update Records -------------------##

def update_records(mysqlobj, db = ' ', table = ' '):
    cursor = mysqlobj.cursor()
    cursor.execute("Use " + db)
    print("1. Name")
    print("2. Designation")
    print("3. Salary")
    print("4. Location")
    ch = int(input("Please Enter the Choice to Update: "))
    if ch>=1 and ch<=4 :
        Id = int(input("Please Enter the Record Id to Update: "))
        boolean = find_id(Id , mysqlobj, db, table)
        if boolean != True:
            print("Invalid Id!!!")
            return None 
        
        elif ch == 1:
            Name = input("Please Enter Correct Name: ")
            query = "Update " + table + "\
                    set Emp_Name = %s where " + "Id = %s"
            values = (Name, Id)
            cursor.execute(query,values)
            mysqlobj.commit()
            print("Record Updated Successfully!")
            cursor.close()
        
        elif ch == 2:
            Designation = input("Please Enter Correct Designation: ")
            query = "Update " + table + "\
                    set Designation = %s where " + "Id = %s"
            values = (Designation, Id)
            cursor.execute(query,values)
            mysqlobj.commit()
            print("Record Updated Successfully!")
            cursor.close()
        
        elif ch == 3:
            Salary = float(input("Please Enter Correct Salary: "))
            query = "Update " + table + "\
                    set Salary = %s where " + "Id = %s"
            values = (Salary, Id)
            cursor.execute(query,values)
            mysqlobj.commit()
            print("Record Updated Successfully!")
            cursor.close()
        
        elif ch == 4:
            Location = input("Please Enter Correct Location: ")
            query = "Update " + table + "\
                    set Location = %s where " + "Id = %s"
            values = (Location, Id)
            cursor.execute(query,values)
            mysqlobj.commit()
            print("Record Updated Successfully!")
            cursor.close()
    else:
        print("Invalid Choice! ")
        display_records(mysqlobj, db, table)
            
##----------------- Delete Records --------------------#

def delete_records(mysqlobj, db = ' ', table = ' '):
    cursor = mysqlobj.cursor()
    cursor.execute("Use " + db)
    Id = int(input("Please Enter Id to Delete the Record: "))
    query = "Delete from " + table + "\
            where Id = %s"
    values = (Id,)
    boolean = find_id(Id, mysqlobj, db, table)
    if boolean == True:
        cursor.executemany(query, values)
        mysqlobj.commit()
        print("Record Deleted Successfully!")
        cursor.close()
    else:
        print("Invalid Id!!!")

##------------------ Display Records -------------------##

def display_records(mysqlobj, db = ' ', table = ' '):
    cursor = mysqlobj.cursor()
    cursor.execute("Use " + db)
    cursor.execute("Select * from " + table)
    records = cursor.fetchall()
    print("List of Records present in " + table)
    print("-"*20)
    print("Id\tName\tDesignation\tSalary\tLocation")
    for r in records:
        print(r[0],end='\t')
        print(r[1],end='\t')
        print(r[2],end='\t')
        print(r[3],end='\t')
        print(r[4])
    print("-"*20)
    cursor.close()
    
##------------------- Find Id --------------------##

def find_id(index, mysqlobj, db = ' ', table = ' '):
    List_Id = []
    cursor = mysqlobj.cursor()
    cursor.execute("Use " + db)
    cursor.execute("Select Id from " + table)
    records = cursor.fetchall()
    for r in records:
        List_Id.append(r[0])
    if index not in List_Id:
        print(index, "Id is not present in table ", table)
    else:
        return True
    
##----------------- Start Point of Program ----------------##

if '__main__':
    try:
        mysqlobj = connect_mysql()
        create_database(mysqlobj)
        create_table(mysqlobj, "Software_Industry")
        list_table(mysqlobj, "Software_Industry")
        print("1. Insert")
        print("2. Update")
        print("3. Delete")
        print("4. Display Records")
        print("5. Exit")
        ch = int(input("Please Enter Your Choice: "))
        while(ch !=5):
            if ch == 1:
                try:
                    insert_record(mysqlobj, "Software_Industry", "Employee_db")
                    print("Record Inserted Successfully!")
                except Exception as e:
                    print("Error: ",e)
            elif ch == 2:
                try:
                    display_records(mysqlobj, "Software_Industry", "Employee_db")
                    update_records(mysqlobj, "Software_Industry", "Employee_db")
                except Exception as e:
                    print("Error ",e)
            elif ch == 3:
                try:
                    display_records(mysqlobj, "Software_Industry", "Employee_db")
                    delete_records(mysqlobj, "Software_Industry", "Employee_db")
                    print("-"*20)
                    display_records(mysqlobj, "Software_Industry", "Employee_db")
                except Exception as e:
                    print("Error ",e)
            elif ch == 4:
                try:
                    display_records(mysqlobj, "Software_Industry", "Employee_db")
                except Exception as e:
                    print("Error ",e)
            elif ch == 5:
                try:
                    close_connection(mysqlobj)
                    break
                except Exception as e :
                    print("Error, ",e)
            else:
                print("Invalid Choice!! ")
    
            print("1. Insert")
            print("2. Update")
            print("3. Delete")
            print("4. Display Records")
            print("5. Exit")
            ch = int(input("Please Enter your Choice: "))
    except Exception as e:
        print(e)