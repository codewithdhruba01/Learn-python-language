# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOPS) is a programming paradigm that organizes code into objects that contain both **data (attributes)** and **behavior (methods)**. Python is an object-oriented programming language that allows developers to implement OOP concepts effectively.

## Key OOP Concepts in Python

1. **Class and Object**  
2. **Encapsulation**  
3. **Inheritance**  
4. **Polymorphism**  
5. **Abstraction**  

---

## 1. Class and Object
A **class** is a blueprint for creating objects. It defines the attributes (variables) and behaviors (methods) of objects.  
An **object** is an instance of a class.

### Example: Creating a Class and an Object
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute
    
    def display_info(self):  # Method
        print(f"Car Brand: {self.brand}, Model: {self.model}")

# Creating an object
car1 = Car("Toyota", "Camry")
car1.display_info()
```
**Output:**
```
Car Brand: Toyota, Model: Camry
```

---

## 2. Encapsulation
Encapsulation is the practice of **hiding data** (attributes) and allowing controlled access through methods. It is achieved using **private and public access modifiers**.

### Example: Encapsulation in Python
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance  # Accessor method

# Creating an object
account = BankAccount(5000)
account.deposit(2000)
print(account.get_balance())  # Output: 7000

# print(account.__balance)  # This will cause an error as __balance is private
```

---

## 3. Inheritance
Inheritance allows a class (**child class**) to inherit the properties and methods of another class (**parent class**). It promotes code reusability.

### Types of Inheritance:
1. **Single Inheritance** – One parent, one child.
2. **Multiple Inheritance** – A child class inherits from multiple parent classes.
3. **Multilevel Inheritance** – A child class inherits from another child class.
4. **Hierarchical Inheritance** – Multiple child classes inherit from a single parent.

### Example: Single Inheritance
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Inheriting from Animal class
    def bark(self):
        print("Dog barks")

# Creating an object
dog1 = Dog()
dog1.speak()  # Inherited method
dog1.bark()   # Child class method
```
**Output:**
```
Animal makes a sound
Dog barks
```

---

## 4. Polymorphism
Polymorphism means "many forms." It allows methods in different classes to have the same name but behave differently.

### Example: Method Overriding (Polymorphism)
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):  # Overriding the parent class method
        print("Dog barks")

class Cat(Animal):
    def speak(self):  # Overriding the parent class method
        print("Cat meows")

# Creating objects
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```
**Output:**
```
Dog barks
Cat meows
```

---

## 5. Abstraction
Abstraction hides unnecessary implementation details and only shows essential features.

In Python, abstraction is implemented using **abstract classes** and **abstract methods** with the `abc` module.

### Example: Abstract Class
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def start(self):
        pass  # Abstract method

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

# Creating objects
c = Car()
c.start()  # Output: Car starts with a key

b = Bike()
b.start()  # Output: Bike starts with a button
```

---

### 1. Create a Class and Object

Task: Create a class `Car` with attributes like `brand` and `model`. Create an object of the class and print its details.

### 2. Class with Method

Task: Create a class `Calculator` with methods `add`, `subtract`, `multiply`, and `divide`. Create an object and call each method with example numbers.

### 3. Constructor (`__init__`) Usage

Task: Create a class `Student` with a constructor that takes `name` and `age` as arguments. Create multiple objects and print their information.

### 4. Class with Class Variable and Instance Variable

Task: Create a class `Employee` with a **class variable** `company_name` and **instance variables** `name` and `salary`. Create multiple objects and show the difference between class and instance variables.

### 5. Inheritance (Single Level)

Task: Create a base class `Person` with attributes `name` and `age`. Derive a class `Teacher` that adds an attribute `subject`. Create an object of `Teacher` and print all details using inheritance.

### 6. Multiple Inheritance

Task: Create two parent classes `A` and `B`, each having a different method. Create a child class `C` that inherits both `A` and `B`, and call methods from both parents using an object of `C`.

### 7. Method Overriding

Task: Create a parent class `Animal` with a method `speak()`. Create a child class `Dog` that overrides the `speak()` method to print “Bark”. Create another class `Cat` that overrides it to print “Meow”. Demonstrate polymorphism by calling `speak()` on different objects.

### 8. Encapsulation (Private Variables)

Task: Create a class `BankAccount` with a private variable `__balance`. Add methods `deposit()` and `withdraw()`. Demonstrate how private variables work and how to update them using methods.

### 9. Abstraction using Abstract Class

Task: Create an abstract class `Shape` with an abstract method `area()`. Then create subclasses `Circle` and `Rectangle` that implement the `area()` method. Use objects to calculate area for both shapes.

### 10. Operator Overloading

Task: Create a class `Vector` with `x` and `y` coordinates. Overload the `+` operator so that you can add two `Vector` objects like `v1 + v2` and get a new `Vector` as the result.

---

## OOP Advantages in Python
✔ Code reusability (Inheritance)  
✔ Better data security (Encapsulation)  
✔ Improved code organization (Class & Objects)  
✔ Flexibility and scalability (Polymorphism)  
✔ Enhances code maintainability  

---
