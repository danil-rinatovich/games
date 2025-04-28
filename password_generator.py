import random
import time

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'
chars = ''
random_password = []

print('Введите количество паролей для генерации:')
while True:
    password_gen = input()
    if password_gen.isdigit() and int(password_gen) > 0:
        password_gen = int(password_gen)
        break
    else:
        print('Введите число больше нуля:')

print('Введите длину пароля')
while True:
    length_ = input()
    if length_.isdigit() and int(length_) > 0:
        length_ = int(length_)
        break
    else:
        print('Введите число больше нуля:')

print('В пароле должны присутствовать цифры? y/n')
while True:
    digit = input()
    if digit in ('y', 'n'):
        break
    else:
        print('Введите букву "Y" или "N"')

print('В пароле должны присутствовать прописные буквы? y/n')
while True:
    lowercase_ = input()
    if lowercase_ in ('y', 'n'):
        break
    else:
        print('Введите букву "Y" или "N"')

print('В пароле должны присутствовать строчные буквы? y/n')
while True:
    uppercase_ = input()
    if uppercase_ in ('y', 'n'):
        break
    else:
        print('Введите букву "Y" или "N"')

print('В пароле должны присутствовать символы: ', PUNCTUATION, 'y/n')
while True:
    chars_ = input()
    if chars_ in ('y', 'n'):
        break
    else:
        print('Введите букву "Y" или "N"')

print('Исключать ли неоднозначные символы il1Lo0O? y/n')
while True:
    no_chars_ = input()
    if no_chars_ in ('y', 'n'):
        break
    else:
        print('Введите букву "Y" или "N"')

if digit == 'y'.lower():
    chars += DIGITS

if lowercase_ == 'y'.lower():
    chars += LOWERCASE_LETTERS

if uppercase_ == 'y'.lower():
    chars += UPPERCASE_LETTERS

if chars_ == 'y'.lower():
    chars += PUNCTUATION

if no_chars_ == 'y'.lower():
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')

def generate_password(length, chrs):
    password = ''
    for _ in range(length):
        password += random.choice(chrs)
    return password

if chars == '':
    print(f'Не могу создать пароль, '
          f'выберите символы, которые будут присутствовать в пароле')
else:
    for _ in range(password_gen):
        random_password.append(generate_password(length_, chars))
    print('Ваш пароль на сегодня:', random.choice(random_password))


