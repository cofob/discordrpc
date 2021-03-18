import discord_rpc
from settings import *
import logging


file_log = logging.FileHandler('log.log')
console_out = logging.StreamHandler()
logging.basicConfig(format='%(levelname)s:%(name)s -> %(message)s [%(asctime)s]',
                    level=logging.DEBUG,
                    handlers=(file_log, console_out))
log = logging.getLogger("drp")


class DRP:
    def __init__(self, app_id: (str, int)):
        callbacks = {
            'ready': self.ready_callback,
            'disconnected': self.disconnected_callback,
            'error': self.error_callback,
        }
        discord_rpc.initialize(app_id, callbacks=callbacks, log=False)

    @staticmethod
    def ready_callback(current_user):
        global CURR_USER
        CURR_USER = current_user
        log.info('User -> {}'.format(current_user))

    @staticmethod
    def disconnected_callback(codeno, codemsg):
        log.error('Disconnected from Discord rich presence RPC. Code {}: {}'.format(codeno, codemsg))

    @staticmethod
    def error_callback(errno, errmsg):
        log.error('An error occurred! Error {}: {}'.format(errno, errmsg))

    @staticmethod
    def update(**kwargs):
        discord_rpc.update_presence(**kwargs)
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

    @staticmethod
    def shutdown():
        discord_rpc.shutdown()
