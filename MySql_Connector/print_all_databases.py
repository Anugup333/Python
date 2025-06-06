import mysql.connector as mysql
mysqlobj = mysql.connect(host='localhost',
                      port='3306',
                     password='Ramgup9393@',
                     user='root')

cursor = mysqlobj.cursor()

# Execute mysql statement "show Databases" using execute method
cursor.execute("show databases")

# 'fetchall()' method fetches all the rows from the 
# last executed statement 
databases = cursor.fetchall()

# iterate and print the list of databases 
for db in databases:
    print(db)