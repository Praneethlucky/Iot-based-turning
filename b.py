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
        print("Left Turn Detected")
        GPIO.output(12,GPIO.LOW)
        GPIO.output(11,GPIO.HIGH)
        sleep(5)
        GPIO.output(11,GPIO.LOW)
        p1 = Process(target = func1)
        p1.start()
def func2():
    if(right()==1):
        print("Right Turn Detected")
        GPIO.output(11,GPIO.LOW)
        GPIO.output(12,GPIO.HIGH)
        sleep(5)
        GPIO.output(12,GPIO.LOW)
        p2 = Process(target = func2)
        p2.start()

if __name__=='__main__':
    p1 = Process(target = func1)
    print(p1.start())
    p2 = Process(target = func2)
    print(p2.start())

