# https://stackoverflow.com/questions/62617789/get-cpu-and-gpu-temp-using-python-windows
# https://stackoverflow.com/questions/252417/how-can-i-use-a-dll-file-from-python

# https://www.delftstack.com/howto/python/python-get-cpu-temperature/
import time
import clr # the pythonnet module.
clr.AddReference(r'C:\\Users\\aaron\\Documents\\github\\Pc-Ally\\PCAllySource_python\\OpenHardwareMonitor\\OpenHardwareMonitorLib.dll') 
clr.AddReference(r'C:\\Users\\aaron\\Documents\\github\\Pc-Ally\\PCAllySource_python\\CPUThermometer\\CPUThermometerLib.dll') 
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.GPUEnabled = True # get the Info about CPU
c.Open()

openhardwaremonitor_sensortypes = [
    "Voltage",
    "Clock",
    "Temperature",
    "Load",
    "Fan",
    "Flow",
    "Control",
    "Level",
    "Factor",
    "Power",
    "Data",
    "SmallData",
]
# while True:
#     for a in range(0, len(c.Hardware[0].Sensors)):
#         print(c.Hardware[0].Sensors[a].Identifier)
#         if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
#             print(c.Hardware[0].Sensors[a].get_Value())
#             c.Hardware[0].Update()

# while True:
#     for a in range(0, len(c.Hardware[0].Sensors)):
#         print("_________", a)
#         print(c.Hardware[0].Sensors[a].Name)
#         print(c.Hardware[0].Sensors[a].Identifier)
#         print(c.Hardware[0].Sensors[a].SensorType)
#         print(c.Hardware[0].Sensors[a].Value)
#         c.Hardware[0].Update()
#         print("_________")
#         # if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
#             # print(c.Hardware[0].Sensors[a].get_Value())
#             # c.Hardware[0].Update()
#     time.sleep(1)
# print(c.Hardware[0].Sensors[0].Identifier)
# print(c.Hardware[0].Sensors[1].SensorType)
def parse_sensor(sensor):
    hardwaretypes = openhardwaremonitor_hwtypes

    if sensor.Value is not None:
        if str(sensor.SensorType) == "Temperature":
            print(
                u"%s %s Temperature Sensor #%i %s - %s\u00B0C"
                % (
                    hardwaretypes[sensor.Hardware.HardwareType],
                    sensor.Hardware.Name,
                    sensor.Index,
                    sensor.Name,
                    sensor.Value,
                )
            )
for i in c.Hardware:
        i.Update()
        for sensor in i.Sensors:
            parse_sensor(sensor)

        for j in i.SubHardware:
            j.Update()
            for subsensor in j.Sensors:
                parse_sensor(subsensor)

