def printRev(index, str):
    
    if index < 0:   # Base Case 
        return;
    print(str[index],end="")    
    printRev(index -1, str)
    

    
str = input("Enter the stringthat you reverse : ")
printRev(len(str)-1,str)
