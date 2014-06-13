import time
import xbmc
import xbmcaddon

'''
    Navigation Functions
    - Up, Down, Left and Right for basic navigation
    - Select to enter an element
    - Back to return to previous level
    - 
'''

def nav_up():
    request = '{"jsonrpc": "2.0", "method": "Input.Up", "params": { }, "id": 1}'
    xbmc.executeJSONRPC(request)

def nav_down():
    request = '{"jsonrpc": "2.0", "method": "Input.Down", "params": { }, "id": 1}'
    xbmc.executeJSONRPC(request)

def nav_left():
    request = '{"jsonrpc": "2.0", "method": "Input.Left", "params": { }, "id": 1}'
    xbmc.executeJSONRPC(request)

def nav_right():
    request = '{"jsonrpc": "2.0", "method": "Input.Right", "params": { }, "id": 1}'
    xbmc.executeJSONRPC(request)

def nav_select():
    request = '{"jsonrpc": "2.0", "method": "Input.Select", "params": { }, "id": 1}'
    xbmc.executeJSONRPC(request)

def nav_back():
    request = '{"jsonrpc": "2.0", "method": "Input.Back", "params": { }, "id": 1}'
    xbmc.executeJSONRPC(request)
 
def notify_start():
    __addon__       = xbmcaddon.Addon()
    __addonname__   = __addon__.getAddonInfo('name')
    __icon__        = __addon__.getAddonInfo('icon')
    
    line1 = "Touchscreen handler is activated."
    time_delay = 5000  #in miliseconds
    
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time_delay, __icon__))
 

notify_start()   
#while (not xbmc.abortRequested):
    '''
    result = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Application.SetMute", "params": { "mute": "toggle" }, "id": 1}')
    time.sleep(2)
    result = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Application.SetMute", "params": { "mute": "toggle" }, "id": 1}')
    time.sleep(2)
    '''
    '''Testing
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
    '''
    
