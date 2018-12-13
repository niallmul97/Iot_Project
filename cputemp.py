import wmi
import time
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
while 1:
 temperature_infos = w.Sensor()
 for sensor in temperature_infos:
     if sensor.SensorType==u'Temperature' and sensor.name==u'CPU Package':
         print(sensor.Name)
         print(sensor.Value)
         time.sleep(0.5)
