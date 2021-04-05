from struct import pack,unpack
from ipaddress import IPv4Address,IPv6Address
from binascii import hexlify
from .learn import *
from .Tcp import TCPSEGMENT
from .Udp import UDPDATAGRAM
class IPPACKET:

    protocols = []

    def getProtoByHexCode(self,hexcode):
        ret = None
        for protocol in self.protocols:
            if protocol['hexcode'] == hexcode:
                ret = protocol
        return ret

    def __init__(self,data):
      
        details = data[:1]
        version,ihl = hexlify(details).decode()[0],hexlify(details).decode()[1]
        self.version = version
        self.ihl = int(ihl)
        self.protocol = "0x"+hexlify(data[9:10]).decode()
        self.src = f"{IPv4Address(data[12:16]):s}"
        self.dst = f"{IPv4Address(data[16:20]):s}"
        self.data = data[int(self.ihl*4):]
        
        #check tcp
        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "tcp":
            self.tcpsegment = TCPSEGMENT(self.data)
        #check udp
        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "udp":
            self.udpdatagram = UDPDATAGRAM(self.data)


    def show(self): 
        self.showText("* source \t: (ip) "+self.src,3)
        self.showText("* destination \t: (ip) "+self.dst,3)
        self.showText("* version \t: "+self.version,3)
        self.showText("* protocol \t: "+self.getProtoByHexCode(self.protocol)['keyword'],3)

        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "tcp":
            self.tcpsegment.show()

        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "udp":
            self.udpdatagram.show()
        

    def showText(self,text,indent=0):
        print('\t'*indent,text)


class IP6PACKET:

    protocols = []

    def getProtoByHexCode(self,hexcode):
        ret = None
        for protocol in self.protocols:
            if protocol['hexcode'] == hexcode:
                ret = protocol
        return ret


    def __init__(self,data):
        details = data[:1]
        version,ihl = hexlify(details).decode()[0],hexlify(details).decode()[1]
        self.version = version
        self.ihl = ihl
        if(hexlify(data[16:20]) != b"\x00\x00\x00\x00"):
            self.src = f"{IPv6Address(data[16:32]):s}"
        else:
            self.src = "::::::::"
        if(hexlify(data[20:24]) != b"\x00\x00\x00\x00"):
            self.dst = f'{IPv6Address(data[32:48]):s}'
        else:
            self.dst = "::::::::"

        self.data = data[24:]


    def show(self): 
        self.showText("* source \t: "+self.src,3)
        self.showText("* destination \t: "+self.dst,3)
        self.showText("* version \t: "+self.version,3)
        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "tcp":
            self.tcpsegment.show()

        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "udp":
            self.udpdatagram.show()


    def showText(self,text,indent=0):
        print('\t'*indent,text)

learnProtos(IPPACKET)
learnProtos(IP6PACKET)