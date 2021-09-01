from pynput import keyboard
speeds = ["1","2","3","3","4","6"]
numkey = ""
dirkey = ""
def forward(num):
    motornumber = int(format(num)[1])
    data = str(1) + ','
    for i in range(6):
        if i == motornumber:
            data = data + str(speeds[motornumber]) + ','
        else:
            data = data + str(0) + ','
    print(data)
def back(num):
    motornumber = int(format(num)[1])
    data = str(1) + ','
    for i in range(6):
        if i == motornumber:
            data = data + "-" + str(speeds[motornumber]) + ','
        else:
            data = data + str(0) + ','
    print(data)
    
def stopall():
    data = str(1) + ','
    for i in range(6):
        data = data + str(0) + ','
    print(data)
   
def on_press(key):
    global numkey
    print("finding",format(key))
    if(format(key) in ["'1'","'2'","'3'","'4'","'5'","'6"]):
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