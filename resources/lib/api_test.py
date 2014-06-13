import time
import xbmc

from api_interface import *

'''
    Test Code
'''

def nav_unit_test():
    
    time.sleep(1)
    nav_up()
    time.sleep(1)
    nav_up()
    time.sleep(1)
    nav_up()
    time.sleep(1)
    nav_up()
    time.sleep(1)
    nav_down()
    nav_down()
    nav_down()
    nav_down()
    time.sleep(1)
    nav_left()
    time.sleep(1)
    nav_select()
    time.sleep(1)
    nav_back()
    time.sleep(1)
    nav_left()
    nav_left()
    nav_left()
    time.sleep(1)
    nav_right()
    nav_right()
    nav_right()
    nav_right()
    
def playback_unit_test():
    
    #playback_toggle_play()
    playback_status()
    time.sleep(4)
    '''
    playback_vol_inc()
    time.sleep(2)
    playback_vol_inc()
    time.sleep(2)
    playback_vol_inc()
    time.sleep(2)
    playback_vol_dec()
    time.sleep(2)
    playback_vol_dec()
    time.sleep(2)
    playback_vol_dec()
    time.sleep(2)
    '''
