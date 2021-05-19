# Setting up influxdb, telegraf

## Install influxdb
1. At your terminal type this
	- `curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list`
   - `sudo apt-get update`
   - `sudo apt-get install influxdb`
   a. if you see this error 
   ```
   "root@TestVersion:~# sudo apt-get install influxdb
	E: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 4509 (unattended-upgr)
	N: Be aware that removing the lock file is not a solution and may break your system.
	E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?"
	```
    b. try method 1 and method 2 in here [https://itsfoss.com/could-not-get-lock-error/]
    -  method 2 ended up working for me
    	```
    	sudo lsof /var/lib/dpkg/lock
		sudo lsof /var/lib/apt/lists/lock
		sudo lsof /var/cache/apt/archives/lock```

		`sudo kill -9 <process_id>`

		`sudo rm /var/lib/apt/lists/lock
		sudo rm /var/cache/apt/archives/lock
		sudo rm /var/lib/dpkg/lock`

		`sudo dpkg --configure -a`

```
## Install telegraf, Kapacitor, Chronograf exactly as written in the documentation
	- https://www.digitalocean.com/community/tutorials/how-to-monitor-system-metrics-with-the-tick-stack-on-ubuntu-16-04


