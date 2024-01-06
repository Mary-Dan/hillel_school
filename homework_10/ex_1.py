calculate = lambda x, y=1: (x**2 + y**2)**0.5
def calculate_hyp(x, y):
    result = list(map(calculate, x, y))
    return result
x = [1, 2, 3]
y = [4, 5, 6]
result1 = calculate_hyp(x, y)
print("result 1:", result1)
result2 = calculate_hyp([1, 2, 3], [5, 6, 7])
print("result 2:", result2)