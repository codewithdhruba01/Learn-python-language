# String in Python

A **string** in Python is a sequence of characters enclosed within **single quotes (`'`), double quotes (`"`)**, or **triple quotes (`'''` or `"""`)**. It is an immutable data type, meaning once created, it cannot be changed.

---

## 1. Creating Strings in Python

You can create a string using different types of quotes:

```python
# Using single quotes
str1 = 'Hello'

# Using double quotes
str2 = "Hello"

# Using triple quotes (for multi-line strings)
str3 = '''Hello,
This is a multi-line string'''

str4 = """Hello,
This is also a multi-line string"""
```

---

## 2. Accessing Characters in a String

Python treats strings as sequences of characters, so you can access individual characters using **indexing** and retrieve a substring using **slicing**.

### (a) Indexing (0-based index)
Each character in a string has a position (index), starting from **0**.

```python
text = "Python"
print(text[0])   # Output: P (first character)
print(text[-1])  # Output: n (last character)
```

### (b) Slicing (Getting a Substring)
You can extract parts of a string using **slicing**.

```python
text = "Python"
print(text[0:4])  # Output: Pyth (characters from index 0 to 3)
print(text[:3])   # Output: Pyt (same as [0:3])
print(text[3:])   # Output: hon (from index 3 to end)
print(text[::2])  # Output: Pto (every second character)
```

---

## 3. String Operations

### (a) Concatenation (Joining Strings)
You can join strings using the `+` operator.

```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World
```

### (b) Repetition
You can repeat a string using the `*` operator.

```python
text = "Hello "
print(text * 3)  # Output: Hello Hello Hello
```

---

## 4. String Methods

Python provides several built-in methods to manipulate strings.
the most commonly used **Python String Methods** along with examples for better understanding.

---

### 🔹 1. `upper()`
**Converts all characters to uppercase.**

```python
text = "hello world"
print(text.upper())   # Output: HELLO WORLD
```


### 🔹 2. `lower()`
**Converts all characters to lowercase.**

```python
text = "HELLO WORLD"
print(text.lower())   # Output: hello world
```

---

### 🔹 3. `title()`
**Capitalizes the first letter of each word.**

```python
text = "hello world"
print(text.title())   # Output: Hello World
```

---

### 🔹 4. `capitalize()`
**Capitalizes only the first letter of the string.**

```python
text = "hello world"
print(text.capitalize())   # Output: Hello world
```

---

### 🔹 5. `strip()`
**Removes leading and trailing whitespace or characters.**

```python
text = "   hello world   "
print(text.strip())   # Output: "hello world"
```

---

### 🔹 6. `replace(old, new)`
**Replaces a substring with another.**

```python
text = "I love Java"
print(text.replace("Java", "Python"))   # Output: I love Python
```

---

### 🔹 7. `find(substring)`
**Returns the index of the first occurrence of the substring. Returns -1 if not found.**

```python
text = "hello world"
print(text.find("world"))   # Output: 6
```

---

### 🔹 8. `split(separator)`
**Splits the string into a list based on the separator.**

```python
text = "apple,banana,mango"
print(text.split(","))   # Output: ['apple', 'banana', 'mango']
```

---

### 🔹 9. `join(iterable)`
**Joins elements of an iterable (like a list) into a string.**

```python
words = ['Hello', 'World']
print(" ".join(words))   # Output: Hello World
```

---

### 🔹 10. `startswith(substring)` / `endswith(substring)`
**Checks if a string starts or ends with the given substring.**

```python
text = "python programming"
print(text.startswith("python"))  # True
print(text.endswith("ing"))       # True
```

---

### 🔹 11. `isalpha()`
**Checks if all characters in the string are alphabets.**

```python
text = "hello"
print(text.isalpha())  # True

text2 = "hello123"
print(text2.isalpha())  # False
```

---

### 🔹 12. `isdigit()`
**Checks if all characters in the string are digits.**

```python
num = "12345"
print(num.isdigit())  # True
```

---

## 5. String Formatting

### (a) Using `f-strings` (Modern Way, Python 3.6+)
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

### (b) Using `format()` Method
```python
print("My name is {} and I am {} years old.".format(name, age))
```

### (c) Using `%` Formatting (Old Style)
```python
print("My name is %s and I am %d years old." % (name, age))
```

---

## 6. String Immutability

Strings in Python **cannot be changed** after creation. If you try to modify an existing string, it will create a new one.

```python
text = "Hello"
text[0] = "J"  # This will raise an error because strings are immutable
```

To modify a string, you must create a new one:

```python
text = "Hello"
text = "J" + text[1:]  # Output: "Jello"
```

---

## 7. Checking Substrings

You can check if a substring exists in a string using the `in` keyword.

```python
text = "Hello, World"
print("Hello" in text)  # Output: True
print("Python" not in text)  # Output: True
```

---

## 8. Escape Characters

Python provides escape sequences for including special characters in strings.

| Escape Character | Meaning | Example |
|-----------------|---------|---------|
| `\n` | Newline | `"Hello\nWorld"` |
| `\t` | Tab space | `"Hello\tWorld"` |
| `\'` | Single quote | `'It\'s a book'` |
| `\"` | Double quote | `"He said \"Hello\""` |
| `\\` | Backslash | `"C:\\path\\to\\file"` |

```python
print("Hello\nWorld")  # Output: Hello (new line) World
```

---

## 9. Raw Strings (`r""`)

A raw string treats backslashes as normal characters.

```python
text = r"C:\Users\Name"
print(text)  # Output: C:\Users\Name
```

---

## 10. String Iteration (Looping Through a String)

```python
text = "Python"
for char in text:
    print(char)
```

Output:
```
P
y
t
h
o
n
```

---

## 11. Converting Other Data Types to Strings

You can convert numbers, lists, or other types to a string using `str()`.

```python
num = 123
text = str(num)
print(text, type(text))  # Output: "123" <class 'str'>
```

---

## 12. Multi-line String Input

```python
text = """This is a
multi-line string."""
print(text)
```

---
