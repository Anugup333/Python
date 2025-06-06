
def show(*value):
    print('='*50)
    for val in value:
        print(f"\t{val}",end="")
    print()
    print('='*50)


# main program
show()
show(10)
show(10,20)
show(10,20,30)
show(10,20,30,40)
show('python','java','Django','DS')