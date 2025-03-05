# Conditional Statements in Python

Conditional statements in Python allow a program to execute different code blocks based on certain conditions. These statements control the flow of execution depending on whether a condition evaluates to `True` or `False`.

## 1. Types of Conditional Statements in Python

Python provides the following conditional statements:
1. **if statement**
2. **if-else statement**
3. **if-elif-else statement**
4. **Nested if statement**
5. **Short-hand if and if-else (Ternary Operator)**

---

## 2. Explanation with Syntax and Examples

### 1. if Statement
The `if` statement executes a block of code only if the given condition evaluates to `True`.

#### Syntax:
```python
if condition:
    # Code to execute if the condition is True
```

#### Example:
```python
age = 18
if age >= 18:
    print("You are eligible to vote.")
```
**Output:**  
```
You are eligible to vote.
```

---

### 2. if-else Statement
The `if-else` statement provides an alternative block of code to execute when the condition is `False`.

#### Syntax:
```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

#### Example:
```python
number = 10
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
**Output:**  
```
Even number
```

---

### 3. if-elif-else Statement
The `if-elif-else` statement is used when there are multiple conditions to check. The program executes the first condition that evaluates to `True`. If none of the conditions are `True`, the `else` block executes.

#### Syntax:
```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
elif condition3:
    # Code to execute if condition3 is True
else:
    # Code to execute if all conditions are False
```

#### Example:
```python
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```
**Output:**  
```
Grade: C
```

---

### 4. Nested if Statement
A nested `if` statement is when an `if` statement is placed inside another `if` or `else` block.

#### Syntax:
```python
if condition1:
    if condition2:
        # Code to execute if both conditions are True
    else:
        # Code to execute if condition1 is True but condition2 is False
else:
    # Code to execute if condition1 is False
```

#### Example:
```python
num = 15

if num > 0:
    print("Positive number")
    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
else:
    print("Negative number")
```
**Output:**  
```
Positive number
Divisible by 5
```

---

### 5. Short-hand if and if-else (Ternary Operator)

#### Short-hand if Statement
If there is only one statement to execute inside the `if` block, we can write it in a single line.

#### Syntax:
```python
if condition: statement
```

#### Example:
```python
x = 10
if x > 5: print("x is greater than 5")
```
**Output:**  
```
x is greater than 5
```

---

#### Short-hand if-else (Ternary Operator)
A short-hand `if-else` can be written using the **ternary operator**.

#### Syntax:
```python
value_if_true if condition else value_if_false
```

#### Example:
```python
num = 10
result = "Even" if num % 2 == 0 else "Odd"
print(result)
```
**Output:**  
```
Even
```

---

## 3. Logical Operators in Conditional Statements
Sometimes, we need to check multiple conditions together using **logical operators**:
- `and` → Returns `True` if both conditions are `True`.
- `or` → Returns `True` if at least one condition is `True`.
- `not` → Reverses the boolean value of a condition.

#### Example:
```python
age = 25
income = 5000

if age > 18 and income > 4000:
    print("Eligible for a loan")
else:
    print("Not eligible for a loan")
```
**Output:**  
```
Eligible for a loan
```

---