# Tuples in Python

A **tuple** in Python is an **ordered, immutable** collection of elements. It is similar to a list but cannot be modified after creation.

**Tuples** are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.


---
## 1. Creating a Tuple
You can create a tuple using parentheses `()`:
```python
my_tuple = (1, 2, 3, "hello", 4.5)
print(my_tuple)  # (1, 2, 3, 'hello', 4.5)
```
For a **single-element tuple**, include a comma:
```python
single_tuple = (5,)
```

---
## 2. Accessing Elements
You can access elements using **indexing**:
```python
my_tuple = (10, 20, 30, 40)
print(my_tuple[0])  # 10
print(my_tuple[-1])  # 40
```

**Slicing** is also possible:
```python
numbers = (0, 1, 2, 3, 4, 5, 6)
print(numbers[1:4])  # (1, 2, 3)
```

---
## 3. Tuple Immutability
Tuples **cannot** be modified after creation:
```python
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # ❌ TypeError: 'tuple' object does not support item assignment
```

---
## 4. Tuple Methods
| Method | Description |
|--------|------------|
| `count(value)` | Returns occurrences of a value in the tuple. |
| `index(value)` | Returns the first index of the value. |

Example:
```python
numbers = (1, 2, 3, 2, 4, 2)
print(numbers.count(2))  # 3
print(numbers.index(3))  # 2
```

---
## 5. Tuple Unpacking
You can assign tuple values to multiple variables:
```python
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)  # 10 20 30
```

Using `*` for variable-length unpacking:
```python
values = (1, 2, 3, 4, 5)
a, *b, c = values
print(b)  # [2, 3, 4]
```

---
## 6. Converting Between Lists and Tuples
Convert a **list to a tuple**:
```python
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
```
Convert a **tuple to a list**:
```python
new_list = list(my_tuple)
```

---
## 7. When to Use Tuples?
| Use Tuples When... | Use Lists When... |
|-------------------|----------------|
| Data should not change | Data needs modification |
| Faster access needed | Performance is not a concern |
| Used as dictionary keys | Not used as dictionary keys |

---
## 8. Summary
- Tuples are **immutable and ordered**.
- Use `()` to define a tuple.
- Supports **indexing, slicing, and unpacking**.
- **Faster and memory-efficient** than lists.

📌 **Use tuples when you need a fixed collection of values!** 🚀
