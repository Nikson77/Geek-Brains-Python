# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'банан', 'киви', 'арбуз']
for number, fruit in enumerate(fruits, start=1):
    print('{}. {:>7}'.format(number, fruit))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]
new_list_1 = set(list_1) - set(list_2)
print(new_list_1)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

random_list = [2, 4, -7, 9, 0, -34, 45]
new_list = []
for num in random_list:
    if num % 2 == 0:
        multiple_num = num / 4
        new_list.append(multiple_num)
    else:
        not_multiple_num = num * 2
        new_list.append(not_multiple_num)
print(new_list)