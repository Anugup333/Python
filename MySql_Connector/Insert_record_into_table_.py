import mysql.connector as sql 

try:
    mysqlobj = sql.connect(host='localhost',
                         port='3306',
                         user='root',
                         password='Ramgup9393@',
                         database='Car_db') 
    # Select databse in order to create table into it

    cursor = mysqlobj.cursor()
    
    query = "INSERT INTO maruti (Model_name, Price, Lauch_year)\
             values(%s,%s,%s)"
    
    # Storing values in a variable 
    values = [('Wagon R',600000.00,'1999'),
              ('Alto',400000.00,'2012'),
              ('Ritz',550000.00,'2016'),
              ('Baleno',800000.00,'2017')]
    
    # insert Multiple values at once
    cursor.executemany(query,values)
    # To Update the changes, execute commit() method of the connection object.
    mysqlobj.commit()
    print(cursor.rowcount," Records inserted successfully into maruti table")
except sql.Error as error:
    print("Failed to insert record into Mysql Table",error)
finally:
    if(mysqlobj.is_connected()):
        cursor.close()
        mysqlobj.close()
        print("Mysql connection is closed")
