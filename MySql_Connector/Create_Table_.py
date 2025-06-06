import mysql.connector as mysql 
mysqlobj = mysql.connect(host='localhost',
                         port='3306',
                         user='root',
                         password='Ramgup9393@',
                         database='Car_db') 
# Select databse in order to create table into it

cursor = mysqlobj.cursor()

# Create Table "maruti" with the primary key id 

cursor.execute("Create Table IF NOT EXISTS \
               maruti(Id int(100) NOT NULL AUTO_INCREMENT PRIMARY KEY,\
               Model_name varchar(250),Price decimal(10,4),\
                Lauch_year year(4))")

cursor.execute("Show tables")
# 'fetchall' method fetches all the rows from the last executed statement
tab = cursor.fetchall()

for t in tab:
    print(t)

cursor.close()
mysqlobj.close()