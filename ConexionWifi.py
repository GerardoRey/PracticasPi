import time
import network

ssid = 'nombre de la red'
password = 'clave'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

max_wait = 10

while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print("waiting for connection")
    time.sleep(1)
    
if wlan.status()!= 3:
    raise RuntimeError('Network connnection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print(' ip = ' + status[0])
