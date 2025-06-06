def filter_alphabets():
    # input as the string 
    line = input("Enter the line of text: ")
    alphabets = list(filter(lambda ch: ch.isalpha() ,line ))
    return "".join(alphabets)

# print("Filter the alphabets : ",filter_alphabets())
    
    
def filter_pos_val():
    # input the values 
    return list(filter(lambda num: num>=0,[int(i) for i in input("Enter Value ").split()]))

print("Filter the Positive Val: ",filter_pos_val())