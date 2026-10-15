"""
Chapter 23: Metaclasses and Dynamic Class Creation - Metaclass Examples
Demonstrates custom metaclass lifecycle (__new__, __init__, __call__),
the Singleton pattern using metaclasses, and the modern __init_subclass__ hook.
"""

# ==========================================
# 1. Custom Validation Metaclass
# ==========================================
print("--- 1. Validation Metaclass ---")

class EnforcePrefixMeta(type):
    """
    Metaclass that ensures all custom methods defined on a class
    start with lowercase letters and forbids methods starting with 'test_'.
    """
    def __new__(mcs, name, bases, namespace):
        for attr_name, attr_val in namespace.items():
            if callable(attr_val) and not attr_name.startswith("__"):
                if attr_name.startswith("test_"):
                    raise ValueError(
                        f"Class '{name}' contains illegal method '{attr_name}'. "
                        f"'test_' prefix is reserved for test suites!"
                    )
        print(f"[Metaclass] Validated and created class: {name}")
        return super().__new__(mcs, name, bases, namespace)

class PaymentGateway(metaclass=EnforcePrefixMeta):
    def process_payment(self, amount):
        return f"Processed ${amount}"

    def refund_payment(self, transaction_id):
        return f"Refunded transaction {transaction_id}"

gateway = PaymentGateway()
print(gateway.process_payment(150))


# ==========================================
# 2. Singleton Metaclass Pattern
# ==========================================
print("\n--- 2. Singleton Metaclass Pattern ---")

class SingletonMeta(type):
    """Metaclass that restricts a class to only one instance."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"[SingletonMeta] Creating unique instance of {cls.__name__}")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print(f"[SingletonMeta] Returning cached instance of {cls.__name__}")
        return cls._instances[cls]

class DatabasePool(metaclass=SingletonMeta):
    def __init__(self, dsn: str):
        self.dsn = dsn

# Both calls return the exact same instance!
db1 = DatabasePool("postgresql://localhost:5432/mydb")
db2 = DatabasePool("postgresql://localhost:5432/mydb")

print("db1 is db2?", db1 is db2)
print("Memory address db1:", id(db1))
print("Memory address db2:", id(db2))


# ==========================================
# 3. Modern Alternative: __init_subclass__
# ==========================================
print("\n--- 3. Subclass Registration via __init_subclass__ ---")

class CommandHandler:
    """Base class that automatically registers commands when subclassed."""
    registry = {}

    def __init_subclass__(cls, command_name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        if command_name in cls.registry:
            raise KeyError(f"Command '{command_name}' is already registered!")
        cls.registry[command_name] = cls
        cls.command_name = command_name
        print(f"Registered command: '{command_name}' -> {cls.__name__}")

    def execute(self):
        raise NotImplementedError

class StartCommand(CommandHandler, command_name="start"):
    def execute(self):
        return "Starting the server..."

class StopCommand(CommandHandler, command_name="stop"):
    def execute(self):
        return "Shutting down the server..."

print("\nRegistered Commands in Registry:")
for cmd, handler in CommandHandler.registry.items():
    print(f"  Command: '{cmd}' => Handler: {handler.__name__}")

# Dispatching
active_command = CommandHandler.registry["start"]()
print("Execution result:", active_command.execute())
