import pyaimp
import time
# Imports PIL module  
from PIL import Image 

try:
    client = pyaimp.Client()

    while True:
        state = client.get_playback_state()

        if state == pyaimp.PlayBackState.Stopped:
            print('Detenido')
        elif state == pyaimp.PlayBackState.Paused:
            print('Pausado')
        elif state == pyaimp.PlayBackState.Playing:
            print('Reproduciendo')
            print(client.get_current_track_info())
            print(client.get_volume())
            print(client.get_player_position()) #tiempo progreso
            print(client.is_shuffled()) #
            print(client.is_track_repeated()) #
            # print(client.pause()) #Pausar
            # print(client.play_pause()) #
            # print(client.prev()) #
            # print(client.set_visualization_fullscreen(1)) #
        try:
            albumArt = "C:\\Users\\aaron\\Music\\Miguel Bosé\\2007 - Papito\\Papito [Disc 2]\\Folder.jpg"
            # im = Image.open(albumArt)
            im = Image.open(albumArt)
            # im = im.resize(50,50)
            im.thumbnail((50, 50))
            # im.show()
            # print(bytearray(im[0,0]))
        except ValueError:
            print("no imagen")
        time.sleep(1)
    print("terminado")

except RuntimeError as re: # AIMP instance not found
    print(re)
except Exception as e:
    print(e)