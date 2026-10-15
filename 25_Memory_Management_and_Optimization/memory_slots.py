"""
Chapter 25: Memory Management and Performance Optimization - Slots & Profiling
Demonstrates memory comparison between default __dict__ instances and __slots__ instances,
and measures memory consumption using sys.getsizeof and tracemalloc.
"""

import sys
import tracemalloc


# ==========================================
# 1. Comparing Instance Footprint: __dict__ vs __slots__
# ==========================================
print("--- 1. Single Instance Overhead ---")

class DefaultPlayer:
    def __init__(self, name: str, level: int, health: float):
        self.name = name
        self.level = level
        self.health = health

class SlottedPlayer:
    __slots__ = ("name", "level", "health")

    def __init__(self, name: str, level: int, health: float):
        self.name = name
        self.level = level
        self.health = health

p1 = DefaultPlayer("Knight", 50, 100.0)
p2 = SlottedPlayer("Knight", 50, 100.0)

print("DefaultPlayer instance size:", sys.getsizeof(p1), "bytes")
print("DefaultPlayer __dict__ size:", sys.getsizeof(p1.__dict__), "bytes")
print("Total size for DefaultPlayer:", sys.getsizeof(p1) + sys.getsizeof(p1.__dict__), "bytes")
print("SlottedPlayer instance size:", sys.getsizeof(p2), "bytes (No __dict__ overhead!)")


# ==========================================
# 2. Large Scale Memory Benchmark using tracemalloc
# ==========================================
print("\n--- 2. Benchmark with 100,000 Objects ---")

def benchmark_default_objects(count: int = 100000):
    tracemalloc.start()
    players = [DefaultPlayer(f"Player_{i}", i % 100, 100.0) for i in range(count)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    del players
    return peak / (1024 * 1024)

def benchmark_slotted_objects(count: int = 100000):
    tracemalloc.start()
    players = [SlottedPlayer(f"Player_{i}", i % 100, 100.0) for i in range(count)]
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    del players
    return peak / (1024 * 1024)

peak_default_mb = benchmark_default_objects(50000)
peak_slotted_mb = benchmark_slotted_objects(50000)

print(f"Memory used by 50,000 Default objects: {peak_default_mb:.2f} MB")
print(f"Memory used by 50,000 Slotted objects: {peak_slotted_mb:.2f} MB")
reduction = ((peak_default_mb - peak_slotted_mb) / peak_default_mb) * 100
print(f"Memory Reduction: {reduction:.1f}% savings with __slots__!")


# ==========================================
# 3. Trying to add arbitrary attributes to __slots__
# ==========================================
print("\n--- 3. Restricting Dynamic Attributes ---")

p1.mana = 250  # Allowed on standard class
print(f"Successfully added dynamic attribute to DefaultPlayer: mana={p1.mana}")

try:
    p2.mana = 250  # Disallowed on __slots__
except AttributeError as e:
    print(f"Caught expected AttributeError on SlottedPlayer: {e}")
