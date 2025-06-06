class Car:
    def __init__(self,make,model) -> None:
        self.make = make
        self._model = model
        self.__speed = 0
    
    def get_speed(self):
        return self.__speed
    
    def accelarate(self,increment):
        if increment >0:
            self.__speed +=increment
        
    def get_model(self):
        return self._model

car = Car("Mahindra","Thar")
print(car.get_model())
car.accelarate(25)
print(car.get_speed())
print(car._model())