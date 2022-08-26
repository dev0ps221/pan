from flet import Text,Row,Column,app,Page


class PanUI:


    def handleSniffedPacket(self,packet):
        print(packet)

    def showMessage(self,message):
        print(message)

    def sniff(self):
        if self.hasSniffer():
            self.sniffer.sniff()

    def hasSniffer(self):
        return hasattr(self,'sniffer') and self.sniffer

    def setSniffer(self,sniffer=None):
        self.sniffer = sniffer
        self.sniffer.set_handler(self.handleSniffedPacket)

    def start_sniffing(self):
        self.sniffer.start()

    def build_ui_parts(self):
        self.ui_container = Column()
        self.ui_topbar = self.build_ui_top()
        self.ui_middlebar = self.build_ui_middle()
        self.ui_bottombar = self.build_ui_bottom()
        self.ui_container.controls = [
            self.ui_topbar,
            self.ui_middlebar,
            self.ui_bottombar
        ]
        self.ui_page.add(self.ui_container)
        self.ui_page.update()

    def build_ui_top(self):
        ui_top = Row()
        return ui_top
        
    def build_ui_middle(self):
        ui_middle = Row()
        return ui_middle

    def build_ui_bottom(self):
        ui_bottom = Row()
        return ui_bottom
        
    def ui_handler(self,page:Page):
        self.ui_page = page
        self.build_ui_parts()
        pass

    def __init__(self):
        self.app = app(target=self.ui_handler)