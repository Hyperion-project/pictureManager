__author__ = 'Kenney'

from multibus import BusCore,BusClient,BusServer

if __name__ == '__main__':
    #setup server
    print("Motor controller Server: init")
    s = BusServer.BusServer(15001)
    s.listen()
    myAngle = 0
    while True:
        packet = s.getPacket()
        if packet.action == BusCore.PacketType.SETMOTOR:
                result = True
                if packet.data['returnport'] is not None:
                    c = BusClient.BusClient(packet.data['returnport'])
                    try:
                        c.send(BusCore.Packet(BusCore.PacketType.SETMOTOR, {'result': result}))
                    except:
                        print("Motor controller Server: failed to send done")