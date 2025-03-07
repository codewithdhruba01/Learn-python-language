# Recursion in Python 

Recursion is a programming technique where a function calls itself to solve smaller instances of a problem until it reaches a base case. It is commonly used for problems that can be broken down into smaller subproblems, such as factorial computation, Fibonacci sequence, tree traversal, and more.

---

## 1. What is Recursion?

Recursion is a method where a function calls itself directly or indirectly to solve a problem. It consists of two main parts:
1. **Base Case** – The condition where the recursion stops.
2. **Recursive Case** – The function calls itself with modified parameters, moving toward the base case.

---

## 2. Understanding Recursion with an Example

### Factorial Calculation Using Recursion
The **factorial** of a number `n` is defined as:

```
n! = n × (n - 1) × (n - 2) × ... × 1
```

Example: `5! = 5 × 4 × 3 × 2 × 1 = 120`

#### Recursive Implementation in Python
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

---

## 3. Types of Recursion

### (a) Direct Recursion
A function calls itself directly.
```python
def direct_recursion(n):
    if n == 0:
        return
    print(n)
    direct_recursion(n - 1)
```

### (b) Indirect Recursion
A function calls another function, which in turn calls the first function.
```python
def func1(n):
    if n > 0:
        print(n)
        func2(n - 1)

def func2(n):
    if n > 0:
        print(n)
        func1(n - 2)

func1(5)
```

---

## 4. Recursion vs Iteration

| Feature      | Recursion | Iteration |
|-------------|----------|----------|
| Function Calls | Uses multiple function calls | Uses loops (for, while) |
| Memory Usage | Uses stack memory (call stack) | Efficient, no extra memory usage |
| Readability | More readable for complex problems | Sometimes less readable |
| Performance | Slower due to function call overhead | Faster |

---

## 5. Common Examples of Recursion

### (a) Fibonacci Series Using Recursion
```python
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8
```

### (b) Reverse a String Using Recursion
```python
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))  # Output: "olleh"
```

### (c) Tower of Hanoi Problem
```python
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)

tower_of_hanoi(3, 'A', 'B', 'C')
```

---

## 6. Recursion Depth and Stack Overflow

Python has a recursion depth limit (default: **1000 calls**). If a function recurses too many times, it may cause a **RecursionError**.

```python
import sys
print(sys.getrecursionlimit())  # Output: 1000

sys.setrecursionlimit(2000)  # Changing recursion depth limit
```

If recursion goes too deep, Python raises:
```
RecursionError: maximum recursion depth exceeded
```

---

## 7. When to Use Recursion?
- When the problem is naturally recursive (e.g., tree traversal, graph traversal).
- When writing a recursive solution is **simpler** and **more readable** than an iterative one.
- When you can ensure that the recursion **won’t exceed memory limits**.
---
- Avoid recursion when an **iterative approach is more efficient**.
- Avoid recursion if **memory constraints are a concern**.

---
