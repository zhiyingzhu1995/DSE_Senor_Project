# boot.py

# There are two files that are treated specially by the ESP8266 when it starts up:
# boot.py and main.py.
# The boot.py script is executed first then the main.py script is executed.


# creating wifi interfaces
import esp
import network
import machine
import ubinascii

esp.osdebug(None)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)


ssid = 'wifi_name'
wifi_pwd = 'wifi_password'



# check if board the connect to wifi
if sta_if.isconnected() is False:
    try:
        sta_if.connect(ssid, wifi_pwd)
        print("Connected connection")
    except:
        print("Board is not connected to the internet")
else:
    print("Connect is already established")


        
