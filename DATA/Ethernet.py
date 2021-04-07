from binascii import hexlify
from .Ip import IPPACKET,IP6PACKET
from .Arp import ARPPACKET
class ETHERNETFRAME:


    def cleanMac(self,mac):
        dirtmac = hexlify(mac).decode()
        cleanmac = ""
        n = 0
        for letter in dirtmac:
            if n == 2:
                cleanmac += ":"
                n = 0
            cleanmac += letter
            n+=1
        return cleanmac


    def __init__(self,data):
        self.data = data[14:]
        self.src = self.cleanMac(data[:6])
        self.dst = self.cleanMac(data[6:12])
        self.type_ = hexlify(data[12:14]).decode()
        self.setPacketType()
        self.setPayload()

    def setPayload(self):
        if self.datatype == 'ip':
            self.payload = IPPACKET(self.data)
        if self.datatype == 'ip6':
            self.payload = IP6PACKET(self.data)
        if self.datatype == 'arp':
            self.payload = ARPPACKET(self.data)

    def show(self):
        # print("/==-----------------------------------------------|")
        self.showText("- Ethernet\t:")
        self.showText("* source   \t: (mac) "+self.src,1)
        self.showText("* destination \t: (mac) "+self.dst,1)
        self.showText("* appendix \t: "+self.type_,1)
        print()
        if hasattr(self,"payload"):
            self.showText("\t"+"- "+self.datatype+" packet",1)
            self.payload.show()

        # print("\-----------------------------------------------==/")
    def showText(self,text,indent=0):
        print('\t'*indent,text)

    def setPacketType(self):
        self.datatype = self.checkPacketType()

    def checkPacketType(self):
        ethernettype = ""
        if self.type_ == "0806":
            ethernettype = "arp"
        if self.type_ == "0800":
            ethernettype = "ip"
        if self.type_ == "86dd":
            ethernettype = "ip6"
        return ethernettype
