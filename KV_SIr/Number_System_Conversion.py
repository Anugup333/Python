while(True):
    s="""-------------------------------------------------------------------
                                 Base Conversion Calculator
    ---------------------------------------------------------------------
                            1.   D to B
                                 D to O
                                 D to H
                            2.   B to D
                                 B to O
                                 B to H
                            3.   O to D
                                 O to B
                                 O to H
                            4.   H to D
                                 H to B
                                 H to O
                            5. Exit
    -----------------------------------------------------------------------"""
    print(s)
    
    ch = int(input("Enter the Choice that you want:  "))
    match(ch):
        case 1:
            d = int(input("Enter the Decimal Number : "))
            b = bin(d)
            o = oct(d)
            h = hex(d)
            print("\tDeciaml Number System Value= ",d)
            print("\tBinary Number System Value= ",b)
            print("\tOctal Number System Value= ", o)
            print("\tHexa Decimal Number System Value= ", h)
        case 2:
            b = input("Enter the Binary Number System Data preceded with 0b OR 0B:")
            d = int(b,2)
            o = oct(d)
            h = hex(d)
            print("\tBinary Number System Value= ",b)
            print("\tDeciaml Number System Value= ",d)
            print("\tOctal Number System Value= ", o)
            print("\tHexa Decimal Number System Value= ", h)
        case 3:
            o = input("Enter the Octal Number System Data preceded with 0o OR 0O:")
            d = int(o,8)
            b = bin(d)
            h = hex(d)
            print("\tOctal Number System Value= ", o)
            print("\tDeciaml Number System Value= ",d)
            print("\tBinary Number System Value= ",b)
            print("\tHexa Decimal Number System Value= ", h)
        case 4:
            h = input("Enter the Binary Number System Data preceded with 0x OR 0X:")
            d = int(h,16)
            b = bin(d)
            o = oct(d)
            print("\tHexa Decimal Number System Value= ", h)
            print("\tDeciaml Number System Value= ",d)
            print("\tBinary Number System Value= ",b)
            print("\tOctal Number System Value= ", o)
        case 5:
            break
        case _:
            print("Please Enter the Valid Choice ")