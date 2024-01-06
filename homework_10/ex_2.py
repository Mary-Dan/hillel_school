def prime_num(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_gen(n, z):
    for num in range(n, z + 1):
        if prime_num(num):
            yield num
import random
n = random.randint(1, 100)
z = random.randint(n, n + 100)
for prime in prime_gen(n, z):
    print(prime, end=' ')