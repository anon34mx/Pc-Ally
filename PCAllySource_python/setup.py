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
            minutos=int((client.get_player_position() / 1000)/60)
            segundos=int((client.get_player_position() / 1000)%60)
            horas=int(minutos/60)
            # milisegundos=((client.get_player_position() / 1000)%60)%1

            print('Reproduciendo')
            print(client.get_current_track_info()['title'])
            print("Vol.", client.get_volume())
            print(str(horas).zfill(2), ":", str(minutos).zfill(2) , ":", str(segundos).zfill(2) ) #tiempo progreso
            print(client.is_shuffled()) #
            print(client.is_track_repeated()) #
            print("\n")
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