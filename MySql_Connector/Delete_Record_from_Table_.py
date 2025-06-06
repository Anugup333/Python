''' Write a program to delete record from the table 
'maruti' whose id is 3.
'''
import mysql.connector as mysql

try:
    mysqlobj = mysql.connect(host='localhost',
                              port='3306',
                              user='root',
                              password='Ramgup9393@',
                              database='Car_db')
    cursor = mysqlobj.cursor()
    cursor.execute("Select * from maruti ")
    records = cursor.fetchall()
    print("Total Number of records before deleting: ",cursor.rowcount)
    
    cursor.execute("Delete from maruti where Id = 3")
    mysqlobj.commit()
    
    cursor.execute("Select * from maruti")
    records = cursor.fetchall()
    print("Total Number of records after Deleting: ",cursor.rowcount)
except mysql.Error as error:
    print("Failed to Delete records from the table",error)
finally:
    if(mysqlobj.is_connected()):
        cursor.close()
        mysqlobj.close()
        print("Mysql connection is closed!")