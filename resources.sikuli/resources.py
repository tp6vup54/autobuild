import os
import time
import logging

from sikuli import *

class IISCryptoResource(object):
    def __init__(self):
        self.run = '1489404478155.png'
        self.accept = '1489404875931.png'
        self.apply = '1489404922811.png'


class RegeditUtil(object):
    def __init__(self):
        self.current_panel = 'left'

    def reset(self):
        for i in range(10):
            type(Key.LEFT)
        type(Key.HOME + Key.RIGHT)

    def switch_panel(self):
        if self.current_panel == 'left':
            type(Key.TAB)
            self.current_panel = 'right'
        elif self.current_panel == 'right':
            type(Key.TAB, KEY_SHIFT)
            self.current_panel = 'left'

    def navigate_to_target(self, target):
        l = target.split('\\')
        self.reset()
        for k in l:
            type(k + Key.RIGHT)

    def copy_key(self, key):
        if self.current_panel == 'left':
            self.switch_panel()
        type(key + Key.ENTER)
        type('c', KEY_CTRL)
        type(Key.ESC)
        self.switch_panel()

    def paste_key(self, key):
        if self.current_panel == 'left':
            self.switch_panel()
        type(key + Key.ENTER)
        type('v', KEY_CTRL)
        type(Key.ENTER)
        self.switch_panel()


