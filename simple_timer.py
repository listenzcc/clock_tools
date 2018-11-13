# coding: utf-8

import time
import threading


class simple_timer:
    # A simple timer tool
    def __init__(self):
        self.begin = time.time()
        self.threads = []

    def status(self):
        print('[Timer status]')
        print('\tBegin at ' + time.ctime(self.begin))
        self.refresh_threads()
        print('\t%d alarms forward' % len(self.threads))
        self.click()

    def refresh_threads(self):
        self.threads = list(e for e in self.threads if e.is_alive())

    def refresh(self):
        self.refresh_threads()
        self.begin = time.time()

    def start(self):
        self.refresh()

    def alarm_after(self, delay, todo='Something'):
        t = threading.Thread(
            target=self.alarm_after_thread, args=(delay, todo))
        self.threads.append(t)
        t.start()

    def alarm_after_thread(self, delay, todo):
        time.sleep(delay)
        print('[Timer alarm]')
        print('\t%d seconds passed, %s'
              % (delay, todo))

    def click(self, message='passed.'):
        print('[Timer click]')
        print('\t%0.2f seconds %s' % (time.time() - self.begin, message))
