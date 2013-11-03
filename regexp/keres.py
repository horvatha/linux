#!/usr/bin/env python
# coding: utf-8
"""

Lefuttatva
-------------

Lefuttatás előtt az utolsó három sort érdemes változtatgatni, vigyázva, hogy a
keres kezdete beljebb legyen húzva az if kezdetű sornál. A lefuttatásnak két
módja szerepel alább.

1. Elindítható parancssorból::

    python keres.py

2. Megnyitható IDLE-ből (vagy IDLE3-ból) és az F5 gombbal elindítható.

Parancsértelmezőből
---------------------

ipython-nal és ipython3-mal vagy a hivatalos python parancsértelmezővel is
működik, és behívható így, ha abban a könyvtárban indítottuk az ipythont, ahol
a keres.py fájl van, vagy benne van az elérési útvonalban::

    from keres import keres

majd használható így::

    keres(
      r"^ http s? :// ([a-z-]+\.)+ [a-z]{2,3} (/[a-z-_\.]+)* $",
      urls )

A keres függvény pontos használatát megtudhatjuk az alábbi paranccsal::

    help(keres)

vagy ipythonban akár így is::

    keres?

"""

from __future__ import print_function


import re

urls = """http://bocs.hu
    http://arek.uni-obuda.hu
    https://elearning.uni-obuda.hu
    http://bocs.hu/ado/index.html
    https://github.com/horvatha/linux/blob/master/regexp/keres_ipy.py
    ftp://ftp.sztaki.hu/pub/tex
    http://.hu
    http://arek..hu
    http://arek.uni-obuda.hungary
    http://bocs.hu//vimrc
    hhttp://bocs.hu
    """.split()

rendszamok = """ABC-001
AAA-000
TRA-548
FERI-12
EWING-1
-01
AAA-
KISAPA-01
KISAPA-0122333
""".split()

IPs = """192.168.3.26
    1.5.222.54
    192.168.3.026
    1992.168.3.26
    184..233.45
    011.12.022.03
    560.370.13.25
    """.split()

emails = """
    joci@csillagasz.at
    horvath.arpad@arek.uni-obuda.hu
    x_ipszilon@gmail.com
    very.common@example.gov
    bobebaba13@futrinka.mtv.hu
    bobe@baba13@futrinka.mtv.hu
    abc.example.com
    bobebaba13@futrinka.mtv.
    bobebaba13@futrinka..hu
    """.split()

print("Példák: rendszamok, IPs, urls, emails")

def keres(regexp, szavak):
    """A regexp reguláris kifejezést keres több szóban.

    regexp:
        A reguláris kifejezés, amit keresünk.
        Több sorba szétszedhető (lásd re.VERBOSE).
    szavak:
        Szavak listája, amiben keres.

    Példa::

        keres(
          r"^ http s? :// ([a-z-]+\.)+ [a-z]{2,3} (/[a-z-_\.]+)* $",
          urls )

    Az első paraméter érdemes r-rel kezdeni r"kifejezés" alakban, mert
    ilyenkor nem kell levédeni a visszaper (\) karaktereket.

    """
    print('00 egyáltalán nem illeszkedik, -- részére illeszkedik, ++ teljesre illeszkedik')
    for szo in szavak:
        print('  ', szo)
        search = re.search(regexp, szo, re.VERBOSE)
        if search:
            if search.start() == 0 and search.end() == len(szo):
                print('++ ', end='')
            else:
                print('-- ', end='')
            print(' '*search.start(), search.group(), sep='', end='')
            groupdict = search.groupdict()
            if groupdict:
                print(" "*(len(szo)-search.end()), ", ".join(["{}={}".format(k, groupdict[k]) for k in groupdict]))
            else:
                print()
        else:
            print("00")

if __name__ == '__main__':
    keres(
      r"^ http s? :// ([a-z-]+\.)+ [a-z]{2,3} (/[a-z-_\.]+)* $",
      urls )
