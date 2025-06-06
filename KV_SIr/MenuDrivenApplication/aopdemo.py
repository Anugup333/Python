from aopmenu import menu
from aopoperations import addop,subop,divop,mulop,modop,expoop
import sys
menu()
while True:
    ch = int(input("Enter the choice : "))
    match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            modop()
        case 6:
            expoop()
        case 7:
            print("Thank you for using the Menu Driven Appplication")
            print("="*50)
            sys.exit()  
        case _:
            print("="*50)
            print("Enter the corrcet Choice ")
            print("="*50)