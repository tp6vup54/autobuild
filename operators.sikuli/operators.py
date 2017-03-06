import logging
import time
from sikuli import *

class Operator(object):
    def __init__(self, screen, os):
        self.screen = screen
        self.current_os = os


class VM_operator(Operator):
    def __init__(self, screen, os):
        super(VM_operator, self).__init__(screen, os)
        self.power_dict = {'start': 'b', 'shutdown': 'e', 'restart': 'r'}
        self._ctrl_alt_delete = '1485418324766.png'
        self._snapshot_manager = '1485419294466.png'
        self._take_snapshot = '1486092101031.png'
        self._yes = '1485419325367.png'

    def jump_out(self):
        logging.debug('>> jump_out')
        keyDown(Key.CTRL + Key.ALT)
        keyUp(Key.CTRL + Key.ALT)
        logging.debug('<< jump_out')

    def click_ctrl_alt_delete(self):
        logging.debug('>> click_ctrl_alt_delete')
        self.jump_out()
        self.screen.doubleClick(self._ctrl_alt_delete)
        logging.debug('<< click_ctrl_alt_delete')

    def power_switch(self, status):
        logging.debug('>> click_ctrl_alt_delete, status = %s' % status)
        self.jump_out()
        k = self.power_dict.get(status)
        if k:
            type(k, KEY_CTRL)
        logging.debug('<< click_ctrl_alt_delete')

    def switch_tab(self, tab_id):
        logging.debug('>> switch_tab, tab id = %d' % tab_id)
        self.jump_out()
        type('t', KEY_ALT)
        type(str(tab_id))
        time.sleep(1)
        logging.debug('<< switch_tab')

    def revert_snapshot(self, image, start=False):
        logging.debug('>> revert_snapshot, image = %s' % image)
        self.jump_out()
        self.screen.click(self._snapshot_manager)
        self.screen.doubleClick(image)
        self.screen.click(self._yes)
        if start:
            time.sleep(2)
            self.power_switch('start')
        time.sleep(10)
        self.screen.waitVanish('1486453801844.png')
        logging.debug('<< revert_snapshot')

    def do_snapshot(self, config, build_id=None):
        logging.debug('>> do_snapshot')
        if build_id == None:
            logging.debug('Get newest build id.')
            self.current_os.get_newest_build()
        self.jump_out()
        self.screen.click(self._take_snapshot)
        time.sleep(1)
        if build_id != None:
            logging.debug('Going to type build id: %s' % build_id)
            type(str(build_id))
        else:
            logging.debug('Going to paste build id')
            type('v', KEY_CTRL)
        type(Key.TAB)
        type(str(config) + Key.TAB + Key.ENTER)
        logging.debug('Snapshot done.')
        logging.debug('<< do_snapshot')

    def login(self):
        logging.debug('>> login')
        self.screen.wait(self.current_os.login_ready, 120)
        self.click_ctrl_alt_delete()
        self.screen.click(self.current_os.username_textbox)
        type('P@ssw0rd' + Key.ENTER)
        self.current_os.after_login()
        logging.debug('<< login')


class P4_operator(Operator):
    def __init__(self, screen, os):
        super(P4_operator, self).__init__(screen, os)
        self._p4v_check = '1486105691903.png'
        self._p4v_workspace_loaded = '1486106198699.png'
        self._staf_root = '1486106394863.png'
        self._sync_finish_check = '1486106607452.png'

    def force_sync_latest(self, password):
        logging.debug('>> force_sync_latest, password = %s' % password)
        self.current_os.open_run()
        logging.debug('Start p4v')
        type('p4v' + Key.ENTER)
        self.screen.wait('1486609237112.png', 10)
        type(Key.ENTER)
        time.sleep(1)
        type(password + Key.ENTER)
        self.screen.wait(self._p4v_check, 60)
        logging.debug('Switch workspace.')
        type('c', KEY_ALT)
        type('k')
        self.screen.wait(self._p4v_workspace_loaded, 10)
        type(Key.END + Key.ENTER)
        time.sleep(1)
        self.screen.click(self._staf_root)
        logging.debug('Force get latest rivision.')
        type('a', KEY_ALT)
        type('n')
        time.sleep(1)
        type('f', KEY_ALT)
        time.sleep(1)
        type(Key.ENTER)
        self.screen.wait(self._sync_finish_check, 10)
        self.screen.waitVanish(self._sync_finish_check, 120)
        logging.debug('Sync finished.')
        logging.debug('<< force_sync_latest')


