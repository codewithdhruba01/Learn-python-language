# Chapter 15: Exception Handling in Python

Exception handling is a mechanism in Python to handle runtime errors gracefully, preventing the program from crashing unexpectedly and allowing it to recover or display user-friendly error messages.

---

## 📌 Table of Contents
1. [Errors vs Exceptions](#1-errors-vs-exceptions)
2. [Why Use Exception Handling?](#2-why-use-exception-handling)
3. [The `try` and `except` Block](#3-the-try-and-except-block)
4. [Handling Multiple Exceptions](#4-handling-multiple-exceptions)
5. [The `else` Block](#5-the-else-block)
6. [The `finally` Block](#6-the-finally-block)
7. [The `raise` Keyword](#7-the-raise-keyword)
8. [Custom / User-Defined Exceptions](#8-custom--user-defined-exceptions)
9. [Built-in Exception Hierarchy](#9-built-in-exception-hierarchy)
10. [Best Practices](#10-best-practices)
11. [Practice Questions](#11-practice-questions)

---

## 1. Errors vs Exceptions

In Python, problems can be categorized into two main types:

| Feature | Syntax Errors (Compile-time) | Exceptions (Runtime) |
|---|---|---|
| **When it occurs** | Parsing stage, before code runs | During code execution |
| **Cause** | Incorrect grammar/syntax | Invalid operations (divide by zero, missing file) |
| **Can be handled?** | No, must fix the code | Yes, using `try-except` |

### Example of Syntax Error:
```python
# Missing colon at the end of if statement
if True
    print("Hello")  # SyntaxError: expected ':'
```

### Example of an Exception:
```python
# Valid syntax, but fails at runtime
num = 10 / 0  # ZeroDivisionError: division by zero
```

---

## 2. Why Use Exception Handling?

Without exception handling:
```python
num = int(input("Enter a number: "))  # User enters "abc"
print(10 / num)
print("Program completed successfully.")  # This line will NEVER run!
```
If an error happens, the script terminates immediately with a red traceback. Exception handling ensures your application remains resilient and continues operating or shuts down cleanly.

---

## 3. The `try` and `except` Block

The core structure:
- **`try`**: Write the suspicious code that might fail.
- **`except`**: Catch and handle the error if it occurs.

### Syntax:
```python
try:
    # Code that might raise an exception
    pass
except SpecificException as e:
    # Code that executes when exception occurs
    pass
```

### Example:
```python
try:
    number = int("hello")
except ValueError as err:
    print(f"Error caught: {err}")

print("Program is still running!")
```
**Output:**
```
Error caught: invalid literal for int() with base 10: 'hello'
Program is still running!
```

---

## 4. Handling Multiple Exceptions

You can handle different exceptions in separate blocks, or catch multiple exceptions together in a tuple.

### Method A: Multiple `except` blocks
```python
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers only!")
except ZeroDivisionError:
    print("Error: Denominator cannot be zero!")
```

### Method B: Single `except` block with a tuple
```python
try:
    file = open("non_existent_file.txt", "r")
    content = file.read()
except (FileNotFoundError, PermissionError) as err:
    print(f"File error: {err}")
```

---

## 5. The `else` Block

The `else` block runs **only if NO exception occurred** inside the `try` block.

```python
try:
    num = int("42")
    res = 100 / num
except ZeroDivisionError:
    print("Division by zero error!")
except ValueError:
    print("Value error!")
else:
    print(f"Operation succeeded! Result is {res}")
```

**Output:**
```
Operation succeeded! Result is 2.380952380952381
```

---

## 6. The `finally` Block

The `finally` block **ALWAYS runs**, whether an exception occurred or not, and even if a `return` statement is executed inside `try` or `except`. It is ideal for cleanup tasks (closing files, releasing locks, closing database connections).

```python
try:
    file = open("sample.txt", "w")
    file.write("Hello, World!")
except IOError as e:
    print(f"IO error: {e}")
finally:
    file.close()
    print("File closed safely.")
```

### Execution Flow Summary:
```
  ┌───────────────┐
  │   try block   │
  └───────┬───────┘
          │
    Exception?
     /         \
   YES          NO
   /             \
┌────────────┐   ┌────────────┐
│ except     │   │ else       │
└─────┬──────┘   └─────┬──────┘
      │                │
      └───────┬────────┘
              │
       ┌──────────────┐
       │   finally    │ (Always executes!)
       └──────────────┘
```

---

## 7. The `raise` Keyword

You can manually trigger an exception using the `raise` keyword when business logic is violated.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Unrealistic age value.")
    print(f"Age set to {age}")

try:
    set_age(-5)
except ValueError as error:
    print("Validation failed:", error)
```
**Output:**
```
Validation failed: Age cannot be negative!
```

---

## 8. Custom / User-Defined Exceptions

You can define your own exceptions by creating a class that inherits from Python's built-in `Exception` class.

### Example:
```python
class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds account balance."""
    def __init__(self, balance, amount):
        super().__init__(f"Attempted to withdraw ₹{amount}, but balance is only ₹{balance}!")
        self.balance = balance
        self.amount = amount

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrawal successful. Remaining balance: ₹{self.balance}")

# Testing custom exception
account = BankAccount(5000)

try:
    account.withdraw(7000)
except InsufficientFundsError as e:
    print(f"Transaction Denied: {e}")
```

**Output:**
```
Transaction Denied: Attempted to withdraw ₹7000, but balance is only ₹5000!
```

---

## 9. Built-in Exception Hierarchy

All built-in exceptions inherit from `BaseException`. Here are the most common ones under `Exception`:

- `Exception`
  - `ArithmeticError`
    - `ZeroDivisionError`
    - `OverflowError`
  - `LookupError`
    - `IndexError` (e.g. `lst[99]` on list of length 3)
    - `KeyError` (e.g. `dict["non_existing_key"]`)
  - `ValueError` (Invalid value passed, e.g. `int("abc")`)
  - `TypeError` (Wrong type, e.g. `"2" + 2`)
  - `FileNotFoundError` (File does not exist)
  - `AttributeError` (Accessing an attribute that doesn't exist)
  - `ImportError` / `ModuleNotFoundError`
  - `StopIteration` (Raised by iterators when done)

---

## 10. Best Practices

1. **Never use bare `except:`**
   ```python
   # ❌ Bad: Catches KeyboardInterrupt, SystemExit, making it hard to stop
   except:
       pass

   # ✅ Good: Catch specific exceptions
   except (ValueError, KeyError) as e:
       print(e)
   ```
2. **Keep the `try` block minimal:** Put only the lines that can actually fail inside `try`.
3. **Use `finally` or context managers (`with`)** for releasing external resources.
4. **Provide helpful error messages** when raising exceptions.

---

## 11. Practice Questions

1. Write a function that takes two inputs from the user, divides them, and handles both `ValueError` (if non-numeric input is given) and `ZeroDivisionError`.
2. Create a custom exception `PasswordTooShortError` that is raised if the user's password is less than 8 characters long.
3. Write a program to open and read a file, and make sure the file is closed properly in the `finally` block even if an exception occurs during reading.
