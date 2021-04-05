#!/usr/bin/env python3
from binascii import hexlify
from struct import unpack
from .learn import *
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
        if self.application:
            if self.application['description'].lower() == "http":
                # "http stuff here" 
                "http stuff here" 
        self.data = data[8:]
    def show(self): 
        print("")
        self.showText("Udp Datagram",4)
        self.showText("source \t: (port) "+str(self.src),5)
        self.showText("destination \t: (port) "+str(self.dst),5)
        print()
        print()
        if self.application:
            self.showText(self.application['description'] + "{}".format("REQUEST" if self.dst == self.application['port number'] else " RESPONSE") )
        if self.application['description'].lower() == "domain name server" :
            data = DNSRecord.parse(self.data)
            for line in data:
                self.showText(line,1)
        else:
            self.showText(hexlify(self.data),1)

        print()
        print()
    
    def showText(self,text,indent=0):
        print('\t'*indent,text)

learnPorts(UDPDATAGRAM)