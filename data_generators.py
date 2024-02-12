import random
import string


def generate_random_string():
    characters = string.ascii_letters.lower()
    return str(''.join(random.choice(characters) for _ in range(15)))


def generate_random_user_name():
    return generate_random_string()


def generate_random_email():
    return f'{generate_random_string()}@gmail.com'


def generate_random_five_symbols_password():
    characters = string.ascii_letters.lower()
    return ''.join(random.choice(characters) for _ in range(4))


def generate_random_six_symbols_password():
    characters = string.ascii_letters.lower()
    return ''.join(random.choice(characters) for _ in range(10))


KNOWN_USER_EMAIL = 'qwe123@gmail.com' # Заранее созданный юзер для последующих тестов с логином
KNOWN_USER_PASSWORD = 'qwe123' # Пароль созданного юзера
