#!/usr/bin/env python3
from netifaces import *
from os import system
def clearScreen():
	system("clear")
class IFACES:
	ifaces   = interfaces()
	defaultgateway,gateways = gateways()
	addrs    = {}
	selectedIFACE = 0
	def __init__(self):
		self.updateIFACES()
	def updateIFACES(self):
		self.ifaces   = interfaces()
		defaultgateway,Gateways = gateways()
		self.defaultgateway = defaultgateway
		self.gateways = gateways()[2]
		self.addrs    = self.updateADDRS()
	def updateADDRS(self):
		addrs = {"default":"empty"}
		for iface in self.ifaces:
			addrs[iface]=ifaddresses(iface)
		return addrs
	def showIFACES(self):
		global n
		n = 1
		def showIface(IF):
			global n
			print(n,IF)
			n = n + 1
		[showIface(IF) for IF in (self.ifaces)]
		return n
	def getByName(self,name):
		found = None
		for iface in self.ifaces:
			if iface == name:
				found = iface
		return found
	def selectIFACE(self):
		print("SELECT YOUR INTERFACE")
		print("default one:",self.ifaces[0])
		l = self.showIFACES()
		selection = self.promptNumber()
		badTries = 5
		while selection == None or selection not in range(len(self.ifaces)+n):
			badTries-=1
			if(badTries == 0):
				badTries = 5
				clearScreen()
			print("BAD CHOICE RETRY")
			selection = self.promptNumber()
		self.selectedIFACE = selection
	
	def promptNumber(self):
		ret = None
		try :
			ret = int(input("=~>"))
		except ValueError :
			ret = None
		return ret

	def getActualIFACE(self):
		return self.ifaces[self.selectedIFACE]

	def getActualAddrs(self):
		return self.addrs[self.getActualIFACE()]

	def getActualIp(self):
		return self.getActualAddrs()[AF_INET]

	def getActualMac(self):
		return self.getActualAddrs[AF_LINK]

	def getActualGateway(self):
		gateway = None
		for gtw in self.gateways:
			if gtw[1] == self.getActualIFACE():
				gateway = gtw
			else: print(self.getActualIFACE())
		return gateway

	

