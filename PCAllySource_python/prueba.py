import serial,time
import serial.tools
import serial.tools.list_ports
from configparser import ConfigParser
import pyautogui
import json
from datetime import datetime,timedelta

config = ConfigParser()
config.read('config.ini')

# CREAR CONFIGURACION
if config.has_section('serial') == False:
    config.add_section('serial')
    config.set('serial', 'puerto', 'NA')
    config.set('serial', 'baudios', '9600')
    with open('config.ini', 'w') as f:
        config.write(f)

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
dispositivo = serial.Serial(config.get('serial', 'puerto'), config.get('serial', 'baudios'))
# comandos="";
while 1:
    #leer
    datos = dispositivo.readline().decode('utf-8').replace("'", '"')
    print(datos)
    comandos=json.loads('{"method":"mousepad","data":{"x":-24.20,"y":-0.00}}')
    #escribir
    dispositivo.write("test de escritura a serial".encode())
    #no es necesario
    # time.sleep(1)
    
    # pyautogui.click(100, 100)
    # pyautogui.moveTo(100, 150)
    # pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
    # pyautogui.dragTo(100, 150)
    print(datetime.timedelta)
    pyautogui.move(4, 4)  # drag mouse 10 pixels down