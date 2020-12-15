import pygetwindow as gw
import time

INTERRUPT_TIMEOUT = 3     # The Twitter window will close after this time(min) 

cnt = 0
while True:
    time.sleep(1)
    if 'Twitter' in gw.getAllTitles():
        cnt += 1
    else:
        cnt = 0
    if cnt == INTERRUPT_TIMEOUT*60:
        try:
            cnt = 0
            target  = gw.getWindowsWithTitle('Twitter')[0]
            target.close()
        except Exception as e:
            print(e)
        