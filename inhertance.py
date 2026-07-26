class person:
    def __init__(self,fname, lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname, self.lname)

# child class
class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year
    def welcome(self):
        print ( "Welcome", self.fname, self.lname, " To the class of ", self.year)

x = student("Allelua", "Olsen", 2027)
x.printname()
x.welcome()

# Class for animal
class animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name)
class Dog(animal):
    pass
d1 = Dog("Rex")
d1.speak()

# polymorphism

class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("drive")

class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail")

class plane:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")
car1 = car("Ford", "Mustang")
boat1 = boat("Ibiza", "Touring 20")
plane1 = plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

# Inherting class polymorphism

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move !")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail")

class Plane(Vehicle):
    def move(self):
        print("FLY!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# python encapsulation

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
p1 = Person("Allelua", 23)
print(p1.name)
print(p1.get_age()) 

# another encupslation example

class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if grade >= 0 or grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")
    def get_grade(self):
        return self.__grade
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"
student = Student("Emile ")
student.set_grade(83)
print(student.get_grade())
print(student.get_status())
        