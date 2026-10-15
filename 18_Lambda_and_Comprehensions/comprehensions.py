"""
Chapter 18: Comprehensions in Python
Demonstrates List, Dictionary, and Set comprehensions with conditions and nesting.
"""

# ==========================================
# 1. List Comprehensions (Basic & Filtered)
# ==========================================
print("--- 1. List Comprehensions ---")
# Squares of even numbers between 1 and 10
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# Conditional value assignment (if-else)
scores = [78, 45, 92, 33, 85, 59]
status = ["Pass" if s >= 50 else "Fail" for s in scores]
print("Exam results:", list(zip(scores, status)))


# ==========================================
# 2. Nested Comprehensions (Matrix flattening & Transpose)
# ==========================================
print("\n--- 2. Matrix Flattening & Transposition ---")
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flattening: row first, then element
flattened = [val for row in grid for val in row]
print("Flattened 1D array:", flattened)

# Transposing a 3x3 matrix
transposed = [[row[col_idx] for row in grid] for col_idx in range(3)]
print("Transposed matrix  :")
for row in transposed:
    print(" ", row)


# ==========================================
# 3. Dictionary Comprehensions
# ==========================================
print("\n--- 3. Dictionary Comprehensions ---")
cities = ["Delhi", "Mumbai", "Kolkata", "Bengaluru"]
# Create mapping of city name -> length
city_lengths = {city: len(city) for city in cities}
print("City lengths:", city_lengths)

# Filtering a dictionary: Keep products costing >= 1000
raw_prices = {"Keyboard": 1500, "Mouse": 600, "Headphones": 2200, "USB Cable": 250}
premium_products = {k: v for k, v in raw_prices.items() if v >= 1000}
print("Premium products:", premium_products)


# ==========================================
# 4. Set Comprehensions
# ==========================================
print("\n--- 4. Set Comprehensions ---")
sentence = "the quick brown fox jumps over the lazy dog"
# Unique vowels present in the sentence
unique_vowels = {char for char in sentence if char in "aeiou"}
print("Unique vowels found:", sorted(unique_vowels))
