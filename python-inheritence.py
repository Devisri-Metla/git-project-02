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


-------------------------------------------------

#Hierarchical Inheritance:
class Parent:
    def show(self):
        print("This is the Parent class.")

class Child1(Parent):
    def display_child1(self):
        print("This is Child1 class.")

class Child2(Parent):
    def display_child2(self):
        print("This is Child2 class.")

# Example usage
child1 = Child1()
child1.show()
child1.display_child1()

child2 = Child2()
child2.show()
child2.display_child2()

print(f"{dog.name}, the {dog.breed}, says: {dog.speak()}")

