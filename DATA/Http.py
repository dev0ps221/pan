#!/usr/bin/env python3
import urllib3
from io import BytesIO
from http.client import HTTPResponse
from binascii import hexlify
from .learn import hexDataToString
class BytesIOSocket:
    def __init__(self, content):
        self.handle = BytesIO(content)

    def makefile(self, mode):
        return self.handle

def response_from_bytes(data):
    sock = BytesIOSocket(data)

    try :
        response = HTTPResponse(sock)
        response.begin()
        return urllib3.HTTPResponse.from_httplib(response)
    except Exception as e:
        print(e)

def request_from_bytes(data):
    sock = BytesIOSocket(data)

    try :
        request = HTTPRequest(sock)
        request.begin()
        return urllib3.HTTPRequest.from_httplib(request)
    except Exception as e:
        print(e)


class HTTPPAYLOAD:

    def __init__(self,data,type_=""):
        self.type = type_
        # headers,data = response_from_bytes(hexlify(data))
        # self.headers = headers
        self.data = data


    def show(self):
        print("")
        self.showText("- HTTP PAYLOAD ",5)
        # self.showText("* HEADERS \t:  "+str(self.headers),6)
        print("length : ",len(self.data))
        self.showText("* DATA \t:  "+hexDataToString(hexlify(self.data).decode("utf")),6)
        print()

    def showText(self,text,indent=0):
        print('\t'*indent,text)
