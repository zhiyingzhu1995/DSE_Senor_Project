# Configure the main and boot python file

	1. Find the local IP address
		- ```Finding your local IP address is really easy. Head to the Apple menu > System Preferences > Network and then select the connection you are currently using: AirPort (wireless) or Ethernet (wired).```
		- My IP address is `192.16x.x.x`

	2. edit the main.py and boot.py file
		a. use `rsync . /pyboard` to sync the file
		c. type `cat /pyboard/boot.py` to see your python file
		d. use `repl` to put you in a python environment
		b. use ctr D to run your python script

	3. install various programs
	`repl`
	import upip
	upip.install("micropython-bme280")
	upip.install("micropython-umqtt.robust")
	upip.install("micropython-umqtt.simple")

	4. CD to the folder that you want, `cd "new_project"`
		Connect with Device `rshell -e emacs --port [your device location] --baud 115200`
		a. in our case, the command would be `rshell -e emacs --port /dev/tty.usbserial-0001 --baud 115200`



# Configiure MQTT
1. `brew install mosquitto`
2. `nano /usr/local/etc/mosquitto/mosquitto.conf`
	a. add this to the bottom of config
	```listener 1883
	allow_anonymous true```
	b. run the config file
	`/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf`
3. On digital ocean, if you want to publish something
	`mosquitto_pub -h localhost -t "test" -m "hello world" -u "admin" -P "admin"`
4. On DO, if you want to use the influx command
	`influx -username admin -password "admin"`


