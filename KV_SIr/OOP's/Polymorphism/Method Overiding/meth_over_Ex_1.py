class Dog:  
    def noise(self):  # Original Method
        print("Dog makes a noise as BOW BOW ")
        
class Cat(Dog):  
    def noise(self):  # Overridden Method
        super().noise()
        print("Cat makes a noise as MEW MEW ")

class Cow(Cat):
    def noise(self):
        super().noise()
        print("Cow makes a noise as Amba Amba ")

# main program 
c = Cow()
c.noise()
