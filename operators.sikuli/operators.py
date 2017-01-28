from sikuli import *
import time

class VM_operator:
    def __init__(self, screen, os):
        self.power_dict = {'start': 'b', 'shutdown': 'e', 'restart': 'r'}
        self.screen = screen
        self.current_os = os

    def jump_out(self):
        keyDown(Key.CTRL + Key.ALT)
        keyUp(Key.CTRL + Key.ALT)

    def click_ctrl_alt_delete(self):
        self.jump_out()
        self.screen.doubleClick("1485418324766.png")

    def power_switch(self, status):
        self.jump_out()
        k = self.power_dict.get(status)
        if k:
            type(k, KEY_CTRL)

    def revert_snapshot(self, image):
        self.jump_out()
        self.screen.click("1485419294466.png")
        self.screen.doubleClick(image)
        self.screen.click("1485419325367.png")
        time.sleep(2)
        self.power_switch('start')
        time.sleep(10)

    def login(self):
        self.screen.wait(self.current_os.login_ready, 120)
        self.click_ctrl_alt_delete()
        self.screen.click(self.current_os.username_textbox)
        type('P@ssw0rd' + Key.ENTER)
        self.current_os.after_login()


class CM_operator:
    def __init__(self, screen, config, os):
        self.screen = screen
        self.config = config
        self.current_os = os

    def copy_build(self, id=None):
        if id == None:
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
        self.screen.waitVanish(self.current_os.build_copied 90)

    def open_run(self):
        self.screen.click(self.current_os.start)
        self.screen.click(self.current_os.run)
        time.sleep(1)

    def get_newest_build(self):
        self.open_run()
        type(r'\\10.201.16.7\build\TMCM\7.0\win32\en\Rel' + Key.ENTER)
        self.screen.wait(self.current_os.build_window_ready, 5)
        type(Key.END + Key.UP + Key.F2)
        type('c', KEY_CTRL)
        type(Key.F4, KEY_ALT)

    def run_install(self):
        self.screen.doubleClick()
        time.sleep(1)
        self.screen.doubleClick()

    def install_build(self):
        pass