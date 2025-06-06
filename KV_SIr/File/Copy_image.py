try:
    inputfile = input("Enter the Source File Name ")
    with open(inputfile,'rb') as cfp:
        outputfile = input("Enter the Destination File Name ")
        with open(outputfile,'wb') as pfp:
            data = cfp.read()
            pfp.write(data)
            print(f"\n {inputfile} Image copied into the {outputfile}")
except FileNotFoundError:
    print("File Does not Exist : ")
