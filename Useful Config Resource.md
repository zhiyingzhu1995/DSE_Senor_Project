# Resources

## Generate SSH on Mac and Digital Ocean
- [how to generate SSH key](https://www.youtube.com/watch?v=ncua01HTxis)

- [How to enable password authentication for SSH server](https://phoenixnap.com/kb/ssh-permission-denied-publickey)

- [How to add a user with SSH Access on Ubuntu](https://www.youtube.com/watch?v=COp6JtP45o8)
	

## Install Influxdb, telegraf, Kapacitor, Chronograf
- [how to install Influxdb, telegraf, Kapacitor, Chronograf](https://www.digitalocean.com/community/tutorials/how-to-monitor-system-metrics-with-the-tick-stack-on-ubuntu-16-04)
- if you see the error below, check out solution in [here](https://itsfoss.com/could-not-get-lock-error/)
```root@TestVersion:~# sudo apt-get install influxdb
E: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 4509 (unattended-upgr)
N: Be aware that removing the lock file is not a solution and may break your system.
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?
```
	
## Grafana installation
- [Install Grafana](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-grafana-on-ubuntu-18-04)

## Grafana linkage to Database
- [Connect Grafana with database](https://www.youtube.com/watch?v=pE7zU4MOqC8) 
- follow 20:15 onward

## Developing visualization dashboard in Grafana
- [Creating Dashboard in Grafana](https://www.youtube.com/watch?v=7kfgTtQzSG0)

## MQTT Broker Installation 
- [MQTT installation](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-debian-10)

## MQTT Broker Listening
- [MQTT open port and start listening](https://www.digitalocean.com/community/questions/how-to-setup-a-mosquitto-mqtt-server-and-receive-data-from-owntracks)

## Connecting influxdb to MQTT
- [Making influxdb subscribe to MQTT](https://www.hackster.io/nacktnasenwombat/temperature-humidity-measurement-with-nodemcu-191c46)
