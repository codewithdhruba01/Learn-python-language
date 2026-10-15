"""
Chapter 24: Descriptors - Introduction
Demonstrates the descriptor protocol (__get__, __set__, __set_name__),
distinction between data vs non-data descriptors, and a pure-Python @property clone.
"""

# ==========================================
# 1. Basic Data Descriptor with __set_name__
# ==========================================
print("--- 1. Basic Data Descriptor ---")

class VerboseAttribute:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.storage_name = f"_descriptor_{name}"

    def __get__(self, instance, owner):
        if instance is None:
            # Accessed from the class (e.g. User.username)
            return self
        value = getattr(instance, self.storage_name, None)
        print(f"[GET] Accessing '{self.public_name}' -> {value}")
        return value

    def __set__(self, instance, value):
        print(f"[SET] Writing '{self.public_name}' = {value}")
        setattr(instance, self.storage_name, value)

class UserAccount:
    username = VerboseAttribute()
    email = VerboseAttribute()

user = UserAccount()
user.username = "codewithdhruba"
user.email = "dhruba@example.com"

print("Read username:", user.username)
print("Read email:", user.email)


# ==========================================
# 2. Non-Data Descriptor vs Data Descriptor
# ==========================================
print("\n--- 2. Non-Data Descriptor (Lazy Cached Attribute) ---")

class LazyProperty:
    """Non-data descriptor: computes value once and caches it in instance __dict__."""
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"[LazyProperty] Calculating expensive value for '{self.name}'...")
        value = self.func(instance)
        # Store directly in instance dictionary so subsequent lookups hit __dict__ directly!
        instance.__dict__[self.name] = value
        return value

class HeavyDataset:
    def __init__(self, size: int):
        self.size = size

    @LazyProperty
    def summary_stats(self):
        # Pretend this is an expensive calculation or database query
        return sum(range(self.size))

dataset = HeavyDataset(1000000)
print("First access (will compute):", dataset.summary_stats)
print("Second access (cached in __dict__):", dataset.summary_stats)


# ==========================================
# 3. Pure-Python Property Clone
# ==========================================
print("\n--- 3. How @property Works Under the Hood ---")

class CustomProperty:
    """Custom implementation of Python's built-in @property descriptor."""
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("Unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("Can't set attribute (read-only property)")
        self.fset(instance, value)

    def setter(self, fset):
        return type(self)(self.fget, fset)

class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @CustomProperty
    def area(self) -> float:
        return self._width * self._height

rect = Rectangle(10, 5)
print("Rectangle Area via CustomProperty:", rect.area)
try:
    rect.area = 100
except AttributeError as e:
    print("Caught expected error attempting to write to read-only property:", e)
