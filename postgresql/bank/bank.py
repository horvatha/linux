#! /usr/bin/python
# coding: utf-8

"""Egy mintaprogram bankszámlák kezelésére.

Használata előtt a
$ psql -f bank.sql
utasítás létrehozza a megfelelő táblázatokat, függvényeket.

Feladatok:

1. A számlanyitás, be/kifizetés és a betétesek lekérdezésének megírása.

2. Egy számbekérő függvény készítése lásd: egesz_be leírása.

3. A függvények átírása, hogy az előbbi függvényt használják pénzösszegek bekérésére.

4. Alakítsuk át a menüt, hogy mindig új feladatot csinál (menüsorszámot kér), amig a kilépést
    nem választjuk.

5. Tegyünk be egy kivételkezelést az atutal (és többi) függvényhez a cursor.execute részhez.
  Pl. ha valamelyik eléri a -20000 Ft-os határt, akkor nem tud végrehajtódni a PostgreSQL átutal parancsa.
"""

# python-pygresql csomag kell hozzá
# (apt-get install python-pygresql)

# http://www.pygresql.org/pgdb.html

import pgdb
# Ha más adatbázis van, akkor csak ezt a sort kell változtatni. Pl:
# import oracledb

connection = pgdb.connect(database='diak', user='diak', password='diak')

def menu():
    print "-"*20, "\nHiper-szuper bankszámla-nyilvántartó program\n", "-"*20
    menulist=("Átutalás", "Új számla", "Befizetés", "Kifizetés", "Betétesek listája", "Kilépés")
    numbers = range(1, len(menulist) +1)
    for i in numbers:
	print i, menulist[i-1]
    print "-" *20
    num=raw_input("Add meg a kívánt menüpont sorszámát! ")

    while 1:
	try:
	    num=int(num)
	    if num in numbers:
		break
	except ValueError:
	    num=raw_input("Hibás adat. Add meg a kívánt menüpont sorszámát!")
    
    if num == 1:
	atutal()
    elif num == 2:
	uj_szamla()
    elif num == 3:
	befizet(irany="be")
    elif num == 4:
	befizet(irany="ki")
    elif num == 5:
	betetesek()
    elif num == 6:
	return

def atutal():
    '''Átutal egy banki számláról a másik számlára. Az adatokat bekéri.'''
    cursor = connection.cursor()
    print "Erről a számláról:"
    errol = szamla_kereses()
    print "-"*20
    print "Erre a számlára:"
    erre = szamla_kereses()
    osszeg = raw_input("Átutalandó összeg: ")
    cursor.execute("SELECT átutal(%d,%d,%s)" % (errol, erre, osszeg))
    connection.commit()
    print "Átutaltam a\n%d számláról\n%d számlára\n%s forintot." % (errol, erre, osszeg)

def uj_szamla():
    '''Létrehozza egy ügyfél új számláját. Nevet, címet, számlaszámot bekéri.
    Fejlettebb változatban a számlaszám a legkisebb még nem létező számlaszám.'''
    pass

def befizet(irany="be"):
    '''Létrehoz egy befizetést (ill. ki irány esetén kifizetést) egy számlára
    (számláról). Az adatokat bekéri.'''
    pass

def betetesek():
    '''Listázza a betéteseket.'''
    pass

def szamla_kereses():
    while 1:
	nev = raw_input("Adja meg a számlatuljadonos nevének egy részét (kis/nagybetű számít)! ")
	cursor = connection.cursor()
	cursor.execute("""SELECT * FROM személyes_adatok
	    WHERE név ~ '%s'""" % nev)
	szamlak = cursor.fetchall()
	print "%d ilyen számla van." % len(szamlak)
	for szamla in szamlak:
	    nev, cim, szamlaszam  = szamla
	    print nev, cim, szamlaszam
	    ezaz = raw_input("Ezt kereste? (i/n) ")
	    if ezaz.lower() in ("i", "y"):
		return szamlaszam

def egesz_be(max, min=1, text="", n=4):
    """min és max közötti egész számot kér be. Hibás bekérésnél újból kérdez.
    (A menu függvényben volt ilyen már.)

    Fejlettebb változatban kiírja a szöveget és a határokat, pl:
    Mekkora összeget? (1-100000)

    Még fejlettebb változatban csak legfeljebb n-szer kérdez, azután kivételt ad.
    """
    pass # Ehelyett jön a programrész.


if __name__ == '__main__':
    menu()
