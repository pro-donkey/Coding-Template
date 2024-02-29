# Greatest Common Divisor (GCD) using Euclidean Algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a






# Least Common Multiple (LCM)
def lcm(a, b):
    return a * b // gcd(a, b)






# Prime Numbers - Sieve of Eratosthenes
def sieve(n):
    primes = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes






# Prime Factorization
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors





# Modular Exponentiation (a^b mod m)
def power(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result





# Modular Inverse (a^-1 mod m)
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)


