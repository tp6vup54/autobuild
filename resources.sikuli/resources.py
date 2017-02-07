import time
import logging

from sikuli import *

class Os(object):
    def __init__(self, screen):
        self.screen = screen
        self._staf_default = {
            'ui_py': {
                'location': r'C:\STAF\lib\python\sCloud\util\GlobalVariable\Module\UI.py',
                'ip': {
                    'content': r'`"%s`"',
                    'default': '127.0.0.1'
                }
            }, 'scdb_py': {
                'location': r'C:\STAF\lib\python\sCloud\util\GlobalVariable\Module\SCDB.py',
                'ip': {
                    'content': r'`"%s`"',
                    'default': '127.0.0.1'
                },
                'username': {
                    'content': r'`"%s`"',
                    'default': 'sa'
                },
                'password': {
                    'content': r'`"%s`"',
                    'default': 'P@ssw0rd'
                }
            }
        }
        self._start = ''
        self._run = ''
        self._login_ready = ''
        self._username_textbox = ''
        self._os_ready = ''
        self._build_window_ready = ''
        self._build_copied = ''
        self._yes = ''
        self._close = ''
        self._next = ''
        self._website_combobox = ''
        self._http_combobox = ''
        self._db_cm_package_radio = ''
        self._db_additional_sql = ''
        self._db_ip_textbox = ''
        self._db_windows_account_radio = ''
        self._db_username = ''
        self._db_password = ''
        self._db_databasename = ''
        self._delete_existing_db_radio = ''
        self._create_root_check = ''
        self._show_readme_checkbox = ''
        self._start_console_checkbox = ''
        self._finish = ''

    @property
    def start(self):
        return self._start

    @property
    def run(self):
        return self._run

    @property
    def login_ready(self):
        return self._login_ready

    @property
    def username_textbox(self):
        return self._username_textbox

    @property
    def os_ready(self):
        return self._os_ready

    @property
    def build_window_ready(self):
        return self._build_window_ready

    @property
    def build_copied(self):
        return self._build_copied

    @property
    def yes(self):
        return self._yes

    @property
    def close(self):
        return self._close

    @property
    def next(self):
        return self._next

    @property
    def website_combobox(self):
        return self._website_combobox

    @property
    def http_combobox(self):
        return self._http_combobox

    @property
    def db_cm_package_radio(self):
        return self._db_cm_package_radio

    @property
    def db_additional_sql(self):
        return self._db_additional_sql

    @property
    def db_ip_textbox(self):
        return self._db_ip_textbox

    @property
    def db_windows_account_radio(self):
        return self._db_windows_account_radio

    @property
    def db_username(self):
        return self._db_username

    @property
    def db_password(self):
        return self._db_password

    @property
    def db_databasename(self):
        return self._db_databasename

    @property
    def delete_existing_db_radio(self):
        return self._delete_existing_db_radio

    @property
    def create_root_check(self):
        return self._create_root_check

    @property
    def show_readme_checkbox(self):
        return self._show_readme_checkbox

    @property
    def start_console_checkbox(self):
        return self._start_console_checkbox

    @property
    def finish(self):
        return self._finish

    def after_login(self):
        pass

    def open_run(self):
        logging.debug('>> open_run')
        self.screen.click(self.start)
        self.screen.click(self.run)
        time.sleep(1)
        logging.debug('<< open_run')

    def get_newest_build(self):
        logging.debug('>> get_newest_build')
        self.open_run()
        type(r'\\10.201.16.7\build\TMCM\7.0\win32\en\Rel' + Key.ENTER)
        self.screen.wait(self.build_window_ready, 5)
        type(Key.END + Key.UP + Key.F2)
        type('c', KEY_CTRL)
        type(Key.F4, KEY_ALT)
        logging.debug('<< get_newest_build')

    def open_powershell(self):
        logging.debug('>> open_powershell')
        self.open_run()
        type('powershell' + Key.ENTER)
        time.sleep(1)
        logging.debug('<< open_powershell')

    def _get_file_changing_command(self, data_root, data_domain, new_content):
        return r'(Get-Content %s) | ForEach-Object { $_ -replace "%s", "%s" } | Set-Content %s' %\
        (
            self._staf_default[data_root]['location'],
            self._staf_default[data_root][data_domain]['content'] % self._staf_default[data_root][data_domain]['default'], 
            self._staf_default[data_root][data_domain]['content'] % new_content,
            self._staf_default[data_root]['location']
            # r'C:\Users\Administrator\Desktop\aaa.txt'
        )

        # config = {
        #       'cm': {'ip': XXX},
        #       'db': {'ip': XXX, 'username': XXX, 'password': XXX},
        #       'ad': {'ip': XXX, 'username': XXX, 'password': XXX}
        # }
    def update_cm_config_in_staf(self, config):
        logging.debug('>> update_cm_config_in_staf, config: ')
        logging.debug(str(config))
        config_template = {
            'cm': ('ip'),
            'db': ('ip'),
            'ad': ('ip', 'username', 'password')
        }
        target_file = {'cm': 'ui_py', 'db': 'scdb_py', 'ad': 'ui_py'}
        if config:
            self.open_powershell()
        for k, v in config_template.iteritems():
            if k in config:
                for _ in v:
                    if _ in config[k]:
                        logging.debug('Key in: ' + self._get_file_changing_command(target_file[k], _, config[k][_]))
                        type(self._get_file_changing_command(target_file[k], _, config[k][_]) + Key.ENTER)
        logging.debug('<< update_cm_config_in_staf')

class Windows2008(Os):
    def __init__(self, screen):
        super(Windows2008, self).__init__(screen)
        self._start = '1485423506166.png'
        self._run = '1485423273150.png'
        self._login_ready = '1485419464673.png'
        self._username_textbox = '1485419481810.png'
        self._os_ready = '1485419533925.png'
        self._build_window_ready = '1485421165687.png'
        self._build_copied = '1485424550312.png'
        self._yes = '1486023680669.png'
        self._close = '1486020199747.png'
        self._next = '1486025858135.png'
        self._website_combobox = '1486030217924.png'
        self._http_combobox = '1486030230900.png'
        self._db_cm_package_radio = '1486031183013.png'
        self._db_additional_sql = '1486033303175.png'
        self._db_ip_textbox = '1486031219128.png'
        self._db_windows_account_radio = '1486031244017.png'
        self._db_username = '1486031264160.png'
        self._db_password = '1486031275366.png'
        self._db_databasename = '1486031286256.png'
        self._delete_existing_db_radio = '1486035602284.png'
        self._create_root_check = '1486037398636.png'
        self._show_readme_checkbox = '1486090986166.png'
        self._start_console_checkbox = '1486090995255.png'
        self._finish = '1486091003463.png'

        self._license_cancel = '1485419515911.png'

        self._server_management_close = '1485419547613.png'

    def after_login(self):
        self.screen.click(self._license_cancel)
        self.screen.wait(self.os_ready, 10)
        self.screen.click(self._server_management_close)


class Windows2012(Os):
    def __init__(self):
        super(Windows2012, self).__init__()