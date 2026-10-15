# Chapter 20: Multithreading and Multiprocessing in Python

Concurrency and parallelism enable Python programs to perform multiple tasks at the same time, speeding up execution for both I/O-bound and CPU-bound operations.

---

## 📌 Table of Contents
1. [Concurrency vs Parallelism](#1-concurrency-vs-parallelism)
2. [I/O-Bound vs CPU-Bound Tasks](#2-io-bound-vs-cpu-bound-tasks)
3. [The Python GIL (Global Interpreter Lock)](#3-the-python-gil)
4. [Multithreading with `threading`](#4-multithreading-with-threading)
5. [Thread Synchronization with `Lock`](#5-thread-synchronization-with-lock)
6. [Multiprocessing with `multiprocessing`](#6-multiprocessing-with-multiprocessing)
7. [The High-Level `concurrent.futures` API](#7-the-high-level-concurrentfutures-api)
8. [Comparison Summary: Threading vs Multiprocessing](#8-comparison-summary)
9. [Practice Questions](#9-practice-questions)

---

## 1. Concurrency vs Parallelism

```
Concurrency (Multithreading on 1 Core):
Core 1: [Task A] -> [Task B] -> [Task A] -> [Task B] (Context switching)

Parallelism (Multiprocessing across multiple CPU Cores):
Core 1: [======= Task A =======]
Core 2: [======= Task B =======] (True simultaneous execution)
```

- **Concurrency**: Managing multiple tasks at the same time by interleaving execution.
- **Parallelism**: Executing multiple computations simultaneously on multiple physical CPU cores.

---

## 2. I/O-Bound vs CPU-Bound Tasks

| Task Type | Definition | Bottleneck | Ideal Solution |
|---|---|---|---|
| **I/O-Bound** | Waiting for network requests, disk read/write, database queries | Input/Output speed | **Multithreading** or **AsyncIO** |
| **CPU-Bound** | Heavy mathematical computation, image/video rendering, ML model inference | CPU processing power | **Multiprocessing** |

---

## 3. The Python GIL (Global Interpreter Lock)

In standard CPython, the **GIL** is a mutex that prevents multiple native threads from executing Python bytecode at the exact same time on multiple cores.

### Impact of GIL:
- For **CPU-bound tasks**, multithreading does NOT make Python code faster (in fact, overhead may make it slower). To utilize all CPU cores for heavy calculations, use **`multiprocessing`**!
- For **I/O-bound tasks**, the thread releases the GIL while waiting for network or disk operations, so **`threading` works wonderfully**!

---

## 4. Multithreading with `threading`

```python
import threading
import time

def download_file(filename, delay):
    print(f"Starting download: {filename}")
    time.sleep(delay)  # Simulates network wait
    print(f"Finished download: {filename}")

# Creating threads
t1 = threading.Thread(target=download_file, args=("file1.zip", 2))
t2 = threading.Thread(target=download_file, args=("file2.zip", 2))

# Starting threads
t1.start()
t2.start()

# Waiting for both threads to finish
t1.join()
t2.join()

print("All downloads complete!")
```

---

## 5. Thread Synchronization with `Lock`

When multiple threads read and write to the same shared memory, a **race condition** can corrupt data. A `Lock` ensures only one thread updates the data at a time.

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100_000):
        with lock:  # Thread-safe increment
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()

print("Final Counter:", counter)  # Exactly 400,000!
```

---

## 6. Multiprocessing with `multiprocessing`

Because each `Process` runs its own Python interpreter with its own GIL and separate memory space, it achieves **true parallelism**.

> **Note on Windows:** You must always wrap process start code inside `if __name__ == '__main__':` to prevent infinite child process spawning.

```python
from multiprocessing import Process
import os

def calculate_heavy_square(n):
    print(f"Process PID: {os.getpid()} calculating square of {n}")
    return n * n

if __name__ == "__main__":
    processes = []
    for num in [10, 20, 30]:
        p = Process(target=calculate_heavy_square, args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
```

---

## 7. The High-Level `concurrent.futures` API

Python provides a cleaner, modern API using `ThreadPoolExecutor` and `ProcessPoolExecutor`.

```python
from concurrent.futures import ThreadPoolExecutor

urls = ["site1.com", "site2.com", "site3.com"]

def fetch(url):
    return f"Data from {url}"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(fetch, urls)
    for res in results:
        print(res)
```

---

## 8. Comparison Summary

| Feature | `threading` | `multiprocessing` |
|---|---|---|
| **Memory** | Shared memory between threads | Separate memory per process |
| **GIL Constraint** | Restricted by GIL | Bypasses GIL (1 GIL per process) |
| **Overhead** | Lightweight creation | Higher RAM & process creation cost |
| **Best For** | Web scraping, file download, network I/O | Data crunching, math, image processing |

---

## 9. Practice Questions

1. Write a script that uses `ThreadPoolExecutor` to simulate downloading 5 web pages concurrently and prints their completion times.
2. Demonstrate a race condition where 2 threads increment a shared variable without a lock, and then fix it using `threading.Lock`.
3. Write a multiprocessing program that computes factorials of several large numbers concurrently across multiple CPU cores.
