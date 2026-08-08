""" class MyClass:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, I'm {self.name}"

obj = MyClass("ally")
print(obj.greet()) """

class Person:
    def __init__(self,name, age):
        self._name = name
        self._age = age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age  cannot be negative")
        self._age = value
    

person = Person("Ally", 23)
print(person.age)

person = Person("Ally", 30)
person.age = 31
print(person.age)
        