# WIFI Stuff
import network


def init():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('***REMOVED***', '***REMOVED***')
    while wlan.isconnected() == False:
        pass

    print('Connection successful')
    print(wlan.ifconfig())