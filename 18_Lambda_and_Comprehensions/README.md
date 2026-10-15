# Chapter 18: Lambda Functions and Comprehensions in Python

Write clean, concise, and expressive Python code using anonymous functions and powerful comprehension techniques for lists, dictionaries, and sets.

---

## 📌 Table of Contents
1. [What is a Lambda Function?](#1-what-is-a-lambda-function)
2. [Lambda vs Regular `def` Functions](#2-lambda-vs-regular-def-functions)
3. [Higher-Order Functions: `map()`, `filter()`, `reduce()`](#3-higher-order-functions)
4. [Custom Sorting with Lambda](#4-custom-sorting-with-lambda)
5. [List Comprehensions](#5-list-comprehensions)
6. [Conditional Logic in Comprehensions](#6-conditional-logic-in-comprehensions)
7. [Nested List Comprehensions (Matrices)](#7-nested-list-comprehensions-matrices)
8. [Dictionary Comprehensions](#8-dictionary-comprehensions)
9. [Set Comprehensions](#9-set-comprehensions)
10. [When to Use Comprehensions vs Regular Loops](#10-when-to-use-comprehensions-vs-regular-loops)
11. [Practice Questions](#11-practice-questions)

---

## 1. What is a Lambda Function?

A **lambda function** is a small, anonymous function defined without a name using the `lambda` keyword.

### Syntax:
```python
lambda arguments: expression
```

- Can take any number of arguments.
- Can only contain **a single expression** (no multi-line statements or assignments).
- Automatically returns the result of the expression.

### Example:
```python
# Regular function
def add(a, b):
    return a + b

# Equivalent lambda
add_lambda = lambda a, b: a + b

print(add_lambda(5, 7))  # 12
```

---

## 2. Lambda vs Regular `def` Functions

| Feature | `def` Function | `lambda` Function |
|---|---|---|
| **Syntax** | Multi-line statements allowed | Single expression only |
| **Name** | Has an explicit name | Anonymous (unnamed) |
| **Return** | Requires explicit `return` | Implicit return |
| **Docstrings** | Supported (`"""doc"""`) | Not supported |
| **Best used for** | Complex, reusable logic | Short throwaway functions (e.g. inside `sort()`) |

---

## 3. Higher-Order Functions

### A. `map(func, iterable)`
Applies a function to all elements in an iterable.
```python
nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8]
```

### B. `filter(predicate, iterable)`
Filters elements based on a condition returning `True`.
```python
nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [10, 20, 30]
```

### C. `reduce(func, iterable)`
Reduces a sequence to a single cumulative value (imported from `functools`).
```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda acc, x: acc * x, nums)
print(product)  # 120 (1 * 2 * 3 * 4 * 5)
```

---

## 4. Custom Sorting with Lambda

Python's `sorted()` function and `list.sort()` method accept a `key` parameter where lambdas shine:

```python
students = [
    {"name": "Sneha", "marks": 88},
    {"name": "Amit", "marks": 95},
    {"name": "Rahul", "marks": 72}
]

# Sort by marks in descending order
by_marks = sorted(students, key=lambda s: s["marks"], reverse=True)
print(by_marks)
```

---

## 5. List Comprehensions

List comprehensions provide a concise way to create lists from other iterables.

### Syntax:
```python
[expression for item in iterable]
```

### Example:
```python
# Traditional approach
squares = []
for x in range(6):
    squares.append(x ** 2)

# List comprehension approach
squares = [x ** 2 for x in range(6)]
print(squares)  # [0, 1, 4, 9, 16, 25]
```

---

## 6. Conditional Logic in Comprehensions

### Filtering with `if` (At the end)
```python
# Keep only even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

### Transforming with `if-else` (In the front)
```python
# Replace odds with 'Odd', evens remain
labels = [x if x % 2 == 0 else "Odd" for x in range(5)]
print(labels)  # [0, 'Odd', 2, 'Odd', 4]
```

---

## 7. Nested List Comprehensions (Matrices)

Flatten a 2D matrix into a 1D list:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Transpose a matrix:
```python
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

---

## 8. Dictionary Comprehensions

### Syntax:
```python
{key_expr: value_expr for item in iterable}
```

### Examples:
```python
# Number to its square mapping
square_dict = {x: x ** 2 for x in range(1, 6)}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Invert keys and values of a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {val: key for key, val in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

---

## 9. Set Comprehensions

Produces a set (unique elements, unordered):
```python
names = ["Amit", "Rohit", "amit", "Sneha", "ROHIT"]
unique_lowercased = {name.lower() for name in names}
print(unique_lowercased)  # {'amit', 'rohit', 'sneha'}
```

---

## 10. When to Use Comprehensions vs Regular Loops

- ✅ **Use comprehensions** for simple mappings, transformations, and light filtering. They are faster and more readable.
- ❌ **Avoid comprehensions** when there are more than 2 nested loops or complicated conditionals with side effects. Code readability always comes first!

---

## 11. Practice Questions

1. Given a list of words, use list comprehension to create a list of words that have length greater than 4 and convert them to uppercase.
2. Given a list of prices in USD, write a dictionary comprehension to convert each item into INR (assume 1 USD = 83 INR).
3. Using `reduce()` and a lambda function, find the maximum number from a list of integers without using the built-in `max()` function.
