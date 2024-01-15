def req_digit(func):
    def start_password(password):
        if not any(i.isdigit() for i in password):
            print("Задайте в пароле хотя бы 1 цифру")
            return False
        return func(password)
    return start_password

def req_alpha(func):
    def start_password(password):
        if not any(i.isalpha() for i in password):
            print("Задайте в пароле хотя бы 1 букву")
            return False
        return func(password)
    return start_password

def req_char(func):
    def start_password(password):
        chars = "!@#$%^&*()_+{}[]:;<>,.?~\\"
        if not any(i in chars for i in password):
            print("Задайте в пароле хотя бы 1 специальный символ")
            return False
        return func(password)
    return start_password

def req_length(func):
    def start_password(password):
        if len(password) < 8:
            print("Пароль должен быть не менее 8 символов")
            return False
        return func(password)
    return start_password

def req_no_space(func):
    def start_password(password):
        if ' ' in password or '\t' in password:
            print("Пароль не должен содержать пробелы или табуляции")
            return False
        return func(password)
    return start_password

@req_digit
@req_alpha
@req_char
@req_length
@req_no_space
def start_password(password):
    print("Пароль принят")
    return True

def get_password():
    password = input("Введите пароль: ")
    return password

while True:
    password = get_password()
    start_password(password)
    break

