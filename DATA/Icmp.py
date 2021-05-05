#!/usr/bin/env python3
from binascii import hexlify

class ICMPPACKET:
    def __init__(self,data):
        type_,code,checksum,authcode,unused,id,seqnum = unpack("!HHQ3s13sQQ",data[:12])
        self.type = hexlify(type_)
        self.code = hexlify(code)
        self.checksum = hexlify(checksum)
        self.authcode = hexlify(authcode)
        self.unused = hexlify(unused)
        self.id = hexlify(id)
        self.seqnum = hexlify(seqnum)
        self.data = data[12:]

    def show(self):
        print()
        self.showText("ICMP DATA",3)
        print()
        self.showText(self.data,4)
        print()

    def showText(self,text,indent=0):
        print('\t'*indent,text)
