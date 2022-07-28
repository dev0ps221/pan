from socket import gethostbyaddr
from struct import pack,unpack
from ipaddress import IPv4Address,IPv6Address
from binascii import hexlify,unhexlify
from .learn import *
from .Tcp import TCPSEGMENT
from .Udp import UDPDATAGRAM
from .Icmp import ICMPPACKET
from kaitaistruct import KaitaiStream, BytesIO
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
        self.srchostname = ["unknown host"]
        self.dsthostname = ["unknown host"]
        try:
            self.srchostname = gethostbyaddr(self.src)
            self.dsthostname = gethostbyaddr(self.dst)
        except Exception :
            pass
        finally:
            self.srchostname = self.srchostname[0] if self.srchostname else "unknown host"
            self.dsthostname = self.dsthostname[0] if self.dsthostname else "unknown host"
        self.data = data[int(self.ihl*4):]

        #check tcp
        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "tcp":
            self.tcpsegment = TCPSEGMENT(self.data)
        #check udp
        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "udp":
            self.udpdatagram = UDPDATAGRAM(self.data)
        #check icmp
        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "icmp":
            self.icmppacket = ICMPPACKET(self.data)


    def show(self):
        self.showText("* source \t: (ip) "+self.src+"\t  (name) "+self.srchostname,3)
        self.showText("* destination \t: (ip) "+self.dst+"\t  (name) "+self.dsthostname,3)
        self.showText("* version \t: "+self.version,3)
        self.showText("* protocol \t: "+self.getProtoByHexCode(self.protocol)['keyword'],3)

        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "tcp":
            self.tcpsegment.show()

        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "udp":
            self.udpdatagram.show()


        if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "icmp":
            self.icmppacket.show()


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


        d = 
        print(d)




        details = data[:1]
        version,ihl = hexlify(details).decode()[0],hexlify(details).decode()[1]
        details = unpack('!s2s5s4s2s2s',data[:16])
        vers,prio,flo,plen,nh,hl=details
        self.version = version
        self.ihl = ihl
        sdata = hexlify(data).decode()
        vers,prio,flo,plen,nh,hl = sdata[0:3],sdata[4:11],sdata[12:31],sdata[32:47],sdata[48:55],sdata[56:63]
        print(details)
        print(len(sdata))
        if((sdata[64:72]) != "00000000"):
            srcstop = int(64+15)
            self.src = f"{IPv6Address(unhexlify(sdata[64:int(srcstop)]))}"
            self.protocol = "0x"+sdata[192:194]
            self.datastart = 194
            dststop = int(192+15)
            self.dst = f'{IPv6Address(unhexlify(sdata[192:int(dststop)]))}'
        else:
            self.src = "::::::::"
            self.dst = "::::::::"
            self.protocol = "0x"+sdata[72:74]
            self.datastart = 74

        self.srchostname = ["unknown host"]
        self.dsthostname = ["unknown host"]

        try:
            self.srchostname = gethostbyaddr(self.src)
            self.dsthostname = gethostbyaddr(self.dst)
        except Exception:
            pass
        finally:
            self.srchostname = self.srchostname[0] if self.srchostname else "unknown host"
            self.dsthostname = self.dsthostname[0] if self.dsthostname else "unknown host"

        self.data = unhexlify(sdata[194:])


    def show(self):
        self.showText("* source \t: (ip) "+self.src+"\t  (name) "+self.srchostname,3)
        self.showText("* destination \t: (ip) "+self.dst+"\t  (name) "+self.dsthostname,3)
        self.showText("* version \t: "+self.version,3)
        self.showText("* protocol \t: "+self.getProtoByHexCode(self.protocol)['keyword'].lower(),3)
        # if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "tcp":
        #     self.tcpsegment.show()
        #
        # if self.getProtoByHexCode(self.protocol)['keyword'].lower() == "udp":
        #     self.udpdatagram.show()
        print()
        self.showText("*IPV6 Payload",4)
        self.showText(self.data,5)


    def showText(self,text,indent=0):
        print('\t'*indent,text)

learnProtos(IPPACKET)
learnProtos(IP6PACKET)
