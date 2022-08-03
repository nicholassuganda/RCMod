import WebcamModule as wM
import DataCollectionModule as dcM
from adafruit_servokit import ServoKit
from time import sleep
import JoyStickModule as jsM
import cv2

kit = ServoKit(channels =16)

record = 0

while True:    
    joyVal = jsM.getJS()
    steering = kit.servo[0].angle 
    if joyVal['axis3'] > 0 and joyVal['axis3'] <=1:
        kit.servo[0].angle = 90 - ((joyVal['axis3']/1)*90)    
    elif joyVal['axis3'] < 0 and joyVal['axis3'] >= -1: 
        kit.servo[0].angle = 90 + ((abs(joyVal['axis3']))/1*90)
    elif joyVal['axis3'] == 0:
        kit.servo[0].angle = 90
    if kit.servo[0].angle >= 160:
            kit.servo[0].angle = 160
    if kit.servo[0].angle <= 30:
            kit.servo[0].angle = 30
    
    throttle = joyVal['axis2']
    if joyVal['axis2'] == -1:
        kit.continuous_servo[1].throttle = 0.12
    elif joyVal['axis2'] == 1:
        kit.continuous_servo[1].throttle = -1
        
    
    if joyVal['L1'] == 1:
        if record ==0: print('Recording Started ...')
        record +=1
        sleep(0.500)
    if record == 1:
        img = wM.getImg(True,size=[480,360])
        dcM.saveData(img,steering)
    elif record == 2:
        dcM.saveLog()
        record = 0

    cv2.waitKey(1)