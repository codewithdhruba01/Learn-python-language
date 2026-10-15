"""
Chapter 24: Descriptors - Practical Applications
Building reusable field validators (Typed, BoundedNumber, NonEmptyString)
similar to validation layers in ORMs (Django, SQLAlchemy, Pydantic).
"""

# ==========================================
# 1. Base Validator Descriptor
# ==========================================
class Validator:
    """Base descriptor enforcing attribute storage and validation hook."""
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"
        self.public_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.private_name, None)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    def validate(self, value):
        """Override in subclasses to perform specific checks."""
        pass


# ==========================================
# 2. Specialized Validators
# ==========================================
class NonEmptyString(Validator):
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"'{self.public_name}' must be a string, got {type(value).__name__}")
        if not value.strip():
            raise ValueError(f"'{self.public_name}' cannot be empty or whitespace only")

class BoundedNumber(Validator):
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"'{self.public_name}' must be a number, got {type(value).__name__}")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"'{self.public_name}' must be >= {self.min_val}, got {value}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"'{self.public_name}' must be <= {self.max_val}, got {value}")


# ==========================================
# 3. Model Definition using Descriptors
# ==========================================
print("--- Using Descriptors as Declarative Field Validators ---")

class Product:
    name = NonEmptyString()
    price = BoundedNumber(min_val=0.01, max_val=100000.0)
    stock = BoundedNumber(min_val=0, max_val=5000)

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, stock={self.stock})"

# Successful creation
laptop = Product("MacBook Air", 999.99, 25)
print("Created product:", laptop)

# Updating attributes
laptop.price = 949.99
laptop.stock = 20
print("Updated product:", laptop)

# Testing validation failures
print("\n--- Testing Validation Errors ---")

try:
    Product("   ", 100.0, 10)
except ValueError as e:
    print("Caught validation error (Empty Name):", e)

try:
    Product("Keyboard", -15.0, 5)
except ValueError as e:
    print("Caught validation error (Negative Price):", e)

try:
    Product("Mouse", 29.99, "in stock")  # type: ignore
except TypeError as e:
    print("Caught validation error (Invalid Type):", e)
