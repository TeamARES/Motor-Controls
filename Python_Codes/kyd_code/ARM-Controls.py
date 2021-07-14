##################################################################################
########################IMPORTING LIBRARIES ######################################
##################################################################################
# importing socket so that we can connect two computer
import socket
from Tkinter import *

# importing time
#import time
# importing Serial to take data from serial port
# import serial
# importing the ke yboard listener from pynput
# from pynput import keyboard
#import numpy as np
##################################################################################
###################### SOCKET OBJECT AND VARIABLES ###################################################
##################################################################################

commands = []  # list of commands

s = socket.socket()
host = '192.168.29.92'
#host = '192.168.10.102'  #IP Address of the Raspberry pi
#host = '192.168.43.91'
port = 9999  # Must be same as that in server.py
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
        self.b1=Button(win, text='Send',command = self.send)
        self.b1.bind('<ButtonPress-1>',send)
        self.b1.bind('<ButtonRelease-1>',stop)

        """motor forward buttons"""
        self.mb1 = Button(win,text='M1-F')
        self.mb1.bind('<ButtonPress-1>',m1send)
        self.mb1.bind('<ButtonRelease-1>',stop)

        self.mb2 = Button(win,text='M2-F')
        self.mb2.bind('<ButtonPress-1>',m2send)
        self.mb2.bind('<ButtonRelease-1>',stop)
        
        self.mb3 = Button(win,text='M3-F')
        self.mb3.bind('<ButtonPress-1>',m3send)
        self.mb3.bind('<ButtonRelease-1>',stop)

        self.mb4 = Button(win,text='M4-F')
        self.mb4.bind('<ButtonPress-1>',m4send)
        self.mb4.bind('<ButtonRelease-1>',stop)

        self.mb5 = Button(win,text='M5-F')
        self.mb5.bind('<ButtonPress-1>',m5send)
        self.mb5.bind('<ButtonRelease-1>',stop)

        self.mb6 = Button(win,text='M6-F')
        self.mb6.bind('<ButtonPress-1>',m6send)
        self.mb6.bind('<ButtonRelease-1>',stop)

        self.mb7 = Button(win,text='M7-F')
        self.mb7.bind('<ButtonPress-1>',m7send)
        self.mb7.bind('<ButtonRelease-1>',stop)

        self.mb8 = Button(win,text='M8-F')
        self.mb8.bind('<ButtonPress-1>',m8send)
        self.mb8.bind('<ButtonRelease-1>',stop)


        """motor reverse buttons"""
        self.mbr1 = Button(win,text='M1-R')
        self.mbr1.bind('<ButtonPress-1>',m1rsend)
        self.mbr1.bind('<ButtonRelease-1>',stop)

        self.mbr2 = Button(win,text='M2-R')
        self.mbr2.bind('<ButtonPress-1>',m2rsend)
        self.mbr2.bind('<ButtonRelease-1>',stop)
        
        self.mbr3 = Button(win,text='M3-R')
        self.mbr3.bind('<ButtonPress-1>',m3rsend)
        self.mbr3.bind('<ButtonRelease-1>',stop)

        self.mbr4 = Button(win,text='M4-R')
        self.mbr4.bind('<ButtonPress-1>',m4rsend)
        self.mbr4.bind('<ButtonRelease-1>',stop)

        self.mbr5 = Button(win,text='M5-R')
        self.mbr5.bind('<ButtonPress-1>',m5rsend)
        self.mbr5.bind('<ButtonRelease-1>',stop)

        self.mbr6 = Button(win,text='M6-R')
        self.mbr6.bind('<ButtonPress-1>',m6rsend)
        self.mbr6.bind('<ButtonRelease-1>',stop)

        self.mbr7 = Button(win,text='M7-R')
        self.mbr7.bind('<ButtonPress-1>',m7rsend)
        self.mbr7.bind('<ButtonRelease-1>',stop)

        self.mbr8 = Button(win,text='M8-R')
        self.mbr8.bind('<ButtonPress-1>',m8rsend)
        self.mbr8.bind('<ButtonRelease-1>',stop)

       
        self.b2=Button(win, text='Stop', command=self.stop)
        self.b3=Button(win, text='Reverse',command=self.reverse)


        """place all forward buttons"""
        self.mb1.place(x=300,y=10)
        self.mb2.place(x=300,y=50)
        self.mb3.place(x=300,y=90)
        self.mb4.place(x=300,y=135)
        self.mb5.place(x=300,y=175)
        self.mb6.place(x=300,y=215)
        self.mb7.place(x=300,y=255)
        self.mb8.place(x=300,y=295)

        """place all backward buttons"""

        self.mbr1.place(x=370,y=10)
        self.mbr2.place(x=370,y=50)
        self.mbr3.place(x=370,y=90)
        self.mbr4.place(x=370,y=135)
        self.mbr5.place(x=370,y=175)
        self.mbr6.place(x=370,y=215)
        self.mbr7.place(x=370,y=255)
        self.mbr8.place(x=370,y=295)

        "place all common buttons"
        self.b1.place(x=150,y=350)
        self.b2.place(x=220, y=350)
        self.b3.place(x=290, y=350)


    def send(self):
        sendDatatoRaspi()
    def stop(self):
        stopallm()
    def reverse(self):
        reversem()
