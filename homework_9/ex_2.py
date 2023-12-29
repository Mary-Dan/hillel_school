import random
def gen_two_list(row=4, col=4):
    return [[random.randint(0, 200) for _ in range(col)] for _ in range(row)]

def sym_two_list(matrix):
    if not matrix:
        print("Список пустой")
        return

    max_width = max(len(str(element)) for row in matrix for element in row)

    for row in matrix:
        for element in row:
            print(f"{element:>{max_width}}", end="  ")
        print()

print("Табличка не получает параметры:")
outcome1 = gen_two_list()
sym_two_list(outcome1)
print("\nТабличка получает 1 параметр:")
outcome2 = gen_two_list(3)
sym_two_list(outcome2)
print("\nТабличка получает 2 параметра:")
outcome3 = gen_two_list(2, 3)
sym_two_list(outcome3)