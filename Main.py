import re
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(11,GPIO.LOW)

GPIO.output(12,GPIO.LOW)

led1=0
led2=0

from uv_left import left
from uv_right import right
def detect_turn1():
    import logging
    import threading
    from time import sleep
    from uv_left import left
    from uv_right import right
    from multiprocessing import Process
    import sys
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    rocket = 0

    def func1():
        if (left()==1):
            GPIO.output(12,GPIO.LOW)
            GPIO.output(11,GPIO.HIGH)
            sleep(5)
            GPIO.output(11,GPIO.LOW)
            p1 = Process(target = func1)
            p1.start()
    def func2():
        if(right()==1):
            GPIO.output(11,GPIO.LOW)
            GPIO.output(12,GPIO.HIGH)
            sleep(5)
            GPIO.output(12,GPIO.LOW)
            p2 = Process(target = func2)
            p2.start()

    p1 = Process(target = func1)
    p1.start()
    p2 = Process(target = func2)
    p2.start()
def detect_turn(res):
    if res=="left":
        if left()==1 or right()==0:
            return 'left'
    if res=="right":
        if right()==1 or left()==0:
            return 'right'
def check():
    global led1
    global led2
    if led1==1 and led2==0:
        return 'left'
    elif led2==1 and led1==0:
        return 'right'
    else:
        return 'no'
def get_time(distance,speed):
    return distance/speed
def set_indicators(res,res1,res2):
    global led1
    GPIO.output(11,GPIO.LOW)
    led1=0
    global led2
    GPIO.output(12,GPIO.LOW)
    led2=0
    time_delay=res2
    c=check()
    if res=='left':
        if c=='left':
            print('Already left On')
            turn=detect_turn(res)
            print('turn detected',turn)
            if turn==res:
                time.sleep(5)
                print("indicator",res,'stopped')
                GPIO.output(11,GPIO.LOW)
                led1=0
            else:
                print("Turn left but right detected")
                exit(0)
        elif c=='right':
            h=10
            exit(0)
        else:
            time.sleep(time_delay)
            led1=1
            GPIO.output(11,GPIO.HIGH)
            print("left on")
            led2=0
            GPIO.output(12,GPIO.LOW)
            turn=detect_turn(res)
            print('turn detected',turn)
            if turn==res:
                    time.sleep(5)
                    print("indicator",res,'stopped')
                    GPIO.output(11,GPIO.LOW)
                    led1=0
                #else :
                #get_directions()
                #main()
    elif res=='right' or res=='U-Turn':
        if c=='right':
            print('already right On')
            turn=detect_turn(res)
            if turn==res:
                time.sleep(5)
                print("indicator",res,'stopped')
                GPIO.output(12,GPIO.LOW)
                led2=0
        elif c=='left':
            #get_directions()
            h=10
            print(h)
            exit(0)
        else:
            time.sleep(time_delay)
            led1=0
            GPIO.output(11,GPIO.LOW)
            print("right on")
            led2=1
            GPIO.output(12,GPIO.HIGH)
            turn=detect_turn(res)
            print("turn detected",turn)
            if turn==res:
                time.sleep(5)
                print("indicator",res,'stopped')
                GPIO.output(12,GPIO.LOW)
                led2=0
            #else :
                #get_directions()
                #main()
        
    else:
        print("continue")
        time.sleep(time_delay)
    
        
def main():
    di=["continue","right","right","left","right","left","left","right","right"]
    le=[45,36,78,100,67,56,76,89,88]
    ti=[7,9,3,10,4,7,5,6,8]
    #print(direct,ler,tim)
    #from Directions_mapBox import get_directions
    #di,le,ti=get_directions()
    print(di,le,ti)
    for i in range(len(di)):
        set_indicators(di[i+1],le[i],ti[i])
main()

