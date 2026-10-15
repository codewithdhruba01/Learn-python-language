"""
Chapter 16: Generators in Python
Demonstrates yield, generator expressions, memory benchmark, and infinite series.
"""
import sys

# ==========================================
# 1. Basic Generator Function with yield
# ==========================================
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1

print("--- 1. Simple Generator ---")
counter = count_up_to(4)
for val in counter:
    print("Yielded:", val)


# ==========================================
# 2. Infinite Fibonacci Generator
# ==========================================
def fibonacci_stream():
    """Generates an infinite stream of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n--- 2. Fibonacci Generator (First 8 numbers) ---")
fib = fibonacci_stream()
first_eight = [next(fib) for _ in range(8)]
print("Fibonacci sequence:", first_eight)


# ==========================================
# 3. Memory Consumption Benchmark: List vs Generator
# ==========================================
print("\n--- 3. Memory Comparison (1 Million Items) ---")
limit = 1_000_000

# Eager evaluation: List stores all elements in RAM
large_list = [x ** 2 for x in range(limit)]
list_memory = sys.getsizeof(large_list)

# Lazy evaluation: Generator computes one item on demand
large_gen = (x ** 2 for x in range(limit))
gen_memory = sys.getsizeof(large_gen)

print(f"List Memory     : {list_memory:,} bytes (~{list_memory / (1024*1024):.2f} MB)")
print(f"Generator Memory: {gen_memory:,} bytes (~{gen_memory / 1024:.2f} KB)")
print(f"Generator is ~{list_memory // gen_memory:,} times more memory-efficient here!")


# ==========================================
# 4. Generator Pipeline (Data Processing)
# ==========================================
print("\n--- 4. Generator Data Pipeline ---")
def numbers_source(n):
    for i in range(1, n + 1):
        yield i

def filter_odds(seq):
    for item in seq:
        if item % 2 != 0:
            yield item

def square_items(seq):
    for item in seq:
        yield item ** 2

# Chaining generators together like a streaming pipeline
pipeline = square_items(filter_odds(numbers_source(10)))
print("Pipeline result (odd squares up to 10):", list(pipeline))
