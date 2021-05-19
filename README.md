# DSE_Senor_Project - Internet of Things (IoT)


 
## Aim
- Build a system to monitor and visualize temperature, humidity, and pressure collected from the BME280 sensor

## Hardware
- BME280 sensor, to collect temperature, humidity, and pressure. [here is the amazon link](https://www.amazon.com/gp/product/B07P4CWGGK/ref=ox_sc_saved_title_2?smid=AA80HCB088OD&psc=1)
- ESP8266, to connect with the sensor and send data over WiFi through micropython. [here is the amazon link](https://www.amazon.com/gp/product/B07PR9T5R5/ref=ox_sc_saved_title_4?smid=A2K4DGCC72N9AG&psc=1)



## Software
- MQTT
- Digital Ocean

## Brief Set-up Process

### 1. Create an account on Digital Ocean (DO)

  1a. Set up a Docker droplet on DO
  
  1b. Generate SSH keys to access the droplet
  
### 2. Install Influxdb, Telegraf, Kapacitor, Chronograf on droplet

  2a. create users
  
  2b. create database
  
### 3. Install Grafanaon droplet

  3a. Connect Grafana to database of interest
  
  3b. Creating Dashboard in Grafana
  
### 4. Install MQTT broker on droplet

  4a. Configure the MQTT port and start listening
  
  4b. Configure the Influxdb to subscribe to MQTT
  
### 5. Connect the ESP8266 to BME280 Sensor
  5a. Configure boot.py file to connect to wifi
  
  5b. Configure main.py file to publish the collected data to MQTT
  
  
## Final Output
- When bme280 is already connected to ESP8266 and data are being published to the cloud MQTT ![](image/locally%20publishing%20data%20to%20Cloud%20MQTT%20Broker.png)

- When the Cloud MQTT starts to receive data,![](image/Cloud%20MQTT%20Receiving%20Data.png)

- Grafana UI starts monitoring telegraf metrics![](image/grafana%20monitoring%20telegraf%20metrics.jpg)

- Grafana UI starts monitoring sensor metrics ![](image/grafana%20monitoring%20sensor%20metrics.jpg)
