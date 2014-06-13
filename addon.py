import time
import json
import xbmc
import xbmcaddon

'''
    Navigation Functions
    - Up, Down, Left and Right for basic navigation
    - Select to enter an element
    - Back to return to previous level
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

'''
    Playback Functions
    - Play/Pause
    - Volume Control
'''

def playback_vol_inc():
#    request = '{"jsonrpc": "2.0", "method": "Application.GetProperties", "params": { "properties" : [
#    "volume", 
#    "muted", 
#    "name", 
#    "version"
#  ] }, "id": 1}'
#    volume = xbmc.executeJSONRPC(request)
#    print(volume)
#    volume = int(volume) + 5
    request = '{"jsonrpc": "2.0", "method": "Application.SetVolume", "params": { "volume" : "increment" }, "id": 1}'
    xbmc.executeJSONRPC(request)

def playback_vol_dec():
    request = '{"jsonrpc": "2.0", "method": "Application.SetVolume", "params": { "volume" : "decrement" }, "id": 1}'
    xbmc.executeJSONRPC(request)

def playback_find_player():
    request = '{"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}'
    player_list = xbmc.executeJSONRPC(request)
    print(player_list)
    try :
        player_id = json.JSONDecoder().decode(player_list)['result'][0]['playerid']
        return player_id
    except IndexError:
        print("No players active")
        return


def playback_toggle_play(): 
    player_id = playback_find_player()
    if player_id == None : return
    request = '{"jsonrpc": "2.0", "method": "Player.PlayPause", "params": { "playerid": ' + str(player_id) + ' } , "id": 1}'
    xbmc.executeJSONRPC(request)

def playback_status():
    player_id = playback_find_player()
    if player_id == None : return
    request = '{"jsonrpc": "2.0", "method": "Player.GetItem", "params": { "properties": ["title", "album", "artist", "duration", "thumbnail", "file", "fanart", "streamdetails"], "playerid":' + str(player_id) +  ' }, "id": "AudioGetItem"}'
    current = xbmc.executeJSONRPC(request)
    title = json.JSONDecoder().decode(current)['result']['item']['title']
    #print title
    return title
    



def notify_start():
    __addon__       = xbmcaddon.Addon()
    __addonname__   = __addon__.getAddonInfo('name')
    __icon__        = __addon__.getAddonInfo('icon')
    
    line1 = "Touchscreen handler is activated."
    time_delay = 5000  #in miliseconds
    
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time_delay, __icon__))
 
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

    
#Add-on Execution Starts
notify_start()   

while (not xbmc.abortRequested):
    playback_unit_test()

    '''
    result = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Application.SetMute", "params": { "mute": "toggle" }, "id": 1}')
    time.sleep(2)
    result = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Application.SetMute", "params": { "mute": "toggle" }, "id": 1}')
    time.sleep(2)
    '''
    
