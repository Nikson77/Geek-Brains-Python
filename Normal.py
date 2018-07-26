# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor

# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована

# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:

    def __init__(self, person_name, person_health, person_damage, person_armor):
        self.name = person_name
        self.health = person_health
        self.damage = person_damage
        self.armor = person_armor

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damage

    def get_armor(self):
        return self.armor

    def set_health(self, new_health):
        self.health = new_health


class Player(Person):

    def __init__(self, person_name, person_health, person_damage, person_armor):
        super().__init__(person_name, person_health, person_damage, person_armor)

    def _damage_to_enemy_under_armor(self, enemy_armor):
        player_damage_under_armor = self.damage / enemy_armor
        print('{} нанёс {} урона'.format(geralt.get_name(), player_damage_under_armor))
        return player_damage_under_armor

    def player_attack(self, enemy_health):
        enemy_health -= geralt._damage_to_enemy_under_armor(wild_hunt.get_armor())
        return enemy_health


geralt = Player('Geralt', 100, 30, 1.2)


class Enemy(Person):

    def __init__(self, person_name, person_health, person_damage, person_armor):
        super().__init__(person_name, person_health, person_damage, person_armor)

    def _damage_to_player_under_armor(self, player_armor):
        enemy_damage_under_armor = self.damage / player_armor
        print('{} нанёс {} урона'.format(wild_hunt.get_name(), enemy_damage_under_armor))
        return enemy_damage_under_armor

    def enemy_attack(self, player_health):
        player_health -= wild_hunt._damage_to_player_under_armor(geralt.get_armor())
        return player_health


wild_hunt = Enemy('Wild Hunt', 100, 30, 1.2)


class Fight:

    def attack(self):
        i = 1
        while True:
            print('Раунд {}'.format(i))
            damage_to_enemy = geralt.player_attack(wild_hunt.get_health())
            wild_hunt.set_health(damage_to_enemy)
            print('Здоровье {}: {}'.format(wild_hunt.get_name(), wild_hunt.get_health()))
            if wild_hunt.get_health() > 0:
                damage_to_player = wild_hunt.enemy_attack(geralt.get_health())
                geralt.set_health(damage_to_player)
                print('Здоровье {}: {}'.format(geralt.get_name(), geralt.get_health()))
                if geralt.get_health() > 0:
                    i += 1
                    continue
                else:
                    print('{} победил! в раунде {}'.format(wild_hunt.get_name(), i))
                    break
            else:
                print('{} победил! в раунде {}'.format(geralt.get_name(), i))
                break


begin_fight = Fight()

begin_fight.attack()


