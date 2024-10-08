import clr  # package pythonnet, not clr

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


def initialize_openhardwaremonitor():
    file = "C:\\Users\\aaron\\Documents\\github\\Pc-Ally\\PCAllySource_python\\OpenHardwareMonitor\\OpenHardwareMonitorLib.dll"

    clr.AddReference(file)

    from OpenHardwareMonitor import Hardware

    handle = Hardware.Computer()
    handle.MainboardEnabled = True
    handle.CPUEnabled = True
    handle.RAMEnabled = True
    handle.GPUEnabled = True
    handle.HDDEnabled = True

    handle.Open()
    return handle


def fetch_stats(handle):
    for i in handle.Hardware:
        i.Update()
        for sensor in i.Sensors:
            parse_sensor(sensor)

        for j in i.SubHardware:
            j.Update()
            for subsensor in j.Sensors:
                parse_sensor(subsensor)


def parse_sensor(sensor):
    hardwaretypes = {}
    # hardwaretypes = openhardwaremonitor_hwtypes

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


if __name__ == "__main__":
    print("OpenHardwareMonitor:")
    HardwareHandle = initialize_openhardwaremonitor()
    fetch_stats(HardwareHandle)