## Factorial of a number nikalne ke liye recursive function likho. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120

## Har step me number ko uske previous number ke factorial se multiply karte hain.
