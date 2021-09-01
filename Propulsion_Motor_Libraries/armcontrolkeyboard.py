from pynput import keyboard
import socket

speeds = ["1","2","3","4","5","6","7"]
numkey = ""
dirkey = ""
s = socket.socket()
host = '192.168.29.87'
#host = '192.168.10.102'  #IP Address of the Raspberry pi
#host = '192.168.43.91'
port = 9999  # Must be same as that in server.py
print('If you dont see working fine as the next msg , change the host as the ip adress of pi')
# In client.py we use another way to bind host and port together by using connect function()
s.connect((host, port))
print('Working fine!')
#
def send(data):
    s.send(str.encode(data))
    checkDataTransfer = s.recv(1024)
    print(checkDataTransfer)

def forward(num):
    motornumber = int(format(num)[1])
    print(motornumber)
    data = str(1) + ','
    for i in range(1,8):
        if i == motornumber:
            data = data + str(speeds[motornumber]) + ','
        else:
            data = data + str(0) + ','
    print(data)
    send(data)

def back(num):
    motornumber = int(format(num)[1])
    data = str(1) + ','
    for i in range(1,8):
        if i == motornumber:
            data = data + "-" + str(speeds[motornumber]) + ','
        else:
            data = data + str(0) + ','
    print(data)
    send(data)
    
def stopall():
    data = str(1) + ','
    for i in range(1,8):
        data = data + str(0) + ','
    print(data)
    send(data)
   
def on_press(key):
    global numkey
    print("finding",format(key))
    if(format(key) in ["'1'","'2'","'3'","'4'","'5'","'6'"]):
        numkey = key  
    elif(format(key) == 'Key.up'):
        forward(numkey)
    elif(format(key) == 'Key.down'):
        back(numkey)


def on_release(key):
    stopall()
    if key == keyboard.Key.esc:      # Stop listener
        return False
    

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()