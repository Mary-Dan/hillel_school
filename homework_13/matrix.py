import random
def create_matrix(M):
    matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]
    return matrix
def print_matrix(matrix):
    M = len(matrix)
    for i in range(M):
        for j in range(M):
            print(matrix[i][j], end="\t")
        print()

    sums = [sum(column) for column in zip(*matrix)]
    for s in sums:
        print(f"{s}\t", end="")
    print()
def sort_matrix(matrix):
    M = len(matrix)
    sums = [0] * M
    for j in range(M):
        for i in range(M):
            sums[j] += matrix[i][j]
    sorted_indices = sorted(range(M), key=lambda x: sums[x])

    odd_columns = [sorted_indices[i] for i in range(M) if i % 2 != 0]
    for i in range(len(odd_columns)):
        matrix.sort(key=lambda x: x[odd_columns[i]])

    even_columns = [sorted_indices[i] for i in range(M) if i % 2 == 0]
    for i in range(len(even_columns)):
        matrix.sort(key=lambda x: x[even_columns[i]], reverse=True)

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