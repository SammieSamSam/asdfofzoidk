import socket

UDP_IP = "123.167.1.2"
UDP_PORT = 3400

sock = socket.socket(socket.AF_INET, #internet
                     socket.SOCK_DGRAM) #UDP

sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) #buffer size
    print "received message: ", data
        
