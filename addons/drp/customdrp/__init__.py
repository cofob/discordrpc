from api import *


class Addon(BaseDRPAddon):
    class Meta(BaseDRPAddon.Meta):
        name = 'Custom DRP'
        description = 'Аддон для смены Discord Rich Presence'
        version = '0.0.1'

    def __init__(self):
        pass
