#!/usr/bin/env python
# -*- encoding: utf-8 -*-
""" szamok modul
  A számokat követő hangrendfüggő ragok kezeléséhez ad segítséget.

  Horváth Árpád, horvath.arpad.szfvar@gmail.com, 2001,2012."""

from __future__ import print_function
import string

alap_ragok = ['szer','es','nek','nél','én','e']

def hangrend(n):
    """ hangrend(n) --> (típus, változat)

      Az n egész számot követő rag hangrendjét adja vissza:
        típus - 'magas','mély','változó'
        változat - ezek különböző ragú csoportjai

    ('magas', 1)  pl. 7-es -szer -nek -én
    ('magas', 2)      5-ös! -ször!
    ('magas', 3)      1-jén!

    ('mély', 1)  pl. 3-as -szor -nak -án
    ('mély', 2)  6-os!

    ('változó', 1)  2-án  2-szer"""

    assert isinstance(n, int), "a számnak egésznek kell lennie"

    if n < 0:
        n = -n

    if n % 1000000 == 0:  #millió milliárd trillió...
        return ('mély', 1)

    if n % 1000 == 0:
        return ('magas', 1)

    if n % 100 == 0:
        return ('mély', 1)

    if n % 10 == 0:   # Tízzel osztahtó
        vege = n % 100  # Utolsó két számjegy
        if vege in [10, 40, 50, 70, 90]:
          return ('magas', 1)
        else:  return ('mély', 1)

    if n == 1:
        return ('magas', 3)

    if n == 2:
        return ('vegyes', 1)

    vege = n % 10   # Utolsó számjegy
    if vege == 5: return ('magas', 2)
    if vege == 6: return ('mély', 2)
    if vege in [1, 2, 4, 7, 9]:
        return ('magas', 1)
    else: return ('mély', 1)

def ragos(n, rag):
    """ragos(n, rag) --> ragos_szám
    Ragozza a számot.
    pl.  a ragos(6, 'szer') eredménye '6-szor'.
    A rag az e (é) betűs alakkal adható meg:
    'szer','es','nek','nél','én','e'"""

    ragok = {
        ('magas', 1) : ['szer','es','nek','nél','én','e'],
        ('magas', 2) : ['ször','ös','nek','nél','én','e'],
        ('magas', 3) : ['szer','es','nek','nél','jén','je'],

        ('mély', 1) : ['szor','as','nak','nál','án','a'],
        ('mély', 2) : ['szor','os','nak','nál','án','a'],

        ('vegyes', 1) : ['szer','es','nek','nél','án','a'],
    }
    
    if rag in alap_ragok:
        sorszam = alap_ragok.index(rag)
        kulcs = hangrend(n)
        rag = ragok[kulcs][sorszam]
        return "-".join([str(n), ragok[kulcs][sorszam]])
    else:
        raise ValueError, 'a rag értéke hibás'

import time
def example():
    """ Ez a tesztfüggvény indul el, ha közvetlenül futtatjuk a fájlt."""

    print(" ".join('%d %s hangrendű.' % (n, hangrend(n)[0])
           for n in [1025, 3, 7, 80]),
           end="\n\n")

    print(ragos(6, 'szer'), ragos(1, 'én'), ragos(5, 'es'), ragos(1000000, 'nek'),
            end="\n\n")

    ido = time.localtime(time.time())
    napsorszam = ido[2]
    print('Ma %s van.' % ragos(napsorszam, 'e'))

def test():
    ragok = ['szer','es','nek','nél','én','e']
    ismert_eredmenyek = (
        (1, "1-szer 1-es 1-nek 1-nél 1-jén 1-je"),
        (2, "2-szer 2-es 2-nek 2-nél 2-án 2-a"),
        (3, "3-szor 3-as 3-nak 3-nál 3-án 3-a"),
        (4, "4-szer 4-es 4-nek 4-nél 4-én 4-e"),
        (5, "5-ször 5-ös 5-nek 5-nél 5-én 5-e"),
        (6, "6-szor 6-os 6-nak 6-nál 6-án 6-a"),
        (7, "7-szer 7-es 7-nek 7-nél 7-én 7-e"),
        (8, "8-szor 8-as 8-nak 8-nál 8-án 8-a"),
        (9, "9-szer 9-es 9-nek 9-nél 9-én 9-e"),
        (10, "10-szer 10-es 10-nek 10-nél 10-én 10-e"),
        (20, "20-szor 20-as 20-nak 20-nál 20-án 20-a"),
        (30, "30-szor 30-as 30-nak 30-nál 30-án 30-a"),
        (11, "11-szer 11-es 11-nek 11-nél 11-én 11-e"),
        (500, "500-szor 500-as 500-nak 500-nál 500-án 500-a"),
        (1000, "1000-szer 1000-es 1000-nek 1000-nél 1000-én 1000-e"),
        )

    for szam, eredmenyek in ismert_eredmenyek:
        for alap, eredmeny in zip(alap_ragok, eredmenyek.split()):
            visszaadott = ragos(szam, alap) 
            if  visszaadott != eredmeny:
                print("Nem egyezik a megadott érték a visszatérésivel:", eredmeny, visszaadott)
            assert ragos(szam, alap) == eredmeny
    print("A teszt sikeresen lefutott.")

if __name__ == '__main__':
    test()
    example()
