import os
import shutil


def go_to_dir(directory):
    try:
        os.chdir(os.path.join(os.getcwd(), directory))
    except FileNotFoundError:
        print('Такой директории не существует!\n')
    else:
        print('Вы перешли в директорию {}\n'.format(directory))


def list_dir(directory):
    path = os.path.join(os.getcwd(), directory)
    files_list = os.listdir(path)
    if len(files_list) == 0:
        print('Пустая директория!')
    else:
        for file in files_list:
            if os.path.isdir(file):
                print('{} - директория'.format(file))
            else:
                print('{} - файл'.format(file))


def remove_dir(directory):
    try:
        shutil.rmtree(os.path.join(os.getcwd(), directory))
    except FileNotFoundError:
        print('Такой директории не существует!\n')
    else:
        print('Директория {} удалена!\n'.format(directory))


def make_dir(directory):
    try:
        os.mkdir(os.path.join(os.getcwd(), directory))
    except FileExistsError:
        print('Такая директория уже существует!\n')
    else:
        print('Директория успешно создана!\n'.format(directory))

