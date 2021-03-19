from funcs import *
from settings import *
import threading
import drp
import os
import pickle
import shutil
import logging


file_log = logging.FileHandler('log.log')
console_out = logging.StreamHandler()
logging.basicConfig(format='%(levelname)s:%(name)s -> %(message)s [%(asctime)s]',
                    level=logging.DEBUG,
                    handlers=(file_log, console_out))
log = logging.getLogger("main")

# SETUP
# create dirs and files
mkdir(BASE_FOLDER, ADDONS_FOLDER)
if not os.path.isfile(get_path([BASE_FOLDER, 'config'])):
    log.info('created config')
    CONFIG = {}
    with open(get_path([BASE_FOLDER, 'config']), 'wb') as f:
        pickle.dump(CONFIG, f)
else:
    try:
        with open(get_path([BASE_FOLDER, 'config']), 'rb') as f:
            CONFIG = pickle.load(f)
    except:
        log.error('cannot load config! created copy config.bak')
        os.remove(get_path([BASE_FOLDER, 'config.bak']))
        shutil.copy(get_path([BASE_FOLDER, 'config']), get_path([BASE_FOLDER, 'config.bak']))
        CONFIG = {}
        with open(get_path([BASE_FOLDER, 'config']), 'wb') as f:
            pickle.dump(CONFIG, f)
mkdir(BASE_FOLDER, ADDONS_FOLDER, DRP_FOLDER)
mkdir(BASE_FOLDER, ADDONS_FOLDER, STATUS_FOLDER)

# DRP INIT
CURRENT_DRP_APP_ID = CONFIG.get('app_id', DRP_DEFAULT_APP_ID)
log.info('current DRP app id -> '+str(CURRENT_DRP_APP_ID))
DRP_THREAD = threading.Thread(target=drp_thread, args=(drp.DRP(CURRENT_DRP_APP_ID), ))
DRP_THREAD.start()

# drp addons import
drp_addon_modules = []
for name in os.listdir(os.path.join(ADDONS_FOLDER, DRP_FOLDER)):
    if name in ADDONS_FILE_BLACKLIST:
        continue
    m = import_module('.'.join([ADDONS_FOLDER, DRP_FOLDER, name]))
    if m is not None:
        drp_addon_modules.append(m)
drp_addons = []
for addon in drp_addon_modules:
    drp_addons.append(addon.Addon())
del drp_addon_modules

active_drp = None
for addon in drp_addons:
    if addon.Meta.app_name == CONFIG['addons']['drp']:
        active_drp = addon
    log.debug(f'Loaded DRP Addon -> \n\tname -> {addon.Meta.name}\n\tdescription -> {addon.Meta.description}\n\t'
              f'version -> {addon.Meta.version}')

# status addons import
status_addon_modules = []
for name in os.listdir(os.path.join(ADDONS_FOLDER, STATUS_FOLDER)):
    if name in ADDONS_FILE_BLACKLIST:
        continue
    m = import_module('.'.join([ADDONS_FOLDER, STATUS_FOLDER, name]))
    if m is not None:
        status_addon_modules.append(m)
status_addons = []
for addon in status_addon_modules:
    status_addons.append(addon.Addon())
del status_addon_modules

active_status = None
for addon in status_addons:
    if addon.Meta.app_name == CONFIG['addons']['status']:
        active_status = addon
    log.debug(f'Loaded Status Addon -> \n\tname -> {addon.Meta.name}\n\tdescription -> {addon.Meta.description}\n\t'
              f'version -> {addon.Meta.version}')

log.debug('loaded addons')

DRP_ADDON_THREAD = threading.Thread(target=drp_addon_thread, args=(active_drp.proxy_thread, ))
DRP_ADDON_THREAD.start()
