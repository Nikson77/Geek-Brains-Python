# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:

    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        return 'Машина {} поехала!'.format(self._name)

    def stop(self):
        return 'Машина {} остановилась!'.format(self._name)

    def turn(self, direction):
        return 'Машина {} повернула {}'.format(self._name, direction)

    def is_police_car(self):
        if self._is_police:
            return 'Это полицейская машина!'
        else:
            return 'Это не полицейская машина.'

    def town_car_purpose(self):
        return 'Машина {} для езды по городу'.format(self._name)


opel_astra = TownCar(100, 'blue', 'Astra', False)
print(opel_astra.go())
print(opel_astra.stop())
print(opel_astra.turn('налево'))
print(opel_astra.is_police_car())
print(opel_astra.town_car_purpose())
print('')


class SportCar:

    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        return 'Машина {} поехала!'.format(self._name)

    def stop(self):
        return 'Машина {} остановилась!'.format(self._name)

    def turn(self, direction):
        return 'Машина {} повернула {}'.format(self._name, direction)

    def is_police_car(self):
        if self._is_police:
            return 'Это полицейская машина!'
        else:
            return 'Это не полицейская машина.'

    def sport_car_purpose(self):
        return 'Машина {} для гонок'.format(self._name)


ferrari_laferrari = SportCar(250, 'red', 'LaFerrari', False)
print(ferrari_laferrari.go())
print(ferrari_laferrari.stop())
print(ferrari_laferrari.turn('направо'))
print(ferrari_laferrari.is_police_car())
print(ferrari_laferrari.sport_car_purpose())
print('')


class WorkCar:

    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        return 'Машина {} поехала!'.format(self._name)

    def stop(self):
        return 'Машина {} остановилась!'.format(self._name)

    def turn(self, direction):
        return 'Машина {} повернула {}'.format(self._name, direction)

    def is_police_car(self):
        if self._is_police:
            return 'Это полицейская машина!'
        else:
            return 'Это не полицейская машина.'

    def work_car_purpose(self):
        return 'Машина {} для езды на работу'.format(self._name)


mini_cooper = WorkCar(70, 'yellow', 'Cooper', False)
print(mini_cooper.go())
print(mini_cooper.stop())
print(mini_cooper.turn('налево'))
print(mini_cooper.is_police_car())
print(mini_cooper.work_car_purpose())
print('')


class PoliceCar:

    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        return 'Машина {} поехала!'.format(self._name)

    def stop(self):
        return 'Машина {} остановилась!'.format(self._name)

    def turn(self, direction):
        return 'Машина {} повернула {}'.format(self._name, direction)

    def is_police_car(self):
        if self._is_police:
            return 'Это полицейская машина!'
        else:
            return 'Это не полицейская машина.'

    def police_car_purpose(self):
        return 'Машина {} для поимки преступников'.format(self._name)


UAZ = PoliceCar(120, 'white-blue', 'Бобик', True)
print(UAZ.go())
print(UAZ.stop())
print(UAZ.turn('налево'))
print(UAZ.is_police_car())
print(UAZ.police_car_purpose())

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        return 'Машина {} поехала!'.format(self._name)

    def stop(self):
        return 'Машина {} остановилась!'.format(self._name)

    def turn(self, direction):
        return 'Машина {} повернула {}'.format(self._name, direction)

    def is_police_car(self):
        if self._is_police:
            return 'Это полицейская машина!'
        else:
            return 'Это не полицейская машина.'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def town_car_purpose(self):
        return 'Машина {} для езды по городу'.format(self._name)


opel_astra = TownCar(100, 'blue', 'Astra')
print(opel_astra.go())
print(opel_astra.stop())
print(opel_astra.turn('налево'))
print(opel_astra.is_police_car())
print(opel_astra.town_car_purpose())
print('')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def sport_car_purpose(self):
        return 'Машина {} для гонок'.format(self._name)


ferrari_laferrari = SportCar(250, 'red', 'LaFerrari')
print(ferrari_laferrari.go())
print(ferrari_laferrari.stop())
print(ferrari_laferrari.turn('направо'))
print(ferrari_laferrari.is_police_car())
print(ferrari_laferrari.sport_car_purpose())
print('')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def work_car_purpose(self):
        return 'Машина {} для езды на работу'.format(self._name)


mini_cooper = WorkCar(70, 'yellow', 'Cooper')
print(mini_cooper.go())
print(mini_cooper.stop())
print(mini_cooper.turn('налево'))
print(mini_cooper.is_police_car())
print(mini_cooper.work_car_purpose())
print('')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def police_car_purpose(self):
        return 'Машина {} для поимки преступников'.format(self._name)


UAZ = PoliceCar(120, 'white-blue', 'Бобик')
print(UAZ.go())
print(UAZ.stop())
print(UAZ.turn('налево'))
print(UAZ.is_police_car())
print(UAZ.police_car_purpose())

