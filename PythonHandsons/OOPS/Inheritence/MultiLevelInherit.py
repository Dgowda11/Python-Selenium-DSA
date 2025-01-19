class Animal:
    def speak(self):
        print("Animal is Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is Barking")
class DogChild(Dog):
    def eat(self):
        print("DOg child is eating")
d = DogChild()
d.bark()
d.speak()
d.eat()