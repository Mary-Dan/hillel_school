with open("text_file.txt", "w") as file:
    while True:
        user_input = input("Введите текст: ")
        if not user_input:
            break
        file.write(user_input + "\n")
print("Ввод завершен")