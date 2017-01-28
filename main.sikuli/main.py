from operators import *
from resources import *

if __name__ == '__main__':
    vm_screen = Screen(1)
    config = {
        'db': 'remote',
        'db_ip': '10.1.173.218',
        'db_auth': 'win',
        'website': 'virtual',
        'licence': 'std'
    }
    os = Windows2008(vm_screen)
    vm = VM_operator(vm_screen, os)
    cm = CM_operator(vm_screen, config, os)
    vm.revert_snapshot("1485421267025.png")
    vm.login()
    cm.copy_build()