class Os(object):
    def __init__(self, screen):
        self.screen = screen
        self.reg = RegeditUtil()
        self.iiscrypto = IISCryptoResource()
        self._staf_default = {
            'server': {
                'location': r'C:\STAF\lib\python\sCloud\util\GlobalVariable\Module\UI.py',
                'ip': {
                    'pattern': r'dict_UI\[\"Server\"\] = \"%s\"',
                    'content': r'dict_UI[\"Server\"] = \"%s\"',
                    'default': '127.0.0.1'
                }
            },
            'ad': {
                'location': r'C:\STAF\lib\python\sCloud\util\GlobalVariable\Module\UI.py',
                'ip': {
                    'pattern': r'dict_UI\[\"ADServerIP\"\] = \"%s\"',
                    'content': r'dict_UI[\"ADServerIP\"] = \"%s\"',
                    'default': '10.201.'
                },
                'username': {
                    'pattern': r'dict_UI\[\"ADUsername\"\] = \"%s\"',
                    'content': r'dict_UI[\"ADUsername\"] = \"%s\"',
                    'default': 'Administrator'
                },
                'password': {
                    'pattern': r'dict_UI\[\"ADPassword\"\] = \"%s\"',
                    'content': r'dict_UI[\"ADPassword\"] = \"%s\"',
                    'default': 'Tmcm@123$'
                },
            },
            'smtp': {
                'location': r'C:\STAF\lib\python\sCloud\util\GlobalVariable\Module\UI.py',
                'ip': {
                    'pattern': r'dict_UI\[\"SMTPServer\"\] = \"%s\"',
                    'content': r'dict_UI[\"SMTPServer\"] = \"%s\"',
                    'default': '10.201.'
                }
            },
            'db': {
                'location': r'C:\STAF\lib\python\sCloud\util\GlobalVariable\Module\SCDB.py',
                'ip': {
                    'pattern': r'dict_SCDB\[\"DBServer\"\] = .+%s\"',
                    'content': r'dict_SCDB[\"DBServer\"] = \"%s\"',
                    'default': 'SQLEXPRESS'
                },
                'username': {
                    'pattern': r'dict_SCDB\[\"User\"\] = \"%s\"',
                    'content': r'dict_SCDB[\"User\"] = \"%s\"',
                    'default': 'sa'
                },
                'password': {
                    'pattern': r'dict_SCDB\[\"Passwd\"\] = \"%s\"',
                    'content': r'dict_SCDB[\"Passwd\"] = \"%s\"',
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
        self._waiting_ftp_password = ''
        self._ftp_password_blank = ''
        self._ok = ''
        self._user_selection = ''
        self._build_window = ''

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

    @property
    def waiting_ftp_password(self):
        return self._waiting_ftp_password

    @property
    def ok(self):
        return self._ok

    @property
    def ftp_password_blank(self):
        return self._ftp_password_blank

    @property
    def user_selection(self):
        return self._user_selection

    @property
    def build_window(self):
        return self._build_window

    def after_login(self):
        pass

    def open_run(self):
        logging.debug('>> open_run')
        self.screen.click(self.start)
        self.screen.click(self.run)
        time.sleep(1)
        logging.debug('<< open_run')

    def check_enter_ftp_password(self, ftp_config):
        logging.debug('>> check_enter_ftp_password')
        if self.screen.exists(self.waiting_ftp_password, 5):
            logging.debug('Detect ftp password field.')
            self.screen.click(self.ftp_password_blank)
            type(ftp_config['password'])
            type(Key.TAB + Key.SPACE + Key.ENTER)
        logging.debug('<< check_enter_ftp_password')

    def try_to_login_ftp(self, ftp_config):
        logging.debug('>> try_to_login_ftp')
        self.open_run()
        type(r'\\10.201.16.7\build\TMCM\7.0\win32\en\Rel' + Key.ENTER)
        self.check_enter_ftp_password(ftp_config)
        self.screen.wait(self.build_window_ready, 5)
        self.screen.click(self.build_window)
        type(Key.F4, KEY_ALT)
        logging.debug('<< try_to_login_ftp')

    def get_newest_build(self, ftp_config):
        logging.debug('>> get_newest_build')
        self.open_run()
        type(r'\\10.201.16.7\build\TMCM\7.0\win32\en\Rel' + Key.ENTER)
        self.check_enter_ftp_password(ftp_config)
        self.screen.wait(self.build_window_ready, 10)
        self.screen.click(self.build_window)
        self.turn_off_numlock()
        type(Key.END + Key.UP + Key.UP + Key.F2)
        type('c', KEY_CTRL)
        type(Key.F4, KEY_ALT)
        logging.debug('<< get_newest_build')

    def turn_off_numlock(self):
        val = Env.isLockOn(Key.NUM_LOCK)
        if val:
            logging.debug('switching off numlock...')
            type(Key.NUM_LOCK)
        logging.debug('Numlock turned off.')

    def open_powershell(self):
        logging.debug('>> open_powershell')
        self.open_run()
        type('powershell' + Key.ENTER)
        time.sleep(1)
        logging.debug('<< open_powershell')

    def _get_file_changing_command(self, template, data_domain, new_content):
        return 'powershell -Command "(gc %s) -replace \'%s\', \'%s\' | Out-File %s"' %\
        (
            template['location'],
            template[data_domain]['pattern'] % template[data_domain]['default'], 
            template[data_domain]['content'] % new_content,
            template['location']
        )

        # config = {
        #       'cm': {'ip': XXX},
        #       'db': {'ip': XXX, 'username': XXX, 'password': XXX},
        #       'ad': {'ip': XXX, 'username': XXX, 'password': XXX}
        # }
    def update_cm_config_in_staf(self, config):
        logging.debug('>> update_cm_config_in_staf, config: ')
        logging.debug(str(config))
        for k1, v1 in config.iteritems():
            if k1 in self._staf_default:
                for k2, v2 in v1.iteritems():
                    if k2 in self._staf_default[k1]:
                        logging.debug('Key in: ' + self._get_file_changing_command(self._staf_default[k1], k2, v2))
                        self.open_run()
                        type(self._get_file_changing_command(self._staf_default[k1], k2, v2) + Key.ENTER)
        logging.debug('<< update_cm_config_in_staf')

    def update_tls12_ODBC_register(self):
        logging.debug('>> update_tls12_ODBC_register')
        pathes = [
            {
                'source': r'HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBCINST.INI\ODBC Drivers',
                'target': r'HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBC.INI\ControlManager_DataBase'
            },
            {
                'source': r'HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\ODBC\ODBCINST.INI\ODBC Drivers',
                'target': r'HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\ODBC\ODBC.INI\ControlManager_DataBase'
            }
        ]
        self.open_run()
        type('regedit' + Key.ENTER)
        time.sleep(1)
        for p in pathes:
            logging.debug('Current operated: %s' % str(p))
            self.reg.navigate_to_target(p['source'])
            type(Key.UP)
            self.reg.copy_key('Driver')
            self.reg.navigate_to_target(p['target'])
            self.reg.paste_key('Driver')
        type(Key.F4, KEY_ALT)
        logging.debug('<< update_tls12_ODBC_register')

    def update_IIS_tls12(self):
        self.open_run()
        type(r'\\10.201.18.44\TMCM_Lab\Private\Sean\tls\IISCrypto' + Key.ENTER)
        self.screen.wait(self.iiscrypto.run, 60)
        self.screen.click(self.iiscrypto.run)
        self.screen.wait(self.iiscrypto.accept, 60)
        self.screen.click(self.iiscrypto.accept)
        self.screen.wait(self.iiscrypto.apply, 10)
        type('mpsstttttttt')
        self.screen.click(self.iiscrypto.apply)
        time.sleep(1)
        type(Key.ENTER + Key.ENTER)


class Windows2008(Os):
    def __init__(self, screen):
        super(Windows2008, self).__init__(screen)
        addImagePath(os.path.dirname(os.path.abspath(__file__)) + '\\Windows2008')
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
        self._waiting_ftp_password = '1488530087175.png'
        self._ok = '1488531174818.png'
        self._ftp_password_blank = '1488769577893.png'
        self._user_selection = '1489397678944.png'
        self._build_window = '1489398946375.png'

        self._license_cancel = '1485419515911.png'

        self._server_management_close = '1485419547613.png'

    def after_login(self):
        logging.debug('>> after_login')
        self.screen.wait(self._license_cancel, 60)
        self.screen.click(self._license_cancel)
        self.screen.wait(self.os_ready, 60)
        self.screen.click(self._server_management_close)
        logging.debug('<< after_login')


class Windows2012(Os):
    def __init__(self):
        super(Windows2012, self).__init__()
        addImagePath(os.path.dirname(os.path.abspath(__file__)) + '\\Windows2012')
        self._start = '.png'
        self._run = '.png'
        self._login_ready = '1487922000502.png'
        self._username_textbox = '1487922168482.png'
        self._os_ready = '1487922298909.png'
        self._build_window_ready = '.png'
        self._build_copied = '.png'
        self._yes = '.png'
        self._close = '.png'
        self._next = '.png'
        self._website_combobox = '.png'
        self._http_combobox = '.png'
        self._db_cm_package_radio = '.png'
        self._db_additional_sql = '.png'
        self._db_ip_textbox = '.png'
        self._db_windows_account_radio = '.png'
        self._db_username = '.png'
        self._db_password = '.png'
        self._db_databasename = '.png'
        self._delete_existing_db_radio = '.png'
        self._create_root_check = '.png'
        self._show_readme_checkbox = '.png'
        self._start_console_checkbox = '.png'
        self._finish = '.png'

        self._server_management_close = '1485419547613.png'

    def after_login(self):
        self.screen.wait(self.os_ready, 10)
        self.screen.click(self._server_management_close)