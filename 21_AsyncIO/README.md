# Chapter 21: AsyncIO and Asynchronous Programming in Python

`asyncio` is Python's built-in library to write concurrent code using the **async / await** syntax. It is the gold standard for high-performance network applications, web scrapers, microservices, and web APIs (FastAPI, aiohttp).

---

## 📌 Table of Contents
1. [Synchronous vs Asynchronous Programming](#1-synchronous-vs-asynchronous-programming)
2. [What is an Event Loop?](#2-what-is-an-event-loop)
3. [The `async` and `await` Keywords](#3-the-async-and-await-keywords)
4. [Running Coroutines with `asyncio.run()`](#4-running-coroutines-with-asynciorun)
5. [Concurrent Execution with `asyncio.gather()`](#5-concurrent-execution-with-asynciogather)
6. [Managing Background Tasks with `asyncio.create_task()`](#6-managing-background-tasks-with-asynciocreatetask)
7. [Handling Timeouts with `asyncio.wait_for()`](#7-handling-timeouts-with-asynciowaitfor)
8. [Threading vs Multiprocessing vs AsyncIO: Which to Choose?](#8-threading-vs-multiprocessing-vs-asyncio)
9. [Common Pitfalls in AsyncIO](#9-common-pitfalls-in-asyncio)
10. [Practice Questions](#10-practice-questions)

---

## 1. Synchronous vs Asynchronous Programming

- **Synchronous (Blocking)**:
  Each line waits for the previous line to finish completely before executing. If an API call takes 2 seconds, the entire program freezes for 2 seconds.
- **Asynchronous (Non-blocking)**:
  While waiting for an external operation (like a network request or database query), Python yields control back to the **Event Loop**, allowing other tasks to run in the meantime.

```
Synchronous:
Task 1 [====Wait====] -> Task 2 [====Wait====] -> Task 3 [====Wait====]  (Total: 6s)

Asynchronous:
Task 1 [Wait]
Task 2 [Wait]  (All wait concurrently on 1 single thread)
Task 3 [Wait]                                                             (Total: ~2s)
```

---

## 2. What is an Event Loop?

The **Event Loop** is the engine behind `asyncio`. It maintains a queue of tasks. Whenever a task is paused waiting on I/O (via `await`), the event loop switches to execute another task that is ready to run.

---

## 3. The `async` and `await` Keywords

- **`async def`**: Declares a coroutine function. Calling it does not run it immediately; it returns a coroutine object.
- **`await`**: Pauses the execution of the coroutine until the awaited operation completes, allowing other tasks to run. Can only be used inside an `async def` function.

```python
import asyncio

async def greet():
    print("Hello...")
    await asyncio.sleep(1)  # Non-blocking pause
    print("...World!")

# Run the coroutine
asyncio.run(greet())
```

---

## 4. Running Coroutines with `asyncio.run()`

`asyncio.run(coroutine)` creates a new event loop, executes the top-level coroutine, and closes the event loop when finished.

---

## 5. Concurrent Execution with `asyncio.gather()`

`asyncio.gather()` takes multiple coroutines and schedules them to run concurrently, returning a list of their results.

```python
import asyncio
import time

async def fetch_user(user_id):
    print(f"Fetching user {user_id}...")
    await asyncio.sleep(1)  # Simulating network latency
    return {"id": user_id, "name": f"User_{user_id}"}

async def main():
    start = time.perf_counter()
    # Runs all 3 calls concurrently:
    results = await asyncio.gather(
        fetch_user(1),
        fetch_user(2),
        fetch_user(3)
    )
    print("Results:", results)
    print(f"Total time: {time.perf_counter() - start:.2f} seconds")

asyncio.run(main())
```
**Output:**
```
Fetching user 1...
Fetching user 2...
Fetching user 3...
Results: [{'id': 1, 'name': 'User_1'}, {'id': 2, 'name': 'User_2'}, {'id': 3, 'name': 'User_3'}]
Total time: 1.01 seconds
```
*(Sequential would have taken 3 seconds!)*

---

## 6. Managing Background Tasks with `asyncio.create_task()`

Use `asyncio.create_task()` to schedule a coroutine immediately in the event loop as a background task.

```python
async def periodic_heartbeat():
    while True:
        print("[HEARTBEAT] System alive...")
        await asyncio.sleep(2)

async def main():
    task = asyncio.create_task(periodic_heartbeat())
    await asyncio.sleep(5)
    task.cancel()  # Stop the background task

asyncio.run(main())
```

---

## 7. Handling Timeouts with `asyncio.wait_for()`

Prevent tasks from hanging indefinitely by enforcing a timeout:

```python
async def slow_api_call():
    await asyncio.sleep(5)
    return "Data"

async def main():
    try:
        data = await asyncio.wait_for(slow_api_call(), timeout=2.0)
        print(data)
    except asyncio.TimeoutError:
        print("Operation timed out after 2 seconds!")

asyncio.run(main())
```

---

## 8. Threading vs Multiprocessing vs AsyncIO

| Feature | `threading` | `multiprocessing` | `asyncio` |
|---|---|---|---|
| **Mechanism** | OS Preemptive Threads | Multiple OS Processes | Cooperative Multitasking (Coroutines) |
| **Concurrency Type**| Multi-threaded | True Multi-core Parallelism | Single-threaded Asynchronous |
| **Resource Usage** | Medium | High (separate memory) | Very Low (thousands of connections) |
| **GIL Limitation** | Yes (limited by GIL) | No (bypasses GIL) | Yes (runs on single thread) |
| **Best For** | Legacy I/O code, GUI apps | CPU calculations, data science | Web scraping, high-concurrency servers, APIs |

---

## 9. Common Pitfalls in AsyncIO

1. **Calling blocking functions inside async code**:
   ```python
   # ❌ Bad: Blocks the entire event loop!
   time.sleep(2)

   # ✅ Good: Non-blocking pause
   await asyncio.sleep(2)
   ```
2. **Forgetting `await`**:
   Calling `my_coroutine()` without `await` only creates a coroutine object; it never executes!
3. **Blocking CPU calculations in async loop**:
   If you have a heavy math loop, run it in a thread/process executor via `loop.run_in_executor()`.

---

## 10. Practice Questions

1. Create an asynchronous function `fetch_stock_price(symbol)` that sleeps for a random time between 0.5 and 1.5 seconds and returns a simulated price. Use `asyncio.gather()` to fetch prices for 5 symbols concurrently.
2. Write a program using `asyncio.wait_for()` that tries to connect to a simulated server with a 3-second timeout.
3. Build a simple producer-consumer queue using `asyncio.Queue`.
