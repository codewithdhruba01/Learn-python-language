# Chapter 27: Regular Expressions (`re` Module) in Python

A **Regular Expression (Regex)** is a powerful domain-specific language for pattern matching and text manipulation. Whether you are validating user forms, parsing server logs, cleaning datasets for data science, or scraping the web, mastering Python's built-in `re` module is essential.

---

## 📌 Table of Contents
1. [Raw Strings in Python (`r"..."`)](#1-raw-strings-in-python-r)
2. [Core Functions of the `re` Module](#2-core-functions-of-the-re-module)
3. [Meta-characters and Quantifiers](#3-meta-characters-and-quantifiers)
4. [Character Classes and Special Sequences](#4-character-classes-and-special-sequences)
5. [Greedy vs Non-Greedy (Lazy) Matching](#5-greedy-vs-non-greedy-lazy-matching)
6. [Capturing Groups and Named Groups](#6-capturing-groups-and-named-groups)
7. [Lookahead and Lookbehind Assertions](#7-lookahead-and-lookbehind-assertions)
8. [Regex Compilation with `re.compile()`](#8-regex-compilation-with-recompile)
9. [Regex Flags](#9-regex-flags)
10. [Practice Questions](#10-practice-questions)

---

## 1. Raw Strings in Python (`r"..."`)

Always prefix regular expression patterns with an `r` to create a **raw string**.
This prevents Python from interpreting backslashes `\` as escape sequences (like `\n` or `\t`):

```python
import re

# Without 'r', Python treats \b as ASCII backspace!
# With 'r', Python leaves \b intact for regex word boundary:
pattern = r"\bword\b"
```

---

## 2. Core Functions of the `re` Module

| Function | Purpose | Return Value |
|----------|---------|--------------|
| `re.search(pattern, text)` | Scans through string looking for the first match anywhere | `Match` object or `None` |
| `re.match(pattern, text)` | Matches pattern **only from the start** of the string | `Match` object or `None` |
| `re.fullmatch(pattern, text)` | Matches if the **entire string** conforms to pattern | `Match` object or `None` |
| `re.findall(pattern, text)` | Finds all non-overlapping matches | List of strings or tuples |
| `re.finditer(pattern, text)` | Finds all matches and yields them lazily | Iterator yielding `Match` objects |
| `re.sub(pattern, repl, text)` | Replaces occurrences with replacement string or function | New string |
| `re.split(pattern, text)` | Splits string by occurrences of pattern | List of strings |

---

## 3. Meta-characters and Quantifiers

### Meta-characters
- `.` : Any character except newline (`\n`).
- `^` : Start of string (or start of line in multiline mode).
- `$` : End of string.
- `|` : OR operator (e.g. `cat|dog`).
- `[]`: Character set (e.g. `[a-z0-9]`).
- `()`: Capturing group.

### Quantifiers
- `*` : 0 or more occurrences.
- `+` : 1 or more occurrences.
- `?` : 0 or 1 occurrence (optional).
- `{n}` : Exactly `n` occurrences.
- `{n,}`: At least `n` occurrences.
- `{n,m}`: Between `n` and `m` occurrences.

---

## 4. Character Classes and Special Sequences

- `\d` : Any digit (`[0-9]`).
- `\D` : Any non-digit.
- `\w` : Any word character (alphanumeric + underscore `[a-zA-Z0-9_]`).
- `\W` : Any non-word character.
- `\s` : Any whitespace (space, tab, newline `[ \t\n\r\f\v]`).
- `\S` : Any non-whitespace character.
- `\b` : Word boundary.
- `\B` : Non-word boundary.

---

## 5. Greedy vs Non-Greedy (Lazy) Matching

By default, quantifiers (`*`, `+`, `{}`) are **greedy**: they match as much text as possible.
Adding a `?` makes them **lazy**: they match as little as possible.

```python
html = "<div>First</div><div>Second</div>"

# Greedy (matches from first <div> to last </div>):
re.findall(r"<div>.*</div>", html)
# Result: ['<div>First</div><div>Second</div>']

# Non-greedy / Lazy (matches each tag separately):
re.findall(r"<div>.*?</div>", html)
# Result: ['<div>First</div>', '<div>Second</div>']
```

---

## 6. Capturing Groups and Named Groups

Named capturing groups `(?P<name>...)` make regex results self-documenting:

```python
log_line = "2026-10-15 14:32:01 [ERROR] Database timeout occurred"

pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<msg>.*)"

match = re.search(pattern, log_line)
if match:
    print(match.group("date"))   # 2026-10-15
    print(match.group("level"))  # ERROR
    print(match.groupdict())     # {'date': '2026-10-15', 'time': '14:32:01', 'level': 'ERROR', 'msg': '...'}
```

---

## 7. Lookahead and Lookbehind Assertions

Zero-width assertions match a position without consuming characters in the match:

- **Positive Lookahead `(?=...)`**: Asserts that what follows matches pattern.
- **Negative Lookahead `(?!...)`**: Asserts that what follows does NOT match pattern.
- **Positive Lookbehind `(?<=...)`**: Asserts that what precedes matches pattern.
- **Negative Lookbehind `(?<!...)`**: Asserts that what precedes does NOT match pattern.

```python
# Match price numbers only when preceded by '$'
text = "The book costs $45 and the pen is 15 rupees."
prices = re.findall(r"(?<=\$)\d+", text)  # ['45']
```

---

## 8. Regex Compilation with `re.compile()`

When using the same pattern repeatedly in a loop or across requests, compile it once.
Compilation turns the pattern into a C-level bytecode object, saving parsing overhead:

```python
email_regex = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$", re.IGNORECASE)

if email_regex.match("user@example.com"):
    print("Valid Email")
```

---

## 9. Regex Flags

Pass flags to `re.compile()` or functions:
- `re.IGNORECASE` (`re.I`): Case-insensitive matching.
- `re.MULTILINE` (`re.M`): `^` and `$` match start/end of each line.
- `re.DOTALL` (`re.S`): Makes `.` match newlines too.
- `re.VERBOSE` (`re.X`): Allows whitespace and comments inside the regex string for clarity.

---

## 10. Practice Questions

1. Write a regex to validate strong passwords: at least 8 characters, at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special symbol using lookaheads.
2. Extract all URLs (http/https) from a block of text using `re.findall`.
3. Use `re.sub` with a replacement callback function to convert `snake_case` words in a string to `camelCase`.
4. Parse an Apache/Nginx web server access log line into an IP, timestamp, HTTP method, and status code using named groups.
