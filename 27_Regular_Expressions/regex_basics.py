"""
Chapter 27: Regular Expressions - Basics
Demonstrating fundamental functions in Python's re module:
re.search, re.match, re.findall, re.finditer, re.sub, and re.split.
"""

import re


# ==========================================
# 1. search vs match vs fullmatch
# ==========================================
print("--- 1. search vs match vs fullmatch ---")

sample_text = "Contact us at support@example.com or sales@company.org"

# re.match only looks at index 0
match_obj = re.match(r"Contact", sample_text)
print("re.match('Contact'):", match_obj.group() if match_obj else "No match")

match_fail = re.match(r"support", sample_text)
print("re.match('support'):", match_fail)  # None!

# re.search scans the whole string for the first hit
search_obj = re.search(r"[\w\.-]+@[\w\.-]+", sample_text)
if search_obj:
    print(f"re.search found first email: {search_obj.group()} at span {search_obj.span()}")


# ==========================================
# 2. findall and finditer
# ==========================================
print("\n--- 2. findall and finditer ---")

emails = re.findall(r"[\w\.-]+@[\w\.-]+", sample_text)
print("re.findall email list:", emails)

log_entries = "Error: Code 404 at line 12. Warning: Code 500 at line 88."
print("\nIterating matches with re.finditer:")
for match in re.finditer(r"Code (\d+) at line (\d+)", log_entries):
    code, line = match.groups()
    print(f"  -> Found Code: {code}, Line: {line} (Position: {match.start()}-{match.end()})")


# ==========================================
# 3. re.sub (Text Replacement and Masking)
# ==========================================
print("\n--- 3. re.sub (Replacement & Masking) ---")

raw_phone_text = "Call Alice at 555-123-4567 or Bob at 555-987-6543."

# Mask all phone digits except last 4
def mask_phone(match):
    full_number = match.group(0)
    return "XXX-XXX-" + full_number[-4:]

masked_text = re.sub(r"\d{3}-\d{3}-\d{4}", mask_phone, raw_phone_text)
print("Original:", raw_phone_text)
print("Masked:  ", masked_text)


# ==========================================
# 4. re.split (Splitting with Multiple Delimiters)
# ==========================================
print("\n--- 4. re.split with Multiple Delimiters ---")

messy_input = "Python,Java;C++   Go\tRust\nJavaScript"
# Split by any sequence of commas, semicolons, or whitespace
tokens = re.split(r"[,;\s]+", messy_input.strip())
print("Clean tokens:", tokens)


# ==========================================
# 5. Compiled Regex Object (re.compile)
# ==========================================
print("\n--- 5. re.compile for Reusability ---")

hex_color_pattern = re.compile(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$")

test_colors = ["#FFF", "#123456", "#G12345", "123456", "#a1B2c3"]
for color in test_colors:
    valid = bool(hex_color_pattern.fullmatch(color))
    print(f"Color {color:<10}: {'VALID' if valid else 'INVALID'}")
