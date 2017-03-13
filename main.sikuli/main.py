import ConfigParser
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

def create_screen(config):
    idx = config.get('init', 'screen')
    if idx is None:
        idx = 0
    return Screen(int(idx))

def create_os(config, screen):
    ret = None
    version = config.get('init', 'os')
    if version == '2008':
        ret = Windows2008(screen)
    elif version == '2012':
        ret = Windows2012(screen)
    else:
        raise Exception('Os not supported: %s.' % version)
    return ret


if __name__ == '__main__':
    set_logger()
    config_source = ConfigParser.ConfigParser()
    config_source.read('autobuild.conf')
    vm_screen = create_screen(config_source)
    os = create_os(config_source, vm_screen)
    procedure = config_source.get('init', 'procedure')
    config = eval(config_source.get('config', 'config'))
    fresh_install = FreshInstall(vm_screen, os, config, {'cm': '1487588603702.png'})
    migration = Migration(vm_screen, os, config, config.get('init_snapshot'))
    try:
        App.focus('VMware Workstation')
        if procedure == 'fresh_install':
            fresh_install.run()
        elif procedure == 'migration':
            migration.run()
    except Exception as e:
        logging.error(e)
        exit()