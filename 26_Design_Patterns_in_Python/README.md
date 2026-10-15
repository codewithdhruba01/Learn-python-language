# Chapter 26: Design Patterns in Python

Design Patterns are time-tested, reusable architectural solutions to common software design challenges. Originally cataloged by the "Gang of Four" (GoF), design patterns in Python are often vastly cleaner, simpler, and more expressive than in languages like C++ or Java thanks to Python's first-class functions, duck typing, and dynamic nature.

---

## 📌 Table of Contents
1. [Categories of Design Patterns](#1-categories-of-design-patterns)
2. [Creational Patterns](#2-creational-patterns)
   - [Singleton Pattern](#singleton-pattern)
   - [Factory Method Pattern](#factory-method-pattern)
   - [Builder Pattern](#builder-pattern)
3. [Structural Patterns](#3-structural-patterns)
   - [Adapter Pattern](#adapter-pattern)
   - [Facade Pattern](#facade-pattern)
4. [Behavioral Patterns](#4-behavioral-patterns)
   - [Observer Pattern (Pub/Sub)](#observer-pattern-pubsub)
   - [Strategy Pattern](#strategy-pattern)
   - [Command Pattern](#command-pattern)
5. [Pythonic Idioms vs Classical GoF](#5-pythonic-idioms-vs-classical-gof)
6. [Practice Questions](#6-practice-questions)

---

## 1. Categories of Design Patterns

| Category | Purpose | Key Python Examples |
|----------|---------|---------------------|
| **Creational** | How objects are created | Singleton, Factory, Builder |
| **Structural** | How classes and objects compose into larger structures | Adapter, Facade, Composite |
| **Behavioral** | How objects communicate and distribute responsibilities | Observer, Strategy, State |

---

## 2. Creational Patterns

### Singleton Pattern
Ensures a class has **only one instance** and provides a global point of access to it (e.g. database connection pools, app settings, loggers).

```python
class AppConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, env="production"):
        if not self._initialized:
            self.env = env
            self._initialized = True
```

---

### Factory Method Pattern
Provides an interface for creating objects in a superclass, but lets subclasses or functions alter the type of objects that will be created.

```python
class EmailNotification:
    def send(self, message): return f"Email: {message}"

class SMSNotification:
    def send(self, message): return f"SMS: {message}"

def notification_factory(channel: str):
    channels = {
        "email": EmailNotification,
        "sms": SMSNotification
    }
    target = channels.get(channel.lower())
    if not target:
        raise ValueError(f"Unknown channel: {channel}")
    return target()
```

---

### Builder Pattern
Separates the construction of a complex object from its representation, allowing stepwise construction.

```python
class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self.fields = "*"
        self.where_clause = ""
        self.limit_val = None

    def select(self, *fields):
        self.fields = ", ".join(fields)
        return self  # Method chaining

    def where(self, condition):
        self.where_clause = f" WHERE {condition}"
        return self

    def limit(self, count):
        self.limit_val = f" LIMIT {count}"
        return self

    def build(self):
        query = f"SELECT {self.fields} FROM {self.table}{self.where_clause}"
        if self.limit_val:
            query += self.limit_val
        return query + ";"
```

---

## 3. Structural Patterns

### Adapter Pattern
Allows objects with incompatible interfaces to collaborate by converting the interface of a class into another interface clients expect.

```python
# Old legacy logger interface
class LegacyLogger:
    def log_message(self, text, severity):
        print(f"[{severity}] {text}")

# Target modern interface expected: log(level, msg)
class LoggerAdapter:
    def __init__(self, legacy_logger):
        self.legacy = legacy_logger

    def log(self, level, msg):
        self.legacy.log_message(msg, severity=level.upper())
```

---

### Facade Pattern
Provides a simplified, unified interface to a complex subsystem (e.g., hiding multi-step audio video transcoding, payment authorization + receipts + inventory updates).

```python
class VideoDownloader:
    def download(self, url): return "raw_video.mp4"

class AudioExtractor:
    def extract(self, video): return "audio.wav"

class SpeechToText:
    def transcribe(self, audio): return "Transcribed text"

# Facade
class MediaTranscriberFacade:
    def __init__(self):
        self.downloader = VideoDownloader()
        self.extractor = AudioExtractor()
        self.stt = SpeechToText()

    def process(self, url):
        vid = self.downloader.download(url)
        aud = self.extractor.extract(vid)
        return self.stt.transcribe(aud)
```

---

## 4. Behavioral Patterns

### Observer Pattern (Publish / Subscribe)
Defines a subscription mechanism where multiple objects (observers) listen for events dispatched by a subject.

```python
class EventEmitter:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, callback):
        self._subscribers.append(callback)

    def emit(self, event_data):
        for callback in self._subscribers:
            callback(event_data)
```

---

### Strategy Pattern
Enables selecting an algorithm's behavior at runtime. In Python, because functions are first-class objects, you can often use plain functions instead of full class hierarchies!

```python
def discount_vip(order_total):
    return order_total * 0.80  # 20% off

def discount_regular(order_total):
    return order_total * 0.95  # 5% off

def checkout(order_total, strategy=discount_regular):
    return strategy(order_total)
```

---

## 5. Pythonic Idioms vs Classical GoF

Many classical GoF design patterns exist solely to bypass rigid restrictions in C++ or Java (like lack of first-class functions or monkey-patching). 
- In Python:
  - **Strategy Pattern** is often implemented simply with functions or lambdas.
  - **Decorator Pattern** is built directly into Python syntax (`@my_decorator`).
  - **Iterator Pattern** is built-in (`__iter__` and `__next__`).
  - **Factory Pattern** can be a simple dictionary mapping string keys to classes or functions.

---

## 6. Practice Questions

1. Implement an event-driven `StockMarket` class using the **Observer Pattern** where multiple trading bots receive price update alerts.
2. Build an **Adapter** that adapts Python's standard `logging` library format to output formatted JSON lines for cloud aggregators.
3. Use the **Strategy Pattern** to support multiple sorting algorithms (e.g., QuickSort vs MergeSort) selectable via configuration.
4. Construct an email message with subject, recipients, attachments, and body using the **Builder Pattern** with fluent method chaining.
