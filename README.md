aprs-arduino-collector
======================

This project uses the [Argent Data Radio Shield](argentdata.com/catalog/product_info.php?products_id=136) to 
receive & decode [Automated Packet Reporting System (APRS)](http://www.aprs.org/) messages using an Arduino microcontroller.  The 
Arduino reads APRS messages over a serial port on the radio shield, and prints to 
its own serial port.  In my case, I connected the Arduino (Uno) to a Raspberry Pi with a USB cable.  The Arduino
will show up as a serial port on the Pi.  The Pi can then read from the Arduino's serial port output.  The Pi
will run a Python script that relays the raw APRS messages to an [APRS Dashboard](https://github.com/urlgrey/aprs-dashboard)
installation running elsewhere.  The APRS Dashboard will aggregate and track the APRS messages so we can do cool stuff
with the data.

This project contains two resources:
  1. Arduino sketch to read from the Radio Shield and print APRS messages to the serial port
  1. Python script to read the APRS from the Arduino output and send them to an APRS Dashboard installation


Arduino Sketch
--------------
Compile and upload the sketch to your Arduino.  In my experience, I had to disconnect the Radio Shield from the 
Arduino in order to upload the sketch (perhaps because of how the shield uses the serial port, not sure).  Once 
uploaded, disconnect the Arduino from power, replace the shield, and connect to power again.

Python Script
-------------
**Note:*** This script is intended for use with the Raspberry Pi, so I've written it to use Python2.

Use the following steps:
 1. Copy the script to the Raspberry Pi
 1. If you plan on running the script for an extended period, I suggest installing & running `screen`
 1. Set the following environment variables: `APRS_DASHBOARD_HOST` and `APRS_DASHBOARD_PORT`
    1. ```export APRS_DASHBOARD_HOST="127.0.0.1"```
    1. ```export APRS_DASHBOARD_PORT="3000"```
 1. If an API key is required by the APRS Dashboard, then set the following:
    1. ```export APRS_DASHBOARD_API_KEY="secret123"```
 1. Run the script: ```python read_arduino.py```

