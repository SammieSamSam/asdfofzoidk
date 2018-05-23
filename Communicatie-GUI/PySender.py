import socket

target = "123.167.1.2"
port = 3400
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def ReadInput():
    while True:
        message = raw_input("Enter message: ")
        SendMessage(message)

def SendMessage(msg):
    print "Message send: ", msg
    sock.sendto(msg, (target, port))

ReadInput()
