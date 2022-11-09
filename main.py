import os
from funcs import *
from settings import *

users = {
    'admin': 'pass'
}

set_settings(settings)
print(os.getcwd())#../


while True:
    com = input('--> ').lower().split()
    match com[0]:
        case 'exit':
            break
        case 'createdir':
            create_dir(com)
        case 'changedir':
            change_dir(com)
        case 'createfile':
            create_file(com)
        case 'writetext':
            write_text(com)
        case 'readfile':
            read_file(com)
        case 'deletefile':
            delete_file(com)
        case 'copyfile':
            copy_file(com)
        case 'movefile':
            copy_file(com)
            delete_file(com)
        case 'renamefile':
            rename_file(com)
        case _:
            print('Неизвестная команда')
