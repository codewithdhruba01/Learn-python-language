"""
Chapter 27: Regular Expressions - Advanced
Demonstrating Named Capture Groups, Lookahead / Lookbehind assertions,
re.VERBOSE flag for readable patterns, and practical validation.
"""

import re


# ==========================================
# 1. Named Capture Groups (?P<name>...)
# ==========================================
print("--- 1. Named Capture Groups ---")

log_entry = "2026-10-15 22:45:10 [ERROR] Connection timed out after 3000ms"

log_regex = re.compile(
    r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) "
    r"\[(?P<severity>DEBUG|INFO|WARNING|ERROR|CRITICAL)\] "
    r"(?P<message>.*)$"
)

match = log_regex.match(log_entry)
if match:
    data = match.groupdict()
    print("Parsed Log Entry as Dictionary:")
    for k, v in data.items():
        print(f"  {k}: {v}")


# ==========================================
# 2. Lookahead Assertions (?=...) and (?!...)
# ==========================================
print("\n--- 2. Lookahead Assertions (Password Validation) ---")

# Enforces:
# - At least 8 characters (?=.{8,})
# - At least 1 lowercase letter (?=.*[a-z])
# - At least 1 uppercase letter (?=.*[A-Z])
# - At least 1 digit (?=.*\d)
# - At least 1 special symbol (?=.*[!@#$%^&*])
password_regex = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
)

passwords = [
    "weak",
    "password123",
    "Admin1234",
    "P@ssw0rd2026!"
]

for pwd in passwords:
    valid = bool(password_regex.match(pwd))
    print(f"Password '{pwd}': {'STRONG' if valid else 'WEAK'}")


# ==========================================
# 3. Lookbehind Assertions (?<=...) and (?<!...)
# ==========================================
print("\n--- 3. Lookbehind Assertions ---")

text = "Item A costs $120. Item B costs €80. Item C is discounted by 15%."

# Positive Lookbehind: Extract only dollar amounts without capturing the '$' symbol
usd_amounts = re.findall(r"(?<=\$)\d+", text)
print("USD amounts found:", usd_amounts)

# Negative Lookbehind: Extract numbers NOT preceded by currency symbols ($ or €)
plain_numbers = re.findall(r"(?<![\$€])\b\d+\b", text)
print("Non-currency standalone numbers:", plain_numbers)


# ==========================================
# 4. re.VERBOSE (Writing Clean, Documented Regex)
# ==========================================
print("\n--- 4. re.VERBOSE Pattern with Comments ---")

url_pattern = re.compile(r"""
    ^
    (?P<protocol>https?)://           # Protocol: http or https
    (?P<domain>[a-zA-Z0-9.-]+)        # Domain name
    (?::(?P<port>\d+))?               # Optional port (:8080)
    (?P<path>/[a-zA-Z0-9._/-]*)?      # Optional resource path
    $
""", re.VERBOSE)

test_url = "https://learnpython.org:8000/chapters/advanced"
m = url_pattern.match(test_url)
if m:
    print("Parsed URL:", m.groupdict())
