from api import *


class Addon(BaseStatusAddon):
    class Meta(BaseStatusAddon.Meta):
        name = 'Custom Status'
        description = 'Аддон для установки анимированного статуса'
        version = '0.0.1'

    def __init__(self):
        pass
