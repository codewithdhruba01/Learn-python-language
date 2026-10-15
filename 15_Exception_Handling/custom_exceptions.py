"""
Chapter 15: Custom Exceptions in Python
Demonstrates how to inherit from Exception and build domain-specific error handling.
"""

class BankError(Exception):
    """Base class for all banking exceptions."""
    pass


class InsufficientFundsError(BankError):
    """Raised when an account does not have enough balance for a withdrawal."""
    def __init__(self, current_balance, withdraw_amount):
        message = (
            f"Withdrawal of ₹{withdraw_amount} rejected. "
            f"Available balance is only ₹{current_balance}."
        )
        super().__init__(message)
        self.current_balance = current_balance
        self.withdraw_amount = withdraw_amount


class NegativeAmountError(BankError):
    """Raised when an operation is performed with a non-positive amount."""
    def __init__(self, amount):
        super().__init__(f"Transaction amount must be positive. Received: ₹{amount}")
        self.amount = amount


class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise NegativeAmountError(amount)
        self.balance += amount
        print(f"[DEPOSIT] ₹{amount} added. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError(amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"[WITHDRAW] ₹{amount} deducted. New Balance: ₹{self.balance}")


# ==========================================
# Testing Custom Exceptions
# ==========================================
if __name__ == "__main__":
    acc = BankAccount("Dhruba", 1000.0)

    # Valid transaction
    acc.deposit(500.0)

    # Test Case 1: Negative amount exception
    print("\nAttempting invalid deposit (-200):")
    try:
        acc.deposit(-200)
    except NegativeAmountError as error:
        print(f"Error Caught -> {error}")

    # Test Case 2: Insufficient funds exception
    print("\nAttempting overdraft withdrawal (₹2500):")
    try:
        acc.withdraw(2500)
    except InsufficientFundsError as error:
        print(f"Error Caught -> {error}")
        print(f"Shortage Amount: ₹{error.withdraw_amount - error.current_balance}")

    # Valid withdrawal
    print("\nAttempting valid withdrawal (₹800):")
    acc.withdraw(800)
