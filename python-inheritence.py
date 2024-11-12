# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make a sound."

# Derived class (Child)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the constructor of the base class
        self.breed = breed

    def speak(self):
        return "Woof! Woof!"

# Using the classes
# Create an object of the base class
generic_animal = Animal("Generic Animal")
print(f"{generic_animal.name} says: {generic_animal.speak()}")

# Create an object of the derived class
dog = Dog("Buddy", "Golden Retriever")
print(f"{dog.name}, the {dog.breed}, says: {dog.speak()}")

