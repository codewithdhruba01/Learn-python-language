"""
Chapter 26: Design Patterns in Python - Behavioral Patterns
Demonstrating Observer (Publish/Subscribe), Strategy, and Command patterns.
"""

from typing import Callable


# ==========================================
# 1. Observer Pattern (Publish / Subscribe)
# ==========================================
print("--- 1. Observer Pattern (Publish / Subscribe) ---")

class NewsletterPublisher:
    def __init__(self):
        self._subscribers: list[Callable[[str], None]] = []

    def subscribe(self, listener: Callable[[str], None]):
        self._subscribers.append(listener)
        print(f"[Subscription] Added new listener: {getattr(listener, '__name__', str(listener))}")

    def unsubscribe(self, listener: Callable[[str], None]):
        self._subscribers.remove(listener)

    def publish_article(self, title: str):
        print(f"\n[Publisher] Publishing new article: '{title}'")
        for listener in self._subscribers:
            listener(title)

# Listeners
def email_subscriber(article_title: str):
    print(f"  -> Email sent to user: Read our new piece '{article_title}'")

def push_notification_subscriber(article_title: str):
    print(f"  -> Push Notification: Breaking news: '{article_title}'")

publisher = NewsletterPublisher()
publisher.subscribe(email_subscriber)
publisher.subscribe(push_notification_subscriber)

publisher.publish_article("Python 3.12 Features You Must Know")


# ==========================================
# 2. Strategy Pattern (Functional Python Style)
# ==========================================
print("\n--- 2. Strategy Pattern ---")

def standard_shipping(weight_kg: float) -> float:
    return weight_kg * 5.0

def express_shipping(weight_kg: float) -> float:
    return (weight_kg * 10.0) + 15.0

def overnight_air_shipping(weight_kg: float) -> float:
    return (weight_kg * 20.0) + 50.0

class Order:
    def __init__(self, weight_kg: float, shipping_strategy: Callable[[float], float]):
        self.weight_kg = weight_kg
        self.shipping_strategy = shipping_strategy

    def calculate_shipping(self) -> float:
        return self.shipping_strategy(self.weight_kg)

order1 = Order(weight_kg=2.5, shipping_strategy=standard_shipping)
print(f"Standard Shipping: ${order1.calculate_shipping():.2f}")

order2 = Order(weight_kg=2.5, shipping_strategy=express_shipping)
print(f"Express Shipping: ${order2.calculate_shipping():.2f}")

order3 = Order(weight_kg=2.5, shipping_strategy=overnight_air_shipping)
print(f"Overnight Air Shipping: ${order3.calculate_shipping():.2f}")


# ==========================================
# 3. Command Pattern (Undo / Redo Action Queue)
# ==========================================
print("\n--- 3. Command Pattern (Text Editor Undo Buffer) ---")

class TextEditor:
    def __init__(self):
        self.content = ""

    def append(self, text: str):
        self.content += text

    def delete_last(self, length: int):
        self.content = self.content[:-length]

class AppendTextCommand:
    def __init__(self, editor: TextEditor, text_to_append: str):
        self.editor = editor
        self.text_to_append = text_to_append

    def execute(self):
        self.editor.append(self.text_to_append)

    def undo(self):
        self.editor.delete_last(len(self.text_to_append))

editor = TextEditor()
history: list[AppendTextCommand] = []

# Action 1
cmd1 = AppendTextCommand(editor, "Hello ")
cmd1.execute()
history.append(cmd1)

# Action 2
cmd2 = AppendTextCommand(editor, "World!")
cmd2.execute()
history.append(cmd2)

print("Editor text after actions:", repr(editor.content))

# Undo Action 2
last_cmd = history.pop()
last_cmd.undo()
print("Editor text after 1 undo:", repr(editor.content))

# Undo Action 1
first_cmd = history.pop()
first_cmd.undo()
print("Editor text after 2nd undo:", repr(editor.content))
