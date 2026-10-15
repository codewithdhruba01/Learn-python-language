"""
Chapter 22: Type Hinting and Static Typing - Basics
Demonstrating fundamental type hints, collections, unions, optionals, and TypedDict.
"""

from typing import Union, Optional, Literal, TypedDict, Callable


# ==========================================
# 1. Basic Variable and Function Annotations
# ==========================================
print("--- 1. Basic Type Annotations ---")

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculates Body Mass Index."""
    return weight_kg / (height_m ** 2)

bmi = calculate_bmi(70.5, 1.75)
print(f"Calculated BMI: {bmi:.2f}")


# ==========================================
# 2. Collections and Modern Generic Types
# ==========================================
print("\n--- 2. Collections (list, dict, tuple) ---")

fruits: list[str] = ["Apple", "Banana", "Cherry"]
fruit_counts: dict[str, int] = {"Apple": 5, "Banana": 12, "Cherry": 30}
geo_coordinate: tuple[float, float] = (28.6139, 77.2090)  # New Delhi

print("Fruit Counts:", fruit_counts)
print("Coordinate:", geo_coordinate)


# ==========================================
# 3. Union and Optional (or Python 3.10 `|`)
# ==========================================
print("\n--- 3. Union and Optional Types ---")

def parse_id(raw_id: int | str) -> int:
    """Accepts either an integer or a string ID, returns an integer."""
    if isinstance(raw_id, str):
        return int(raw_id.strip())
    return raw_id

def search_user(username: str) -> str | None:
    """Returns email if user found, otherwise None."""
    mock_db = {"alice": "alice@example.com", "bob": "bob@example.com"}
    return mock_db.get(username.lower())

print("Parsed ID (from str):", parse_id("  1024 "))
print("Parsed ID (from int):", parse_id(2048))
print("Search Alice:", search_user("alice"))
print("Search Unknown:", search_user("charlie"))


# ==========================================
# 4. Literal Types (Restricting Values)
# ==========================================
print("\n--- 4. Literal Types ---")

Theme = Literal["light", "dark", "system"]

def apply_theme(theme: Theme) -> None:
    print(f"Applying theme: {theme.upper()}")

apply_theme("dark")
apply_theme("light")


# ==========================================
# 5. TypedDict (Structured Dictionary)
# ==========================================
print("\n--- 5. TypedDict ---")

class StudentProfile(TypedDict):
    name: str
    age: int
    courses: list[str]
    gpa: float

student1: StudentProfile = {
    "name": "Dhruba",
    "age": 21,
    "courses": ["Python", "DSA", "AsyncIO"],
    "gpa": 3.9
}

print(f"Student: {student1['name']}, Enrolled in: {student1['courses']}")


# ==========================================
# 6. Callable (Function as Parameters)
# ==========================================
print("\n--- 6. Callable Function Types ---")

def process_numbers(numbers: list[int], operation: Callable[[int], int]) -> list[int]:
    return [operation(n) for n in numbers]

def double(x: int) -> int:
    return x * 2

nums = [1, 2, 3, 4, 5]
doubled = process_numbers(nums, double)
print(f"Original: {nums} -> Doubled: {doubled}")
