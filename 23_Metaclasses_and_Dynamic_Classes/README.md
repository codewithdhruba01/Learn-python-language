# Chapter 23: Metaclasses and Dynamic Class Creation in Python

> *"Metaclasses are deeper magic than 99% of users should ever worry about. If you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don’t need an explanation of why)."*  
> — **Tim Peters** (Author of the Zen of Python)

While Tim Peters' famous quote highlights their advanced nature, understanding metaclasses unlocks the absolute depths of how Python's object model and frameworks (like Django ORM, Pydantic, SQLAlchemy) actually work.

---

## 📌 Table of Contents
1. [Everything is an Object — Even Classes!](#1-everything-is-an-object--even-classes)
2. [What is `type`?](#2-what-is-type)
3. [Creating Classes Dynamically with `type()`](#3-creating-classes-dynamically-with-type)
4. [What is a Metaclass?](#4-what-is-a-metaclass)
5. [The Metaclass Lifecycle (`__new__` vs `__init__`)](#5-the-metaclass-lifecycle-__new__-vs-__init__)
6. [Controlling Instance Creation with `__call__`](#6-controlling-instance-creation-with-__call__)
7. [Real-World Use Cases: Singleton Pattern](#7-real-world-use-cases-singleton-pattern)
8. [Enforcing Class Rules / Validation](#8-enforcing-class-rules--validation)
9. [The Modern Alternative: `__init_subclass__`](#9-the-modern-alternative-__init_subclass__)
10. [Practice Questions](#10-practice-questions)

---

## 1. Everything is an Object — Even Classes!

In Python, classes are first-class citizens. That means:
- You can pass a class to a function.
- You can assign a class to a variable.
- You can add attributes to a class at runtime.
- You can create a class inside a function.

```python
class Robot:
    pass

r = Robot()
print(type(r))      # <class '__main__.Robot'>
print(type(Robot))  # <class 'type'>
```
Notice that the type of an instance `r` is `Robot`, but the type of the class `Robot` itself is **`type`**!

---

## 2. What is `type`?

In Python:
1. When passed **one argument**, `type(obj)` returns the object's type.
2. When passed **three arguments**, `type(name, bases, dict)` creates and returns a **new class dynamically**!

```python
# type(class_name, tuple_of_base_classes, dict_of_attributes_and_methods)
```

---

## 3. Creating Classes Dynamically with `type()`

Traditional declaration:
```python
class Dog:
    species = "Canine"
    def bark(self):
        return "Woof!"
```

Dynamic creation with `type()`:
```python
def bark_func(self):
    return "Woof!"

Dog = type("Dog", (), {"species": "Canine", "bark": bark_func})

d = Dog()
print(d.species)      # "Canine"
print(d.bark())       # "Woof!"
```
Both produce identical classes under the hood!

---

## 4. What is a Metaclass?

A **metaclass is the class of a class**. Just as an object is an instance of a class, a class is an instance of a metaclass.

```
Metaclass (creates)  --->  Class (creates)  --->  Instance (Object)
  type               --->  Dog              --->  my_dog
```

By default, the metaclass for all classes in Python is `type`. By defining your own metaclass that inherits from `type`, you can intercept, modify, validate, or enhance classes at the exact moment they are defined!

```python
class CustomMeta(type):
    pass

class MyClass(metaclass=CustomMeta):
    pass
```

---

## 5. The Metaclass Lifecycle (`__new__` vs `__init__`)

When Python encounters a class definition:
1. `__new__(mcs, name, bases, namespace)`: Allocates and creates the class object itself. Returns the new class.
2. `__init__(cls, name, bases, namespace)`: Initializes the created class object (similar to `__init__` on normal objects).

```python
class UpperCaseAttributesMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Convert all user attributes to uppercase
        uppercase_attr = {}
        for key, val in namespace.items():
            if not key.startswith("__"):
                uppercase_attr[key.upper()] = val
            else:
                uppercase_attr[key] = val
        return super().__new__(mcs, name, bases, uppercase_attr)

class Config(metaclass=UpperCaseAttributesMeta):
    port = 8080
    host = "localhost"

print(Config.PORT)  # 8080
print(Config.HOST)  # "localhost"
```

---

## 6. Controlling Instance Creation with `__call__`

When you call `MyClass()`, Python executes the `__call__` method of the class's metaclass!
This makes metaclasses the cleanest and most robust way to implement the **Singleton Design Pattern**:

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        print("Connected to Database!")

db1 = DatabaseConnection()  # Prints: "Connected to Database!"
db2 = DatabaseConnection()  # Does NOT reconnect!
print(db1 is db2)           # True (Same instance)
```

---

## 7. The Modern Alternative: `__init_subclass__`

In Python 3.6+, PEP 487 introduced `__init_subclass__`. For 90% of common metaclass tasks (such as validating subclasses or registering plugins), `__init_subclass__` is much simpler and avoids metaclass conflicts!

```python
class PluginBase:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.registry.append(cls)
        print(f"Registered plugin: {cls.__name__}")

class AudioPlugin(PluginBase):
    pass  # Prints: Registered plugin: AudioPlugin

class VideoPlugin(PluginBase):
    pass  # Prints: Registered plugin: VideoPlugin

print("All plugins:", PluginBase.registry)
```

---

## 8. Practice Questions

1. Create a dynamic class `Car` using `type()` that has attributes `brand` and `model` and a method `drive()`.
2. Write a metaclass `RequireDocstringMeta` that raises a `TypeError` if any class or any method inside it lacks a docstring (`__doc__`).
3. Implement a `SingletonMeta` metaclass and demonstrate that multiple instantiations return the exact same object in memory.
4. Use `__init_subclass__` to build an automatic API route registry that registers subclasses whenever they inherit from `BaseRoute`.
