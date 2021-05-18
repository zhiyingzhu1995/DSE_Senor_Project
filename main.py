# main.py

from umqtt.robust import MQTTClient
from machine import Pin, I2C
import utime as time
import gc
import bme280

##def connect_and_subscribe():
##client_id = ubinascii.hexlify(machine.unique_id())
##
###client = MQTTClient(client_id, "192.168.1.3")
###client = MQTTClient("esp32-01", "192.168.1.3")
###client = MQTTClient("esp32-01", "167.71.96.74")
##client = MQTTClient(client_id, "167.71.96.74")
##
##
##
##i2c = I2C(scl=Pin(5), sda=Pin(4), freq = 100000)
##
### this checks if it's connected to the sensor, output:[119]
##device = i2c.scan()
##
##def publish():
##    if len(device) >0:
##        count = 1
##        while count != 5:
##            #pin5.value(0)
##            #checkwifi()
##            # the first index would be your device address
##            bme = bme280.BME280(i2c=i2c, address = device[0])
##            v = bme.values
##            msg = b'{"MsgId":%u,"Mem":%u,"Celsius":%s,"Pressure":%s,"Humidity":%s}' % (count, gc.mem_free(), v[0][:-1], v[1][:-3], v[2][:-1])
##            client.publish(b"home/weather", msg)
##            #pin5.value(1)
##            count = count + 1
##            print(v)
##            print(msg)
##            time.sleep(5)
##    else:
##        print("Device is not found!")
##
##try:
##  client = connect_and_subscribe()
##except OSError as e:
##  restart_and_reconnect()
##
##  
##try:
##    client.connect()
##except OSError as e:
##    print('Failed to connect to MQTT broker. Reconnecting...')
##    time.sleep(3)
##    machine.reset()

# Wifi connect established in the boot.py file. Uncomment if needed
# import network
# sta_if = network.WLAN(network.STA_IF)
# sta_if.active(True)
# sta_if.connect("NCW", "malolos5459")

# client address is '192.168.1.3'
# client id is 'esp32-01'
# pin5 = machine.Pin(5, machine.Pin.OUT)

#client = MQTTClient("esp32-01", "192.168.1.3")

def connect_and_subscribe():
    # MQTT Server IP addresss
    mqtt_server = "167.71.96.74"
    #mqtt_server = "192.168.1.3"

    # To create an MQTT client, we need to get the ESP unique ID
    client_id = ubinascii.hexlify(machine.unique_id())

    # create a MQTT client connection
    client = MQTTClient(client_id, mqtt_server)


    # connect the clients
    client.connect()

    print("Connect to %s MQTT broker"% mqtt_server)
    return client


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(3)
  machine.reset()

  
## Next, write the topic the ESP#1 is subscribed to,
## and the topic it will be publishing messages:
##topic_sub = b'home/weather'


i2c = I2C(scl=Pin(5), sda=Pin(4), freq = 100000)

# this checks if it's connected to the sensor, output:[119]
device = i2c.scan()

def publish():
    if len(device) >0:
        count = 1
        while count != 5:
            #pin5.value(0)
            #checkwifi()
            # the first index would be your device address
            bme = bme280.BME280(i2c=i2c, address = device[0])

            ## Next, write the topic the ESP#1 is subscribed to,
            ## and the topic it will be publishing messages:
            topic_sub = b'home/weather'
            v = bme.values
            msg = b'{"MsgId":%u,"Mem":%u,"Celsius":%s,"Pressure":%s,"Humidity":%s}' % (count, gc.mem_free(), v[0][:-1], v[1][:-3], v[2][:-1])
            client = connect_and_subscribe()
            client.publish(topic_sub, msg)
            #pin5.value(1)
            count = count + 1
            print(v)
            print(msg)
            time.sleep(5)
    else:
        print("Device is not found!")

try:
    client = connect_and_subscribe()
    publish()
except OSError as e:
    restart_and_reconnect()
    
##client.reconnect()
##
##publish()

