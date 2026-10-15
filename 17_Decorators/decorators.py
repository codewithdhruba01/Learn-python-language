"""
Chapter 17: Decorators Basics
Demonstrates first-class functions, closures, wrapper functions, and functools.wraps.
"""
from functools import wraps

# ==========================================
# 1. First-Class Functions & Closures
# ==========================================
print("--- 1. First-Class Functions & Closures ---")
def power_factory(exponent):
    def calculate(base):
        return base ** exponent
    return calculate

square = power_factory(2)
cube = power_factory(3)

print("Square of 4:", square(4))
print("Cube of 4  :", cube(4))


# ==========================================
# 2. Basic Decorator Syntax
# ==========================================
print("\n--- 2. Basic Decorator Syntax ---")
def banner_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("=" * 40)
        result = func(*args, **kwargs)
        print("=" * 40)
        return result
    return wrapper

@banner_decorator
def display_welcome(name):
    """Displays a welcome greeting message."""
    print(f"🎉 Welcome to Python Learning, {name}! 🎉")

display_welcome("Dhruba")
print("Function name preserved:", display_welcome.__name__)
print("Function doc preserved :", display_welcome.__doc__)


# ==========================================
# 3. Chaining Multiple Decorators
# ==========================================
print("\n--- 3. Chaining Decorators ---")
def make_bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def make_italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@make_bold
@make_italic
def format_text(msg):
    return msg

# Notice order: make_italic runs first, then make_bold wraps it
print("Formatted string:", format_text("Python Decorators Rule!"))
