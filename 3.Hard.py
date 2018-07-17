# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:
        print(check_account(person))
    elif choice == 2:
        try:
            count = float(input('Сумма к снятию:'))
        except ValueError:
            print('Необходимо ввести число!')
        else:
            if count > 0:
                print(withdraw_money(person, count))
            else:
                print('Необходимо ввести сумму больше 0!')


def start():
    try:
        card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
    except ValueError:
        print(
            'Необходимо вести верные номер карты и пинкод через пробел, для ввода допустимы только целые числа! '
            'Повторите ввод корректно!')
    else:
        try:
            card_number = int(card_number)
            pin_code = int(pin_code)
        except ValueError:
            print('Для ввода допустимы только целые числа!')
        else:
            person = get_person_by_card(card_number)
            if person and is_pin_valid(person, pin_code):
                while True:
                    try:
                        choice = int(input('Выберите пункт:\n'
                                           '1. Проверить баланс\n'
                                           '2. Снять деньги\n'
                                           '3. Выход\n'
                                           '---------------------\n'
                                           'Ваш выбор:'))
                    except ValueError:
                        print('Введите целое число от 1 до 3!')
                    else:
                        if choice == 3:
                            break
                        elif choice > 3:
                            print('Такого пункта меню нет, повторите ввод!')
                        process_user_choice(choice, person)
            else:
                print('Номер карты или пин код введены не верно!')


start()
