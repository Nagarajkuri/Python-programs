class Car:
    def turn_on(self):
        print("you start the engine")
        return self

    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you step on brakes")
        return self
    def turn_off(self):
        print("you turn off the engine")
        return self

car=Car()
car.turn_on() 
car.drive()
car.turn_on().drive()
car.brake().turn_off()
car.turn_on().drive().brake().turn_off()