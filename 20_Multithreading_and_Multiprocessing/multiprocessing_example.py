"""
Chapter 20: Multiprocessing in Python
Demonstrates bypassing the GIL for CPU-bound computations across physical cores.
"""
from multiprocessing import Process, current_process
import time
import os

def cpu_heavy_computation(number):
    """Performs an intensive calculation on a separate process."""
    proc = current_process()
    print(f"[{proc.name} | PID: {os.getpid()}] Starting computation for {number}...")
    
    total = sum(i * i for i in range(number))
    
    print(f"[{proc.name} | PID: {os.getpid()}] Completed.")
    return total

if __name__ == "__main__":
    print("--- Multiprocessing for CPU-bound Tasks ---")
    start = time.perf_counter()

    processes = []
    task_sizes = [6_000_000, 6_000_000, 6_000_000]

    # Spawn processes
    for idx, size in enumerate(task_sizes, start=1):
        p = Process(target=cpu_heavy_computation, args=(size,), name=f"Worker-{idx}")
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    total_time = time.perf_counter() - start
    print(f"\nAll parallel processes finished in {total_time:.2f} seconds!")
