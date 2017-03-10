import logging
import logging.config

from resources import *
from procedures import *

def set_logger():
    logging.config.fileConfig('logging.conf')
    root = logging.getLogger()
    level = logging.DEBUG
    if os.getenv("DEBUG") == '1':
        level = logging.DEBUG
    root.setLevel(level)


if __name__ == '__main__':
    set_logger()
    vm_screen = Screen(1)
    os = Windows2008(vm_screen)
    config = {
        'ftp': {
            'password': 'P@ssw0rdP'
        },
        'db': {
            'from': 'additional',           # 'cm package' or 'additional'
            'db': 'remote',                 # 'local' or 'remote', if 'local', 'ip' won't be used in db setting.
            'ip': '10.1.172.12',            # empty means don't change.
            'auth': 'win',                  # 'win' or 'sa'
            'username': 'administrator',
            'password': 'P@ssw0rd',
            'database_name': '',            # empty means don't change.
            'db_duplicated': 'delete'       # 'append', 'delete' or 'create'
        },
        'root': {
            'id': 'root',
            'password': '111111'
        },
        'p4': {
            'username': '',
            'password': 'P@ssw0rdP'
        },
        'smtp': {
            'ip': '10.1.173.218'
        },
        'ad': {
            'ip': '10.1.173.218',
            'username': 'Administrator',
            'password': 'P@ssw0rdP'
        },
        'website': 'virtual',               # 'virtual' or 'default'.
        'license': 'adv',                   # 'std' or 'adv'.
        'http': 'http+s'                    # 'https only', 'http only' or 'http+s'.
    }
    fresh_install = FreshInstall(vm_screen, os, config, {1: '1487588603702.png'})
    migration = Migration(vm_screen, os, config, {1: '1489142293061.png', 3: '1489142293061'})
    try:
        # fresh_install.run()
        migration.run()
    except Exception as e:
        logging.error(e)
        exit()