"""
Chapter 25: Memory Management and Performance Optimization - Garbage Collection & Weak References
Demonstrates reference counting, cyclic reference generation, manual gc collection,
and preventing memory leaks using the weakref module.
"""

import sys
import gc
import weakref


# ==========================================
# 1. Reference Counting Inspection
# ==========================================
print("--- 1. Reference Counting Inspection ---")

sample_list = ["alpha", "beta", "gamma"]
print("Initial reference count:", sys.getrefcount(sample_list))  # includes getrefcount arg

alias_1 = sample_list
alias_2 = sample_list
print("After 2 new aliases:", sys.getrefcount(sample_list))

del alias_1
del alias_2
print("After deleting aliases:", sys.getrefcount(sample_list))


# ==========================================
# 2. Circular References and Cyclic GC
# ==========================================
print("\n--- 2. Circular References & Cyclic GC ---")

class GraphNode:
    def __init__(self, name: str):
        self.name = name
        self.adjacent = None

    def __repr__(self):
        return f"GraphNode({self.name})"

# Create two nodes that point to each other
node_a = GraphNode("Node-A")
node_b = GraphNode("Node-B")
node_a.adjacent = node_b
node_b.adjacent = node_a

# Delete strong variables; they remain in memory due to the cycle!
del node_a
del node_b

# Disable automatic collection briefly to demonstrate manual sweep
gc.disable()
unreachable_before = gc.collect()  # Clean any lingering objects
gc.enable()

print(f"Triggered manual gc.collect(): cleaned {unreachable_before} cyclic objects.")


# ==========================================
# 3. Using weakref to Break Cycles
# ==========================================
print("\n--- 3. Using weakref.ref to Avoid Cycles ---")

class Parent:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = weakref.ref(self)  # Weak reference back to parent!

    def __del__(self):
        print(f"[Deallocated] Parent '{self.name}' destroyed.")

class Child:
    def __init__(self, name: str):
        self.name = name
        self.parent = None  # Will hold a weakref.ref

    def get_parent_name(self):
        if self.parent is not None:
            parent_obj = self.parent()  # Resolve weak reference
            if parent_obj:
                return parent_obj.name
        return "No parent"

    def __del__(self):
        print(f"[Deallocated] Child '{self.name}' destroyed.")

# Instantiate parent and child
p = Parent("Parent-1")
c = Child("Child-1")
p.add_child(c)

print(f"Child sees parent: {c.get_parent_name()}")

# When parent is deleted, weakref ensures immediate reclamation!
print("Deleting parent...")
del p

print(f"Child query after parent deletion: {c.get_parent_name()}")
print("Deleting child...")
del c
