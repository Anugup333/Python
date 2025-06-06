# ****** Find the Total Numbers in Subject and Its Percentage Of a Student ********

def proccess_file(name):
    file1 = open(name,"r")
    n = int(file1.readline())
    print("Total number of Students: ",n)
    for i in range(n):
        print(f"Student {i+1} : ",end="")
        allgrates = (file1.readline().split())
        print(allgrates)
        sum = 0
        for j in range(len(allgrates)):
            sum = sum + int(allgrates[j])
        per = float(sum/n)
        print(f"Total = {sum} \n Percentage = {per}")
        print("\n")
proccess_file("F_H_1.txt")
