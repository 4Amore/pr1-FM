import os

settings = {
    'start_dir': '/Users/ivanselin/PycharmProjects/FileManager/Workspace'
}


def set_settings(settings):
    os.chdir(settings['start_dir'])
    print(os.getcwd())
