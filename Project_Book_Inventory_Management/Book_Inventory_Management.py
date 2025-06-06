from tkinter import *
import tkinter.font as font
import mysql.connector as mysql
# --------------------------------------------------------- #
class mysqlConfiguaration():
    
    def __init__(self):
         print("Constrctor")
    
    def connect(self):
        self.myCon = mysql.connect(
            host = "localhost"
            user = "root"
            password = "Ramgup9393@"
        )
        return self.myCon
    
    def create_database(self,db = " "):
        mysqlobj = self.connect()
        cursor = mysqlobj.cursor()
        cursor.execute("Create Database IF NOT EXISTS "+db)
        cursor.execute("Show Databases")
        records = cursor.fetchall()
        print("-"*20)
        for i in records:
            print(i)
            print("-"*20)
        cursor.close()        
    
    def close_connection(self):
        mysqlcon = self.connect()
        print("Close the Connection ")
        mysqlcon.close()
        print("Connection close successfully ")

    def create_table(self, db = " ", table = " "):
        mysqlcon = self.connect()
        cursor = mysqlcon.cursor()
        cursor.execute("Use "+db)
        print("Using Databases "+db)
        cursor.execute("Create Table IF NOT EXISTS "+table+"(id INTEGER(100)\
             NOT NULL AUTO_INCREMENT PRIMARY KEY,\
               title text, author text, year integer, isbn integer ) ")
        print("Table is successfully created ")
        cursor.close()        

# --------------------------------------------------------------- #

class bookInventoryOperations(mysqlConfiguaration):

    def add_Book(self):
        pass
    
    def delete_Book(self):
        pass
    
    def update_Book(self):
        pass
    
    def clear_Entrybox(self):
        pass
    
    def insert(self):
        pass
    
    def get_selected_row(self):
        pass
    
    def show_Books(self):
        pass


# -------------------------------------------------------------- #

class DisplayGUI(bookInventoryOperations):
    
    def __init__(self):
        pass



# -------------------------------------------------------------- #

if __name__ == '__main__':
    pass
    