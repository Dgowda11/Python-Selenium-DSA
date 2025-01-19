class Person:
    count  = 0 # Class Variable
    def __init__(self,name,age):
        self.name = name # THis is the instanc varibales
        self.age = age
        Person.count += 1 # calling the class varibales using the class name

p1 = Person("Darshan","24")
p2 = Person("Darshan","24")
print(Person.count)  # COunt  = 2 , Since the Object instance created is 2