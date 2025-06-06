class Dog:
    def noise(self):
        print("Dog makes a noise as BOW BOW ")
        
class Cat(Dog):
    def noise(self):
        print("Cat makes a noise as MEW MEW ")

class Cow(Cat):
    def noise(self):
        print("Cow makes a noise as Amba Amba ")
        Cat.noise(self)
        Dog.noise(self)

# main program 
c = Cow()
c.noise()
