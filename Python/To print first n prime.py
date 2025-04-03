#Write a python program to print first n prime numbers

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    num = 2  # Starting from the first prime number
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Input from the user
n = int(input("Enter the value of n: "))
prime_numbers = first_n_primes(n)
print(f"The first {n} prime numbers are: {prime_numbers}")
