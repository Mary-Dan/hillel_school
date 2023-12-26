list_1 = [1, 2, 3, 4, 5]
list_2 = ["a", "b", "c", "d", "e"]

a = {list_1[i]: list_2[i] for i in range(len(list_1))}
print(a)