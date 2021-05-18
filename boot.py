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


ssid = 'NETGEAR75'
wifi_pwd = 'orangepiano456'

# Next, write the topic the ESP#1 is subscribed to,
# and the topic it will be publishing messages:
topic_sub = b'home/weather'

# To create an MQTT client, we need to get the ESP unique ID
client_id = ubinascii.hexlify(machine.unique_id())

# check if board the connect to wifi
if sta_if.isconnected() is False:
    try:
        sta_if.connect(ssid, wifi_pwd)
        print("Connected connection")
    except:
        print("Board is not connected to the internet")
else:
    print("Connect is already established")


        
