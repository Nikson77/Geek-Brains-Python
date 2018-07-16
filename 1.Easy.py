# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def about_my_self(name, age, city):
    age_list = list(str(age))
    years_1 = 'лет'
    years_2 = 'год(а)'
    if int(age_list[-1]) == 0 or 5 <= int(age_list[-1]) <= 9 or int(age_list[-2]) == 1:
        return '{}, {} {}, проживает в городе {}.'.format(name, age, years_1, city)
    else:
        return '{}, {} {}, проживает в городе {}.'.format(name, age, years_2, city)


print(about_my_self('Василий', 113, 'Москва'))


# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def the_largest_number(num1, num2, num3):
    nums_list = []
    nums_list.append(num1)
    nums_list.append(num2)
    nums_list.append(num3)
    max_nums_list = max(nums_list)
    return 'Наибольшее из введённых чисел: {}'.format(max_nums_list)


print(the_largest_number(4, 7, 5))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

def the_longest_string(*args):
    max_len = 0
    the_longest_strings_list = []
    for i in args:
        if len(i) > max_len:
            max_len = len(i)
    for j in args:
        if len(j) == max_len:
            the_longest_strings_list.append(j)
    return 'Список самых длинных строк: {}'.format(the_longest_strings_list)


print(the_longest_string('a', 'bbb', 'ccccc', 'ddd', 'eeeee', 'ff'))