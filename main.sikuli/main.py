import logging
import logging.config

from operators import *
from resources import *

def set_logger():
    logging.config.fileConfig(r'C:\Users\sean_c_chen\git\autobuild\logging.conf')
    root = logging.getLogger()
    level = logging.DEBUG
    if os.getenv("DEBUG") == '1':
        level = logging.DEBUG
    root.setLevel(level)

if __name__ == '__main__':
    set_logger()
    vm_screen = Screen(1)
    config = {
        'db': {
            'from': 'additional',           # 'cm package' or 'additional'
            'db': 'remote',                 # 'local' or 'remote', if 'local', 'ip' is useless.
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
            'password': 'P@ssw0rd'
        },
        'website': 'virtual',
        'license': 'std',
        'http': 'http+s'
    }
    os = Windows2008(vm_screen)
    vm = VM_operator(vm_screen, os)
    cm = CM_operator(vm_screen, config, os)
    p4 = P4_operator(vm_screen, os)
    try:
        vm.revert_snapshot('1486093318278.png')
        vm.login()
        cm.copy_build()
        cm.install_build()
        p4.force_sync_latest(config.get('p4').get('password'))
        cm.get_newest_build()
        vm.do_snapshot(config)
    except Exception as e:
        logging.error(e)
        exit()