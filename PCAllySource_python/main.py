# https://pypi.org/project/truck-telemetry/
# https://epocdotfr.github.io/pyaimp/
# https://build-system.fman.io/pyqt5-tutorial
# https://github.com/openmv/openmv/blob/master/tools/rpc/rpc_image_transfer_jpg_streaming_as_the_controller_device.py # imagen por conexion serial

import serial,time
import serial.tools
import serial.tools.list_ports
from configparser import ConfigParser
import pyautogui
import json
from datetime import timedelta

config = ConfigParser()
config.read('config.ini')

def crear_configuracion():
    config.add_section('serial')
    config.set('serial', 'puerto', 'NA')
    config.set('serial', 'baudios', '9600')
    with open('config.ini', 'w') as f:
        config.write(f)

def mouse_move(comandos):
    print("X: ", comandos["data"]["X"])
    print("Y: ", comandos["data"]["X"])
    pyautogui.moveRel(comandos["data"]["X"], comandos["data"]["y"])
    
# CREAR CONFIGURACION
if config.has_section('serial') == False:
    crear_configuracion()

if "NA" == config.get('serial', 'puerto'):
    puertos=serial.tools.list_ports.comports()
    for puerto, desc, hwid in sorted(puertos):
        print(puerto)
    config_puerto = input()
    print("Usar")
    print(config_puerto)

    config.set('serial', 'puerto', config_puerto)
    with open('config.ini', 'w') as f:
        config.write(f)

# INICIALIZAR
try:
    dispositivo = serial.Serial(config.get('serial', 'puerto'), config.get('serial', 'baudios'))
except ValueError:
    exit()
comandos={};
# delta = ini_time_for_now = datetime.now()
while 1:
    # delta
    # ini_time_for_now = datetime.now()
    # print(delta, ", ",ini_time_for_now,", ", datetime.timedelta(days=64, seconds=29156, microseconds=10))
    # delta=ini_time_for_now

    #leer
    datos = dispositivo.readline().decode('utf-8').replace("'", '"')
    print(datos)
    try:
        if datos!="":
            comandos=json.loads(datos)
        else:
            comandos=False
        # print(type(comandos))
    except ValueError:
        print("json invalido F")
        print(datos)
        comandos=False
        # exit()

    print(type(comandos), type(comandos) is dict)
    if type(comandos) is dict:
        try:
            # if comandos["method"] == "mouse_move":
            #     print("X: ", comandos["data"]["X"])
            #     print("Y: ", comandos["data"]["X"])
            #     pyautogui.moveRel(comandos["data"]["X"], comandos["data"]["y"])
            # match comandos["method"]:
            #     case "mouse_move":
            #         print("X: ", comandos["data"]["X"])
            #         print("Y: ", comandos["data"]["X"])
            #         pyautogui.moveRel(comandos["data"]["X"], comandos["data"]["y"])
            #         break;
            match comandos["method"]:
                case "mouse_move":
                    mouse_move(comandos)
                    break;
        except ValueError:
            print(datos)
            print("no se pudo imprimir :c")
        
    # if comandos["method"] == "mouse":
    #     print("mover raton")

    #escribir
    # dispositivo.write("test de escritura a serial".encode())
    #no es necesario
    # time.sleep(1)
    
    # pyautogui.click(100, 100)
    # pyautogui.moveTo(100, 150)
    # pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
    # pyautogui.dragTo(100, 150)
    # pyautogui.move(4, 4)  # drag mouse 10 pixels down

