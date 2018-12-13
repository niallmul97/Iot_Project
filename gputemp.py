import socket
import wmi
import time
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
count=0
HOST = '192.168.43.128'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
while 1:
    temperature_infos = w.Sensor()
    output = ''
    for sensor in temperature_infos:
        if sensor.SensorType==u'Temperature' and sensor.name==u'CPU Package':
            output = str(sensor.Value)
            time.sleep(0.5)
    s.sendall(output.encode())
    data = s.recv(1024)
    print(data)
s.close
