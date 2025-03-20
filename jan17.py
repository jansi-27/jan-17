# Print next prime and previous prime of a given number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

# Find previous prime
prev_prime = num - 1
while prev_prime > 1 and not is_prime(prev_prime):
    prev_prime -= 1

# Find next prime
next_prime = num + 1
while not is_prime(next_prime):
    next_prime += 1

print("Previous prime:", prev_prime if prev_prime > 1 else "No previous prime")
print("Next prime:", next_prime)
