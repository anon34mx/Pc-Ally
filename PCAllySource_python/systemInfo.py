# https://stackoverflow.com/questions/62617789/get-cpu-and-gpu-temp-using-python-windows
# https://stackoverflow.com/questions/252417/how-can-i-use-a-dll-file-from-python
import clr # the pythonnet module.
clr.AddReference(r'C:\\Users\\aaron\\Downloads\\gabotonera\\OpenHardwareMonitor\\OpenHardwareMonitorLib.dll') 
# e.g. clr.AddReference(r'OpenHardwareMonitor/OpenHardwareMonitorLib'), without .dll

from OpenHardwareMonitor.Hardware import Computer

c = Computer()
c.CPUEnabled = True # get the Info about CPU
c.Open()


print(c.Hardware[0].Sensors[0].Identifier)
print(len(c.Hardware[0].Sensors[1].get_Value()))


# while True:
#     for a in range(0, len(c.Hardware[0].Sensors)):
#         # print(c.Hardware[0].Sensors[a].Identifier)
#         if "/temperature" in str(c.Hardware[0].Sensors[a].Identifier):
#             print(c.Hardware[0].Sensors[a].get_Value())
#             c.Hardware[0].Update()