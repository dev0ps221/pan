#!/usr/bin/env python3

class Sniffer:


    run = True

    def get_handler(self):
        return self.handler if hasattr('handler',self)

    def start(self):
    
        while self.run:
            try:
                sniff(prn=self.get_handler())
                # handlePacket(listener.recv(65565))
                # sleep(0.5)
            except KeyboardInterrupt:
                self.run = False
            except Exception as e:
                print(e)


    def __init__(self,handler):
        self.handler = handler
        