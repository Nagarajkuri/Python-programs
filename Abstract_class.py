from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def go(self):
        print("you drive the car")
    def stop(self):
        print("this car has stopped") 
        pass

class Motorcycle(Vehicle):
    def go(self):
        print("you ride the motorcycle")
    def stop(self):
        print("this motorcycle has stopped")        
#vehicle=Vehicle()
car=Car()
motorcycle=Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()

