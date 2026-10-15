"""
Chapter 17: Practical Real-World Decorators
Demonstrates Execution Timer, Call Logger, Authentication, and Decorators with Arguments.
"""
import time
from functools import wraps

# ==========================================
# 1. Performance / Execution Timer Decorator
# ==========================================
def timer(func):
    """Measures and prints function execution duration."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[TIMER] '{func.__name__}' executed in {elapsed:.6f} seconds.")
        return result
    return wrapper


@timer
def heavy_computation(n):
    return sum(i * i for i in range(n))


# ==========================================
# 2. Detailed Logger Decorator
# ==========================================
def logger(func):
    """Logs the arguments and returned values of function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
        print(f"[LOG] Calling {func.__name__}({arg_str})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned -> {result}")
        return result
    return wrapper


@logger
def calculate_tax(amount, tax_rate=0.18):
    return round(amount * tax_rate, 2)


# ==========================================
# 3. Decorator with Arguments (Configurable Retry / Repeat)
# ==========================================
def retry(max_attempts=3, delay_sec=1):
    """Retries a failing function a specified number of times."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"[RETRY] Attempt {attempts}/{max_attempts} failed with: {e}")
                    if attempts < max_attempts:
                        time.sleep(delay_sec)
                    else:
                        print("[RETRY] All attempts exhausted!")
                        raise
        return wrapper
    return decorator


# Test flaky function
attempt_count = 0

@retry(max_attempts=3, delay_sec=0.1)
def unstable_network_call():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ConnectionError("Network timeout!")
    return "Data fetched successfully on 3rd attempt!"


# ==========================================
# Main Execution
# ==========================================
if __name__ == "__main__":
    print("--- 1. Testing Timer Decorator ---")
    val = heavy_computation(500_000)

    print("\n--- 2. Testing Logger Decorator ---")
    tax = calculate_tax(1500.0, tax_rate=0.12)

    print("\n--- 3. Testing Retry Decorator ---")
    result = unstable_network_call()
    print("Final result:", result)
