import random
a = {f"key_{i}": random.randint(1, 100) for i in range(1, 21)}
print(a)

result = 1
for i in a.values():
    result *= i
    print(result)