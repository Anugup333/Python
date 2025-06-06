try:
    inputfile = input("Enter the Source File Name ")
    with open(inputfile,'r') as cfp:
        outputfile = input("Enter the Destination File Name ")
        with open(outputfile,'w') as pfp:
            data = cfp.read()
            pfp.write(data)
            print(f"\n {inputfile} file data copied into the {outputfile}")
except FileNotFoundError:
    print("File Does not Exist : ")