class CM_operator(Operator):
    def __init__(self, screen, config, os):
        super(CM_operator, self).__init__(screen, os)
        self.config = config
        self.activation = {
            'std': 'TM-72JG-LSBBS-4RMHY-NKKTD-WHJVB-MPS4N',
            'adv': 'TM-22DX-VXZK8-AMMZ5-7GU2N-W7QS5-PJMLE'
        }
        self.http_combo_order = {'https only': 2, 'http only': 1, 'http+s': 0}

    def copy_build(self, ftp_config, id=None):
        logging.debug('>> copy_build')
        if id == None:
            logging.debug('id = None, going to get newest build.')            
            self.current_os.get_newest_build(ftp_config)
        self.current_os.open_run()
        type('xcopy \\\\10.201.16.7\\build\\TMCM\\7.0\\win32\\en\\Rel\\')
        if id == None:
            type('v', KEY_CTRL)
        else:
            type(id)
        type(r'\release\output\image\standard_CD\win32\release C:\Users\Administrator\Desktop\release /s/e' + Key.ENTER)
        time.sleep(1)
        type('D')
        time.sleep(1)
        self.screen.waitVanish(self.current_os.build_copied, 90)
        logging.debug('<< copy_build')

    def run_setup(self):
        logging.debug('>> run_setup')
        self.current_os.open_run()
        time.sleep(1)
        type(r'C:\Users\Administrator\Desktop\release\setup.exe' + Key.ENTER)
        logging.debug('<< run_setup')

    def install_requirements(self):
        logging.debug('>> install_requirements')
        while True:
            if self.screen.exists(self.current_os.next):
                logging.debug('find next')
                break
            if self.screen.exists(self.current_os.yes):
                logging.debug('find yes')
                type(Key.ENTER)
                time.sleep(1)
            if self.screen.exists(self.current_os.close):
                logging.debug('find close')
                type(Key.ENTER)
        logging.debug('<< install_requirements')

    def _empty_textbox(self):
        logging.debug('>> _empty_textbox')
        type('a', KEY_CTRL)
        type(Key.BACKSPACE)
        logging.debug('<< _empty_textbox')

    def _run_preprocess(self):
        logging.debug('>> _run_preprocess')
        self.screen.click(self.current_os.next)
        self.screen.click(self.current_os.yes)
        self.screen.wait(self.current_os.next, 10)
        self.screen.click(self.current_os.next)
        logging.debug('Try to find SQL alert.')
        if self.screen.exists(self.current_os.ok):
            logging.debug('Find SQL alert.')
            self.screen.click(self.current_os.ok)
        self.screen.click(self.current_os.next)
        logging.debug('<< _run_preprocess')

    def _enter_activation(self):
        logging.debug('>> _enter_activation')
        logging.debug('License in config: %s' % self.config.get('license'))
        license = self.activation.get(self.config.get('license'))
        logging.debug('License going to type: %s' % license)
        if not license:
            raise CMException('Cannot get license code.')
        type(license)
        self.screen.click(self.current_os.next)
        logging.debug('<< _enter_activation')

    def _after_activation(self):
        logging.debug('>> _after_activation')
        self.screen.click(self.current_os.next)
        self.screen.click(self.current_os.next)
        logging.debug('<< _after_activation')

    def _specify_web_server(self):
        logging.debug('>> _specify_web_server')
        website = self.config.get('website')
        http = self.config.get('http')
        logging.debug('Website: %s, HTTP: %s' % (website, http))
        if website == 'virtual':
            self.screen.click(self.current_os.website_combobox)
            type(Key.DOWN)
        if http != 'http+s':
            self.screen.click(self.current_os.http_combobox)
            for i in range(self.http_combo_order[http]):
                type(Key.UP)
            type(Key.ENTER)
        self.screen.click(self.current_os.next)
        logging.debug('<< _specify_web_server')

    def _after_web_server(self):
        logging.debug('>> _after_web_server')
        time.sleep(1)
        type(Key.ENTER)
        self.screen.click(self.current_os.next)
        logging.debug('<< _after_web_server')

    def _input_db_ip(self, ip):
        logging.debug('>> _input_db_ip, ip = %s' % ip)
        self.screen.click(self.current_os.db_ip_textbox)
        self._empty_textbox()
        type(ip)
        logging.debug('<< _input_db_ip')

    def _setup_account(self, auth, username, password):
        logging.debug('>> _setup_account, auth = %s, username = %s, password = %s' % (auth, username, password))
        if auth == 'win':
            self.screen.click(self.current_os.db_windows_account_radio)
        self.screen.click(self.current_os.db_username)
        self._empty_textbox()
        type(username)
        self.screen.click(self.current_os.db_password)
        type(password)
        logging.debug('<< _setup_account')

    def _input_database_name(self, name):
        logging.debug('>> _input_database_name, name = %s' % name)
        self.screen.click(self.current_os.db_databasename)
        self._empty_textbox()
        type(name)
        logging.debug('<< _input_database_name')

    def _setup_DB_with_cm_package(self, db_setting):
        logging.debug('>> _setup_DB_with_cm_package')
        self.screen.click(self.current_os.db_cm_package_radio)
        logging.debug('<< _setup_DB_with_cm_package')

    def _setup_DB_with_additional_DB(self, db_setting):
        logging.debug('>> _setup_DB_with_additional_DB')
        self.screen.click(self.current_os.db_additional_sql)
        if db_setting.get('db') == 'local':
            self._input_db_ip('(local)')
        else:
            self._input_db_ip(db_setting.get('ip'))
        logging.debug('<< _setup_DB_with_additional_DB')

    def _handle_duplicate_db(self, action):
        logging.debug('>> _handle_duplicate_db, action = %s' % action)
        target = {
            'append': '',
            'delete': self.current_os._delete_existing_db_radio,
            'create': ''
        }.get(action)
        self.screen.click(target)
        type(Key.ENTER)
        logging.debug('<< _handle_duplicate_db')

    def _setup_DB(self):
        logging.debug('>> _setup_DB')
        logging.debug('DB setting is as followed.')
        db_setting = self.config.get('db')
        logging.debug(db_setting)
        {
            'cm package': self._setup_DB_with_cm_package,
            'additional': self._setup_DB_with_additional_DB
        }.get(db_setting.get('from'))(db_setting)
        self._setup_account(
            db_setting.get('auth'),
            db_setting.get('username'),
            db_setting.get('password')
        )
        if db_setting.get('database_name'):
            self._input_database_name(db_setting.get('database_name'))
        self.screen.click(self.current_os.next)
        if self.screen.exists(self.current_os.yes):
            self.screen.click(self.current_os.yes)
        if self.screen.exists(self.current_os.delete_existing_db_radio, 10):
            self._handle_duplicate_db(db_setting.get('db_duplicated'))
        logging.debug('<< _setup_DB')

    def _create_root_account(self):
        root = self.config.get('root')
        logging.debug('>> _create_root_account, root = ')
        logging.debug(root)
        logging.debug('Waiting for creating root account...')
        self.screen.wait(self.current_os.create_root_check, 300)
        logging.debug('Going to create root account.')
        type(root.get('id'))
        type(Key.TAB + Key.TAB)
        type(root.get('password'))
        type(Key.TAB)
        type(root.get('password'))
        self.screen.click(self.current_os.next)
        logging.debug('<< _create_root_account')

    def _finish(self):
        logging.debug('>> _finish')
        logging.debug('Waiting for finish...')
        time.sleep(300)
        self.screen.wait(self.current_os.finish, 600)
        logging.debug('CM installation finished.')
        self.screen.click(self.current_os.show_readme_checkbox)
        self.screen.click(self.current_os.start_console_checkbox)
        self.screen.click(self.current_os.finish)
        logging.debug('<< _finish')

    def install_cm(self):
        logging.debug('>> install_cm')
        self._run_preprocess()
        self._enter_activation()
        self._after_activation()
        self._specify_web_server()
        self._after_web_server()
        self._setup_DB()
        self._create_root_account()
        self._finish()
        logging.debug('<< install_cm')

    def install_build(self):
        logging.debug('>> install_build')
        self.run_setup()
        self.screen.wait(self.current_os.yes, 20)
        self.install_requirements()
        self.install_cm()
        logging.debug('<< install_build')


class CMException(Exception):
    def __init__(self, message):
        self.cause = 'CMException'
        self.message = message
        super(CMException, self).__init__(self.cause, self.message)
