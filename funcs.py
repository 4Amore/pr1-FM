import os
import shutil
from settings import *

def change_dir(com):
    os.chdir(com[1])
    if settings['start_dir'] not in com:
        print('Выход за пределы стартовой папки!')
        return False
    print(os.getcwd())#../

def create_dir(com):
    if com[1] not in os.listdir():
        f = open(str(os.getcwd()) + f'/{com[1]}', 'w')
    else:
        print('Директория с таким именем уже существует')

def create_file(com):
    if com[1] not in os.listdir():
        f = open(f'{os.getcwd()}/{com[1]}', 'w')
        f.close()
    else:
        print('Файл с таким именем уже существует')

def write_text(com):
    if com[1] in os.listdir():
        f = open(com[1], 'w')
        f.write(com[2])
        f.close()
    else:
        print('Директории не существует')

def read_file(com):
    f = open(com[1], 'r')
    for line in f.readlines():
        print(line)
    f.close()

def delete_file(com):
    os.remove(f'{os.getcwd()}/{com[1]}')

def copy_file(com):
    shutil.copy(com[1], com[2])

def rename_file(com):
    os.rename(com[1], com[2])