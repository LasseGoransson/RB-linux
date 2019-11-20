# CamJam EduKit 3 - Robotics
# Worksheet 6 - Measuring Distance
import sys
import time  # Import the Time library
from gpiozero import DistanceSensor  # Import the GPIO Zero Library
from gpiozero import CamJamKitRobot


from simple_pid import PID
pid = PID(2, 0.5, 0, setpoint=0.50)
pid.output_limits = (-0.1,0.1)

# Set the relative speeds of the two motors, between 0.0 and 1.0
leftmotorspeed = 1.0
rightmotorspeed = 1.0

motorforward = (leftmotorspeed, rightmotorspeed)
motorbackward = (-leftmotorspeed, -rightmotorspeed)
motorleft = (leftmotorspeed, 0)
motorright = (0, rightmotorspeed)

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)


robot = CamJamKitRobot()
try:
    # Repeat the next indented block forever
    while True:
        #print("Distance: %.1f cm" % sensor.distance * 100)

        control = pid(sensor.distance)
        ##print(control)
        
        #if (sensor.distance < 0.50):
        #    turnA=0.05
        #else:
        #    turnA=-0.05



        turnA=control

        leftmotorspeed=0.9*( 0.5*turnA+0.5)
        rightmotorspeed=0.9*(-0.5*turnA+0.5)

        motorforward = (leftmotorspeed, rightmotorspeed)
        robot.value=motorforward

        time.sleep(0.1)
        print(sensor.distance, end = ',')
        print(leftmotorspeed,end=";")
        print(rightmotorspeed,end="")
        print(); 
        sys.stdout.flush()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    print("Exiting")




