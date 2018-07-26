# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class CreateToy:

    def __init__(self, name, color, type_of):
        self._name = name
        self._color = color
        self._type = type_of

    def get_type(self):
        print(self._type)

    def purchase(self):
        print('Закупаем материал...')

    def sewing(self):
        print('Шьём...')

    def coloring(self):
        print('Красим...')


class BearToy(CreateToy):

    def __init__(self, name, color, type_of):
        super().__init__(name, color, type_of)

    def result_bear(self):
        print('Создан медведь!')


bear = BearToy('Тедди', 'Коричневый', 'Животное')
bear.purchase()
bear.sewing()
bear.coloring()
bear.get_type()
bear.result_bear()
print('')


class FoxToy(CreateToy):

    def __init__(self, name, color, type_of):
        super().__init__(name, color, type_of)

    def result_fox(self):
        print('Создана лиса!')


fox = FoxToy('Фокси', 'оранжевый', 'Животное')
fox.purchase()
fox.sewing()
fox.coloring()
fox.get_type()
fox.result_fox()
print('')


class CatToy(CreateToy):

    def __init__(self, name, color, type_of):
        super().__init__(name, color, type_of)

    def result_cat(self):
        print('Создан котя!')


cat = CatToy('Фокси', 'оранжевый', 'Животное')
cat.purchase()
cat.sewing()
cat.coloring()
cat.get_type()
cat.result_cat()


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

