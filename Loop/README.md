# Python Loops -

Loops in Python are used to execute a block of code multiple times. Instead of writing the same code repeatedly, loops help automate repetitive tasks. Python provides two main types of loops:
## There are two types of loops in Python
1. **for loop**
2. **while loop**

---

## 1. for Loop
The `for` loop is used when we want to iterate over a sequence (such as a list, tuple, string, or range).

### Syntax:
```python
for variable in sequence:
    # Code to execute in each iteration
```

### Example 1: Iterating through a list
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple  
banana  
cherry  
```

### Example 2: Using `range()` in a for loop

`range()` function return a sequence of numbers, string form ( '0' by default ) and increments by ( 1 by default)
And stop before a specified number.
```python
for i in range(5):
    print(i)
```
**Output:**
```
0  
1  
2  
3  
4  
```

### Example 3: Looping through a string
```python
for char in "Python":
    print(char)
```
**Output:**
```
P  
y  
t  
h  
o  
n  
```

### Using else with for loop
Python allows an `else` block to be used with `for` loops. The `else` block runs after the loop finishes all iterations.
```python
for i in range(3):
    print(i)
else:
    print("Loop finished!")
```
**Output:**
```
0  
1  
2  
Loop finished!  
```

---

## 2. while Loop
A `while` loop runs as long as a specified condition remains `True`.

### Syntax:
```python
while condition:
    # Code to execute
```

### Example 1: Basic while loop
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```
**Output:**
```
1  
2  
3  
4  
5  
```

### Example 2: Using break in while loop
The `break` statement is used to exit the loop immediately.
```python
num = 1
while num <= 5:
    if num == 3:
        break
    print(num)
    num += 1
```
**Output:**
```
1  
2  
```

### Example 3: Using continue in while loop
The `continue` statement skips the current iteration and moves to the next one.
```python
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
```
**Output:**
```
1  
2  
4  
5  
```

### Using else with while loop
Just like `for`, `while` also supports an `else` block.
```python
x = 1
while x < 4:
    print(x)
    x += 1
else:
    print("Loop ended!")
```
**Output:**
```
1  
2  
3  
Loop ended!  
```
---

## Practice Problems

### Problem 1: Print Even Numbers
Write a Python program to print all even numbers from 1 to 20 using a `for` loop.

### Problem 2: Sum of First N Natural Numbers
Write a Python program using a `while` loop to find the sum of the first 10 natural numbers.

### Problem 3: Reverse a String
Write a `for` loop that iterates over a string and prints it in reverse order.

### Problem 4: Find First Multiple of 7
Write a `while` loop that finds and prints the first multiple of 7 greater than 50.

### Problem 5: Count Vowels in a String
Write a program that uses a `for` loop to count the number of vowels in a given string.



## Conclusion
- Use `for` loops when iterating over a sequence (lists, strings, tuples, etc.).
- Use `while` loops when the number of iterations is not fixed and depends on a condition.
- Use `break` to exit a loop prematurely.
- Use `continue` to skip an iteration and move to the next one.
- Use `else` with loops for additional execution after the loop finishes normally.

---