"""
Chapter 20: Multithreading in Python
Demonstrates Thread creation, I/O simulation, and Thread synchronization using Lock.
"""
import threading
import time

# ==========================================
# 1. Basic Multithreading (Simulating I/O tasks)
# ==========================================
def worker_task(task_name, duration):
    print(f"[{task_name}] Started (will take {duration}s)...")
    time.sleep(duration)
    print(f"[{task_name}] Completed.")

print("--- 1. Running Tasks with Multithreading ---")
start_time = time.perf_counter()

# Create two threads
t1 = threading.Thread(target=worker_task, args=("Download-Images", 2))
t2 = threading.Thread(target=worker_task, args=("Fetch-UserData", 2))

t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

elapsed = time.perf_counter() - start_time
print(f"Both tasks finished in {elapsed:.2f}s (Sequential would have taken 4.00s)!\n")


# ==========================================
# 2. Race Condition and Synchronization with Lock
# ==========================================
print("--- 2. Thread Safety with Lock ---")
shared_counter = 0
counter_lock = threading.Lock()

def safe_increment(iterations):
    global shared_counter
    for _ in range(iterations):
        # Acquire lock before modifying shared memory
        with counter_lock:
            shared_counter += 1

threads = []
num_threads = 5
iterations_per_thread = 20_000

for i in range(num_threads):
    t = threading.Thread(target=safe_increment, args=(iterations_per_thread,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

expected = num_threads * iterations_per_thread
print(f"Expected Counter: {expected}")
print(f"Actual Counter  : {shared_counter}")
print("Lock successfully prevented race condition!")
