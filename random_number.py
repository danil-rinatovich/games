from random import randint

def is_valid(s):
    if str(s).isdigit():
        num = int(s)
        return num > 1
    return False

def game(n):
    count = 0
    print('Введите число:')
    while True:
        number = input()
        if is_valid(number):
            number = int(number)
            if number > n:
                print('Ваше число больше загаданного, попробуйте еще разок')
                count += 1
            elif number < n:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                count += 1
            elif number == n:
                print('Вы угадали, поздравляем!')
                print('Число ваших попыток:', count)
                print('Спасибо, что играли в числовую угадайку!')
                break
        else:
            print('А может быть все-таки введем целое число больше нуля:')

def new_game():
    print('Готовы к еще одному раунду? Введите: "yes" или "no":')
    while True:
        yes_no = input()
        if yes_no == 'yes'.lower():
            print('Введите предел до которого вы хотели бы угадать число:')
            while True:
                y = input()
                if is_valid(y):
                    x = randint(1, int(y))
                    game(x)
                    break
                else:
                    print('А может быть все-таки введем целое число больше нуля:')
                    continue
        elif yes_no == 'no'.lower():
                print('Спасибо за игру! Удачи вам!')
                break
        else:
            print('Неверный ввод. Введите "yes" или "no":')

print('Добро пожаловать в числовую угадайку! Попробуйте отгадать число от 1 до 100!')
n = randint(1, 100)
game(n)
new_game()