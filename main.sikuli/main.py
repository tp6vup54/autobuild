import logging
import logging.config

from operators import *
from resources import *

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
    config = {
        'db': {
            'from': 'additional',           # 'cm package' or 'additional'
            'db': 'local',                 # 'local' or 'remote', if 'local', 'ip' won't be used in db setting.
            'ip': '127.0.0.1',            # empty means don't change.
            'auth': 'sa',                  # 'win' or 'sa'
            'username': 'sa',
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
        'website': 'virtual',               # 'virtual' or 'default'.
        'license': 'adv',                   # 'std' or 'adv'.
        'http': 'http+s'                    # 'https only', 'http only' or 'http+s'.
    }
    os = Windows2008(vm_screen)
    vm = VM_operator(vm_screen, os)
    cm = CM_operator(vm_screen, config, os)
    p4 = P4_operator(vm_screen, os)
    try:
        # vm.switch_tab(3)
        # vm.revert_snapshot('1486441003439.png')
        # vm.switch_tab(1)
        vm.revert_snapshot('1486093318278.png', start=True)
        vm.login()
        cm.copy_build()
        cm.install_build()
        p4.force_sync_latest(config.get('p4').get('password'))
        os.update_cm_config_in_staf(config)
        vm.do_snapshot(config)
    except Exception as e:
        logging.error(e)
        exit()