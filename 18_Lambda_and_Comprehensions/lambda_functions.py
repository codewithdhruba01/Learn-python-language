"""
Chapter 18: Lambda Functions & Higher-Order Functions in Python
Demonstrates lambda, map(), filter(), reduce(), and custom sorting keys.
"""
from functools import reduce

# ==========================================
# 1. Basic Lambda Syntax
# ==========================================
print("--- 1. Basic Lambda Functions ---")
cube = lambda x: x ** 3
multiply = lambda a, b: a * b
is_even = lambda n: n % 2 == 0

print("Cube of 3     :", cube(3))
print("Multiply 6 x 7:", multiply(6, 7))
print("Is 14 even?   :", is_even(14))


# ==========================================
# 2. map(), filter(), and reduce()
# ==========================================
print("\n--- 2. map(), filter(), reduce() ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map(): Double each number
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled)

# filter(): Select only multiples of 3
multiples_of_three = list(filter(lambda x: x % 3 == 0, numbers))
print("Multiples of 3 :", multiples_of_three)

# reduce(): Cumulative sum of all elements
total_sum = reduce(lambda acc, x: acc + x, numbers)
print("Total sum (reduce):", total_sum)


# ==========================================
# 3. Custom Sorting with Lambda Key
# ==========================================
print("\n--- 3. Custom Sorting with Lambda ---")
inventory = [
    {"product": "Laptop", "price": 55000, "stock": 5},
    {"product": "Mouse", "price": 800, "stock": 45},
    {"product": "Keyboard", "price": 2500, "stock": 20},
    {"product": "Monitor", "price": 18000, "stock": 8}
]

# Sort products by price ascending
sorted_by_price = sorted(inventory, key=lambda item: item["price"])
print("Sorted by Price (low to high):")
for item in sorted_by_price:
    print(f"  {item['product']:<10} : ₹{item['price']}")

# Sort products by stock descending
sorted_by_stock = sorted(inventory, key=lambda item: item["stock"], reverse=True)
print("\nSorted by Stock (high to low):")
for item in sorted_by_stock:
    print(f"  {item['product']:<10} : {item['stock']} units")