def send(event):
    sendDatatoRaspi()
def stop(event):
    stopallm()

"""forward functions"""
def m1send(event):
    sendm1()
def m2send(event):
    sendm2()
def m3send(event):
    sendm3()
def m4send(event):
    sendm4()
def m5send(event):
    sendm5()
def m6send(event):
    sendm6()
def m7send(event):
    sendm7()
def m8send(event):
    sendm8()

"backward functions"
def m1rsend(event):
    sendm1r()
def m2rsend(event):
    sendm2r()
def m3rsend(event):
    sendm3r()
def m4rsend(event):
    sendm4r()
def m5rsend(event):
    sendm5r()
def m6rsend(event):
    sendm6r()
def m7rsend(event):
    sendm7r()
def m8rsend(event):
    sendm8r()


def stopallm():
    stringData = str(mode) + ',' + str(0) + ',' + str(0)+ ',' + str(
            0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def reversem():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + '-'+str(m1tk.get()) + ',' + '-'+str(m2tk.get()) + ',' + '-'+str(
            m3tk.get()) + ',' + '-'+str(m4tk.get()) + ',' + '-'+str(m5tk.get()) + ',' + '-'+str(m6tk.get()) + ','+ '-'+str(m7tk.get()) + ',' + '-'+str(m8tk.get())
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)



"""
Forward functions:
Only read the values for the motors whose function is called and rest are zero
"""
def sendm1():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(m1tk.get()) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm2():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(m2tk.get()) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm3():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(m3tk.get()) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm4():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(m4tk.get()) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm5():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(m5tk.get()) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm6():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(m6tk.get()) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm7():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(m7tk.get()) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm8():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(m8tk.get())
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)



"""
Reverse functions:
Only read the values for the motors whose function is called and rest are zero.
Reverse those values and send
"""
def sendm1r():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str("-" + m1tk.get()) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm2r():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str("-"+ m2tk.get()) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm3r():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str( "-"  + m3tk.get()) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm4r():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str("-" +  m4tk.get()) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm5r():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str("-"+m5tk.get()) + ',' + str(0) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm6r():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str("-"+ m6tk.get()) + ','+ str(0) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm7r():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str("-"+ m7tk.get()) + ',' + str(0)
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

def sendm8r():
    global m1, m2, m3, m4, m5, m6, m7 , m8
    global mode
    stringData = str(mode) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ',' + str(0) + ','+ str(0) + ',' + str("-"+m8tk.get())
    s.send(str.encode(stringData))
    # After sending we check if it was recieved or not
    checkDataTranfer = s.recv(1024)
    print(checkDataTranfer)

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
window.title('Arm Control')
window.geometry("500x600+10+10")


"""place all the entry boxes in a grid"""
m1entry.grid(row=0,column=0,pady=10)
m2entry.grid(row=1,column=0,pady=10)
m3entry.grid(row=2,column=0,pady=10)
m4entry.grid(row=3,column=0,pady=10)
m5entry.grid(row=4,column=0,pady=10)
m6entry.grid(row=5,column=0,pady=10)
m7entry.grid(row=6,column=0,pady=10)
m8entry.grid(row=7,column=0,pady=10)

"""place all the labels in the grid"""
ac1.grid(row=0,column=1,pady=10)
ac2.grid(row=2,column=1,pady=10)
Base.grid(row=3,column=1,pady=10)
Roll.grid(row=4,column=1,pady=10)
Pitch.grid(row=5,column=1,pady=10)
Load_Screw.grid(row=6,column=1,pady=10)

"""main loop"""
window.mainloop()
