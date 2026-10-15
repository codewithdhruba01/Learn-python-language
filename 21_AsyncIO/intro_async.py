"""
Chapter 21: AsyncIO Basics
Demonstrates async def, await, coroutines, and running with asyncio.run().
"""
import asyncio
import time

# ==========================================
# 1. Defining and Running Coroutines
# ==========================================
async def async_worker(worker_id, wait_seconds):
    print(f"[Worker {worker_id}] Starting work (takes {wait_seconds}s)...")
    # asyncio.sleep is non-blocking (unlike time.sleep)
    await asyncio.sleep(wait_seconds)
    print(f"[Worker {worker_id}] Finished work!")
    return f"Result from worker {worker_id}"


async def main():
    print("--- 1. Running Asynchronous Coroutines ---")
    start = time.perf_counter()

    # Calling directly with await (sequential inside coroutine)
    res1 = await async_worker(1, 1.0)
    res2 = await async_worker(2, 1.0)

    print("Returned:", res1, "and", res2)
    print(f"Sequential async took: {time.perf_counter() - start:.2f}s\n")


# ==========================================
# 2. Background Task Execution with create_task
# ==========================================
async def background_counter():
    count = 1
    while count <= 3:
        print(f"  [Background Ping #{count}]")
        await asyncio.sleep(0.5)
        count += 1

async def task_demo():
    print("--- 2. Background Tasks with asyncio.create_task ---")
    # Schedule background task on event loop immediately
    bg_task = asyncio.create_task(background_counter())

    # Do other work on the main coroutine
    print("Main task doing work...")
    await asyncio.sleep(1.2)
    print("Main task work done!")

    # Await background task completion
    await bg_task

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(task_demo())
