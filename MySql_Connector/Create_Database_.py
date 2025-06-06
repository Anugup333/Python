import mysql.connector as mysql
# create mysql connetor obj 
mysqlobj = mysql.connect(host='localhost',
                         port='3306',
                         user='root',
                         password='Ramgup9393@')
# Create Cursor obj
cursor = mysqlobj.cursor()

# Execute following mysql statement to create database
# cursor.execute("")

cursor.execute("Show Databases")

# 'fetchall' method fetches all the rows from the last executed sataemnt 

database = cursor.fetchall()

for db in database:
    print(db)

cursor.close()
mysqlobj.close()