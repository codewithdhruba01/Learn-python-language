## Sum of First n Natural Numbers

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))  # Output: 15

## Har call me current number ko uske previous numbers ke sum me add karte hain.
