#!/usr/bin/env python3

class Sniffer:


    run = True
   

    
    def handlePacket(packet):
        data = packet.original
        packet = ETHERNETFRAME(data,packet)
        showText("- PACKET -")
        # print(data)
        packet.show()
        # showText("- HEXADECIMAL DUMP -")
        print()
        # hexdump(data)
        showText("- Tek-Tech 2021 -",5)
        print()
        print()
        [print() for n in range(3)]
        sleep(0.5)




    def get_handler(self):
        return self.handler if hasattr(self,'handler') else self.handlePacket

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


    def __init__(self,handler=None):
        self.handler = handler
        