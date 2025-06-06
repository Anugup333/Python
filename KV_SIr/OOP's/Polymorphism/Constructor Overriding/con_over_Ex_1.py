class Test:
    def __init__(self):   # Original Constructor
        print("Test Class Constructor ")


class Sample(Test): 
    def __init__(self):  # Overridden Constructor
        super().__init__()
        print("Sample Class Constructor ")

# main program
s = Sample()
