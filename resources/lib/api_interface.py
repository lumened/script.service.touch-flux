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
   
