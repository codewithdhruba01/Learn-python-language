# Chapter 19: Context Managers in Python

Context managers provide an elegant, safe, and automated way to allocate and release system resources such as files, database connections, locks, and network sockets using the `with` statement.

---

## 📌 Table of Contents
1. [Why Context Managers? (The Resource Leak Problem)](#1-why-context-managers)
2. [The `with` Statement](#2-the-with-statement)
3. [The Context Manager Protocol: `__enter__` and `__exit__`](#3-the-context-manager-protocol)
4. [Handling Exceptions in `__exit__`](#4-handling-exceptions-in-__exit__)
5. [Creating Context Managers using `contextlib`](#5-creating-context-managers-using-contextlib)
6. [Useful Utilities in `contextlib`](#6-useful-utilities-in-contextlib)
7. [Real-World Use Cases](#7-real-world-use-cases)
8. [Practice Questions](#8-practice-questions)

---

## 1. Why Context Managers?

When working with external resources (files, sockets, thread locks), you must always clean them up:

```python
# ❌ Risky: If an error happens before file.close(), the file handle leaks!
file = open("data.txt", "w")
file.write("Hello")
# If an exception happens here, file is never closed!
file.close()
```

Without context managers, you are forced to write verbose `try...finally` blocks every single time:
```python
file = open("data.txt", "w")
try:
    file.write("Hello")
finally:
    file.close()  # Guaranteed, but verbose!
```

---

## 2. The `with` Statement

The `with` statement simplifies this by automatically handling cleanup:

```python
with open("data.txt", "w") as file:
    file.write("Hello, World!")
# The file is GUARANTEED to be closed here, even if write() crashes!
```

---

## 3. The Context Manager Protocol

Any class can become a context manager by implementing two magic methods:
1. **`__enter__(self)`**:
   - Runs when entering the `with` block.
   - Its return value is bound to the variable after `as` (e.g. `with MyResource() as res:`).
2. **`__exit__(self, exc_type, exc_val, exc_tb)`**:
   - Runs when leaving the `with` block (both on success and on error).
   - Receives exception details if an error occurred inside the block.

### Example: Custom File Manager
```python
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("[ENTER] Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[EXIT] Closing file...")
        if self.file:
            self.file.close()

# Usage:
with ManagedFile("hello.txt", "w") as f:
    f.write("Written via ManagedFile!")
```

---

## 4. Handling Exceptions in `__exit__`

The arguments to `__exit__` are:
- `exc_type`: Exception class (e.g., `ValueError`)
- `exc_val`: Exception instance (e.g., `ValueError("invalid")`)
- `exc_tb`: Traceback object

### Suppressing vs Propagating Exceptions:
- If `__exit__` returns **`True`**, the exception is **suppressed** (swallowed) and execution continues outside the `with` block.
- If `__exit__` returns `False` or `None`, the exception is **propagated** normally.

```python
class SuppressErrors:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"[EXIT] Handled and suppressed exception: {exc_val}")
            return True  # Suppress the exception!

with SuppressErrors():
    x = 10 / 0  # ZeroDivisionError is suppressed!

print("Program continues without crashing!")
```

---

## 5. Creating Context Managers using `contextlib`

Instead of creating a full class, you can write a generator function decorated with `@contextmanager`:

```python
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename, mode):
    # Setup code (equivalent to __enter__)
    file = open(filename, mode)
    try:
        yield file  # Value yielded becomes target of 'as'
    finally:
        # Teardown / cleanup code (equivalent to __exit__)
        file.close()

with open_managed_file("test.txt", "w") as f:
    f.write("Written easily!")
```

---

## 6. Useful Utilities in `contextlib`

### A. `contextlib.suppress(*exceptions)`
Ignores specified exceptions cleanly without messy try/except blocks:
```python
import os
from contextlib import suppress

# Silently ignore if file doesn't exist
with suppress(FileNotFoundError):
    os.remove("ghost_file.txt")
```

### B. `contextlib.redirect_stdout`
Redirects `print()` outputs temporarily to a file or memory buffer:
```python
import sys
from contextlib import redirect_stdout

with open("output.log", "w") as f:
    with redirect_stdout(f):
        print("This text goes into output.log, not the terminal!")
```

---

## 7. Real-World Use Cases

1. **Database Connections**: Committing transactions on success, rolling back on error, closing connection on exit.
2. **Thread / Process Locks**: Acquiring mutex lock upon entering, releasing upon exiting (`with lock:`).
3. **Timer / Profiler**: Measuring the exact elapsed time for any block of code.
4. **Temporary Directory Changes**: Changing current directory temporarily and resetting back to original on exit.

---

## 8. Practice Questions

1. Create a class-based context manager `ExecutionTimer` that records how long a block of code took to execute and prints the result on exit.
2. Build a generator-based context manager `@temporary_env_var(key, value)` that sets an environment variable temporarily inside the `with` block and restores its original value upon exit.
3. Build a context manager `DatabaseTransaction` that prints `"Transaction Committed"` if no errors occur, or `"Transaction Rolled Back"` if an error occurs.
