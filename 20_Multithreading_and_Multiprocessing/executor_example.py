"""
Chapter 20: Concurrent.Futures (ThreadPoolExecutor & ProcessPoolExecutor)
Demonstrates the modern, high-level interface for concurrent task execution.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def simulate_fetch_user_data(user_id):
    """Simulates an API call with varying response times."""
    duration = (user_id % 3) + 1
    time.sleep(duration * 0.5)
    return {
        "user_id": user_id,
        "name": f"User_{user_id}",
        "time_taken": duration * 0.5
    }

def main():
    user_ids = [101, 102, 103, 104, 105]

    print("--- 1. Using ThreadPoolExecutor with map() ---")
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        # map() returns results in the original order of the input iterable
        results = executor.map(simulate_fetch_user_data, user_ids)
        for res in results:
            print(f"Fetched: {res}")
    print(f"Finished in {time.perf_counter() - start:.2f}s\n")


    print("--- 2. Using as_completed() for fastest-first processing ---")
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks individually to get Future objects
        futures = {executor.submit(simulate_fetch_user_data, uid): uid for uid in user_ids}
        for future in as_completed(futures):
            uid = futures[future]
            try:
                data = future.result()
                print(f"Result ready for ID {uid}: {data}")
            except Exception as e:
                print(f"Error fetching ID {uid}: {e}")
    print(f"Finished in {time.perf_counter() - start:.2f}s")

if __name__ == "__main__":
    main()
