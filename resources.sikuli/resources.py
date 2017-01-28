from sikuli import *

class Os():
    def __init__(self, screen):
        self.screen = screen
        self._start = ''
        self._run = ''
        self._login_ready = ''
        self._username_textbox = ''
        self._os_ready = ''
        self._build_window_ready = ''
        self._build_copied = ''

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

    def after_login(self):
        pass


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

        self._license_cancel = '1485419515911.png'

        self._server_management_close = '1485419547613.png'

    def after_login(self):
        self.screen.click(self._license_cancel)
        self.screen.wait(self.os_ready, 10)
        self.screen.click(self._server_management_close)


class Windows2012(Os):
    def __init__(self):
        super(Windows2012, self).__init__()