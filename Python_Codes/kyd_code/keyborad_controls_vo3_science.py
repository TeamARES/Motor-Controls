##################################################################################
########################IMPORTING LIBRARIES ######################################
##################################################################################
# importing socket so that we can connect two computer
import socket
from Tkinter import *

# importing time
import time
# importing Serial to take data from serial port
import serial
# importing the ke yboard listener from pynput
from pynput import keyboard
import numpy as np
##################################################################################
###################### SOCKET OBJECT AND VARIABLES ###################################################
##################################################################################

commands = []  # list of commands

s = socket.socket()
#host = '192.168.29.92'  #IP Address of the Raspberry pi
host = '192.168.10.102'
port = 9998  # Must be same as that in server.py
print('If you dont see working fine as the next msg , change the host as the ip adress of pi')
# In client.py we use another way to bind host and port together by using connect function()
s.connect((host, port))
print('Working fine!')
###########################SERIAL OBJECT ##############################################
# serialPortMac = '/dev/tty.usbmodem14101' #FOR MACBOOK
# serialPortWin = '/dev/ttyUSB0'           #FOR WINDOWS
# serialPortUbuntu = '/dev/ttyACM0'        #FOR UBUNTU
# ser = serial.Serial(serialPortUbuntu, 9600,timeout=0.005)
#######################################################################################
mode = 1  # 0-> Propulsion, 1-> Robotic Arm

m1 = 0
m2 = 0
m3 = 0
m4 = 0
m5 = 0
m6 = 0
m7 = 0
m8 = 0
class MyWindow:
    def __init__(self, win):
        global m1, m2, m3, m4, m5, m6, m7,m8
        global m1entry,m2entry,m3entry,m4entry,m5entry,m6entry,m7entry,m8entry
        global ac1,ac2,Base,Pitch,Load_Screw,Roll
        m1entry = Entry(win , text= "M1",textvariable = m1tk)
        m2entry = Entry(win ,text = "M2",textvariable= m2tk)
        ac1 = Label(win,text = "AC1")
        ac2 = Label(win,text = "AC2")
        Base = Label(win,text = "Base")
        Pitch = Label(win,text = "Pitch")
        Load_Screw = Label(win,text = "Load Screw")
        Roll = Label(win,text = "Roll")
        m3entry = Entry(win,text = "M3" ,textvariable =m3tk)
        m4entry = Entry(win,text = "M4" ,textvariable =m4tk)
        m5entry = Entry(win,text = "M5" ,textvariable =m5tk)
        m6entry = Entry(win,text = "M6" ,textvariable =m6tk)
        m7entry = Entry(win,text = "M7" ,textvariable =m7tk)
        m8entry = Entry(win,text = "M8" ,textvariable=m8tk)
        self.btn1 = Button(win, text='Send')
        self.b1=Button(win, text='Send', command=self.send)
        self.b1.place(x=200, y=200)


    def send(self):
        sendDatatoRaspi()

def sendDatatoRaspi():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(m1tk.get()) + ',' + str(m2tk.get()) + ',' + str(
            m3tk.get()) + ',' + str(m4tk.get()) + ',' + str(m5tk.get()) + ',' + str(m6tk.get()) + ','+ str(m7tk.get()) + ',' + str(m8tk.get())
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

window = Tk()
m1tk = StringVar()
m2tk = StringVar()
m3tk = StringVar()
m4tk = StringVar()
m5tk = StringVar()
m6tk = StringVar()
m7tk = StringVar()
m8tk = StringVar()


mywin = MyWindow(window)
window.title('Science Control')
window.geometry("400x300+10+10")
m1entry.grid(row=0,column=0)
ac1.grid(row=1,column=1)
ac2.grid(row=7,column=1)
Base.grid(row=3,column=1)
Pitch.grid(row=5,column=1)
Load_Screw.grid(row=6,column=1)
Roll.grid(row=4,column=1)
m2entry.grid(row=1,column=0)
m3entry.grid(row=2,column=0)
m4entry.grid(row=3,column=0)
m5entry.grid(row=4,column=0)
m6entry.grid(row=5,column=0)
m7entry.grid(row=6,column=0)
m8entry.grid(row=7,column=0)
window.mainloop()
