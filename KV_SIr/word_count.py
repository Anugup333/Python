line = input("Enter the line : ")
if(line.isspace()):
    print("="*50)
    print("Don't enter the space for line of text ")
    print("="*50)
elif(len(line)==0):
    print("="*50)
    print("don't enter the empty line: ")
else:
    words = line.split()
    metadata_line = {}
    for word in words:
        metadata_line[word] = {"length":len(word),"no_times":words.count(word)}
    else:
        print("="*50)
        print("Printing the Mata data of the line ")
        for word in metadata_line:
            print("="*50)
            print(f"word = {word}\t ")
            print(f"length = {metadata_line[word]['length']}")
            print(f"No of times = {metadata_line[word]['no_times']}")
