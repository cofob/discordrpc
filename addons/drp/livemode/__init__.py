from api import *


class Addon(BaseDRPAddon):
    class Meta(BaseDRPAddon.Meta):
        name = 'Live Mode'
        description = 'Аддон для отображения текущего активного окна в Windows'
        version = '0.0.1'

    def __init__(self):
        pass
