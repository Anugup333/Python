rom_num = input("Enter the Roman that you find to Digit: ")
if (len(rom_num) == 0 or 'CCCC' in rom_num or 'XXXX' in rom_num or 'IIII' in rom_num):
    print("="*50)
    print(f"{rom_num} This is not a valid Roman Number Plase Enter the valid Roman Number")
else:
    digit = 0
    num = list(rom_num)
    print(num)
    while len(num) >=1 and num[0] ==  "M":
        digit += 1000
        del num[0]
    if len(num) >=2 and num[0] == 'C' and num[1] == "M" :
        digit += 900
        del num[0:2]
    if len(num) >=1 and num[0]== "D":
        digit += 500
        del num[0]
    if len(num) >=2 and num[0] == "C" and num[1] == "D":
        digit += 400
        del num[0:2]
    while len(num) >=1 and num[0] == "C":
        digit += 100
        del num[0]
    if len(num) >=2 and num[0] == "X" and num[1] == "C":
        digit += 90
        del num[0:2]
    if len(num) >=1 and num[0] =="L":
        digit += 50
        del num[0]
    if len(num) >=2 and num[0] == "X" and num[1] == "L":
        digit += 40
        del num[0:2]
    while len(num) >=1 and num[0] == "X":
        digit += 10
        del num[0]
    if len(num) >=2 and num[0] == "I" and num[1] == "X":
        digit += 9
        del num[0:2]
    if len(num) >=1 and num[0] =="V":
        digit += 5
        del num[0]
    if len(num) >=2 and num[0] == "I" and num[1] == "V":
        digit += 4
        del num[0:2]
    while len(num) >=1 and num[0] == "I":
        digit += 1
        del num[0]
    if(len(num) == 0):
        print(f"{rom_num} = {digit}")
    else:
        print("="*50)
        print(f"{rom_num} This is not a valid Roman Number Plase Enter the valid Roman Number")
        