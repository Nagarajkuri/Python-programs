class Car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    def drive(self):
        print("hey car is started")

    def stop(self):
        print("car is stopped")