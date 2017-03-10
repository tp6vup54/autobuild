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
            self.vm.switch_tab(3)
            self.vm.revert_snapshot(self.init_snapshot[3])
            self.vm.switch_tab(1)
        self.vm.revert_snapshot(self.init_snapshot[1], start=True)
        self.vm.login()
        self.cm.copy_build(self.config['ftp'])
        self.cm.install_build()
        self.p4.force_sync_latest(self.config.get('p4').get('password'))
        self.os.update_cm_config_in_staf(self.config)
        self.vm.do_snapshot(self.config)


class Migration(InstallProcedure):
    def __init__(self, screen, os, config, init_snapshot):
        super(Migration, self).__init__(screen, os, config, init_snapshot)

    def run(self):
        if self.config['db']['db'] == 'remote':
            self.vm.switch_tab(3)
            self.vm.revert_snapshot(self.init_snapshot[3])
            self.vm.switch_tab(1)
        self.vm.revert_snapshot(self.init_snapshot[1])
        self.vm.into_vm()
        self.cm.copy_build(self.config['ftp'])
        self.cm.migrate()
        self.p4.force_sync_latest(self.config.get('p4').get('password'))
        self.os.update_cm_config_in_staf(self.config)
        self.vm.do_snapshot(self.config)