#!/usr/bin/env python3
from .autologo import *
from hexdump import hexdump
from time import sleep
from scapy.all import sniff
from .DATA.Ethernet import ETHERNETFRAME
class Sniffer:


    run = True
   
    def showText(self,text,indent=0):
        print('\t'*indent,text)


    
    def handlePacket(self,packet):
        self.showText("- PACKET -")
        # print(data)
        packet.show()
        # self.showText("- HEXADECIMAL DUMP -")
        print()
        # hexdump(data)
        self.showText("- Tek-Tech 2021 -",5)
        print()
        print()
        [print() for n in range(3)]
        sleep(0.5)

    def set_handler(self,handler):
        self.handler = handler
    
    def get_handler(self):
        return self.handler if hasattr(self,'handler') and self.handler!=None else self.handlePacket

    def start(self):
        def process_packet(packet):
            data = packet.original
            packet = ETHERNETFRAME(data,packet)
            self.get_handler()(packet)

        while self.run:
            try:
                sniff(prn=process_packet)
                # handlePacket(listener.recv(65565))
                # sleep(0.5)
            except KeyboardInterrupt:
                self.run = False
            except Exception as e:
                print(e)


    def __init__(self,handler=None):
        self.set_handler(handler)
        