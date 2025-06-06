import mysql.connector as mysql
# how to connect the databese to python'
conn1 = mysql.connect(host='localhost',
                      port='3306',
                     password='Ramgup9393@',
                     user='root',
                     db='world')

# check the connection create successfully or not
if conn1.is_connected():
    print("Connection established")

# Print the connection id 
print("conn1 Connection id for conn1",conn1.connection_id)

# code to create a cursor without create this we
# can not use the database
cur = conn1.cursor()
cur.close()
conn1.close()