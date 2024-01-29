def get_user_input():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        return num1 + num2
    except ValueError:
        str1 = input("Хоча б одне з чисел не є числом. Введіть перший рядок: ")
        str2 = input("Введіть другий рядок: ")
        return str1 + str2
