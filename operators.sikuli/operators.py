import logging
import time
from sikuli import *

class VM_operator(object):
    def __init__(self, screen, os):
        self.power_dict = {'start': 'b', 'shutdown': 'e', 'restart': 'r'}
        self.screen = screen
        self.current_os = os

    def jump_out(self):
        logging.debug('>> jump_out')
        keyDown(Key.CTRL + Key.ALT)
        keyUp(Key.CTRL + Key.ALT)
        logging.debug('<< jump_out')

    def click_ctrl_alt_delete(self):
        logging.debug('>> click_ctrl_alt_delete')
        self.jump_out()
        self.screen.doubleClick("1485418324766.png")
        logging.debug('<< click_ctrl_alt_delete')

    def power_switch(self, status):
        logging.debug('>> click_ctrl_alt_delete, status = %s' % status)
        self.jump_out()
        k = self.power_dict.get(status)
        if k:
            type(k, KEY_CTRL)
        logging.debug('<< click_ctrl_alt_delete')

    def revert_snapshot(self, image):
        logging.debug('>> revert_snapshot, image = %s' % image)
        self.jump_out()
        self.screen.click("1485419294466.png")
        self.screen.doubleClick(image)
        self.screen.click("1485419325367.png")
        time.sleep(2)
        self.power_switch('start')
        time.sleep(10)
        logging.debug('<< revert_snapshot')

    def login(self):
        logging.debug('>> login')
        self.screen.wait(self.current_os.login_ready, 120)
        self.click_ctrl_alt_delete()
        self.screen.click(self.current_os.username_textbox)
        type('P@ssw0rd' + Key.ENTER)
        self.current_os.after_login()
        logging.debug('<< login')


class CM_operator(object):
    def __init__(self, screen, config, os):
        self.screen = screen
        self.config = config
        self.current_os = os

    def copy_build(self, id=None):
        logging.debug('>> copy_build')
        if id == None:
            logging.debug('id = None, going to get newest build.')            
            self.get_newest_build()
        self.open_run()
        type('cmd' + Key.ENTER)
        type(r'mkdir C:\Users\Administrator\Desktop\release' + Key.ENTER)
        type('exit' + Key.ENTER)
        
        self.open_run()
        type('xcopy \\\\10.201.16.7\\build\\TMCM\\7.0\\win32\\en\\Rel\\')
        if id == None:
            type('v', KEY_CTRL)
        else:
            type(id)
        type(r'\release\output\image\standard_CD\win32\release C:\Users\Administrator\Desktop\release /s/e' + Key.ENTER)
        time.sleep(1)
        self.screen.waitVanish(self.current_os.build_copied, 90)
        logging.debug('<< copy_build')

    def open_run(self):
        logging.debug('>> open_run')
        self.screen.click(self.current_os.start)
        self.screen.click(self.current_os.run)
        time.sleep(1)
        logging.debug('<< open_run')

    def get_newest_build(self):
        logging.debug('>> get_newest_build')
        self.open_run()
        type(r'\\10.201.16.7\build\TMCM\7.0\win32\en\Rel' + Key.ENTER)
        self.screen.wait(self.current_os.build_window_ready, 5)
        type(Key.END + Key.UP + Key.F2)
        type('c', KEY_CTRL)
        type(Key.F4, KEY_ALT)
        logging.debug('<< get_newest_build')

    def run_setup(self):
        logging.debug('>> run_setup')
        self.open_run()
        time.sleep(1)
        type(r'C:\Users\Administrator\Desktop\release\setup.exe' + Key.ENTER)
        logging.debug('<< run_setup')

    def install_requirements(self):
        logging.debug('>> install_requirements')
        while True:
            if self.screen.exists(self.current_os.next):
                logging.debug('find next')
                print 'find next'
                break
            if self.screen.exists(self.current_os.yes):
                logging.debug('find yes')
                print 'find yes'
                type(Key.ENTER)
                time.sleep(1)
            if self.screen.exists(self.current_os.close):
                logging.debug('find close')
                print 'find close'
                type(Key.ENTER)
        logging.debug('<< install_requirements')

    def install_build(self):
        logging.debug('>> install_build')
        self.run_setup()
        self.screen.wait(self.current_os.yes, 10)
        self.install_requirements()
        logging.debug('<< install_build')

