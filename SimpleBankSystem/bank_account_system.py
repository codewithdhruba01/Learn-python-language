class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.__balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print("Interest applied")

    def display_balance(self):
        super().display_balance()
        print(f"Interest Rate: {self.interest_rate * 100}%")

if __name__ == "__main__":
    acc = SavingsAccount("John Doe", 1000, 0.05)
    acc.deposit(500)
    acc.withdraw(200)
    acc.apply_interest()
    acc.display_balance()
