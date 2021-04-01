from struct import pack
from ipaddress import IPv4Address,IPv6Address
from binascii import hexlify
from .learn import *
class IPPACKET:
    protocols = []
    def __init__(self,data):
        self.src = f"{IPv4Address(data[12:16]):s}"
        self.dst = f"{IPv4Address(data[16:20]):s}"
        
        self.data = data[20:]


    def show(self): 
        self.showText("source \t: "+self.src,3)
        self.showText("destination \t: "+self.dst,3)

    def showText(self,text,indent=0):
        print('\t'*indent,text)


class IP6PACKET:
    def __init__(self,data):

        if(hexlify(data[16:20]) != b"\x00\x00\x00\x00"):
            self.src = f"{IPv6Address(data[16:20]):s}"
        else:
            self.src = "::::::::"
        if(hexlify(data[20:24]) != b"\x00\x00\x00\x00"):
            self.dst = f'{IPv6Address(pack("<L",hexlify(data[20:24]))):s}'
        else:
            self.dst = "::::::::"
        self.data = data[24:]


    def show(self): 
        self.showText("source \t: "+self.src,3)
        self.showText("destination \t: "+self.dst,3)

    def showText(self,text,indent=0):
        print('\t'*indent,text)
learnProtos(IPPACKET)