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
def detect_turn():
    ir1=left()
    print(ir1)
    ir2=right()
    if ir1==1 and ir2==0:
        return 'left'
    elif ir1==0 and ir2==1:
        return 'right'
    #else:
        #detect_turn()
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
    #GPIO.output(11,GPIO.LOW)
    led1=0
    global led2
    #GPIO.output(12,GPIO.LOW)
    led2=0
    left=0
    right=0
    time_delay=res2-5
    c=check()
    if res=='left':
        if c=='left':
            print('Already left On')
            turn=detect_turn()
            print('turn detected',turn)
            if turn==res:
                time.sleep(5)
                print("indicator",res,'stopped')
                GPIO.output(11,GPIO.LOW)
                led1=0
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
            turn=detect_turn()
            print('turn detected',turn)
            if turn==res:
                    time.sleep(5)
                    print("indicator",res,'stopped')
                    GPIO.output(11,GPIO.LOW)
                    led1=0
                #else :
                #get_directions()
                #main()
    elif res=='right':
        if c=='right':
            print('already right On')
            turn=detect_turn()
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
            turn=detect_turn()
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
    print('right',led2,'left',led1)
        
def main():
    from directions import get_directions
    direction, length, times = get_directions()
    print(direction,length,times)
    for i in range(len(direction)):
        res=direction[i]
        print(res)
	#set_indicators(res,length[i],times[i])
main()
#while(True):
#cg=(detect_turn())
#print(cg)
