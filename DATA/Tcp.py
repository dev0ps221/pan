#!/usr/bin/env python3
from binascii import hexlify
from codecs import decode as codecode
from struct import unpack
from .learn import *
from http_parser.http import HttpStream
class TCPSEGMENT:


    ports = []

    def __init__(self,data):




        src,dst,seqnum,acknum,offsetreservedflags = unpack("!2H2LH",data[:14])
        
        # urg,ack,psh,rst,syn,fin = map(lambda x : [n for n in x],flags)
        # window = interm[6:]
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
        if self.application:
            if self.application['description'].lower() == "http":
                # "http stuff here" 
                "http stuff here" 
    def show(self): 
        print("")
        self.showText("-Tcp Segment",4)
        self.showText("source \t: (port) "+str(self.src),5)
        self.showText("destination \t: (port) "+str(self.dst),5)
        print()
        print()
        if self.application:
            self.showText(self.application['description'] + "{}".format("REQUEST" if self.dst == self.application['port number'] else " RESPONSE") )
        
        if self.application['description'] == "http":
            data = HttpStream(self.data)
            data = [data.header(),data.body_file.read()]
        else:
            data = self.data
        self.showText(hexlify(data),1)

        print()
        print()
    def showText(self,text,indent=0):
        print('\t'*indent,text)



learnPorts(TCPSEGMENT)