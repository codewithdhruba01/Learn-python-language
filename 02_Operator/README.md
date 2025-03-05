# Operators in Python 

Operators in Python are special symbols that perform operations on variables and values. They are essential for performing computations, making decisions, and manipulating data.

## Types of Operators in Python

1. **Arithmetic Operators**
2. **Comparison (Relational) Operators**
3. **Logical Operators**
4. **Bitwise Operators**
5. **Assignment Operators**
6. **Identity Operators**
7. **Membership Operators**

---

## 1. Arithmetic Operators

These operators perform mathematical operations.

| Operator | Description     | Example (`a = 10, b = 3`) |
|----------|---------------|------------------------------|
| `+`  | Addition        | `a + b = 13`  |
| `-`  | Subtraction     | `a - b = 7`   |
| `*`  | Multiplication  | `a * b = 30`  |
| `/`  | Division (float)| `a / b = 3.33` |
| `//` | Floor Division  | `a // b = 3`  |
| `%`  | Modulus (Remainder) | `a % b = 1`  |
| `**` | Exponentiation  | `a ** b = 1000` |

---

## 2. Comparison (Relational) Operators

These operators compare two values and return `True` or `False`.

| Operator | Description | Example (`a = 10, b = 3`) |
|----------|------------|------------------------------|
| `==`  | Equal to       | `a == b → False` |
| `!=`  | Not equal to   | `a != b → True`  |
| `>`   | Greater than   | `a > b → True`   |
| `<`   | Less than      | `a < b → False`  |
| `>=`  | Greater than or equal to | `a >= b → True` |
| `<=`  | Less than or equal to | `a <= b → False` |

---

## 3. Logical Operators

Used to combine conditional statements.

| Operator | Description | Example (`x = True, y = False`) |
|----------|------------|-------------------------------------|
| `and`   | Returns `True` if both conditions are true | `x and y → False` |
| `or`    | Returns `True` if at least one condition is true | `x or y → True` |
| `not`   | Returns the opposite of the condition | `not x → False` |

---

## 4. Bitwise Operators

These operators work at the **binary level**.

| Operator | Description | Example (`a = 5 (101), b = 3 (011)`) |
|----------|--|--------------------------------------|
| `&`      | Bitwise AND | `a & b → 1 (001)`                    |
|          | Bitwise OR  |                                      |
| `^`      | Bitwise XOR | `a ^ b → 6 (110)`                    |
| `~`      | Bitwise NOT | `~a → -6`                            |
| `<<`     | Left shift | `a << 1 → 10 (1010)`                 |
| `>>`     | Right shift | `a >> 1 → 2 (10)`                    |

---

## 5. Assignment Operators

Assign values to variables.

| Operator | Description | Example (`a = 10`) |
|----------|------------|---------------------|
| `=`   | Assign      | `a = 10`  |
| `+=`  | Add and assign | `a += 5` (now `a = 15`) |
| `-=`  | Subtract and assign | `a -= 5` (now `a = 5`) |
| `*=`  | Multiply and assign | `a *= 2` (now `a = 20`) |
| `/=`  | Divide and assign | `a /= 2` (now `a = 5.0`) |
| `//=` | Floor divide and assign | `a //= 3` (now `a = 3`) |
| `%=`  | Modulus and assign | `a %= 3` (now `a = 1`) |
| `**=` | Exponentiate and assign | `a **= 2` (now `a = 100`) |

---

## 6. Identity Operators

Check if two variables refer to the same memory location.

| Operator | Description | Example (`a = [1, 2, 3]`, `b = a`, `c = [1, 2, 3]`) |
|----------|------------|------------------------------------------|
| `is`   | Returns `True` if both variables reference the same object | `a is b → True` |
| `is not` | Returns `True` if both variables reference different objects | `a is not c → True` |

---

## 7. Membership Operators

Check if a value exists in a sequence (list, string, tuple, etc.).

| Operator | Description | Example (`x = [1, 2, 3]`) |
|----------|------------|-----------------------------|
| `in`    | Returns `True` if the value is found in the sequence | `2 in x → True` |
| `not in` | Returns `True` if the value is **not** found in the sequence | `5 not in x → True` |

---

## Examples

### Using Arithmetic Operators
```python
x = 10
y = 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.33
print(x // y) # 3
print(x % y)  # 1
print(x ** y) # 1000
```

### Using Logical Operators
```python
x = True
y = False
print(x and y) # False
print(x or y)  # True
print(not x)   # False
```

### Using Membership Operators
```python
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)   # True
print(10 not in numbers)  # True
```

### Using Identity Operators
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)    # True
print(a is c)    # False
print(a == c)    # True (because values are same)
```

---


