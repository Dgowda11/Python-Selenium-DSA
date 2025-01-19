class Animal:
    def speak(self):
        print("Animal is Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is Barking")

d = Dog()
d.bark()
d.speak()