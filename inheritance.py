class Animal:
    alive= True
    def eat(self):
        print("the animal is eating")
    def sleep(self):
        print("the animal is sleeping")
class Rabbit(Animal):
    def cook(self):
        print("animal is cooking")
    pass
class Fish(Animal):
    pass
class Hawk(Animal):
    pass
#these 3 are objects
rabbit=Rabbit()
fish=Fish()
hawk=Hawk()
print(rabbit.alive)
fish.eat()
hawk.sleep()
print(fish.alive)
rabbit.sleep()
rabbit.cook()