def sum_pair(num, sum):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):

            if num[i] + num[j] == sum:
                return True
    return False

num1 = [1, 2, 3, 4, 5]
sum1 = 5
result1 = sum_pair(num1, sum1)
print(f"в списке {num1} и сумме {sum1} результат: {result1}")

num2 = [6, 7, 8, 9, 10]
sum2 = 20
result2 = sum_pair(num2, sum2)
print(f"в списке {num2} и сумме {sum2} результат: {result2}")
