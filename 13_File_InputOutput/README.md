# File Input and Output (I/O) in Python

File handling in Python is essential for reading and writing data to files. Python provides built-in functions to handle file operations such as opening, reading, writing, and closing files.

---

## 1. Opening a File in Python
- The key function for working with files in Python is the open() function.
- The open() function takes two parameters; filename, and mode.
- There are six different methods (modes) for opening a file:

### Syntax:
```python
file = open("filename", "mode") 
```
- `"filename"`: Name of the file to be opened.
- `"mode"`: Mode in which the file should be opened.

### File Modes in Python

| Mode | Description |
|------|------------|
| `'r'` | Read mode (default). Opens a file for reading. |
| `'w'` | Write mode. Creates a new file or overwrites an existing file. |
| `'a'` | Append mode. Adds data to the end of the file. |
| `'x'` | Exclusive creation. Fails if the file exists. |
| `'b'` | Binary mode (used with `'rb'`, `'wb'`, etc.). |
| `'t'` | Text mode (default, used with `'rt'`, `'wt'`, etc.). |

---

<img alt="files" height="200" src="./images/ExWNT-white-bg.png" width="350"/>

## 2. Reads Entire File
To read a file, we use the `read()` method or `readline()` / `readlines()`.

### Example: Reading an entire file
```python
file = open("example.txt", "r")  # Open file in read mode
content = file.read()  # Read entire file content
print(content)
file.close()  # Close the file
```

### Example: Reading line by line
```python
file = open("example.txt", "r")
for line in file:
    print(line.strip())  # Removes newline character
file.close()
```

### Example: Using `readline()` and `readlines()`
```python
file = open("example.txt", "r")
print(file.readline())   # Reads one line
print(file.readlines())  # Reads all lines and returns a list
file.close()
```

---

## 3. Writing to a File
To write data into a file, we use `write()` or `writelines()`.

### Example: Writing to a file
```python
file = open("example.txt", "w")  # Open file in write mode
file.write("Hello, World!\n")  # Write a single line
file.write("Python file handling example.")
file.close()
```

### Example: Appending to a file
```python
file = open("example.txt", "a")  # Open file in append mode
file.write("\nAppending new text.")
file.close()
```

---

## 4. Using `with` Statement (Best Practice)
Using `with open()` automatically closes the file after use, preventing file corruption.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File automatically closes after exiting the block
```

---

## 5. Working with Binary Files
For handling non-text files (images, audio, etc.), use binary mode.

### Example: Copying an image
```python
with open("image.jpg", "rb") as source:
    with open("copy.jpg", "wb") as destination:
        destination.write(source.read())
```

---

## 6. File Handling with Exception Handling
To handle errors (e.g., file not found), use `try-except`.

```python
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file name.")
```

---

## 7. Working with File Paths
Use the `os` and `pathlib` modules for handling file paths.

### Example: Checking if a file exists
```python
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")
```

### Using `pathlib` (Recommended)
```python
from pathlib import Path

file_path = Path("example.txt")
if file_path.exists():
    print("File exists")
```

---

## 8. File Handling with CSV Files
Python’s `csv` module allows reading and writing CSV files.

### Writing to a CSV file
```python
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "San Francisco"])
```

### Reading from a CSV file
```python
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## 9. JSON File Handling
Python’s `json` module helps in working with JSON data.

### Writing JSON Data
```python
import json

data = {"name": "Alice", "age": 25, "city": "New York"}

with open("data.json", "w") as file:
    json.dump(data, file)  # Convert Python dictionary to JSON
```

### Reading JSON Data
```python
with open("data.json", "r") as file:
    data = json.load(file)  # Convert JSON to Python dictionary
    print(data)
```

---

## 10. Deleting a File
To delete a file, use the `os` module.

```python
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted")
else:
    print("File does not exist")
```

---