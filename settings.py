import time
import os
import inspect
import sys


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


BASE_FOLDER = get_script_dir()
ADDONS_FOLDER = 'addons'
DRP_FOLDER = 'drp'
STATUS_FOLDER = 'status'
ADDONS_FILE_BLACKLIST = ['__pycache__']
DRP_IS_RUNNING = True
DRP_THREAD = None
DRP_ADDON_THREAD = None
STATUS_ADDON_THREAD = None
DRP_CONFIG = {
                'details': 'Discord Rich Presence changer',
                'large_image_key': 'drpc_avatar',
                'start_timestamp': int(time.time())
            }
DRP_UPDATE_TIME = 1
DRP_DEFAULT_APP_ID = 808725586230771752
CONFIG = {}
CURR_USER = {}
