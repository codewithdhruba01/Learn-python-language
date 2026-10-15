# Chapter 25: Memory Management and Performance Optimization in Python

Writing fast, production-grade Python applications requires understanding how CPython manages memory behind the scenes: how objects are allocated, how references are counted, how the generational garbage collector frees unused memory, and how you can optimize memory usage with `__slots__` and `weakref`.

---

## 📌 Table of Contents
1. [How Python Manages Memory](#1-how-python-manages-memory)
2. [Reference Counting Mechanism](#2-reference-counting-mechanism)
3. [The Problem of Reference Cycles](#3-the-problem-of-reference-cycles)
4. [Generational Garbage Collection (`gc` Module)](#4-generational-garbage-collection-gc-module)
5. [Weak References with `weakref`](#5-weak-references-with-weakref)
6. [Drastic Memory Optimization with `__slots__`](#6-drastic-memory-optimization-with-__slots__)
7. [Measuring Object Size with `sys.getsizeof()`](#7-measuring-object-size-with-sysgetsizeof)
8. [Tracking Memory Allocations with `tracemalloc`](#8-tracking-memory-allocations-with-tracemalloc)
9. [Shallow Copy vs. Deep Copy](#9-shallow-copy-vs-deep-copy)
10. [Practice Questions](#10-practice-questions)

---

## 1. How Python Manages Memory

In CPython (the standard Python implementation):
- Memory is managed in a **private heap** containing all Python objects and data structures.
- Programmers do not manually allocate or free memory (no `malloc` or `free`).
- Python employs a two-tier memory manager:
  1. **Reference Counting** (Primary, real-time deallocation).
  2. **Generational Cyclic Garbage Collector** (Secondary, runs periodically to break reference cycles).

---

## 2. Reference Counting Mechanism

Every Python object has an internal reference count (stored in its `PyObject` header).
- When a reference to an object is created (e.g., assignment, passing to a function, appending to a list), its counter increases by `1`.
- When a reference goes out of scope or is deleted via `del`, its counter decreases by `1`.
- **When the counter reaches 0, the memory occupied by the object is immediately reclaimed.**

You can inspect the reference count using `sys.getrefcount(obj)` (Note: `sys.getrefcount` itself temporarily adds `1` while inspecting):

```python
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # 2 (variable 'a' + argument to getrefcount)

b = a
print(sys.getrefcount(a))  # 3

del b
print(sys.getrefcount(a))  # 2
```

---

## 3. The Problem of Reference Cycles

Reference counting alone has one major flaw: **circular references**.

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None

node1 = Node("A")
node2 = Node("B")

# Circular reference:
node1.partner = node2
node2.partner = node1

# Now delete the external references:
del node1
del node2
```
Even though the program can no longer access `node1` or `node2`, their internal reference counts remain `1` because they point to each other! Reference counting will **never** free them.

---

## 4. Generational Garbage Collection (`gc` Module)

To fix circular reference leaks, Python includes a **cyclic garbage collector** that detects self-referencing groups of unreachable objects.

Python categorizes objects into **3 generations**:
- **Generation 0**: Newly created objects. Collected very frequently.
- **Generation 1**: Objects that survive a Gen 0 collection. Collected less frequently.
- **Generation 2**: Long-lived objects (e.g., loaded modules, global variables). Collected rarely.

```python
import gc

# Force a manual garbage collection cycle
collected = gc.collect()
print(f"Freed {collected} unreachable objects.")

# Inspect GC collection thresholds
print("GC thresholds (Gen 0, Gen 1, Gen 2):", gc.get_threshold())
```

---

## 5. Weak References with `weakref`

A **weak reference** allows you to reference an object without increasing its reference count. If all strong references are destroyed, the object is collected immediately, even if weak references exist.

This is ideal for **caching**, **observer subscriptions**, and **parent-child graphs**:

```python
import weakref

class HeavyData:
    def __init__(self, name):
        self.name = name

obj = HeavyData("ServerCache")
weak_obj = weakref.ref(obj)

print("Weak reference resolves to:", weak_obj().name)  # ServerCache

del obj  # Strong reference destroyed

print("Weak reference after deletion:", weak_obj())    # None!
```

---

## 6. Drastic Memory Optimization with `__slots__`

By default, every Python instance stores its attributes in an internal dictionary called `__dict__`. 
- `__dict__` enables adding arbitrary attributes at runtime, but each dictionary introduces significant memory overhead (~150 to 200+ bytes per instance).
- If your program creates **millions of objects** (e.g. data points, coordinates, particles), this overhead causes gigabytes of wasted RAM.

By defining `__slots__`, Python allocates a fixed array of pointers for the attributes and **does not create `__dict__`**:

```python
class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ('x', 'y')  # Saves ~60-70% memory per object!
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 7. Tracking Memory with `tracemalloc`

Python provides the built-in `tracemalloc` module to trace memory usage and locate memory leaks down to exact source line numbers:

```python
import tracemalloc

tracemalloc.start()

# Code to measure
data = [str(i) * 100 for i in range(10000)]

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current / 1024:.2f} KB; Peak memory: {peak / 1024:.2f} KB")

tracemalloc.stop()
```

---

## 8. Practice Questions

1. Create 100,000 instances of a class with `__dict__` vs `__slots__` and compare the total execution time and memory footprint using `tracemalloc`.
2. Write a bidirectional `Parent` and `Child` tree node structure that uses `weakref` for child-to-parent pointers to prevent memory cycles.
3. Write a small script that deliberately introduces a circular reference between two objects, and use `gc.collect()` to find and free it.
4. Explain the difference between `copy.copy()` (shallow) and `copy.deepcopy()` (deep) when dealing with nested lists or dictionaries.
