def start_password(password):
    if not any(i.isdigit() for i in password):
        print("Задайте в пароле хотя бы 1 цифру")
        return False
    if not any(i.isalpha() for i in password):
        print("Задайте в пароле хотя бы 1 букву")
        return False
    special_chars = "!@#$%^&*()_+{}[]:;<>,.?~\\"
    if not any(i in special_chars for i in password):
        print("Задайте в пароле хотя бы 1 специальний символ")
        return False
    if len(password) < 8:
        print("Пароль должен быть не менее 8 символов")
        return False
    if ' ' in password or '\t' in password:
        print("Пароль не должен иметь символы или табуляцию")
        return False
    return True
def get_password():
    password = input("Введите пароль: ")
    return password

while True:
    password = get_password()
    if start_password(password):
        print("Пароль принят")
        break