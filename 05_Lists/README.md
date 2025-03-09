# Python Lists

A **list** in Python is a built-in data structure that allows you to store multiple items in a single variable. Lists are **ordered, mutable (modifiable), and allow duplicate values**.

## Creating a List
Lists are created using square brackets `[]` and can contain different data types.

```python
# Creating lists
empty_list = []  # Empty list
numbers = [1, 2, 3, 4, 5]  # List of integers
fruits = ["apple", "banana", "cherry"]  # List of strings
mixed_list = [10, "hello", 3.14, True]  # Mixed data types
nested_list = [[1, 2], [3, 4], [5, 6]]  # List of lists
```

## Accessing Elements
You can access list elements using **indexing** and **slicing**.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: cherry
```

### Slicing
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])   # Output: [2, 3, 4, 5]
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## Modifying Lists
### Adding Elements
```python
fruits.append("grape")  # Add to end
fruits.insert(1, "mango")  # Insert at index 1
fruits.extend(["pineapple", "pear"])  # Add multiple
```

### Removing Elements
```python
fruits.remove("banana")  # Remove by value
fruits.pop(2)  # Remove by index
del fruits[1]  # Delete element
fruits.clear()  # Remove all elements
```

## Looping Through a List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## List Methods
| Method | Description |
|--------|------------|
| `append(x)` | Adds `x` to the end |
| `insert(i, x)` | Inserts `x` at index `i` |
| `remove(x)` | Removes the first occurrence of `x` |
| `pop(i)` | Removes and returns element at index `i` |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the list |

## Sorting and Reversing
```python
numbers = [5, 2, 9, 1, 7]
numbers.sort()  # Ascending order
numbers.sort(reverse=True)  # Descending order
numbers.reverse()  # Reverse order
```

## List Comprehension
```python
squares = [x**2 for x in range(1, 6)]  # Output: [1, 4, 9, 16, 25]
even_numbers = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

## Copying a List
```python
import copy
list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)
list1[0][0] = 99
print(list2)  # Output: [[1, 2], [3, 4]]
```
