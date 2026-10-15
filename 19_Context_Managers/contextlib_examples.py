"""
Chapter 19: Context Managers using contextlib
Demonstrates @contextmanager generator decorator and standard context utilities.
"""
import os
import sys
from contextlib import contextmanager, suppress, redirect_stdout
from io import StringIO

# ==========================================
# 1. Generator-based Context Manager with @contextmanager
# ==========================================
@contextmanager
def temporary_flag(obj, attribute, temporary_value):
    """Temporarily changes an attribute on an object and restores it afterwards."""
    original_value = getattr(obj, attribute)
    setattr(obj, attribute, temporary_value)
    try:
        yield obj
    finally:
        setattr(obj, attribute, original_value)


class ApplicationConfig:
    debug_mode = False

config = ApplicationConfig()
print("--- 1. Testing @contextmanager Decorator ---")
print("Initial debug mode:", config.debug_mode)

with temporary_flag(config, "debug_mode", True):
    print("Inside context block -> debug mode:", config.debug_mode)

print("Outside context block -> debug mode restored:", config.debug_mode)


# ==========================================
# 2. Using contextlib.suppress
# ==========================================
print("\n--- 2. contextlib.suppress ---")
# Gracefully suppress specific exceptions without verbose try/except
with suppress(FileNotFoundError):
    os.remove("temporary_non_existing_file_xyz.tmp")

print("File removal attempt completed safely without throwing FileNotFoundError.")


# ==========================================
# 3. Using contextlib.redirect_stdout
# ==========================================
print("\n--- 3. contextlib.redirect_stdout ---")
buffer = StringIO()

with redirect_stdout(buffer):
    print("This line is captured inside the in-memory string buffer!")
    print("Another hidden output line.")

captured_text = buffer.getvalue()
print("Captured Output Successfully:")
print(f"'''\n{captured_text.strip()}\n'''")
