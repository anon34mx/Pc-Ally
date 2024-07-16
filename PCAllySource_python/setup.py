import pyaimp
import time
import datetime
# Imports PIL module  
from PIL import Image
import json

import serial,time
import serial.tools
import serial.tools.list_ports
ser = None #Serial Port
serial_out_buffer = {} #Serial Port

def millisToTime(time, format):
    minutes=int((time / 1000)/60)
    seconds=int((time / 1000)%60)
    hours=int(minutes/60)
    miliseconds=int(((time / 1000)%60)%1*100)
    if format=="int":
        return hours,minutes,seconds,miliseconds
    else:
        return str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2) #+"."+str(miliseconds).zfill(2)
        

try:
    ser = serial.Serial('COM3', 9600)
    # ser.write(bytearray('S','ascii'))
    # time.sleep(0.1)
    # ser.close()
except serial.SerialException:
    print("crash")
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

            # print('Reproduciendo')
            # print(client.get_current_track_info()['title'])
            # print("Vol.", client.get_volume())
            # print(str(horas).zfill(2), ":", str(minutos).zfill(2) , ":", str(segundos).zfill(2) ) #tiempo progreso
            # print(client.is_shuffled()) #
            # print(client.is_track_repeated()) #
            # print("\n")
            # print(client.pause()) #Pausar
            # print(client.play_pause()) #
            # print(client.prev()) #
            # print(client.set_visualization_fullscreen(1)) #
            # ser.write(bytearray(client.get_current_track_info()['title']+"\n",'utf8'))


            # ser.write(str(client.get_current_track_info()['title']+"\n").encode())
            time.sleep(0.1)
            # ser.close()
            elapsed=millisToTime(client.get_player_position(), "string")
            serial_out_buffer={
                "mode":"music",
                "state":"playig",
                "title":client.get_current_track_info()['title'],
                "time": elapsed,
                "duration":"duration"
            }
            print(serial_out_buffer)
            ser.write(json.dumps(serial_out_buffer).encode())
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