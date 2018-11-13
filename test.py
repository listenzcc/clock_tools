# coding: utf-8

from simple_timer import simple_timer
import time

if __name__ == '__main__':
    print('hello world')
    st = simple_timer('Tim')
    st1 = simple_timer('AA')
    st.status()
    st.alarm_after(2, '2 seconds alarm')
    st1.alarm_after(10, '10 seconds alarm')
    st1.status()
    st.alarm_after(5, '5 seconds alarm')
    time.sleep(3)
    st.status()

    time.sleep(10)
    print('renew')
    st.total()
    st.click()
    time.sleep(1)
    st.total()
    st.click()
