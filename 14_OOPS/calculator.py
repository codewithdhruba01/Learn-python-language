# Class with Method Task: Create a class Calculator with methods add, subtract, multiply, and divide. Create an object and call each method with example numbers.

class Calculator:
    # Method for addition
    def add(self, a, b):
        return a + b

    # Method for subtraction
    def subtract(self, a, b):
        return a - b

    # Method for multiplication
    def multiply(self, a, b):
        return a * b

    # Method for division
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b


# Create an object of Calculator class
calc = Calculator()

# Example calls
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))
