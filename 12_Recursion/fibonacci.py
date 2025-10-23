## Fibonacci series ka nth term recursive function se find karo.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # Output: 8

## fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) formula use hota hai.
