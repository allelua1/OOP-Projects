""" class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, My name is {self.name}")
p1 = Person("John", 36)
p1.greet()

class person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return "Hello, "+ self.name
    def welcome(self):
        message = self.greet()
        print(message + "! Welcome to our website. ")

class car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Brand: ", self.brand)
c1 = car("Ford")
c1.show()
print(c1.brand)
        
 """
# class Student:
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
s1 =Student("Anna", "A")
print(s1.grade)
s1.grade = "B"
print(s1.grade)

# calculator
class calculator:
    def add(self, a, b):
        return a + b
    def multiply(self, a, b):
        return a * b

calc = calculator()
print(calc.add(2,3))
print(calc.multiply(2,3))

# __Str__() used to control what willbe printed when the object is printed
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = 24
    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = person ("Allelua", 23)
print(p1)

class playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
        print(f"Added song: {song}")
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed Song: {song}")
    def show_songs(self):
        print(f"Playlist '{self.name}")
        for song in self.songs:
            print(f"- {song}")

my_playlist = playlist("Favorites")
my_playlist.add_song("Maaso")
my_playlist.add_song("Inana")
my_playlist.show_songs()