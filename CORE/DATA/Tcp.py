#!/usr/bin/env python3
from binascii import hexlify
from codecs import decode as codecode
from struct import unpack
from .learn import *
from .Http import HTTPPAYLOAD
class TCPSEGMENT:


    ports = []

    def __init__(self,data):
        """
            INIT TCP SEGMENT :
            TAKES RAW TCP DATA , PARSES IT AND RETURNS A TCP SEGMENT WITH HEADERS FLAGS, AND THE DATA
            TYPE help(TCPSEGMENT) for more info
        """
        src,dst,seqnum,acknum,offsetreservedflags = unpack("!2H2LH",data[:14])
        hlen = (offsetreservedflags >> 12) * 4
        urg = (offsetreservedflags & 32) * 5
        ack = (offsetreservedflags & 16) * 4
        psh = (offsetreservedflags & 8) * 3
        rst = (offsetreservedflags & 4) * 2
        syn = (offsetreservedflags & 2) * 1
        fin = (offsetreservedflags & 1)

        self.src = src
        self.dst = dst
        self.seqnum = seqnum
        self.acknum = acknum
        self.hlen = hlen
        self.urg = urg
        self.ack = ack
        self.syn = syn
        self.rst = rst
        self.fin = fin
        self.psh = psh
        self.data = data[hlen:]
        self.application = [getPortByNumber(self,str(self.src)),getPortByNumber(self,str(self.dst))]
        for protocol in self.application:
            if protocol:
                self.application = protocol
        if type(self.application) != list:
            try :
                if self.application["port number"]:
                    self.application['port number'] = int(self.application['port number'])

                    if self.application['description'].lower() == "http":
                        self.httppayload = HTTPPAYLOAD(self.data,"REQUEST" if self.dst == self.application['port number'] else " RESPONSE")
                
                else:
                    print('ki nena')
                    print(self.application['description'].lower())
            except TypeError as e:
                print(e)
                print(self.application)
    def show(self):
        print("")
        self.showText("-Tcp Segment",4)
        self.showText("source \t: (port) "+str(self.src),5)
        self.showText("destination \t: (port) "+str(self.dst),5)
        print()
        print()

        try :
            if type(self.application) is not list and self.application["port number"]:

                self.showText(self.application['description'] + "{}".format("REQUEST" if self.dst == self.application['port number'] else " RESPONSE") )

                if self.application['description'].lower() == "http":
                    self.httppayload.show()
                else:
                    print(self.application['description'].lower())
                    data = self.data
                    self.showText(hexDataToString(hexlify(data).decode()),1)
                # data = [data.headers(),data.body_file.read()]
            else:
                data = self.data
                self.showText(hexDataToString(hexlify(data).decode()),1)
        except TypeError as e:
            print(e)

        print()
        print()
    def showText(self,text,indent=0):
        print('\t'*indent,text)



learnPorts(TCPSEGMENT)
