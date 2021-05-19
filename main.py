# main.py

from umqtt.robust import MQTTClient
from machine import Pin, I2C
import utime as time
import gc
import bme280


def connect_and_subscribe():
    
    # MQTT Server IP addresss on Digital Ocean
    mqtt_server = "167.71.96.74"
    

    # To create an MQTT client, we need to get the ESP unique ID
    LOCATION = "home"
    
    # create a MQTT client connection
    client = MQTTClient("umqtt_client_"+LOCATION, mqtt_server)


    # connect the clients
    client.connect()

    print("Connect to %s MQTT broker"% mqtt_server)
    return client


def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(3)
  machine.reset()

  

def publish():
    if len(device) >0:
        connOk = True if len(device) >0 else False

        # while the connection is there, keep sending data
        while connOk == True:
            try: 
                # the first index would be your device address
                bme = bme280.BME280(i2c=i2c, address = device[0])
                v = bme.values
                memory = str(gc.mem_free()) # need to convert "memoory to string order to turn into 'byte' format
                temperature = v[0][:-1]
                humidity = v[2][:-1]
                pressure = v[1][:-3]

                
                # create a topic that you can subscrib to
                LOCATION = "living_room"
                MQTT_TOPIC = "sensors/"+LOCATION

                # create a message in json format
                msg = b'{"location":"' + LOCATION + '","temperature(C)":' + temperature + ',"humidity (%)":' + humidity + ',"memory":' + memory + ',"pressure (hPa)":' + pressure + '}'
                client = connect_and_subscribe()
                client.publish(b""+MQTT_TOPIC, msg)
                print(v)
                print(msg)
            except:
                connOK = False

            # sends data at every 5 second
            time.sleep(5)
                
    else:
        print("Device is not found!")



# This does the I2C scan
i2c = I2C(scl=Pin(5), sda=Pin(4), freq = 100000)

# this checks if it's connected to the sensor, output:[119]
device = i2c.scan()



try:
    client = connect_and_subscribe()
    publish()
except OSError as e:
    restart_and_reconnect()
  


