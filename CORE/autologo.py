#!/usr/bin/env python3
from os import get_terminal_size,system
from math import ceil
from time import sleep
import cursor
hide_cursor,show_cursor = cursor.hide,cursor.show

hide_cursor()
minSize = 17
minSizeH = 7
Size=16
size = ceil(get_terminal_size().columns*Size/100)
sizeH = ceil(get_terminal_size().lines*Size/100)
def clear():
	system('clear')
def logo(Size=16,Marg=0):
	size = ceil(get_terminal_size().columns*Size/100)
	sizeH = ceil(get_terminal_size().lines*Size/100)
	size = minSize if size < minSize else size
	sizeH = minSizeH if sizeH < minSizeH else sizeH
	def prctDeSize(prct,H=None):
		return ceil(prct*(size if H == None else sizeH)/100)
	margin		= prctDeSize(24)
	longT		= prctDeSize(39)
	largT		= prctDeSize(34,1)
	longTail	= prctDeSize(45)
	largTail	= prctDeSize(45)
	heart		= prctDeSize(50)
	largExp 	= f'{" "*margin}{"■"}{" "*heart}{"███"}'
	revLargExp 	= f'{" "*(margin-1)}{"███"}{" "*heart}{"■"}'
	longExp		= f'{" "*margin}{"■"*longT}{"█"*longT}'
	revLongExp	= f'{"█"*longT}{"■"*(longT+1)}'
	def showCentered(expr,ssize=None):
		half = " "*ceil((get_terminal_size().columns - (size if ssize == None else size))/2)
		expr = " "*ceil((ssize-len(expr))/2)+expr if ssize else expr
		print(f'{half}{expr}{half}')
	def show(s=None):
		clear()
		print("\n"*ceil((get_terminal_size().lines-sizeH)/3))
		[showCentered(longExp,s) for n in range(1)]
		[showCentered(largExp,s) for n in range(ceil((largT)/2))]
		[showCentered(revLargExp,s) for n in range(ceil((largT)/2))]
		[showCentered(revLongExp,s) for n in range(1)]
	show()
def showCentered(expr,ssize=None,end='\n'):
	ssize = (size if ssize == None else size)
	half = " "*ceil((get_terminal_size().columns - ssize)/2)
	expr = " "*int((ssize-len(expr))/2)+expr if ssize else expr
	bs = '\b'
	expr = f"{bs*ceil((len(expr)-ssize)/2)}{expr}" if len(expr) > ssize else expr
	print(f'{half}{expr}{half}',end=end)
anim = [l for l in range(20)]
anim.reverse()
for l in anim:
	logo(Size+l)
	sleep(l/((l/20)+1)/100)
print("\n"*2)
showCentered("TEK-TECH",size)
showCentered("Et Si On Parlait Technologies",size)
print("\n"*ceil((get_terminal_size().lines-sizeH)/4))
showCentered("░Entree pour Commencer░",size,end='\b')
input("\b\b\b")
clear()
show_cursor()
