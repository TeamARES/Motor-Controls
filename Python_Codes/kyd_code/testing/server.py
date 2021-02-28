import socket

def strToInt(string):
    if(len(string) == 0):
#        print('string length 0')
        return 0;
    x=0
    flag = 0
    if(string[0]=='-'):
        flag=1
        
    for i in range (0,len(string)):
                    if string[i].isdigit():
                        x+=int(string[i])*10**int(len(string)-i-1)
#                        print('In strToInt',i,x)
    if (flag ==1):
        return (-1)*x
    else:
        return x

def create_socket():
    try:
        # Creating following 3 global variables
        global host
        global port
        global s  # This is socket variable which is named s

        # Assigning values to these 3 global variables
        host = ""
        port = 9999
        s = socket.socket()    # Creating a socket and assigning it to s

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def bind_socket():
    try:
        # Declaring them again so that we can use the above global variable
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()

def read_commands(conn):
    global mode,motorspeed1, motorspeed2, forward_left_motor, forward_right_motor, backward_left_motor, backward_right_motor;
    
    #IPCheckRoutine()
    while True:
        dataFromBase = str(conn.recv(1024))
        print("\n Received Data = "+dataFromBase)
        #        print('lengthOfData', len(dataFromBase))
        if(len(dataFromBase) > 3):
            send_command(conn,'YES')
            index1 = dataFromBase.index(',')
            modeStr = dataFromBase[0:index1]
            
            mode = strToInt(modeStr)
            
            if(mode == 0):
                propulsion(dataFromBase,index1);
            elif(mode == 1):
                science(dataFromBase,index1);
    
        else:
            print("Not sending",dataFromBase)
            send_command(conn,'NO')

def socket_accept():
    #s.accept retuens : conn: object of a conversation and address is a list of IP adress and a port
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    read_commands(conn) #A function defined below to send command to client
    conn.close() #whenever the connection has been establised, at the end we want to close the connection

def propulsion(data1,data2):
    print("Propulsion", data1,data2)

def science(dataFromBase,index1):
    global m1, m2, m3, m4, m5, m6, m7, m8;
    
    index2 = dataFromBase.index(',',index1+1)
    StrbaseMotorSpeed = dataFromBase[index1+1:index2]
    m1 = strToInt(StrbaseMotorSpeed);
    print("m1:",m1)

    index3 = dataFromBase.index(',',index2+1)
    StrbaseMotorSpeed = dataFromBase[index2+1:index3]
    m2 = strToInt(StrbaseMotorSpeed);
    print("m2:",m2)

    index4 = dataFromBase.index(',',index3+1)
    StrbaseMotorSpeed = dataFromBase[index3+1:index4]
    m3 = strToInt(StrbaseMotorSpeed);
    print("m3:",m3)

    index5 = dataFromBase.index(',',index4+1)
    StrbaseMotorSpeed = dataFromBase[index4+1:index5]
    m4 = strToInt(StrbaseMotorSpeed);
    print("m4:",m4)

    index6 = dataFromBase.index(',',index5+1)
    StrbaseMotorSpeed = dataFromBase[index5+1:index6]
    m5 = strToInt(StrbaseMotorSpeed);
    print("m5:",m5)

    index7 = dataFromBase.index(',',index6+1)
    StrbaseMotorSpeed = dataFromBase[index6+1:index7]
    m6 = strToInt(StrbaseMotorSpeed);
    print("m6:",m6)

    index8 = dataFromBase.index(',',index7+1)
    StrbaseMotorSpeed = dataFromBase[index7+1:index8]
    m7 = strToInt(StrbaseMotorSpeed);
    print("m7:",m7)
    
    print(index8)
    #index9 = dataFromBase.index(',',index8+1)
    StrbaseMotorSpeed = dataFromBase[index8+1:]
    m8 = strToInt(StrbaseMotorSpeed);
    print("m8:",m8)
    

def send_command(conn1,data1):
    conn1.send(str.encode(data1))




create_socket()
bind_socket()
socket_accept()
