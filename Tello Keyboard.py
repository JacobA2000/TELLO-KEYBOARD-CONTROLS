import threading
import socket
import sys
import time
import keyboard

host = ''
port = 9000
locaddr = (host,port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

print ('Python Tello Keyboard Control')
print ('c - command, t - takeoff, l - land, w - forward')

recvThread = threading.Thread(target=recv)
recvThread.start()

def sendmsg(msg):
    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address)

def start():
    sendmsg('command')

def takeoff():
    sendmsg('takeoff')

def land():
    sendmsg('land')

def forward():
    sendmsg('forward 20')

def back():
    sendmsg('back 20')

def up():
    sendmsg('up 20')

def down():
    sendmsg('down 20')

def cw():
    sendmsg('cw 5')

def ccw():
    sendmsg('ccw 5')

wpressed = False
spressed = False

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('w'):
            wpressed == True
            while wpressed == True:
                print("forward")
                forward()
        elif keyboard.is_pressed('s'):
            spressed = True
            while spressed == True:
                print("backward")
                back()
        elif keyboard.is_pressed('up'):
            print('up 20')
            up()
        elif keyboard.is_pressed('down'):
            print('down 20')
            down()
        elif keyboard.is_pressed('right'):
            print('cw 5')
            cw()
        elif keyboard.is_pressed('left'):
            print('ccw 5')
            ccw()
        elif keyboard.is_pressed('t'):
            print('takeoff')
            takeoff()
        elif keyboard.is_pressed('l'):
            print('land')
            land()
        elif keyboard.is_pressed('c'):
            print('command')
            start()
        else:
            pass
    except:
        break