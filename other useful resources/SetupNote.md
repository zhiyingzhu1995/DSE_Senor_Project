## ESP Board Set up

1. Install esptool by run the command in  the terminal:  `pip install esptool`
2. Check the location of the ESP board using command: `ls /dev/tty.*`
   1. usually be `/dev/tty.usbserial-0001`

3. Check if the board is connect by try to get  the board information with command: `esptool.py flash_id`

   1. if  get issue like **"Failed to connect to Espressif device: Timed out waiting for packet header"**

      1. check out [this](https://www.youtube.com/watch?v=v8s-UMqcTJs&ab_channel=firebitlab)

   2. Note:

      1. EN=reset, BOOT=bootloader mode
      2. Hold BOOT, then press EN briefly to enter the bootloader, then release BOOT. This way you can flash a new firmware on it. 

   3. Expected Output for Board Info (should be something similar)

      ```
      esptool.py v3.0
      Found 6 serial ports
      Serial port /dev/cu.usbserial-0001
      Connecting....
      Detecting chip type... ESP32
      Chip is ESP32-D0WDQ6 (revision 1)
      Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
      Crystal is 40MHz
      MAC: 24:0a:c4:ec:12:34
      Uploading stub...
      Running stub...
      Stub running...
      Manufacturer: d8
      Device: 4016
      Detected flash size: 4MB
      Hard resetting via RTS pin...
      ```

4. Download the Micropython through this [link](https://micropython.org/download/)

   1. Find the correct version for your ESP board version
   2. If you have ESP 8266 download: [esp8266-20210418-v1.15.bin](https://micropython.org/resources/firmware/esp8266-20210418-v1.15.bin)  
   3. If you have ESP 32 download: [esp32-20210418-v1.15.bin](https://micropython.org/resources/firmware/esp32-20210418-v1.15.bin)


5. do `cd Downloads`, you should see the esp32-20210418-v1.15.bin file in the folder

6. While holding down the “BOOT/FLASH” button, run the following command to erase the ESP8266 flash memory:
	```esptool.py --chip esp8266 erase_flash```

	expected output
		```
		esptool.py v3.0
		Found 6 serial ports
		Serial port /dev/cu.usbserial-0001
		Connecting....
		Chip is ESP8266EX
		Features: WiFi
		Crystal is 26MHz
		MAC: 48:3f:da:a4:3a:85
		Uploading stub...
		Running stub...
		Stub running...
		Erasing flash (this may take a while)...
		Chip erase completed successfully in 3.0s
		Hard resetting via RTS pin...
		```


6. Program the firmware starting at address 0x1000

   1. Make source you are locate at the same location of your micro python file

   2. Run  the command

	  With your ESP8266 flash memory erased, you can finally flash the MicroPython firmware. You need your serial port name (COM7 in our case) and the ESP8266 .bin file location. Replace the next command with your details:
			`esptool.py --chip esp8266 --port <serial_port> write_flash --flash_mode dio --flash_size detect 0x0 <esp8266-X.bin>`

		a. in our case, the final command looks like 
		serial_port = is where you see in the above expected output

			```
			esptool.py --chip esp8266 --port /dev/cu.usbserial-0001 write_flash --flash_mode dio --flash_size detect 0x0 esp8266-20210418-v1.15.bin
			```

     
   3. Expected Output

      ```
      esptool.py v3.0
      Serial port /dev/tty.usbserial-0001
      Connecting........_
      Chip is ESP32-D0WDQ6 (revision 1)
      Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
      Crystal is 40MHz
      MAC: 24:0a:c4:ec:12:34
      Uploading stub...
      Running stub...
      Stub running...
      Changing baud rate to 460800
      Changed.
      Configuring flash size...
      Auto-detected Flash size: 4MB
      Compressed 1469216 bytes to 953244...
      Wrote 1469216 bytes (953244 compressed) at 0x00000000 in 22.8 seconds (effective 515.1 kbit/s)...
      Hash of data verified.
      Leaving...
      Hard resetting via RTS pin...
      ```





# Connect with RShell

1. Install rshell:`pip install rshell`

2. CD to the folder that you want, `cd "new_project"`

3. Connect with Device `rshell -e emacs --port [your device location] --baud 115200`
		a. in our case, the command would be `rshell -e emacs --port /dev/tty.usbserial-0001 --baud 115200`
   1. Expected Output

      ```
      Using buffer-size of 32
      Connecting to /dev/tty.usbserial-0001 (buffer-size 32)...
      Trying to connect to REPL . connected
      Retrieving sysname ... esp32
      Testing if ubinascii.unhexlify exists ... Y
      Retrieving root directories ... /boot.py/
      Setting time ... May 02, 2021 17:05:13
      Evaluating board_name ... pyboard
      Retrieving time epoch ... Jan 01, 2000
      Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
      ```

      