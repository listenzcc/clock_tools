# coding: utf-8

import time
import threading


class simple_timer:
    # A simple timer tool
    def __init__(self, name='Timer'):
        # happy birthday
        self.begin = time.time()
        self.lastclick = time.time()
        # name myself
        self.name = name
        # set empty threads for alarmers
        self.threads = []

    def status(self):
        # print status of self
        print('[%s status]' % self.name)
        print('\tBegin at ' + time.ctime(self.begin))
        self.refresh_threads()
        print('\t%d alarms forward' % len(self.threads))
        self.click()

    def refresh_threads(self):
        # refresh threads, discharging outdate alamer
        self.threads = list(e for e in self.threads if e.is_alive())

    def refresh(self):
        # refresh threads and reset birthday
        self.refresh_threads()
        self.begin = time.time()
        self.lastclick = time.time()

    def start(self):
        # false start function ^_^
        self.refresh()

    def alarm_after(self, delay, todo='Something'):
        # setup an alarmer
        t = threading.Thread(
            target=self.alarm_after_thread, args=(delay, todo))
        # stack into threads
        self.threads.append(t)
        # running as new threading
        t.start()

    def alarm_after_thread(self, delay, todo):
        # alarmer function, delay and report
        time.sleep(delay)
        print('[%s alarm]' % self.name)
        print('\t%d seconds passed, %s'
              % (delay, todo))

    def click(self, message='passed.'):
        # report time passed from lastclick
        print('[%s click]' % self.name)
        print('\t%0.2f seconds %s' % (time.time() - self.lastclick, message))
        # refresh lastclick
        self.lastclick = time.time()

    def total(self, message='passed.'):
        # report total time passed
        print('[%s total]' % self.name)
        print('\t%0.2f seconds %s' % (time.time() - self.begin, message))
