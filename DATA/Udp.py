#!/usr/bin/env python3
from binascii import hexlify
from struct import unpack
from .learn import *
from .Bootp import BOOTPPACKET
from dnslib import DNSRecord
class UDPDATAGRAM:

    ports = []


    def __init__(self,data):
        
        src,dst = unpack("!2H",data[:4])
        self.src = src
        self.dst = dst
        self.application = [getPortByNumber(self,str(self.src)),getPortByNumber(self,str(self.dst))]
        for protocol in self.application:
            if protocol:
                self.application = protocol
        self.data = data[8:]


        if self.application:
            if self.application['description'].lower() == "http":
                # "http stuff here" 
                "http stuff here" 
            if self.application['description'].lower() == "bootstrap protocol server":    
                self.bootppacket = BOOTPPACKET(self.data)
    
    def show(self): 
        print("")
        self.showText("Udp Datagram",4)
        self.showText("source \t: (port) "+str(self.src),5)
        self.showText("destination \t: (port) "+str(self.dst),5)
        print()
        if self.application:
            if self.application['description'].lower() == "domain name server" :
                self.showText(self.application['description'] + "{}".format("REQUEST" if self.dst == self.application['port number'] else " RESPONSE"),5) 
                data = DNSRecord.parse(self.data)
                for line in str(data).split("\n"):
                    self.showText(line,6)
            elif self.application['description'].lower() == "bootstrap protocol server":
                self.bootppacket.show()
            else:
                self.showText(self.application['description'] + "{}".format("REQUEST" if self.dst == self.application['port number'] else " RESPONSE") )
        else:
            self.showText(hexlify(self.data),6)

        print()
        print()
    
    def showText(self,text,indent=0):
        print('\t'*indent,text)

learnPorts(UDPDATAGRAM)