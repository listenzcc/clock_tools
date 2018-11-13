# coding: utf-8

import time


class simple_timer:
    def __init__(self):
        self.begin = time.time()
        self.timing = False

    def start(self):
        self.begin = time.time()
        self.timing = True

    def restart(self):
        self.start()

    def click(self):
        print(time.time() - self.begin)

    def stop(self):
        self.click()
        self.timing = False
