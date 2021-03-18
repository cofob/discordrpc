import os
import pickle
import importlib.util
from settings import *
import time


def check_module(module_name):
    module_spec = importlib.util.find_spec(module_name)
    if module_spec is None:
        print('Module: {} not found'.format(module_name))
        return None
    else:
        return module_spec


def import_module_from_spec(module_spec):
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def import_module(module):
    module_spec = check_module(module)
    if module_spec is not None:
        return import_module_from_spec(module_spec)


def get_path(args):
    if len(args) == 0:
        raise AttributeError
    if len(args) == 1:
        return args[0]
    path = args[0]
    for i in args[1:]:
        path = os.path.join(path, i)
    return path


def mkdir(*args):
    path = get_path(args)
    if not os.path.isdir(path):
        os.mkdir(path)


def mkfile(*args):
    path = get_path(args)
    if not os.path.isfile(path):
        f = open(path, 'w')
        f.close()


def save_cfg():
    with open(get_path([BASE_FOLDER, 'config']), 'wb') as f:
        pickle.dump(CONFIG, f)


pjoin = os.path.join


def drp_thread(DRP):
    global DRP_CONFIG
    while True:
        time.sleep(DRP_UPDATE_TIME)
        if not DRP_IS_RUNNING:
            continue
        DRP.update(**DRP_CONFIG)
    DRP.shutdown()


def drp_addon_thread(func):
    global DRP_CONFIG
    while True:
        time.sleep(DRP_UPDATE_TIME)
        if not DRP_IS_RUNNING:
            continue
        DRP_CONFIG = func()


def get_user_avatar(user):
    return f'https://cdn.discordapp.com/avatars/{user["id"]}/{user["avatar"]}.png?size=128'
