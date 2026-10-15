# Chapter 16: Iterators and Generators in Python

Iterators and Generators are fundamental concepts in Python that enable memory-efficient data streaming, lazy evaluation, and smooth iteration over custom collections.

---

## 📌 Table of Contents
1. [Iterable vs Iterator](#1-iterable-vs-iterator)
2. [How `for` Loops Work Internally](#2-how-for-loops-work-internally)
3. [Building a Custom Iterator](#3-building-a-custom-iterator)
4. [What is a Generator?](#4-what-is-a-generator)
5. [The `yield` Keyword vs `return`](#5-the-yield-keyword-vs-return)
6. [Memory Efficiency: List vs Generator](#6-memory-efficiency-list-vs-generator)
7. [Generator Expressions](#7-generator-expressions)
8. [Infinite Sequences with Generators](#8-infinite-sequences-with-generators)
9. [Advanced Generator Methods (`send`, `close`)](#9-advanced-generator-methods)
10. [Practice Questions](#10-practice-questions)

---

## 1. Iterable vs Iterator

Understanding the distinction is crucial:

| Feature | Iterable | Iterator |
|---|---|---|
| **Definition** | Any object that can return an iterator (can be looped over) | An object with a state that remembers where it is during iteration |
| **Methods Required** | Implements `__iter__()` | Implements both `__iter__()` and `__next__()` |
| **Examples** | `list`, `str`, `tuple`, `dict`, `set` | Object returned by `iter(list)`, files, generators |
| **Can use `next()`?** | ❌ No, raises `TypeError` | ✅ Yes, returns subsequent items |

### Checking in Python:
```python
numbers = [1, 2, 3]  # Iterable

# Calling next() directly on iterable will fail:
# next(numbers)  -> TypeError: 'list' object is not an iterator

# Convert iterable to an iterator using iter():
num_iter = iter(numbers)  # Iterator

print(next(num_iter))  # 1
print(next(num_iter))  # 2
print(next(num_iter))  # 3
# print(next(num_iter)) -> StopIteration exception!
```

---

## 2. How `for` Loops Work Internally

When you write a simple `for` loop:
```python
for item in [10, 20, 30]:
    print(item)
```

Python executes something equivalent behind the scenes:
```python
iterator = iter([10, 20, 30])
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break  # End of iteration reached safely
```

---

## 3. Building a Custom Iterator

To create a custom iterator class, implement two special methods (the **Iterator Protocol**):
1. `__iter__(self)`: Must return the iterator object itself (`return self`).
2. `__next__(self)`: Must return the next value, or raise `StopIteration` when no more elements remain.

### Example: Custom Countdown Iterator
```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Usage:
for count in Countdown(3):
    print(count)
```
**Output:**
```
3
2
1
```

---

## 4. What is a Generator?

A **Generator** is a simpler and more elegant way to create an iterator without writing a boilerplate class with `__iter__()` and `__next__()`.

A generator is written just like a normal function, but whenever it needs to return a value, it uses the **`yield`** keyword instead of `return`.

```python
def my_generator():
    yield "First"
    yield "Second"
    yield "Third"

gen = my_generator()
print(next(gen))  # First
print(next(gen))  # Second
print(next(gen))  # Third
```

---

## 5. The `yield` Keyword vs `return`

| `return` | `yield` |
|---|---|
| Terminates the function completely | Pauses execution and remembers current state |
| Returns a single value | Can produce a sequence of values lazily over time |
| Local variables are destroyed | Local variables and execution pointer are preserved |

---

## 6. Memory Efficiency: List vs Generator

This is one of the most powerful reasons to use generators!

- A **list** computes all items at once and loads them entirely into RAM.
- A **generator** produces items **on-demand (lazily)** one at a time, consuming virtually zero extra RAM!

### Code Comparison:
```python
import sys

# List: Allocates memory for 1,000,000 integers
list_comp = [x * 2 for x in range(1_000_000)]
print("List size in bytes:", sys.getsizeof(list_comp))
# Output: ~8.4 MB

# Generator: Only stores generator state
gen_exp = (x * 2 for x in range(1_000_000))
print("Generator size in bytes:", sys.getsizeof(gen_exp))
# Output: ~104 bytes!
```

---

## 7. Generator Expressions

Similar to list comprehensions, but use parentheses `()` instead of square brackets `[]`.

```python
# List comprehension (eager evaluation, square brackets)
squares_list = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Generator expression (lazy evaluation, round parentheses)
squares_gen = (x ** 2 for x in range(5))   # <generator object>

for val in squares_gen:
    print(val, end=" ")  # 0 1 4 9 16
```

---

## 8. Infinite Sequences with Generators

Because generators produce values on demand, they can easily represent infinite mathematical series without causing memory overflows.

### Example: Fibonacci Generator
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Generate first 7 Fibonacci numbers
fib = fibonacci()
for _ in range(7):
    print(next(fib), end=" ")
```
**Output:**
```
0 1 1 2 3 5 8
```

---

## 9. Advanced Generator Methods

Generators also support two-way communication:
- `gen.send(val)`: Sends a value into the generator that becomes the result of the current `yield` expression.
- `gen.close()`: Terminates the generator immediately by raising `GeneratorExit`.

```python
def running_average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        if term is None:
            break
        total += term
        count += 1
        average = total / count

avg = running_average()
next(avg)  # Prime the generator
print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0
avg.close()
```

---

## 10. Practice Questions

1. Create a custom iterator class `EvenNumbers` that takes a limit `n` and iterates over even numbers from 2 up to `n`.
2. Write a generator function `read_large_file(file_path)` that yields one line at a time stripped of whitespace, demonstrating how to process a multi-gigabyte file without high RAM usage.
3. Write a generator function that produces prime numbers up to a given limit.
