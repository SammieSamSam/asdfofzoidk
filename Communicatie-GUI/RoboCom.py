import socket
import TestRun
import threading
import time
import RoboGlobalVars as gvar
import DistanceSensor
import os

class Worker (threading.Thread):
    def __init__(self, threadID, name, method):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.method = method

    def run(self):
        self.method()

UDP_IP = "123.167.1.2"
UDP_PORT = 3400
delimiter = "-"

sock = socket.socket(socket.AF_INET, #internet
                    socket.SOCK_DGRAM) #UDP

sock.bind((UDP_IP, UDP_PORT))

def executeCommand(command, arg):
    if command == "SYS":
        gvar.stop = True
        if arg == "STD":
            gvar.shutdown = True
        if arg == "RBT":
            gvar.reboot = True
    elif command == "DCE":
        threadDance.start()
    elif command == "DCB":
        threadDanceBeat.start()
    elif command == "OBC":
        threadObstacleCourse.start()
    elif command == "CWA":
        threadCannonWalk.start()
    elif command == "SCA":
        if arg == "ON":
            gvar.stopScan = False
            threadScan.start()
        elif arg == "OFF":
            gvar.stopScan = True
    elif command == "AUB":
        threadBuild.start()

def socketCommunication():
    while gvar.stop == False:
        data, addr = sock.recvfrom(1024) #buffer size
        parseLine(data)

def parseLine(line):
    values = line.split(delimiter)
    command = values[0]
    if len(values) == 1:
        arg = command
    else:
        arg = values[1]
    executeCommand(command, arg)

def microphone():
    test = ""    

def distanceSensor():
    while gvar.stop == False:
        DistanceSensor.calcDistance()

def dance():
    test = ""

def beatDance():
    test = ""

def obstacleCourse():
    test = ""

def cannonWalk():
    #alleen nodig als we autonoom doen.
    test = ""
    
def scan():
    while gvar.stopScan == False:
        #run script
        test = ""

def autoBuild():
    test = ""

#create threads
threadMic = Worker(1, "MicWorker", microphone)
threadDistSensor = Worker(2, "DistWorker", distanceSensor)
threadDance = Worker(3, "DanceWorker", dance)
threadDanceBeat = Worker(4, "DanceBeatWorker", beatDance)
threadObstacleCourse = Worker(5, "ObstacleWorker", obstacleCourse)
threadCannonWalk = Worker(6, "CannonWorker", cannonWalk)
threadScan = Worker(7, "ScanWorker", scan)
threadBuild = Worker(8, "BuildWorker", autoBuild)

#start threads
#threadMic.start()
threadDistSensor.start()

#start mainthread
socketCommunication()

#join threads
#threadMic.join()
threadDistSensor.join()
#threadDance.join()
#threadDanceBeat.join()
#threadObstacleCourse.join()
#threadCannonWalk.join()
#threadScan.join()
#threadBuild.join()

if gvar.shutdown == True:
    os.system('systemctl poweroff')
elif gvar.reboot == True:
    os.system('systemctl reboot')
