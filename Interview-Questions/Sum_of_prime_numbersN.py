#Sum of prime numbers upto N:
#The optimal approach for this problem is the Sieve of Eratosthenes, but the brute-force approach also got accepted.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_of_primes_brute(N):
    return sum(i for i in range(2, N+1) if is_prime(i))

# Example usage:
N = 20
print(sum_of_primes_brute(N))  # Output: 77