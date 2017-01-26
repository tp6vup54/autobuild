from operators import *

if __name__ == '__main__':
    config = {
        'db': 'remote',
        'db_ip': '10.1.173.218',
        'db_auth': 'win',
        'website': 'virtual',
        'licence': 'std'
    }
    vm = VM_util(Screen(1))
    cm = CM_util(Screen(1), config)
    vm.revert_snapshot("1485421267025.png")
    vm.login()
    cm.copy_build()