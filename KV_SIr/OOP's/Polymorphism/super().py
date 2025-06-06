class Person:
    def __init__(self):  # Original Constructor 
        print("Person Constructor")
    
    def do(self):   # Original Method 
        print("Person Do")
    
    def person_work(self):
        print("Person work")


class Anuj(Person):
    def __init__(self):   # Overridden Constructor 
        super().__init__()
        print("Anuj Constructor ")
    
    def do(self):    # Overridden  Method 
        print("Anuj Do")
        super().do()
        super().person_work()

# main program 
a = Anuj(12,13)
a.do()