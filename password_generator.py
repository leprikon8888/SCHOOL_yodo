import random
import string

def main():
    letters_count = int(input('Сколько букв должно быть в пароле? '))
    symbols_count = int(input('Сколько символов? '))
    numbers_count = int(input('Сколько цифр? '))

    password = generate_password(letters_count, symbols_count, numbers_count)
    print(f'Ваш сгенерированный пароль: {password}')


def generate_password(letters_count, symbols_count, numbers_count):
    all_letters = string.ascii_letters
    all_symbols = string.punctuation
    all_numbers = string.digits

    password = []

    for _ in range(letters_count):
        password.append(random.choice(all_letters))

    for _ in range(symbols_count):
        password.append(random.choice(all_symbols))

    for _ in range(numbers_count):
        password.append(random.choice(all_numbers))

    random.shuffle(password)

    return ''.join(password)

if __name__ == '__main__':
    main()