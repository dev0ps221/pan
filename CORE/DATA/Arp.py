from socket import inet_ntoa,inet_ntop
from binascii import hexlify
class ARPPACKET:

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
        self.htype = hexlify(data[:2]).decode()
        self.ptype = hexlify(data[2:4]).decode()
        self.hal = hexlify(data[4:5]).decode()
        self.pal = hexlify(data[5:6]).decode()
        self.op = hexlify(data[6:8]).decode()
        self.setOPType()
        hal  = self.hal
        pal = self.pal
        self.srcmac = self.cleanMac(data[8:8+int(hal)])
        self.src = inet_ntoa(data[12+int(hal):12+int(hal)+int(pal)])
        self.dstmac = self.cleanMac(data[12+int(hal)+int(pal):12+(int(hal)*2)+int(pal)])
        self.dst = inet_ntoa(data[12+(int(hal)*2):12+(int(hal)*2)+(int(pal))])
        self.data = data[24+int(self.hal):]

    def setOPType(self):
        if (self.op == "0001"):
            self.optype = 'REQUEST'
        else:
            self.optype = 'REPLY'


    def show(self):
        self.showText(self.optype,3)
        print()
        if(self.optype == 'REQUEST'):
            self.showText(""+self.src+" demande a "+self.dst+" :",2)
            print()
            self.showText("ou est "+self.srcmac+" ?",4)
            print()
        if(self.optype == 'REPLY'):
            self.showText(""+self.src+" fait savoir a "+self.dst+" que :",2)
            print()
            self.showText(self.src+" est a "+self.srcmac,4)
            print()


    def showText(self,text,indent=0):
        print('\t'*indent,text)
