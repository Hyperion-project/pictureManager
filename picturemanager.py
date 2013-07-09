__author__ = 'Kenney'

import cv2
import multibus
from multibus import BusClient, BusCore, BusServer

pictureNumber = 1
motorA = 0
motorB = 0
motorC = 0
motorManager = BusClient.BusClient(15001)

def setMotor(motor, angle):

    motorManager.send(BusCore.Packet(BusCore.PacketType.SETMOTOR, {'motor': motor, 'angle': angle, 'returnport': 16001}))
    while True:
        donePacket = s.getPacket()
        if donePacket.action == BusCore.PacketType.SETMOTOR:
            done = (donePacket.data['result'])
            return done

def takePicture(Number):
    capture = cv2.VideoCapture(0)
    _,image = capture.retrieve()
    cv2.imwrite("Pictures/"+str(Number)+".jpg", image)
    cv2.destroyAllWindows()
    global pictureNumber
    pictureNumber = pictureNumber + 1

def parseAction(x):
    return {
        BusCore.PacketType.EMPTY: 'empty',
        BusCore.PacketType.TEST: 'test',
        BusCore.PacketType.STARTSCAN: 'start scan',
        BusCore.PacketType.SETMOTOR: 'set motor'
    }.get(x, 'something else')

#def sendPicture(mA, mB, mC, picNumber):
#    pictureHandler = BusClient.BusClient(10001)
#    pictureHandler.send(BusCore.Packet(BusCore.PacketType.PROCESSPICTURE, {"test": message}))

if __name__ == '__main__':
    print("Picture Manager: init")
    s = BusServer.BusServer(16001)
    s.listen()
    while True:
        packet = s.getPacket()
        if packet.action == BusCore.PacketType.STARTSCAN:
            for motorB in range(0, 360, 45):
                if setMotor("B", motorB):
                    for motorA in range(-13, 13, 1):
                        if setMotor("A", motorA):
                            takePicture(pictureNumber)
