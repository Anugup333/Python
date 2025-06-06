''' Write a program to fetch all records that we have 
    stored within the table 'maruti'
'''
import mysql.connector as mysql 

try:
    mysqlobj = mysql.connect(host='localhost',
                         port='3306',
                         user='root',
                         password='Ramgup9393@',
                         database='Car_db')
    cursor = mysqlobj.cursor()
    cursor.execute("Select * from maruti")
    records = cursor.fetchall()
    print("Total Number of records within maruti table are: ",cursor.rowcount)
    print("Records are as Follows: ")
    print("Id  Model_name\tPrice\tYear")
    for row in records:
        print(" ",row[0],end=" ")
        print(" ",row[1],end="\t")
        print(" ",row[2],end=" ")
        print(" ",row[3],end="\n")
    print("--------------------------")
except mysql.Error as error:
    print("Failed to read records from the table ",error)
finally:
    if(mysqlobj.is_connected()):
        cursor.close()
        mysqlobj.close()
        print("Mysql connection is closed")