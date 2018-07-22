# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2

import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('copy <file_name> - создает копию указанного файла')
    print('remove <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print('change <full_path or relative_path> - меняет текущую директорию на указанную')
    print('list отображение полного пути текущей директории')


def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name))
    except FileExistsError:
        print('директория {} уже существует'.format(name))


def ping():
    print("pong")


def copy_file():
    path = os.path.join(os.getcwd(), name)
    if os.path.isdir(path):
        shutil.copytree(path, '{}_copy'.format(name))
        print('Копия директории {} успешно создана!\n'.format(name))
    elif os.path.isfile(name):
        split_name = name.split('.')
        shutil.copy(path, '{}_copy.{}'.format(split_name[0], split_name[1]))
        print('Копия файла {} успешно создана\n!'.format(name))
    else:
        print('Такого файла не существует, либо Вы пытаетесь передать неизвестный тип данных!\n')


def remove_file():
    path = os.path.join(os.getcwd(), name)
    if os.path.isdir(path):
        shutil.rmtree(path)
        print('Директория {} удалена!\n'.format(name))
    elif os.path.isfile(name):
        os.remove(path)
        print('Файл {} удалён!\n'.format(name))
    else:
        print('Такого файла не существует, либо Вы пытатесь удалить неизвесный тип данных!')


def change_dir():
    if os.path.isdir(name):
        if os.path.exists(name):
            os.chdir(name)
        else:
            os.chdir(os.path.join(os.getcwd(), name))
        print('Полный путь, в который Вы перешли: {}'.format(os.path.join(os.getcwd())))
    else:
        print('Не является директорией, либо неверно указан путь!')


def print_full_path():
    path = os.path.join(os.getcwd())
    print('Полный путь текущей директории: {}'.format(path))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'copy': copy_file,
    'remove': remove_file,
    'change': change_dir,
    'list': print_full_path
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        try:
            do[key]()
        except TypeError:
            print('Некорректный тип данных второго аргумента!\n')
    else:
        print("Задан неверный ключ\n")
        print("Укажите ключ help для получения справки\n")
