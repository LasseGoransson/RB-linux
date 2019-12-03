 Linux Mandatory Assignment 2
 
Group 4
 Lasse Gøransson
 Nicholai Bjerke Jensen
 Marc Elton Evald

The following scripts are added to enable wallfollowing remotely.
The Raspberry Pi Zero on the robot, has been setup to join an AdHoc wireless 
network with IP 192.168.99.4
SSID - pibot

The scripts are started via RC.local at startup.

 - CamJam Edukit 3 - GPIO Zero/Code/server.sh       - Server which processes commands and returns data.
 - CamJam Edukit 3 - GPIO Zero/Code/startserver.sh  - Is run at startup by RC.local to start socat server.
 - CamJam Edukit 3 - GPIO Zero/Code/rigtig.py       - The code that controls the robot wallfollower.


The robot accepts the following commands:
echo "start" | socat - tcp:192.168.99.4:8080 - Start the robot
echo "stop" | socat - tcp:192.168.99.4:8080 - Stops the robot
echo "getDist" | socat - tcp:192.168.99.4:8080 - Returns the measurement from ultrasound sensor
echo "getMotors" | socat - tcp:192.168.99.4:8080 - Returns the motor values Left and Right respectively.
