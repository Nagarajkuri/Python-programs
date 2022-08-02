#program1
class Organism:

    alive=True

class Animal(Organism):

    def eat(self):
        print("this animal is eating")

class Dog(Animal):
     def bark(self):
         print("this dog is barking")

dog=Dog()
print(Dog.alive)
dog.eat()
dog.bark()

#program2
class Prey:
    def flee(self):
        print("this animal flees")

class Predator:
    def hunt(self):
        print("this animal is hunting")


class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass
rabbit=Rabbit()
hawk=Hawk()
fish=Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
