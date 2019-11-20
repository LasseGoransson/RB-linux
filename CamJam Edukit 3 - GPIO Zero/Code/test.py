
from gpiozero import Robot
from time import sleep

robot = Robot(left=(9,10), right=(7,8))

robot.forward()
