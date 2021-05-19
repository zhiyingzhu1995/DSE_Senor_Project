# Setup MQTT Communication - MAC Instruction

## MQTT Broker - Eclipse Mosquitto
1. [Install Reference](https://mosquitto.org/download/)
	- using brew: `brew install mosquitto`

2. Set password for broker
	- `mosquitto_passwd -c password_filename username`

3. Start MQTT Broker to listen for client
	- `/usr/local/sbin/mosquitto -v`
	- will be different if in Window system

4. Note
	- mosquitto 2.0 may block the non localhost connection
	- To allow it connect with local ip address, add below two line in the `mosquitto.conf` file
		```
		listener 1883
		allow_anonymous true
		```
	- Then start using
		`/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf`

## MQTT Client - Device
- Package Need:
```
import upip

# install package for mqtt
upip.install('micropython-umqtt.robust')
upip.install('micropython-umqtt.simple')
```

# Install MQTT on the cloud
reference:
[MQTT installation]
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-debian-10
[MQTT open port and start listening]
https://www.digitalocean.com/community/questions/how-to-setup-a-mosquitto-mqtt-server-and-receive-data-from-owntracks
**Dont bother with users and password setup**


## Setting up MQTT Broker on this VM Machine
	1.Type the following on the DO terminal
	```
	sudo apt update
	sudo apt install mosquitto mosquitto-clients
	mosquitto_sub -h localhost -t test (in one terminal)
	mosquitto_pub -h localhost -t test -m "hello world" (in a second terminal)
	sudo systemctl restart mosquitto
	```
	
	2. then set up the port 1883 for listening, type this in the terminal
	
	```
	editor /etc/mosquitto/conf.d/default.conf
	```

	3. add this to your config file
	```
		listener 1883 <yourIP>
		persistence true
		persistence_location /var/lib/mosquitto/
		persistence_file mosquitto.db
		log_dest syslog
		log_dest stdout
		log_dest topic
		log_type error
		log_type warning
		log_type notice
		log_type information
		connection_messages true
		log_timestamp true
		allow_anonymous true
	```

	4. then type this
	```
	/sbin/ldconfig

	mosquitto -c /etc/mosquitto/conf.d/default.conf
	```

	5. in a different window, type this
	`mosquitto_sub -h <yourIP address> -p 1883 -v -t 'home'`
	in our case is `mosquitto_sub -h 167.71.96.74 -p 1883 -v -t 'home'`

	6. paste this in your init file
	```
	vim /etc/init/mosquitto.conf

	#THEN PASTE IN:

	description "Mosquitto MQTT broker"
	start on net-device-up
	respawn
	exec /usr/sbin/mosquitto -c /etc/mosquitto/conf.d/default.conf
	```

	7. Start listening (If you want to start listening, use this)
	`mosquitto -c /etc/mosquitto/conf.d/default.conf`

	8. If you are using Uncomplicated Firewall, configure it to allow connections to port8888:
	```sudo ufw allow 8888/tcp```



## Make influxdb suscribe to the MQTT broker
resource: 
[making influxdb subscribe to MQTT]
https://www.hackster.io/nacktnasenwombat/temperature-humidity-measurement-with-nodemcu-191c46

	1. Create a new databases in influx
		```
		influx -username 'admin' -password 'admin'
		CREATE DATABASE rooms
		```
	2. Edit the influxdb configuration file
		```sudo nano /etc/influxdb/influxdb.conf```

	3. Delete the "#" before
		```
		[http]
		 # Determines whether HTTP endpoint is enabled.
		  enabled = true
		 # The bind address used by the HTTP service.
		  bind-address = ":8086"
		 # Determines whether user authentication is enabled over HTTP/HTTPS.
		  auth-enabled = true
		```
	4. after that you have to restart the service:
		```sudo systemctl restart influxdb```
	5. Edit Telegraf configuration file
		```
		sudo nano /etc/telegraf/telegraf.conf
		```
		```
		omit_hostname = true
		[[outputs.influxdb]]
		 ## The target database for metrics; will be created as needed.
		  database = "telegraf"
		# we create a seperate database for our measurements, so we don't want the 
		#  data in the telegraf-database
		  namedrop = ["sensors*"]
		 ## HTTP Basic Auth
		  username = "admin"
		  password = "password"
		```
	6. Now the configuration file for our data:
		```
		sudo nano /etc/telegraf/telegraf.d/sensors.conf
		```
		```
		# Input data as json-String
		[[inputs.mqtt_consumer]]
		 servers = ["tcp://localhost:1883"]
		 topics = [
		   "sensors/#",
		 ]
		 client_id = "telegraf"
		 data_format = "json"
		 name_prefix = "sensors_"
		 json_name_key = "location"
		 tag_keys = ["temperature","humidity"]
		 json_string_fields = ["location"]
		# Output for influxdb
		[[outputs.influxdb]]
		 urls = ["http://127.0.0.1:8086"]
		 username = "admin"
		 password = "password"
		 database = "rooms"
		 namepass = ["sensors*"]
		```

