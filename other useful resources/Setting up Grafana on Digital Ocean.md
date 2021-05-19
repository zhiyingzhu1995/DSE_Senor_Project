#Setting up Grafana on Digital Ocean

## Installation
	1. installing grafana, type in the DO terminal
		- `wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -`
		- `sudo add-apt-repository "deb https://packages.grafana.com/oss/deb stable main"`
		- `sudo apt update`
		- `apt-cache policy grafana`
	       expected output:
	       		```grafana:
				  Installed: (none)
				  Candidate: 6.3.3
				  Version table:
				     6.3.3 500
				        500 https://packages.grafana.com/oss/deb stable/main amd64 Packages```
		- `sudo apt install grafana`
		- `sudo systemctl start grafana-server`
		- check status `sudo systemctl status grafana-server`
		- enable grafana on boot `sudo systemctl enable grafana-server`

	2. Enable firewall, type in the DO terminal
		- `sudo ufw allow 3000/tcp`


	3. Open the google chrome browser, type in this
		`http://167.71.96.74:3000/`
		- use the default login as username: `admin`, password: `admin`

## Connect to databases
	- https://www.youtube.com/watch?v=pE7zU4MOqC8 
	- follow 20:15 onward


## Creating Dashboard in Grafana
	- https://www.youtube.com/watch?v=7kfgTtQzSG0
	- follow this video

