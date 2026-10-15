# Chapter 24: Python Descriptors and Attribute Management

Descriptors are the hidden engine powering Python's object-oriented system. If you have ever used `@property`, `@classmethod`, `@staticmethod`, or worked with an ORM like Django or SQLAlchemy, you have already used descriptors without knowing it!

---

## 📌 Table of Contents
1. [What is a Descriptor?](#1-what-is-a-descriptor)
2. [The Descriptor Protocol](#2-the-descriptor-protocol)
3. [Data vs. Non-Data Descriptors](#3-data-vs-non-data-descriptors)
4. [Python Attribute Lookup Order](#4-python-attribute-lookup-order)
5. [The Modern `__set_name__` Method (Python 3.6+)](#5-the-modern-__set_name__-method-python-36)
6. [How `@property` Works Under the Hood](#6-how-property-works-under-the-hood)
7. [How `@classmethod` and `@staticmethod` Work](#7-how-classmethod-and-staticmethod-work)
8. [Building Real-World Field Validators (Mini-ORM)](#8-building-real-world-field-validators-mini-orm)
9. [Practice Questions](#9-practice-questions)

---

## 1. What is a Descriptor?

A **descriptor** is an object attribute whose access behavior is overridden by methods in the descriptor protocol.

Instead of just storing a value in an instance dictionary (`self.__dict__`), an attribute access like `obj.attr` or `obj.attr = value` is routed through special methods:
- `__get__(self, obj, objtype=None)`
- `__set__(self, obj, value)`
- `__delete__(self, obj)`

---

## 2. The Descriptor Protocol

```python
class MyDescriptor:
    def __get__(self, instance, owner):
        """Called when reading: instance.attr or OwnerClass.attr"""
        if instance is None:
            return self  # Accessed from class
        return f"Fetching value for {instance}"

    def __set__(self, instance, value):
        """Called when writing: instance.attr = value"""
        print(f"Setting value {value} on {instance}")

    def __delete__(self, instance):
        """Called when deleting: del instance.attr"""
        print(f"Deleting attribute from {instance}")
```

---

## 3. Data vs. Non-Data Descriptors

This distinction is crucial for understanding how Python resolves attribute lookups:

| Type | Methods Defined | Precedence over Instance `__dict__` | Example |
|------|-----------------|--------------------------------------|---------|
| **Data Descriptor** | Defines `__set__` and/or `__delete__` | **Higher** (takes priority over `obj.__dict__`) | `@property`, custom validators |
| **Non-Data Descriptor** | Defines only `__get__` | **Lower** (can be shadowed by `obj.__dict__`) | Regular methods, `@staticmethod`, `@classmethod` |

---

## 4. Python Attribute Lookup Order

When you execute `instance.x`, Python follows this strict resolution sequence:

1. **Data Descriptors**: Python checks the class (and its MRO) for a data descriptor named `x`. If found, `x.__get__(instance, Owner)` is called.
2. **Instance Dictionary**: Python checks `instance.__dict__['x']`. If present, it returns that value.
3. **Non-Data Descriptors**: Python checks the class (and MRO) for a non-data descriptor named `x`. If found, `x.__get__(instance, Owner)` is called.
4. **Class Dictionary**: Python returns `Owner.__dict__['x']`.
5. **Fallback**: If not found anywhere, Python calls `__getattr__(self, 'x')`. If not defined, raises `AttributeError`.

---

## 5. The Modern `__set_name__` Method (Python 3.6+)

Before Python 3.6, descriptors did not know the variable name they were assigned to. You had to pass the name manually in `__init__`.
With `__set_name__`, Python automatically passes the owning class and attribute name upon class creation:

```python
class LoggedAttribute:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        print(f"Setting {self.public_name} = {value}")
        setattr(obj, self.private_name, value)

class Person:
    name = LoggedAttribute()
    age = LoggedAttribute()

p = Person()
p.name = "Dhruba"  # Output: Setting name = Dhruba
p.age = 25         # Output: Setting age = 25
```

---

## 6. How `@property` Works Under the Hood

The built-in `@property` is simply a C-implemented data descriptor! Here is a pure-Python equivalent:

```python
class MyProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("Unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute (read-only)")
        self.fset(obj, value)

    def setter(self, fset):
        return type(self)(self.fget, fset)
```

---

## 7. Building Real-World Field Validators (Mini-ORM)

Descriptors are the clean, reusable solution to input validation without repeating `@property` getters and setters on every class:

```python
class IntegerField:
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"Expected int, got {type(value).__name__}")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"Value must be >= {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"Value must be <= {self.max_val}")
        setattr(obj, self.name, value)
```

---

## 8. Practice Questions

1. Create a non-data descriptor that implements a lazy property (evaluates a heavy function once, caches the result in `obj.__dict__`, and avoids re-computation).
2. Build a descriptor `PositiveNumber` that ensures a numeric value cannot be negative.
3. Build a descriptor `NonEmptyString` that validates that the value assigned is a string with at least one non-whitespace character.
4. Explain why standard Python methods are considered non-data descriptors and how they bind to instances as `bound methods`.
