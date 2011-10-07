#!/usr/bin/env python
# coding: utf-8
from __future__ import division
#Ezelőttieket ne változtassuk

a=7
print a
print 7/3 # Íme, most nem egész az eredmény (3. sor eredménye)

a=2
while a < 30:
    a = 2*a
    print a

#####################
# Vezérlőszerkezetek
#####################

# if a<4:
#     <valami>
# elif a<8:
#     <valami más>
# else:
#     <mégmásabb>

# for i in lista:

# while a<1000:

# def valami():

# class Valami():

#####################
# Adattípusok
#####################

# a=5 # Egész
# a=2.5 # Lebegőpontos (valós)
# a=2+3j # komplex

# s= 'Sztring = karakterlánc '
# print s*5
# s="Sztring: Pythonban ez is jó"
# s="Egyikfajta idézőjel 'levédi' a másikat."

# t=(1, 3, 'valami')   # nem változtatható (tuple)
# l=[1, 4+3j, 'lista'] # változtatható (lista)
# print l[0]  # A 0. az első elem, az 1.

# d={"Józsi": "22/333-444", "Peti": "20/344-443"} # szótár {kulcs: érték}
# print d["Józsi"]


#####################
# Pár egyéb
#####################

# Fromátumsztring használata (mint C-ben)
# print "%d darab %s" % (5, "alma")

# Hogy direktbe futtatva a fájlt menjen, de modulként hívva ne:
# if __name__ == "__main__":
#     <a kívánt programrész, pl. teszt>
