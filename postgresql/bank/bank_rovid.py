#! /usr/bin/python
# coding: utf-8
from __future__ import division

"""Egyszerű program az adatbázis elérésére Pythonból."""

# python-pygresql csomag kell hozzá
# (apt-get install python-pygresql)

# http://www.pygresql.org/pgdb.html

import pgdb
# Ha más adatbázis van, akkor csak ezt a sort kell változtatni. Pl:
# import oracledb

connection = pgdb.connect(database='diak', user='diak',
		    password='diak', dsn='mail.roik.bmf.hu')

cursor = connection.cursor()
cursor.execute("SELECT * FROM betétesek;")
connection.commit() # Csak SELECT parancs esetén nem fontos

lekert_adatok = cursor.fetchall()

for nev, cim, egyenleg in lekert_adatok:
    print nev, cim, egyenleg
    #print nev.left(20), cim.left(20), egyenleg.left(
    #print "%(nev)20s | %(cim)20s | %(egyenleg)5s" % vars()

