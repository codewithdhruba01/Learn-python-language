"""
Chapter 23: Metaclasses and Dynamic Class Creation - Dynamic Classes
Demonstrates creating classes dynamically using `type()`, introspecting class dictionaries,
and modifying class behavior at runtime.
"""

# ==========================================
# 1. Understanding `type` as a class builder
# ==========================================
print("--- 1. Creating a Class with type() ---")

# Normal way:
# class Person:
#     species = "Homo sapiens"
#     def __init__(self, name):
#         self.name = name

def person_init(self, name):
    self.name = name

def person_greet(self):
    return f"Hello, my name is {self.name} and I am {self.species}."

Person = type(
    "Person",                         # Class Name
    (object,),                        # Base classes tuple
    {                                 # Attributes & methods namespace
        "species": "Homo sapiens",
        "__init__": person_init,
        "greet": person_greet
    }
)

p = Person("Dhruba")
print("Instance:", p)
print("Type of instance:", type(p))
print("Type of Person class:", type(Person))
print("Greeting:", p.greet())


# ==========================================
# 2. Dynamic Factory for Data Model Classes
# ==========================================
print("\n--- 2. Class Factory Function ---")

def make_record_class(class_name: str, fields: list[str]):
    """Dynamically generates a custom data container class."""
    def __init__(self, *args):
        if len(args) != len(fields):
            raise TypeError(f"Expected {len(fields)} arguments, got {len(args)}")
        for field_name, value in zip(fields, args):
            setattr(self, field_name, value)

    def __repr__(self):
        field_repr = ", ".join(f"{f}={getattr(self, f)!r}" for f in fields)
        return f"{class_name}({field_repr})"

    namespace = {
        "__init__": __init__,
        "__repr__": __repr__,
        "_fields": fields
    }

    return type(class_name, (object,), namespace)

Point3D = make_record_class("Point3D", ["x", "y", "z"])
Book = make_record_class("Book", ["title", "author", "price"])

pt = Point3D(10, 20, 30)
b = Book("Fluent Python", "Luciano Ramalho", 49.99)

print("Dynamic Point3D:", pt)
print("Dynamic Book:", b)
print("Point x attribute:", pt.x)


# ==========================================
# 3. Dynamic Inheritance
# ==========================================
print("\n--- 3. Dynamic Inheritance with Bases ---")

class LoggerMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__} LOG]: {message}")

# Dynamically inherit from LoggerMixin
ServiceClass = type("ServiceClass", (LoggerMixin,), {"status": "ACTIVE"})

service = ServiceClass()
print("Service status:", service.status)
service.log("Service started successfully.")
