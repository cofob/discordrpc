import logging


class BaseDRPAddon:
    class Meta:
        name = 'BaseDRPAddon'
        description = 'BaseDRPAddon description'
        version = '0.0.1'
        app_name = 'basedrpaddon'

    def thread(self):
        return {'details': 'nothing'}

    def proxy_thread(self):
        r = self.thread()
        self.log.debug('returned '+str(r))
        return r

    def __init__(self):
        file_log = logging.FileHandler('log.log')
        console_out = logging.StreamHandler()
        logging.basicConfig(format='%(levelname)s:%(name)s -> %(message)s [%(asctime)s]',
                            level=logging.DEBUG,
                            handlers=(file_log, console_out))
        self.log = logging.getLogger("addon.drp." + self.Meta.app_name)
        self.setup()

    def setup(self):
        pass


class BaseStatusAddon:
    class Meta:
        name = 'BaseStatusAddon'
        description = 'BaseStatusAddon description'
        version = '0.0.1'
        app_name = 'basestatusaddon'

    def thread(self):
        return {'details': 'nothing'}

    def proxy_thread(self):
        r = self.thread()
        self.log.debug('returned '+str(r))
        return r

    def __init__(self):
        file_log = logging.FileHandler('log.log')
        console_out = logging.StreamHandler()
        logging.basicConfig(format='%(levelname)s:%(name)s -> %(message)s [%(asctime)s]',
                            level=logging.DEBUG,
                            handlers=(file_log, console_out))
        self.log = logging.getLogger("addon.status."+self.Meta.app_name)
        self.setup()

    def setup(self):
        pass
