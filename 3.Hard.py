# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player = {'name': 'Geralt', 'health': 90, 'damage': 50}
enemy = {'name': 'Wild Hunt', 'health': 110, 'damage': 50}


def attack(attacker, deffender):
    deffender['health'] = deffender['health'] - attacker['damage']
    print('Игрок {} нанёс {} урона.\nЗдоровье {} составляет {} hp.'.format(attacker['name'], attacker['damage'],
                                                                           deffender['name'], deffender['health']))


attack(player, enemy)
attack(enemy, player)

print(player, enemy)


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player = {'name': 'Geralt', 'health': 100, 'damage': 50, 'armor': 1.2}

with open(player['name'] + '.txt', 'w', encoding='UTF-8') as player_file:
    for key, arg in dict.items(player):
        player_file.write('{} {}\n'.format(key, arg))

enemy = {'name': 'Wild_Hunt', 'health': 90, 'damage': 50, 'armor': 1.5}

with open(enemy['name'] + '.txt', 'w', encoding='UTF-8') as enemy_file:
    for key, arg in dict.items(enemy):
        enemy_file.write('{} {}\n'.format(key, arg))


def under_armor(attacker, defender):
    damage_under_armor = attacker['damage'] / defender['armor']
    return damage_under_armor


def attack(attacker, defender):
    while True:
        defender['health'] = defender['health'] - under_armor(attacker, defender)
        print('Игрок {} нанёс {} урона.\nЗдоровье {} составляет {} hp.'.format(attacker['name'],
                                                                               under_armor(attacker, defender),
                                                                               defender['name'], defender['health']))
        if defender['health'] > 0:
            attacker, defender = defender, attacker
        else:
            print('{} погиб!'.format(defender['name']))
            break


def game():
    with open(player['name'] + '.txt', 'r', encoding='UTF-8') as player_file:
        keys_list = []
        args_list = []
        for line in player_file:
            split_line = line.split()
            keys_list.append(split_line[0])
            args_list.append(split_line[-1])
    player_dict = dict(zip(keys_list, args_list))
    player_dict['health'] = float(player_dict['health'])
    player_dict['damage'] = float(player_dict['damage'])
    player_dict['armor'] = float(player_dict['armor'])

    with open(enemy['name'] + '.txt', 'r', encoding='UTF-8') as enemy_file:
        keys_list = []
        args_list = []
        for line in enemy_file:
            split_line = line.split()
            keys_list.append(split_line[0])
            args_list.append(split_line[-1])
    enemy_dict = dict(zip(keys_list, args_list))
    enemy_dict['health'] = float(enemy_dict['health'])
    enemy_dict['damage'] = float(enemy_dict['damage'])
    enemy_dict['armor'] = float(enemy_dict['armor'])

    attack(player_dict, enemy_dict)


game()