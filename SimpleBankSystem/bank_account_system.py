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
    print("=== Welcome to the Savings Account System ===")
    name = input("Enter account holder name: ")

    try:
        balance = float(input("Enter initial balance: "))
        interest_rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
    except ValueError:
        print("Invalid input. Exiting.")
        exit()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        exit()

    acc = SavingsAccount(name, balance, interest_rate)

    while True:
        print("\nSelect an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Apply Interest")
        print("4. Display Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                acc.deposit(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                acc.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == '3':
            acc.apply_interest()
        elif choice == '4':
            acc.display_balance()
        elif choice == '5':
            print("Thank you! Exiting.")
            break
        else:
            print("Invalid choice. Please select again.")
