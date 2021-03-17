import importlib
import os
from funcs import *
import api

# create dirs and files
mkdir('addons')
mkdir('addons', 'drp')
mkdir('addons', 'status')

# drp addons import
drp_addon_modules = []
for name in os.listdir(os.path.join('addons', 'drp')):
    if name in ['__pycache__']:
        continue
    m = import_module('addons.drp.'+name)
    if m is not None:
        drp_addon_modules.append(m)
drp_addons = []
for addon in drp_addon_modules:
    drp_addons.append(addon.Addon())
del drp_addon_modules

for addon in drp_addons:
    print(f'Loaded DRP Addon -> \n\tname -> {addon.Meta.name}\n\tdescription -> {addon.Meta.description}\n\t'
          f'version -> {addon.Meta.version}\n')

# status addons import
status_addon_modules = []
for name in os.listdir(os.path.join('addons', 'status')):
    if name in ['__pycache__']:
        continue
    m = import_module('addons.status.'+name)
    if m is not None:
        status_addon_modules.append(m)
status_addons = []
for addon in status_addon_modules:
    status_addons.append(addon.Addon())
del status_addon_modules

for addon in status_addons:
    print(f'Loaded Status Addon -> \n\tname -> {addon.Meta.name}\n\tdescription -> {addon.Meta.description}\n\t'
          f'version -> {addon.Meta.version}\n')
