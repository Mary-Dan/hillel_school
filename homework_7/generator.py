import random
a = [random.randint(1, 100) for _ in range(15)]
print(a)
odd_numbers = [i for i in a if i % 2 != 0]
even_numbers = [i for i in a if i % 2 == 0]

if sum(odd_numbers) > sum(even_numbers):
    print("Yes")
else:
    print("No")

