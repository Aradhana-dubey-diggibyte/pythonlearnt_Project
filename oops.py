#oops ex
#Class and Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

# Creating an object
p1 = Person("Alice", 25)
p1.greet()


#Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print("Area:", c.area())


#Polymorphism
class Bird:
    def sound(self):
        print("Generic bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks")

def make_sound(bird):
    bird.sound()

make_sound(Sparrow())  # Output: Sparrow chirps
make_sound(Parrot())   # Output: Parrot talks


#Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())


#Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

#types of inheritance
#Single
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


#Multiple
class Father:
    def skill(self):
        print("Father knows carpentry")

class Mother:
    def talent(self):
        print("Mother knows painting")

class Child(Father, Mother):
    def hobby(self):
        print("Child likes music")

c = Child()
c.skill()
c.talent()
c.hobby()


#Multilevel 
class Grandparent:
    def house(self):
        print("Grandparent has a house")

class Parent(Grandparent):
    def car(self):
        print("Parent has a car")

class Child(Parent):
    def bike(self):
        print("Child has a bike")

c = Child()
c.house()
c.car()
c.bike()


#Hierarchical
class Vehicle:
    def fuel(self):
        print("Needs fuel")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

car = Car()
bike = Bike()
car.fuel()
car.wheels()
bike.fuel()
bike.wheels()


#Hybrid
class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C:
    def method_c(self):
        print("Class C")

class D(B, C):   
    def method_d(self):
        print("Class D")

obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()


