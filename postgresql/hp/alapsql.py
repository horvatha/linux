#!/usr/bin/env python
# encoding: utf-8

"""
PostgreSQL-adatok lekérdezése Python-CGI-ből.
"""

import cgi
import cgitb; cgitb.enable()  # A hibafigyeléshez (debug) kell
import pgdb # PostgreSQL adatbázis kezeléséhez kell.
from htmltabla import html_tablazat, html, fejlec

print "Content-Type: text/html\n" ## CGI


# Itt lehet állítani az adatbázist:
connection = pgdb.connect(database='diak', user='diak', password='diak', dsn='django.arek.uni-obuda.hu')

cursor = connection.cursor()

# Itt lehet az utasítást megadni:
#cursor.execute("""INSERT INTO szemelyek (nev) VALUES ('Igor Karkarov');""")
cursor.execute("""SELECT * FROM adatok;""")
# order by, where

# Ez akkor kell, ha az adatbázist módosítjuk (UPDATE, INSERT, DELETE). Lekérdezésnél nem kell.
connection.commit()

eredmeny = cursor.fetchall()

print fejlec
print "<h1>Képek a Harry Potter filmekből</h1>"

tablafejlec = ['Név', 'Kép', 'Képfelirat', 'Anyja neve', 'Apja neve']
print "\n".join(html_tablazat(eredmeny, fejlec=tablafejlec))

for tabla in "szemelyek kepek kepek_szemelyek".split():
    print html(tabla, connection)


print "</body>\n</html>"