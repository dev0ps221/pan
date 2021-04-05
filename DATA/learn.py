filepref = (__file__.split("/"))
filepref.pop()
filepref = "/".join(filepref)+"/"
def learnProto(line):
    details = line.split(">")
    if len(details) > 4:
        hexcode,protonumber,keyword,protocol,rfc = details
    elif len(details) > 3:
            hexcode,protonumber,keyword,protocol = details
            rfc = "unknown"
    elif len(details) > 2:
            hexcode,protonumber,keyword = details
            rfc = "unknown"
            protocol = "unknown"
    elif len(details) > 1:
            hexcode,protonumber = details
            rfc = "unknown"
            protocol = "unknown"
            keyword = "unknown"
    else:
        hexcode = details[0]
        protonumber = "unknown"
        rfc = "unknown"
        protocol = "unknown"
        keyword = "unknown"
            
    proto = {
        "hexcode":hexcode,
        "protonumber":protonumber,
        "keyword":keyword,
        "protocol":protocol,
        "rfc":rfc
    }
    return proto
def learnProtos(self):
    self.learnProto = learnProto
    with open(filepref+"../protos") as protos:
        lines = protos.readlines()
        for line in lines:
            self.protocols.append(self.learnProto(line))

def getProtoByHexCode(self,hexcode):
    ret = None
    for protocol in protocols:
        if protocol['hexcode'] == hexcode:
            ret = protocol
    return ret

def getProtoByName(self,hexcode):
    ret = None
    for protocol in protocols:
        if protocol['hexcode'] == hexcode:
            ret = protocol
    return ret

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


def learnEthertypes(self):
    with open(filepref+"../etherTypes") as ethertypes:
        lines = ethertypes.readlines()
        labels = lines[0].split(",")
        lines  = lines[1:]
        ret = []
        for line in lines:
            etherType = {}
            line = line.split(",")
            n = 0
            for label in labels:
                if ")" in label.lower() and ")" in label.lower(): 
                    etherType[label.lower().split(")")[0].split("(")[1]] = line[n] if n < len(line) else "unknown" 
                else:
                    etherType[label.lower()] = line[n] if n < len(line) else "unknown"
                n+=1
            ret.append(etherType)
        return ret

def learnPorts(self):
    with open(filepref+"../ports") as ports:
        lines = ports.readlines()
        labels = lines[0].split(",")
        lines  = lines[1:]
        ret = []
        for line in lines:
            port = {}
            line = line.split(",")
            n = 0
            for label in labels:
                if ")" in label.lower() and ")" in label.lower(): 
                    port[label.lower().split(")")[0].split("(")[1]] = line[n] if n < len(line) else "unknown" 
                else:
                    port[label.lower()] = line[n] if n < len(line) else "unknown"
                n+=1
            ret.append(port)
        self.ports = ret
        return ret


def getEtherTypeByHex(self,hexcode):
    ret = None
    for etherType in self.etherTypes:
        if etherType['hex'] == hexcode: ret = etherType
    return ret
    
def getEtherTypeByName(self,name):
    ret = None
    for etherType in self.etherTypes:
        if etherType['name'] == name: ret = etherType
    return ret

def getPortByNumber(self,number):
    ret = None
    for port in self.ports:
        if port['port number'] == number: ret = port
    return ret
    
    