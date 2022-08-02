class Animal:
    alive= True
    def eat(self):
        print("the animal is eating")
    
class Rabbit(Animal):
    #here we are writting eat method again. 
    def eat(self):
        print("this rabbit is eating carrot")
rabbit=Rabbit()
rabbit.eat()#we will get the o/p from Rabbit class not from the parent clss(animal)