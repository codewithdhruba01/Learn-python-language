# Python Dictionary 

A **dictionary** in Python is a built-in data structure that stores data as **key-value pairs**. It allows fast retrieval and modification of data.
Dictionary is a collection which is ordered*, changeable and do not allow duplicates.
## Features of a Dictionary
- **Unordered**: The elements are not stored in a fixed order.
- **Mutable**: Dictionaries can be modified after creation.
- **Key-Value Pairs**: Data is stored in pairs where keys are unique.
- **Fast Lookup**: Values can be accessed quickly using keys.

---

## Creating a Dictionary
A dictionary can be created using curly braces `{}` or the `dict()` function.

```python
# Creating a dictionary
student = {
    "name": "John",
    "age": 22,
    "city": "Austin",
    "skills": ["Python", "JavaScript"]
}

print(student)
```

**Output:**
```python
{'name': 'John', 'age': 22, 'city': 'Austin', 'skills': ['Python', 'JavaScript']}
```

---

## Accessing Values in a Dictionary

```python
print(student["name"])   # Output: John
print(student.get("age"))  # Output: 22
```

Using `get()` is recommended as it prevents errors if a key does not exist.

```python
print(student.get("country", "USA"))  # Output: USA (default value)
```

---

## Updating and Adding Data
```python
student["age"] = 23  # Update an existing value
student["country"] = "USA"  # Add a new key-value pair
```

---

## Removing Items
```python
del student["city"]  # Remove a key-value pair

age = student.pop("age")  # Remove and return value

student.popitem()  # Remove the last inserted key-value pair
```

---

## Retrieving Keys, Values, and Items
```python
print(student.keys())   # Returns all keys
print(student.values()) # Returns all values
print(student.items())  # Returns all key-value pairs
```

---

## Looping Through a Dictionary
```python
for key, value in student.items():
    print(f"{key}: {value}")
```

**Output:**
```
name: John
skills: ['Python', 'JavaScript']
country: USA
```

---

## Dictionary Comprehension
```python
squares = {x: x*x for x in range(1, 6)}
print(squares)
```

**Output:**
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Common Questions

1. **What is a dictionary in Python?**
   - A dictionary is a data structure that stores data as key-value pairs.

2. **How do you create a dictionary?**
   - You can create a dictionary using `{}` or the `dict()` function.

3. **How do you access values in a dictionary?**
   - You can access values using `dict[key]` or `dict.get(key)`.

4. **How do you update a dictionary?**
   - You can update an existing key-value pair or add a new one using `dict[key] = value`.

5. **How do you remove an item from a dictionary?**
   - You can remove items using `del dict[key]`, `dict.pop(key)`, or `dict.popitem()`.

6. **What are the advantages of using a dictionary?**
   - Fast lookups, dynamic size, and flexibility in storing different data types.

---

