import time
import json
import xbmc
import xbmcaddon

from resources.lib.api_interface import *
from resources.lib.api_test import *
from resources.lib.gui_interface import *

def notify_start():
    __addon__       = xbmcaddon.Addon()
    __addonname__   = __addon__.getAddonInfo('name')
    __icon__        = __addon__.getAddonInfo('icon')
    
    line1 = "Touchscreen handler is activated."
    time_delay = 5000  #in miliseconds
    
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time_delay, __icon__))

 

    
#Add-on Execution Starts
notify_start()   
start_gui()

while (not xbmc.abortRequested):
    update_gui()

#pygame.event.Event(QUIT)

#    playback_unit_test()

    '''
    result = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Application.SetMute", "params": { "mute": "toggle" }, "id": 1}')
    time.sleep(2)
    result = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Application.SetMute", "params": { "mute": "toggle" }, "id": 1}')
    time.sleep(2)
    '''
    
