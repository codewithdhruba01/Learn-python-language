"""
Chapter 16: Iterators in Python
Demonstrates the Iterator Protocol (__iter__ and __next__) and built-in iteration.
"""

# ==========================================
# 1. Built-in iterables vs iterators
# ==========================================
fruits = ["Apple", "Mango", "Banana"]
fruit_iterator = iter(fruits)

print("--- 1. Using iter() and next() ---")
print("First item :", next(fruit_iterator))
print("Second item:", next(fruit_iterator))
print("Third item :", next(fruit_iterator))

# Next call would raise StopIteration:
try:
    print(next(fruit_iterator))
except StopIteration:
    print("Reached the end of iterator (StopIteration raised).")


# ==========================================
# 2. Building a Custom Iterator Class
# ==========================================
class RangeIterator:
    """A custom implementation of range(start, stop, step) iterator."""
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        # Must return the iterator object itself
        return self

    def __next__(self):
        # Stop condition
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value


print("\n--- 2. Custom Range Iterator ---")
custom_range = RangeIterator(10, 25, 5)
for number in custom_range:
    print("Value:", number)


# ==========================================
# 3. Custom Reverse Iterator
# ==========================================
class ReverseList:
    """Iterates over a list from end to beginning without modifying it."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


print("\n--- 3. Custom Reverse Iterator ---")
names = ["Amit", "Rohit", "Sneha", "Dhruba"]
for name in ReverseList(names):
    print("Reversed:", name)
