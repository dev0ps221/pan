#!/usr/bin/env python3
from  struct import unpack
class BOOTPPACKET:



    def __init__(self,data):
        opcode,hardtype,hardaddr,hopcount,transid,nsecs,unused,cliaddr,hostaddr,srvaddr,gtwaddr = unpack("!iiiiL2H4L",data[:24])
        self.opcode = opcode
        self.hardwaretype = hardtype
        self.hardwareaddress = hardaddr 
        self.hopcount = hopcount
        self.transactionid = transid
        self.numberofseconds = nsecs
        self.unused = unused
        self.clientip = cliaddr
        self.hostip = hostaddr
        self.serverip = srvaddr
        self.gatewayip = gtwaddr
        
    def show(self):
        print("")
        self.showText("- Bootstrap Protocol Datagram (BOOTP)",5)
        self.showText("* opcode \t:  "+str(self.opcode),6)
        # self.showText("destination \t: (port) "+str(self.dst),5)
        print()

    def showText(self,text,indent=0):
        print('\t'*indent,text)
