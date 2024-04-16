def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Base cases: 0 and 1 are not prime
    if n <= 1:
        return False
    # Base cases: 2 and 3 are prime
    elif n <= 3:
        return True
    # If the number is divisible by 2 or 3, it's not prime
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        # Starting from 5, we only need to check up to the square root of n
        i = 5
        while i * i <= n:
            # If n is divisible by i or i+2, it's not prime
            if n % i == 0 or n % (i + 2) == 0:
                return False
            # Increment i by 6, as all primes greater than 3 can be written as 6k ± 1
            i += 6
        return True
