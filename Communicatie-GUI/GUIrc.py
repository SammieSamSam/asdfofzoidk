from Tkinter import *
import socket

win_width = 800
win_height = 400
global status
status = False

target = "123.167.1.2"
port = 3400
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendMessage(msg):
    print "Message send: ", msg
    sock.sendto(msg, (target, port))

def createDisplay():
    global tk
    tk = Tk()
    tk.winfo_toplevel().title("Robot Controls Display")
    canvas = Canvas(tk, width=win_width, height=win_height)
    canvas.grid(row=10, column=10)

    exitBtn = Button(tk, text="Exit", command=terminate, bg="red", fg="white")
    exitBtn.grid(row=0, column=0)

    manualControlBtn = Button(tk, text="Manual control", command=enableManControl, bg="green", fg="white")
    manualControlBtn.grid(row=0, column=10)

    danceBtn = Button(tk, text="Perform dance", command=dance, bg="green", fg="white")
    danceBtn.grid(row=1, column=10)

    beatDanceBtn = Button(tk, text="Perform beatdance", command=beatDance, bg="green", fg="white")
    beatDanceBtn.grid(row=2, column=10)

    obstacleBtn = Button(tk, text="Obstacle course", command=obstacleCourse, bg="green", fg="white")
    obstacleBtn.grid(row=3, column=10)

    cannonBtn = Button(tk, text="Cannon walk", command=cannonWalk, bg="green", fg="white")
    cannonBtn.grid(row=4, column=10)

    scanBtn = Button(tk, text="Scan tower", command=scan, bg="green", fg="white")
    scanBtn.grid(row=5, column=10)

    autoBuildBtn = Button(tk, text="Build tower", command=autoBuild, bg="green", fg="white")
    autoBuildBtn.grid(row=6, column=10)

    stdBtn = Button(tk, text="Shutdown", command=shutdown, bg="green", fg="white")
    stdBtn.grid(row=0, column=1)

    rbtBtn = Button(tk, text="Reboot", command=reboot, bg="green", fg="white")
    rbtBtn.grid(row=1, column=1)
    
    tk.mainloop()

def enableManControl():
    #control legs, grab arm.
    #overgaan naar manual control wanneer nodig.
    sendMessage("")

def dance():
    #dans script uitvoeren.
    sendMessage("DCE")

def beatDance():
    #danst autonoom op beat.
    sendMessage("DCB")

def obstacleCourse():
    #autonoom obstacle course volgen.
    sendMessage("OBC")

def cannonWalk():
    #lijn volgen en halve minuut stilstaan.
    #kan manual of autonoom.
    sendMessage("CWA")

def scan():
    #scannen van toren.
    #status switch
    global status
    status = not status
    #check welke status na switch.
    if status == True:
        sendMessage("SCA-ON")
    elif status == False:
        sendMessage("SCA-OFF")

def autoBuild():
    #autonoom bouwen.
    sendMessage("AUB")

def shutdown():
    sendMessage("SYS-STD")

def reboot():
    sendMessage("SYS-RBT")

def terminate():
    global tk
    tk.destroy()    

createDisplay()
