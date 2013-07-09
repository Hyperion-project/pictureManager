__author__ = 'Kenney'

from multibus import BusCore,BusClient

if __name__ == '__main__':
    c = BusClient.BusClient(16001)
    c.send(BusCore.Packet(BusCore.PacketType.STARTSCAN, {"test": "80"}))