"""
Chapter 19: Custom Context Managers in Python
Demonstrates class-based context managers (__enter__ and __exit__) and error handling.
"""
import time

# ==========================================
# 1. Class-based Code Execution Timer
# ==========================================
class CodeTimer:
    def __init__(self, label="Operation"):
        self.label = label
        self.start_time = None
        self.duration = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        print(f"[{self.label}] Started...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.duration = time.perf_counter() - self.start_time
        print(f"[{self.label}] Finished in {self.duration:.6f} seconds.")
        # Returning None/False ensures exceptions (if any) are not swallowed
        return False


print("--- 1. Testing CodeTimer Context Manager ---")
with CodeTimer("Summation of 1M Numbers") as timer:
    total = sum(i for i in range(1_000_000))
    print("Computed total:", total)


# ==========================================
# 2. Database Transaction Simulator with Rollback
# ==========================================
class DatabaseTransaction:
    """Simulates a transactional context that commits or rolls back."""
    def __init__(self, db_name="ProductionDB"):
        self.db_name = db_name

    def __enter__(self):
        print(f"\n[DB: {self.db_name}] Transaction started. BEGIN WORK;")
        return self

    def execute_query(self, query):
        print(f"[DB: {self.db_name}] Executing: {query}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"[DB: {self.db_name}] ❌ Exception encountered: {exc_val}")
            print(f"[DB: {self.db_name}] Rolling back changes... ROLLBACK WORK;")
            return False  # Propagate exception up
        else:
            print(f"[DB: {self.db_name}] ✅ No errors. Committing changes... COMMIT WORK;")
            return True


print("\n--- 2. Successful Database Transaction ---")
with DatabaseTransaction() as db:
    db.execute_query("UPDATE users SET balance = balance - 100 WHERE id = 1;")
    db.execute_query("UPDATE users SET balance = balance + 100 WHERE id = 2;")

print("\n--- 3. Failed Database Transaction (Rollback) ---")
try:
    with DatabaseTransaction() as db:
        db.execute_query("UPDATE accounts SET status = 'ACTIVE' WHERE id = 5;")
        raise RuntimeError("Network disconnect during transaction!")
except RuntimeError as err:
    print(f"Application caught outer error: {err}")
