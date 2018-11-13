# coding: utf-8

from simple_timer import simple_timer
import time

if __name__ == '__main__':
    print('hello world')
    st = simple_timer()
    st.status()
    st.alarm_after(2, '2 seconds alarm')
    st.alarm_after(5, '5 seconds alarm')
    time.sleep(3)
    st.status()
