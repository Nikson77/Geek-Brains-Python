# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import sys
import os

print(sys.argv)


def make_dirs():
    i = 1
    try:
        while i <= 9:
            os.mkdir(os.path.join(os.getcwd(), 'dir_{}'.format(i)))
            i += 1
    except FileExistsError:
        print('Такие директории уже существуют!')
    else:
        print('Директории dir_1 - dir_9 созданы!')


def remove_dirs():
    i = 1
    try:
        while i <= 9:
            os.rmdir(os.path.join(os.getcwd(), 'dir_{}'.format(i)))
            i += 1
    except FileNotFoundError:
        print('Таких директорий не существует!')
    else:
        print('Директории dir_1 - dir_9 удалены!')


actions = {
    'mkdirs': make_dirs,
    'rmdirs': remove_dirs
}

try:
    request = sys.argv[1]
except IndexError:
    print('Для работы скрипта необходимо ввести команду mkdirs или rmdirs!')
else:
    actions[request]()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

path = os.path.join(os.getcwd())

for file in os.listdir(path):
    if os.path.isdir(file):
        print(file)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys
import shutil
import os

path = sys.argv[0]
path_list = os.path.split(path)
file_name_list = path_list[1].split('.')
file_name = file_name_list[0]
file_expansion = file_name_list[1]

shutil.copyfile(path, '{}_copy.{}'.format(file_name, file_expansion))

print('Копия файла успешно создана!')