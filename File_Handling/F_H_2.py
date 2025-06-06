# ********* Find Largest Line in file F_H_2.txt *******

def Find_largest(name):
    file1 = open(name,"r")
    long = ""
    l = 0
    count = 0
    for line in file1:
        count += 1
        print(f"line no: {count}")
        print(line)
        print(f"NUmbers of Characters = {len(line)}")
        print("--------------------------------------------")
        if(len(line)>len(long)):
            long = line
    print(f"{long} is the Longest Line with {len(long)} Characters ")

Find_largest("F_H_2.txt")

            