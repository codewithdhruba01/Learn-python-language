"""
Chapter 22: Type Hinting and Static Typing - Advanced
Demonstrating Generics (TypeVar, Generic), Protocols (Structural Subtyping),
and runtime type introspection.
"""

from typing import TypeVar, Generic, Protocol, Sequence, get_type_hints


# ==========================================
# 1. Generics with TypeVar
# ==========================================
print("--- 1. Generic Functions with TypeVar ---")

T = TypeVar("T")  # Represents any arbitrary type

def get_first_and_last(items: Sequence[T]) -> tuple[T, T]:
    """Returns a tuple containing the first and last elements while maintaining type."""
    if not items:
        raise ValueError("Sequence cannot be empty")
    return items[0], items[-1]

int_pair = get_first_and_last([10, 20, 30, 40])
str_pair = get_first_and_last(["apple", "banana", "cherry"])

print(f"Integer pair: {int_pair}")
print(f"String pair: {str_pair}")


# ==========================================
# 2. Generic Classes
# ==========================================
print("\n--- 2. Generic Classes (Stack Implementation) ---")

ItemType = TypeVar("ItemType")

class Stack(Generic[ItemType]):
    """A generic LIFO stack data structure."""
    def __init__(self) -> None:
        self._items: list[ItemType] = []

    def push(self, item: ItemType) -> None:
        self._items.append(item)

    def pop(self) -> ItemType:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __repr__(self) -> str:
        return f"Stack({self._items})"

# Stack holding strings
str_stack: Stack[str] = Stack()
str_stack.push("First")
str_stack.push("Second")
print("Stack contents:", str_stack)
print("Popped item:", str_stack.pop())


# ==========================================
# 3. Protocols (Structural Subtyping / Duck Typing)
# ==========================================
print("\n--- 3. Protocols (Duck Typing) ---")

class Notifiable(Protocol):
    """Any object with a notify(message: str) method satisfies this Protocol."""
    def notify(self, message: str) -> None:
        ...

class EmailNotifier:
    def notify(self, message: str) -> None:
        print(f"[Email] Sending: {message}")

class SMSNotifier:
    def notify(self, message: str) -> None:
        print(f"[SMS] Dispatching text: {message}")

class DiscordWebhook:
    def notify(self, message: str) -> None:
        print(f"[Discord] Posting payload: {message}")

def alert_team(notifier: Notifiable, alert_msg: str) -> None:
    # Any class that implements notify() can be passed here!
    notifier.notify(alert_msg)

alert_team(EmailNotifier(), "Database CPU usage > 90%")
alert_team(SMSNotifier(), "Deployment server restarted")
alert_team(DiscordWebhook(), "New release v1.2 published")


# ==========================================
# 4. Runtime Type Introspection
# ==========================================
print("\n--- 4. Runtime Type Introspection ---")

class ConfigService:
    host: str
    port: int
    debug_mode: bool

    def __init__(self, host: str, port: int, debug_mode: bool = False) -> None:
        self.host = host
        self.port = port
        self.debug_mode = debug_mode

hints = get_type_hints(ConfigService)
print("Class attributes and their hinted types:")
for attr, typ in hints.items():
    print(f"  - {attr}: {typ}")
