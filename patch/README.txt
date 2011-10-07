==========================================
Patch létrehozása és használata
==========================================

Hozzunk létre patch (folt)-fájlt::

  diff -u szoveg1 szoveg2 >patch_file

Csináljunk egy másolatot a szoveg1-ről::

  cp szoveg1 szoveg1_masolat

Szúrjunk be szöveget oda, ahol nincs különbség::

  vimdiff szoveg1_masolat szoveg2

(Az első ablakot szerkesszük.)

A folttal csináljuk egyezővé a szöveg2-vel::

  patch  szoveg1_masolat patch_file

Hasonlítsuk össze a foltozott szöveget szoveg2-vel::

  (vim)diff szoveg1_masolat szoveg2

Ismét készítsünk másolatot!
Szúrjunk be olyan helyre szöveget, ahol különbség van! Mi lesz ekkor a
patch során? 
