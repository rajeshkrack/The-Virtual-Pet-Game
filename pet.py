# pet/pet.py

class Pet:
    def __init__(self, name, species, age):
        self._name = name  # Private attribute
        self._species = species  # Private attribute
        self._age = age  # Private attribute
        self._hunger = 50  # Initial hunger level
        self._happiness = 50  # Initial happiness level
        self._health = 100  # Initial health status

    # Encapsulation with getter and setter methods
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_species(self):
        return self._species

    def set_species(self, species):
        self._species = species

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def feed(self):
        self._hunger -= 10
        self._happiness += 5
        self._health += 3

    def play(self):
        self._hunger += 5
        self._happiness += 10
        self._health += 2

    def groom(self):
        self._happiness += 3
        self._health += 1

    def take_to_vet(self):
        self._health += 10

    def display_status(self):
        print(f"Name: {self._name}")
        print(f"Species: {self._species}")
        print(f"Age: {self._age}")
        print(f"Hunger: {self._hunger}")
        print(f"Happiness: {self._happiness}")
        print(f"Health: {self._health}")

    # Method overriding
    def speak(self):
        return ""  # Placeholder for polymorphism

# Inheritance for specialized types of pets
class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, "Dog", age)  # Call parent class constructor
    
    # Method overriding
    def speak(self):
        return "Woof!"

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, "Cat", age)  # Call parent class constructor
    
    # Method overriding
    def speak(self):
        return "Meow!"
