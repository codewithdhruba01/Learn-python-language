# Chapter 22: Type Hinting and Static Typing in Python

Type hinting was introduced in Python 3.5 (PEP 484) and has revolutionized modern Python development. While Python remains a **dynamically typed** language at runtime, type hints allow static analyzers (like **Mypy**, **Pyright**, and IDE linters) to catch bugs before execution, enable superior auto-completion, and serve as live documentation.

---

## 📌 Table of Contents
1. [Why Use Type Hinting?](#1-why-use-type-hinting)
2. [Basic Type Annotations](#2-basic-type-annotations)
3. [Modern Typing Syntax (Python 3.10+)](#3-modern-typing-syntax-python-310)
4. [Collections and Containers](#4-collections-and-containers)
5. [Optional and Union Types](#5-optional-and-union-types)
6. [Callable (Function Signatures)](#6-callable-function-signatures)
7. [TypedDict and Literal](#7-typeddict-and-literal)
8. [Generics with TypeVar](#8-generics-with-typevar)
9. [Protocols (Structural Subtyping / Duck Typing)](#9-protocols-structural-subtyping--duck-typing)
10. [Type Narrowing and Runtime Inspection](#10-type-narrowing-and-runtime-inspection)
11. [Practice Questions](#11-practice-questions)

---

## 1. Why Use Type Hinting?

Python does not enforce types at runtime. For example, `def add(a, b): return a + b` works for both integers and strings. 

However, in large projects, type hinting provides:
- **Early Bug Detection**: Catches `NoneType` errors, mismatched arguments, and typo errors before code runs.
- **Superior IDE Autocompletion**: Your IDE knows the exact methods available on an object.
- **Self-Documenting Code**: No need for lengthy docstrings explaining what each argument accepts and returns.
- **Powers Modern Frameworks**: Frameworks like **FastAPI**, **Pydantic**, and **SQLModel** use type annotations for validation and data serialization.

---

## 2. Basic Type Annotations

Variables and function arguments can be annotated using the `:` syntax, and return types using `->`:

```python
# Variable annotations
age: int = 25
name: str = "Alice"
is_active: bool = True
temperature: float = 36.6

# Function signature annotation
def calculate_area(width: float, height: float) -> float:
    return width * height
```

---

## 3. Modern Typing Syntax (Python 3.10+)

Starting with Python 3.10+, you no longer need to import `Union` or `Optional` from the `typing` module for basic operations:

| Old Syntax (`typing` module) | Modern Syntax (Python 3.10+) | Meaning |
|-----------------------------|------------------------------|---------|
| `Union[int, str]` | `int | str` | Either int OR str |
| `Optional[str]` | `str | None` | Either str OR None |
| `typing.List[int]` | `list[int]` | Built-in collection generics |
| `typing.Dict[str, int]` | `dict[str, int]` | Dictionary with string keys and int values |

---

## 4. Collections and Containers

Annotate complex data structures with the types of their items:

```python
# Lists and Sets
names: list[str] = ["Alice", "Bob", "Charlie"]
unique_ids: set[int] = {101, 102, 103}

# Dictionaries
user_scores: dict[str, int] = {"Alice": 95, "Bob": 88}

# Tuples
# Fixed length and types:
coordinates: tuple[float, float] = (12.9716, 77.5946)
# Arbitrary length of identical types:
scores: tuple[int, ...] = (10, 20, 30, 40)
```

---

## 5. Optional and Union Types

When a function can accept or return multiple types, or can return `None`:

```python
from typing import Optional, Union

# Python 3.10+ style:
def find_user_by_id(user_id: int) -> str | None:
    database = {1: "Alice", 2: "Bob"}
    return database.get(user_id)

def parse_input(data: int | str) -> int:
    return int(data)
```

---

## 6. Callable (Function Signatures)

Use `Callable[[Arg1Type, Arg2Type], ReturnType]` when passing functions as arguments (e.g. callbacks or higher-order functions):

```python
from typing import Callable

def apply_transformation(numbers: list[int], func: Callable[[int], int]) -> list[int]:
    return [func(n) for n in numbers]

def square(x: int) -> int:
    return x * x

result = apply_transformation([1, 2, 3], square)  # [1, 4, 9]
```

---

## 7. TypedDict and Literal

### `Literal`
Restricts values to specific constant literals:

```python
from typing import Literal

def set_status(mode: Literal["light", "dark", "system"]) -> None:
    print(f"Theme set to: {mode}")

set_status("dark")   # OK
# set_status("blue") # Type Checker Error!
```

### `TypedDict`
Specifies exact key-value schemas for standard dictionaries:

```python
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float

movie: Movie = {
    "title": "Inception",
    "year": 2010,
    "rating": 8.8
}
```

---

## 8. Generics with TypeVar

Generics allow functions or classes to work with any type while maintaining type relationships between arguments and return values:

```python
from typing import TypeVar, Sequence

T = TypeVar("T")  # Can represent any type

def first_element(items: Sequence[T]) -> T:
    """Returns the first element of sequence while preserving its exact type."""
    if not items:
        raise IndexError("Empty sequence")
    return items[0]

# Type checker knows x is an int, y is a str!
x = first_element([10, 20, 30])
y = first_element(["a", "b", "c"])
```

---

## 9. Protocols (Structural Subtyping / Duck Typing)

Python is famous for duck typing: *"If it walks like a duck and quacks like a duck, it's a duck."*
`typing.Protocol` lets you statically type-check interfaces without requiring explicit inheritance.

```python
from typing import Protocol

class Renderable(Protocol):
    def render(self) -> str:
        ...

class Button:
    def render(self) -> str:
        return "<button>Click Me</button>"

class Image:
    def render(self) -> str:
        return "<img src='logo.png' />"

def display(component: Renderable) -> None:
    print(component.render())

# Both work without inheriting from Renderable!
display(Button())
display(Image())
```

---

## 10. Type Narrowing and Runtime Inspection

### Type Narrowing with `isinstance`
Static analyzers understand control flow:

```python
def process_data(value: str | int) -> int:
    if isinstance(value, str):
        # Here, analyzer knows value is strictly `str`
        return len(value)
    else:
        # Here, analyzer knows value is strictly `int`
        return value * 2
```

### Inspecting Annotations at Runtime
```python
from typing import get_type_hints

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}"

print(get_type_hints(greet))
# Output: {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
```

---

## 11. Practice Questions

1. Create a function `find_max` that takes a generic sequence of numbers (`int` or `float`) and returns the maximum value.
2. Define a `TypedDict` for a `UserAccount` containing `username`, `email`, and an optional `bio`.
3. Define a `Protocol` called `Serializable` with a method `serialize() -> dict[str, str]`, and implement two unrelated classes that satisfy this interface.
4. Write a function `safe_divide` that takes `numerator: float` and `denominator: float` and returns `float | None` (returning `None` if denominator is 0).
