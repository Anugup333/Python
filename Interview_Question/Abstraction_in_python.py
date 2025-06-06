from abc import ABC,abstractmethod

# Abstract Class

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Subcalsses to implemet the Abstract  Class

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"


dog = Dog()
cat = Cat()

print(dog.make_sound())
print(cat.make_sound())