"""
Chapter 15: Exception Handling - Basic Examples
Learn try, except, else, and finally blocks in Python.
"""

# ==========================================
# 1. Simple try-except block
# ==========================================
print("--- 1. Simple try-except block ---")
try:
    num = 10 / 0
except ZeroDivisionError as error:
    print(f"Caught ZeroDivisionError: {error}")


# ==========================================
# 2. Handling multiple specific exceptions
# ==========================================
print("\n--- 2. Handling Multiple Exceptions ---")
def safe_divide(a, b):
    try:
        val1 = float(a)
        val2 = float(b)
        result = val1 / val2
        return result
    except ValueError:
        return "Error: Both arguments must be valid numbers!"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

print("safe_divide(10, 2):", safe_divide(10, 2))
print("safe_divide(10, 0):", safe_divide(10, 0))
print("safe_divide(10, 'abc'):", safe_divide(10, 'abc'))


# ==========================================
# 3. try-except-else-finally pattern
# ==========================================
print("\n--- 3. Full try-except-else-finally pattern ---")
def parse_percentage(text):
    try:
        val = float(text.replace("%", ""))
    except ValueError as e:
        print(f"[EXCEPT] Could not parse value: {e}")
        return None
    else:
        print(f"[ELSE] Successfully parsed: {val}%")
        return val / 100
    finally:
        print("[FINALLY] Parsing attempt completed (cleanup done).")

print("Valid case:")
res1 = parse_percentage("85.5%")
print("Returned:", res1)

print("\nInvalid case:")
res2 = parse_percentage("eighty-five")
print("Returned:", res2)


# ==========================================
# 4. Raising exceptions manually
# ==========================================
print("\n--- 4. Raising Exceptions with 'raise' ---")
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0 or age > 120:
        raise ValueError(f"Age must be between 0 and 120, got {age}")
    return f"Valid age: {age}"

try:
    print(validate_age(25))
    print(validate_age(-5))
except (ValueError, TypeError) as err:
    print("Validation Error:", err)
