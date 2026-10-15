# Chapter 17: Decorators in Python

Decorators are one of the most powerful and idiomatic features in Python. They allow you to dynamically modify or extend the behavior of a function or class without modifying its source code.

---

## 📌 Table of Contents
1. [Prerequisites: First-Class Functions](#1-prerequisites-first-class-functions)
2. [Closures in Python](#2-closures-in-python)
3. [What is a Decorator?](#3-what-is-a-decorator)
4. [The `@decorator` Syntax](#4-the-decorator-syntax)
5. [Decorating Functions with Arguments (`*args`, `**kwargs`)](#5-decorating-functions-with-arguments)
6. [Returning Values from Decorated Functions](#6-returning-values-from-decorated-functions)
7. [Preserving Metadata with `functools.wraps`](#7-preserving-metadata-with-functoolswraps)
8. [Decorators that Accept Arguments](#8-decorators-that-accept-arguments)
9. [Chaining Multiple Decorators](#9-chaining-multiple-decorators)
10. [Real-World Use Cases (Timer, Logger, Auth)](#10-real-world-use-cases)
11. [Practice Questions](#11-practice-questions)

---

## 1. Prerequisites: First-Class Functions

In Python, **functions are first-class objects**, meaning:
1. They can be assigned to variables.
2. They can be passed as arguments to other functions.
3. They can be returned from other functions.
4. They can be defined inside another function.

### Example:
```python
def shout(text):
    return text.upper()

# 1. Assign to variable
yell = shout
print(yell("hello"))  # HELLO

# 2. Pass as argument
def greet(func):
    return func("welcome to python")

print(greet(shout))  # WELCOME TO PYTHON
```

---

## 2. Closures in Python

A **closure** is an inner function that remembers and has access to variables from its enclosing outer function scope, even after the outer function has finished executing.

```python
def outer_multiplier(factor):
    def inner_multiply(number):
        return number * factor  # 'factor' is remembered from outer scope
    return inner_multiply

double = outer_multiplier(2)
triple = outer_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

---

## 3. What is a Decorator?

A decorator is a function that takes another function as an argument, adds some functionality or behavior before/after it, and returns the modified wrapper function.

### Basic Manual Structure:
```python
def my_decorator(original_function):
    def wrapper():
        print("Before original function runs...")
        original_function()
        print("After original function runs...")
    return wrapper

def say_hello():
    print("Hello, World!")

# Manually decorating
decorated_hello = my_decorator(say_hello)
decorated_hello()
```

---

## 4. The `@decorator` Syntax

Python provides syntactic sugar using the `@` symbol to avoid manual assignment:

```python
@my_decorator
def say_hello():
    print("Hello, World!")

# Calling say_hello() will now automatically run through wrapper()
say_hello()
```

---

## 5. Decorating Functions with Arguments

If the decorated function takes arguments, the `wrapper` must accept `*args` and `**kwargs`:

```python
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(a, b):
    return a + b

print("Sum:", add(10, 25))
```

---

## 6. Returning Values from Decorated Functions

Notice that in the previous example, `wrapper` explicitly uses `return func(*args, **kwargs)`. If you forget the `return` statement in the wrapper, the decorated function will return `None`!

---

## 7. Preserving Metadata with `functools.wraps`

When you wrap a function, its `__name__` and `__doc__` (docstring) get overwritten by the wrapper. To preserve the original function's identity, always use `@functools.wraps`:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper documentation"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet_user(name):
    """Greets a user by name."""
    return f"Hello, {name}!"

print(greet_user.__name__)  # 'greet_user' (preserves name, NOT 'wrapper')
print(greet_user.__doc__)   # 'Greets a user by name.'
```

---

## 8. Decorators that Accept Arguments

If your decorator needs to accept configuration options (e.g. `@repeat(num_times=3)`), you need a 3-tier nested function (decorator factory):

```python
from functools import wraps

def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Dhruba")
```
**Output:**
```
Hello, Dhruba!
Hello, Dhruba!
Hello, Dhruba!
```

---

## 9. Chaining Multiple Decorators

You can apply multiple decorators to a single function. They are executed in **bottom-to-top** order (the decorator closest to the function runs first):

```python
@decorator_two
@decorator_one
def my_func():
    pass

# Equivalent to:
# my_func = decorator_two(decorator_one(my_func))
```

---

## 10. Real-World Use Cases

1. **Execution Timer**: Measuring performance of operations.
2. **Access Control / Authentication**: Checking if a user is logged in or has admin rights before executing an endpoint.
3. **Caching / Memoization**: Python's `@functools.lru_cache` saves previous computation results.
4. **Input Validation**: Verifying types or bounds of function parameters.
5. **Rate Limiting**: Preventing API abuse by restricting call frequencies.

---

## 11. Practice Questions

1. Write a `@timer` decorator that calculates and prints the execution time of any function in seconds.
2. Write a `@debug` decorator that prints the function name, arguments passed, and returned value whenever the function is called.
3. Create an `@ensure_logged_in` decorator that checks a global or context variable `is_logged_in` before allowing a function to execute, raising a `PermissionError` if `False`.
