def is_prime(n):
  """Check if a number is prime."""
    if n < 2:  # 0 and 1 are not prime
              return False
    for i in range(2, int(n**0.5) + 1):
       if n % i == 0:
           return False
          return True
        print(is_prime(7))  # True
print(is_prime(8))  # False
