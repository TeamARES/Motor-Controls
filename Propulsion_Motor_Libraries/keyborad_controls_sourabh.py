##################################################################################
########################IMPORTING LIBRARIES ######################################
##################################################################################
#importing socket so that we can connect two computer
import socket
#importing time
import time
#importing Serial to take data from serial port
#import serial
#importing the keyboard listener from pynput
from pynput import keyboard
import threading

##################################################################################
###################### SOCKET OBJECT AND VARIABLES ###################################################
##################################################################################
s = socket.socket()
host = '192.168.10.102'  #IP Address of Xavier
port = 9999            #Must be same as that in server.py
#In client.py we use another way to bind host and port together by using connect function()
s.connect((host, port))
###########################SERIAL OBJECT ##############################################
# serialPortMac = '/dev/tty.usbmodem14101' #FOR MACBOOK
# serialPortWin = '/dev/ttyUSB0'           #FOR WINDOWS
# serialPortUbuntu = '/dev/ttyACM0'        #FOR UBUNTU
# ser = serial.Serial(serialPortUbuntu, 9600,timeout=0.005)

def sendDatatoXavier():
    global forwardBackwardSpeed
    global leftRightSpeed
    stringData = '0,' + str(forwardBackwardSpeed) + ',' + str(leftRightSpeed)
    # Sendng this data from socket to the raspberry pi
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)
##################################################################################
############################### Variables amd functions for speed ################
##################################################################################
forwardBackwardSpeed = 0
leftRightSpeed = 0
deaclereration_counter = time.perf_counter()
def increaseForwardBackwardSpeed():
    global forwardBackwardSpeed
    forwardBackwardSpeed = min(forwardBackwardSpeed + 1, 100)
    printSpeeds()
    sendDatatoXavier()

def decreaseForwardBackwardSpeed():
    global forwardBackwardSpeed
    forwardBackwardSpeed = max(forwardBackwardSpeed - 1, -100)
    printSpeeds()
    sendDatatoXavier()

def increaseleftRightSpeed():
    global leftRightSpeed
    '''
    if leftRightSpeed<=1 and leftRightSpeed>=0:
        leftRightSpeed = leftRightSpeed + 0.1
    elif leftRightSpeed<=10 and leftRightSpeed>=0:
        leftRightSpeed = leftRightSpeed + 0.1*leftRightSpeed
    else:
        leftRightSpeed = leftRightSpeed + 1
    if (leftRightSpeed > 100):
        leftRightSpeed = 100
    '''
    leftRightSpeed = min(leftRightSpeed + 1, 100)
    printSpeeds()
    sendDatatoXavier()

def decreaseleftRightSpeed():
    global leftRightSpeed
    '''
    if leftRightSpeed>=-1 and leftRightSpeed<=0:
        leftRightSpeed = leftRightSpeed - 0.1
    elif leftRightSpeed>=-10 and leftRightSpeed<=0:
        leftRightSpeed = leftRightSpeed - abs(0.1*leftRightSpeed)
    else:
        leftRightSpeed = leftRightSpeed - 1
    if (leftRightSpeed < -100):
        leftRightSpeed = -100
    '''
    leftRightSpeed = max(leftRightSpeed - 1, -100)
    printSpeeds()
    sendDatatoXavier()

def stopMotor():
    global leftRightSpeed
    global forwardBackwardSpeed
    leftRightSpeed = 0
    forwardBackwardSpeed = 0
    printSpeeds()
    sendDatatoXavier()
##################################################################################
############################### print statements ##################################
##################################################################################
def printSpeeds():
    global forwardBackwardSpeed
    global leftRightSpeed
    stringData = '0,' + str(forwardBackwardSpeed) + ',' + str(leftRightSpeed)
    print(" - ",stringData)

##################################################################################
############################### keyboard listener commands  ######################
##################################################################################
def on_press(key):
    global deaclereration_counter
    if(format(key)=='Key.up'):
        deaclereration_counter = time.perf_counter()
        increaseForwardBackwardSpeed()
    elif(format(key)=='Key.down'):
        deaclereration_counter = time.perf_counter()
        decreaseForwardBackwardSpeed()
    elif(format(key)=='Key.left'):
        decreaseleftRightSpeed()
    elif(format(key)=='Key.right'):
        increaseleftRightSpeed()
    elif(format(key) == 'Key.space'):
        print('stopingMotor')
        stopMotor()

def on_release(key):
    if key == keyboard.Key.esc:      # Stop listener
        return False
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
def decelerate():
    global listener
    global deaclereration_counter
    global forwardBackwardSpeed
    global leftRightSpeed
    while True:
        stop_deaclereration_counter = time.perf_counter()
        if stop_deaclereration_counter - deaclereration_counter >= 0.1:
            if forwardBackwardSpeed >= 1:
                forwardBackwardSpeed -= 1
            elif forwardBackwardSpeed <= -1:
                forwardBackwardSpeed += 1
            if leftRightSpeed >= 1:
                leftRightSpeed -= 1
            elif leftRightSpeed <= -1:
                leftRightSpeed += 1
            deaclereration_counter = time.perf_counter()
            sendDatatoXavier()
            printSpeeds()
        if not listener.running:
            break
decelerate_thread = threading.Thread(target=decelerate, name="decelerate")
decelerate_thread.start()
##################################################################################
##################################################################################

