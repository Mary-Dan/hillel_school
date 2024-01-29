import random

def create_matrix(M):
    matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]
    return matrix

def print_matrix(matrix):
    M = len(matrix)
    column_sums = [0] * M
    for i in range(M):
        for j in range(M):
            print(matrix[i][j], end="\t")
            column_sums[j] += matrix[i][j]
        print()

    sorted_indices = sorted(range(M), key=lambda x: column_sums[x])

    for s in sorted(column_sums):
        print(f"{s}\t", end="")
    print()

def sort_matrix(matrix):
    M = len(matrix)
    column_sums = [0] * M
    for j in range(M):
        for i in range(M):
            column_sums[j] += matrix[i][j]

    sorted_indices = sorted(range(M), key=lambda x: column_sums[x])

    for i in range(M):
        if i % 2 == 0:
            matrix.sort(key=lambda x: x[sorted_indices[i]])
        else:
            matrix.sort(key=lambda x: x[sorted_indices[i]], reverse=True)

if __name__ == "__main__":
    M = int(input("Введите размер таблицы: "))

    if M <= 5:
        print("Размер должен быть больше 5")
    else:
        matrix = create_matrix(M)
        print("До сортировки:")
        print_matrix(matrix)

        sort_matrix(matrix)

        print("\nПосле сортировки:")
        print_matrix(matrix)
