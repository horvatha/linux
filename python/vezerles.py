#!/usr/bin/env python
# coding: utf-8
"""Első ismerkedés a Python ciklusaival és pár egyéb dologgal.

Az első sor megadja, hogy milyen értlemező értelmezze a kódot a héj (shell) helyett.
    Ezt még a  bash értlemezi.

A második sor megadja a fájl karakterkódolását. Ez a Python értelmezőjének kell.

Az egyjegyű szám kezelésénél a kivételkezeléssel ismerkedhetünk meg. Ha a try ágban kivétel lép fel, akkor az except
ág hajtódik végre.

A factorial egy példa függvénydefinícióra. Benne láthatunk egy if-else szerkezetet.
"""

answer = raw_input("Kezdhetem? (i/n) ")
if answer[0] in "iIyY":
	print "Kezdem."
elif answer[0] in "nN":
	print "Csakazértis kezdem."
else:
	print "Nem értem a választ. Azért csak folytatom."

a=13
while -50 < a < 30:
	print a
	a += 3

while 1:
	answer = raw_input("Kérek egy egyjegyű pozitív számot! ")
	try:
		answer = int(answer)
	except ValueError:
		print "Nem (valós) szám. Adjon meg pozitív egészet!"
		continue
	if answer not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
		print "Az egész szám nem egyjegyű vagy nem pozitív!"
		continue
	print "Köszönöm!"
	break

def factorial(n):
    """Faktoriálist számol"""
    if n==0:
	return 1
    else:
	return factorial(n-1)*n

print "5 faktoriálisa", factorial(5)
