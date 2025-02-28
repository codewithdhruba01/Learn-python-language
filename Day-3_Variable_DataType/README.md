# Variables and Data Types in Python

## 1. Variables in Python
A **variable** is a name that refers to a value stored in memory. Python automatically determines the type based on the assigned value.

### 1.1 Declaring and Assigning Variables
```python
x = 10          # Integer
name = "John"   # String
pi = 3.14       # Float
is_valid = True # Boolean
```

### 1.2 Rules for Naming Variables
- Must start with a letter (A-Z or a-z) or an underscore (_).
- The rest of the name can contain letters, numbers (0-9), or underscores.
- Variable names are case-sensitive.
- Reserved keywords cannot be used as variable names.

#### Examples:
```python
_myVar = 5       # Valid
myVar2 = "Hi"    # Valid
2myVar = 10      # Invalid (Cannot start with a number)
my-var = "Hello" # Invalid (Cannot contain special characters like -)
```

---

## 2. Data Types in Python
Python has several built-in data types:

| Data Type | Description | Example |
|-----------|-------------|---------|
| `int` | Integer numbers | `x = 100` |
| `float` | Decimal numbers | `pi = 3.14` |
| `str` | String (text) | `name = "Alice"` |
| `bool` | Boolean values | `is_active = True` |
| `list` | Ordered, mutable collection | `numbers = [1, 2, 3]` |
| `tuple` | Ordered, immutable collection | `coordinates = (10, 20)` |
| `set` | Unordered, unique collection | `unique_numbers = {1, 2, 3}` |
| `dict` | Key-value pairs | `person = {"name": "Alice", "age": 25}` |

### Examples:
```python
age = 25
print(type(age))  # <class 'int'>

pi = 3.14159
print(type(pi))  # <class 'float'>

name = "Alice"
print(type(name))  # <class 'str'>

is_raining = False
print(type(is_raining))  # <class 'bool'>
```

---

## 3. Type Conversion (Type Casting)
Python allows converting one data type to another using built-in functions.

| Function | Converts To |
|----------|-------------|
| `int()` | Integer |
| `float()` | Floating-point number |
| `str()` | String |
| `bool()` | Boolean |
| `list()` | List |
| `tuple()` | Tuple |

### Example:
```python
a = "100"
b = int(a)  # Convert string to integer
print(type(b))  # <class 'int'>

c = float(b)  # Convert integer to float
print(type(c))  # <class 'float'>
```

---

## 4. Checking Data Type (`type()`)
Use `type()` to check the data type of a variable.

### Example:
```python
x = 10
print(type(x))  # <class 'int'>

y = "Hello"
print(type(y))  # <class 'str'>
```

---

