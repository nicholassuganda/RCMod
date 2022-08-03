from adafruit_servokit import ServoKit
#from time import sleep
import JoyStickModule as jsM

kit = ServoKit(channels =16)
#kit.continuous_servo[1].throttle = -1

while True:
    joyVal = jsM.getJS()
    if joyVal['axis2'] == -1:
        kit.continuous_servo[1].throttle = 0.03
    elif joyVal['axis2'] == 1:
        kit.continuous_servo[1].throttle = -1

    