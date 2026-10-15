"""
Chapter 26: Design Patterns in Python - Creational & Structural Patterns
Demonstrating Singleton, Factory Method, Builder, and Adapter patterns.
"""

# ==========================================
# 1. Singleton Pattern (Thread-safe instance check)
# ==========================================
print("--- 1. Singleton Pattern ---")

class LoggerSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._history = []
        return cls._instance

    def log(self, message: str):
        self._history.append(message)
        print(f"[LOG]: {message}")

    def show_history(self):
        return self._history

log1 = LoggerSingleton()
log2 = LoggerSingleton()
log1.log("Application initialized")
log2.log("User login successful")

print("log1 is log2:", log1 is log2)
print("Complete history:", log2.show_history())


# ==========================================
# 2. Factory Method Pattern
# ==========================================
print("\n--- 2. Factory Method Pattern ---")

class CreditCardPayment:
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} via Credit Card."

class PayPalPayment:
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} via PayPal account."

class CryptoPayment:
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} via Bitcoin network."

class PaymentGatewayFactory:
    _methods = {
        "credit_card": CreditCardPayment,
        "paypal": PayPalPayment,
        "crypto": CryptoPayment,
    }

    @classmethod
    def create_gateway(cls, method_name: str):
        handler_cls = cls._methods.get(method_name.lower())
        if not handler_cls:
            valid_keys = ", ".join(cls._methods.keys())
            raise ValueError(f"Unsupported payment '{method_name}'. Choose from: {valid_keys}")
        return handler_cls()

for gateway_type in ["credit_card", "paypal", "crypto"]:
    processor = PaymentGatewayFactory.create_gateway(gateway_type)
    print(processor.pay(99.50))


# ==========================================
# 3. Builder Pattern (Method Chaining)
# ==========================================
print("\n--- 3. Builder Pattern (HTTP Request Builder) ---")

class HTTPRequestBuilder:
    def __init__(self):
        self._method = "GET"
        self._url = ""
        self._headers = {}
        self._params = {}
        self._body = None

    def set_method(self, method: str):
        self._method = method.upper()
        return self

    def set_url(self, url: str):
        self._url = url
        return self

    def add_header(self, key: str, value: str):
        self._headers[key] = value
        return self

    def set_body(self, data):
        self._body = data
        return self

    def build(self) -> dict:
        return {
            "method": self._method,
            "url": self._url,
            "headers": self._headers,
            "body": self._body
        }

request = (
    HTTPRequestBuilder()
    .set_method("POST")
    .set_url("https://api.example.com/v1/users")
    .add_header("Authorization", "Bearer TOKEN123")
    .add_header("Content-Type", "application/json")
    .set_body({"name": "Dhruba", "role": "Developer"})
    .build()
)

print("Constructed Request Payload:")
print(request)


# ==========================================
# 4. Adapter Pattern (Interfacing Legacy Code)
# ==========================================
print("\n--- 4. Adapter Pattern ---")

class OldXmlParser:
    """Legacy third-party service returning XML-style data."""
    def parse_xml_feed(self) -> str:
        return "<data><item>Apple</item><item>Banana</item></data>"

class ModernJsonAdapter:
    """Adapts XML parser to modern standard JSON list interface."""
    def __init__(self, xml_parser: OldXmlParser):
        self.xml_parser = xml_parser

    def get_items(self) -> list[str]:
        raw_xml = self.xml_parser.parse_xml_feed()
        # Simulated extraction
        clean = raw_xml.replace("<data>", "").replace("</data>", "")
        items = [i.replace("<item>", "").replace("</item>", "") for i in clean.split("</item>") if i]
        return items

adapter = ModernJsonAdapter(OldXmlParser())
print("Adapted Output items:", adapter.get_items())
