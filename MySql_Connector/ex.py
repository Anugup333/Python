''' Write a program to update record present within the table 
    'maruti'. Update price as 500000.00 for id = 3
'''
import mysql.connector as mysql

try:
    mysqlobj = mysql.connect(host='localhost',
                              port='3306',
                              user='root',
                              password='Ramgup9393@',
                              database='Car_db')
    cursor = mysqlobj.cursor()
    cursor.execute("Select * from maruti where Id = 4")
    record = cursor.fetchone()
    print(record)
    
    Model_name = "Suzuki"
    Id = 4
    values = "Model_name"+ str(Id)
    query = "Update maruti set Model_name = %s "+"where Id = %s"
    cursor.executemany(query,values)
    # To Update the changes, execute commit() method of the connection object.
    mysqlobj.commit()
    print("Record Updated Successfully! ")
    
    print("After Updating Record")
    cursor.execute("Select * from maruti where Id = 4")
    record = cursor.fetchone()
    print(record)

except Exception as e:
    print("Failed to Update record into the table ",e)

finally:
    if(mysqlobj.is_connected()):
        cursor.close()
        mysqlobj.close()
        print("MySql connection is closed!")