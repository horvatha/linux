#! /usr/bin/env python
# -*- encoding: utf-8 -*-
r'''Szövegkezelés és reguláris kifejezések a Pythonban

metakarakterek: . ^ $ * + ? { [ \ | ( )

Ellentétben a Vimmel a (, { és + karakterek elé nem kell \
Legtöbb nyelvnél a reguláris kifejezések között max ennyi különbség van.
Van ahol a {n,m} és + lehetőség hiányzik.

Tanulományozzuk sorban a függvényeket, azt a függvényt, amelyet
vizsgálunk, alul vegutf-8 ki a megjegyzésből (#). A megjegyzésben lévő
feladatokat hajtsuk végre.

Kis összefoglaló:
. egy karakter
$ sorvégre illeszkedik
* előző karakter(csoport) 0 vagy több előfordulása
+ előző karakter(csoport) 1 vagy több előfordulása
{n,m} előző karakter(csoport) n és m közötti számú előfordulása (n vagy m hiányozhat)
? előző karakter(csoport) esetleges előfordulása
[ karaktercsoportokat kezd [A-Z]
^ szögletes zárójelben ellentettjére változtat [^A-Z] =nem nagybetűk
\ levédi a következő spec. jelentését, vagy fordítva (speciálissá teszi)
| kettő közül egyik (vagy)
( és ) csoportok képzése
'''

import re

def szoveg():
    print "LaTeX".lower()
    nevlista = ["Csitári Emil", "CSiTáRi EmIl", "CSITARI EMIL"]
    for nev in nevlista:
	if nev.lower() == "csitári emil":
	    print nev, "egyezik"
	else:
	    print nev, "nem egyezik"
    
    gyumolcsok = "alma,körte,banán".split(",")
    for gyumolcs in gyumolcsok:
	print gyumolcs

    print "indexek"
    print gyumolcsok[0]
    print gyumolcsok[1]
    print gyumolcsok[-1]

    #szedjünk szét tagokra egy fájl teljes útvonalát, és irassuk ki a fájlnevet
    filehely="/home/diak15/.bashrc"

def felhasznalok():
    # Beolvasom a /etc/passwd sorait a lines listába
    f = open("/etc/passwd", "r")
    lines = f.readlines()
    f.close

    print "*** /etc/passwd első sora"
    print lines[0]

    print "*** Így szedhetjük szét a : elválasztóval összerakott sort\n*** Ehhez nem kell re modul."
    elemek = lines[0].split(":")
    print "*** Ezekre szedtem szét"
    print elemek
    print "*** Ez az első elem"
    print elemek[0]

    felhasznalok = []
    for line in lines:
	elemek = line.split(":")
	felhasznalok.append(elemek[0])
    print felhasznalok

    # Itt már reguláris kifejezés van.
    for felhasznalo in felhasznalok:
	if re.search("^.y", felhasznalo):
	    print felhasznalo, "nevének második betűje y"
	if re.search("\d", felhasznalo) and not re.search("\d$", felhasznalo) :
	    print felhasznalo, "nevében van számjegy de nem arra végződik."
	    print felhasznalo.upper(), "ugyanez nagbetűkkel."
    
    # Keressük meg azokat, akiknél a második helyen szerepel y

def alma():
    print "*** Keresés: search(mit, miben)"
    talalat=re.search(r"[a-z]+", r"Itt van egy alma")
    if talalat:
	print talalat.group()
	print talalat.start()
	print talalat.end()
    print "*** \w betűkre illeszkedik"
    talalat=re.search(r"\w+", r"Keverő.")
    print talalat.group()
    talalat=re.search(r"\w+", r"Különböző ékezetek.")
    print talalat.group()
    print "*** csere: sub(mit, mire, miben)"
    print re.sub(r"[xX]+", "-", r"Xerxész mexerkesztette a kexet.")
    print re.sub(r"(kék|zöld)", "szines", r"kék az ég és zöld a föld.")
    print re.sub(r"(kék|zöld)", r"(\1)", r"kék az ég és zöld a föld.")

    #Helyettesítsük egy szövegben

def helyettesit():
    """Olvassuk be ~/.bashrc sorait, és  jelenítsük meg az alias tartalmú sorokat."""
    #Készítsünk olyan függvényt, amely kiírja a .bashrc-nk alias tartalmú sorait
    #Majd változtassuk meg, hogy a többi sor írja ki.
    #Majd változtassuk meg, csak azokat a sorokat írja ki, ahol az alias nincs megjegyzésben (# után)
    #Majd bővítsük, hogy az aliasokat tartalmazó teljes sorokat cserélje le nagybetűsre.
    print "Ide jönnek a parancsok."

if __name__ == "__main__":
    szoveg()
    #alma()
    #felhasznalok()
    #helyettesit()

