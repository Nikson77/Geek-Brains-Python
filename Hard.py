# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

split_equation = equation.split()
print(split_equation)

k = float(split_equation[2][:-1])
print('k = {}'.format(k))

b = float(split_equation[4])
print('b = {}'.format(b))

y = k * x + b
print('Заданное выражение: {}\nЕго решение: {}'.format(equation, y))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# # Пример корректной даты
# date = '01.11.1985'
#
# # Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

data = '30.05.0601'
split_data = data.split('.')
day_str = split_data[0]
month_str = split_data[1]
year_str = split_data[2]
day = float(split_data[0])
month = float(split_data[1])
year = float(split_data[2])

if day != int(day) or day < 1 or day > 31 or len(day_str) != 2:
    print('День введён некорректно!')
elif month != int(month) or month < 1 or month > 12 or len(month_str) != 2:
    print('Месяц введён некорректно!')
elif year != int(year) or year < 1 or year > 9999 or len(year_str) != 4:
    print('Год введён некорректно!')
elif 1 <= month <= 7 and month % 2 == 0 and day > 30:
    print('В этом месяце меньше дней!')
elif 8 <= month <= 12 and month % 2 != 0 and day > 30:
    print('В этом месяце меньше дней!')
else:
    print('{} - дата введена корректно!'.format(data))
