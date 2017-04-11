import logging
from sikuli import *

from operators import *

class InstallProcedure(object):
    def __init__(self, screen, os, config, init_snapshot):
        self.os = os
        self.vm = VM_operator(screen, os)
        self.cm = CM_operator(screen, config, os)
        self.p4 = P4_operator(screen, os)
        self.config = config
        self.init_snapshot = init_snapshot

    def run(self):
        pass


class FreshInstall(InstallProcedure):
    def __init__(self, screen, os, config, init_snapshot):
        super(FreshInstall, self).__init__(screen, os, config, init_snapshot)

    def run(self):
        if self.config['db']['db'] == 'remote':
            self.vm.switch_tab(int(self.config['vm_tab']['db']))
            self.vm.revert_snapshot(self.init_snapshot['db']['name'], self.init_snapshot['db']['start'])
            self.vm.switch_tab(int(self.config['vm_tab']['cm']))
        self.vm.revert_snapshot(self.init_snapshot['cm']['name'], self.init_snapshot['cm']['start'])
        logging.debug('CM VM status: %s started' % ('not' if self.init_snapshot['cm']['start'] else ''))
        if self.init_snapshot['cm']['start']:
            self.vm.login()
        else:
            self.vm.into_vm()
        self.cm.copy_build(self.config['ftp'])
        self.cm.install_build()
        self.p4.force_sync_latest(self.config.get('p4').get('password'))
        # self.os.update_cm_config_in_staf(self.config)
        # self.os.update_tls12_ODBC_register()
        # self.os.update_IIS_tls12()
        # self.vm.power_switch('restart')
        # self.vm.login()
        self.vm.do_snapshot(self.config)


class Migration(InstallProcedure):
    def __init__(self, screen, os, config, init_snapshot):
        super(Migration, self).__init__(screen, os, config, init_snapshot)

    def run(self):
        if self.config['db']['db'] == 'remote':
            self.vm.switch_tab(int(self.config['vm_tab']['db']))
            self.vm.revert_snapshot(self.init_snapshot['db']['name'], self.init_snapshot['db']['start'])
            self.vm.switch_tab(int(self.config['vm_tab']['cm']))
        self.vm.revert_snapshot(self.init_snapshot['cm']['name'], self.init_snapshot['cm']['start'])
        logging.debug('CM VM status: %s started' % ('not' if self.init_snapshot['cm']['start'] else ''))
        if self.init_snapshot['cm']['start']:
            self.vm.login()
        else:
            self.vm.into_vm()
        self.cm.copy_build(self.config['ftp'])
        self.cm.migrate()
        self.p4.force_sync_latest(self.config.get('p4').get('password'))
        self.os.update_cm_config_in_staf(self.config)
        self.os.update_tls12_ODBC_register()
        self.os.update_IIS_tls12()
        self.vm.power_switch('restart')
        self.vm.login()
        self.vm.do_snapshot(self.config)