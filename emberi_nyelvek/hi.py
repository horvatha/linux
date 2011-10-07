#!/usr/bin/env python
# coding: utf-8
'''
Linuxvilág 2006. június (ott C-re írja le):
Többnyelvű programok létrehozása GNU gettext rendszerrel (Czirkos Zoltán)
/usr/share/doc/gettext-doc/examples/ könyvtárban több programnyelvű példa

Futtassuk valahogy:
python hi.py
vagy
chmod a+x hi.py
./hi.py

hi: üzenetkatalógus (ilyen mo-et keres (machine object))

Sablonkészítés: (portable object template)
xgettext -d hi -o hi.pot hi.py
# esetleg xgettext --package-name=hi -d hi -o hi.pot hi.py

És beállítom a karakterkódolást
15. sorban UTF-8  -ra az ékezetes karakterek miatt,
Beállíthatom a 8. sorban a verziót (pl. 0.2).

Egyedi nyelvhez fájlt készítek:
msginit -l hu_HU -i hi.pot

Lefordítom a szöveg(ek)et:
vim (kbabel, gtranslator...)

mo készítése
msgfmt -c -v -o hi.mo hu.po
-c részletes ellenőrzés, -v bőbeszédű

Egy szöveg megjegyzésekkel:
# fordító megjegyzései (szóköz fontos # után)
#. automatikus megjegyzések
#: hivatkozás
#, flagek
msgid "idegen"
msgstr "magyar"

-o kimeneti fájl nevei, -i input, -l nyelv (lang.)

(export LC_ALL=hu_HU ha kell)
%%%%%%%%%% sudo cp hi.mo /usr/share/locale/hu/LC_MESSAGES
cp hi.mo ./locale/hu/LC_MESSAGES
(előtte hozzuk létre a locale/hu/LC_MESSAGES könyvtárat; mkdir -p)

Változtassuk meg ezt a programot:
Hello után írjunk vesszőt

Bővítsük (végére rakjuk):
import os
print _("This program is running as process number %(pid)d.") \
      % { 'pid': os.getpid() }

Bővítés után új sablon készítése:
xgettext -d hi -o hi_uj.pot hi.py

Összefűzés a régivel:
msgmerge -U hu.po hi_uj.pot

Fordítsuk újra a hu.po fájlt... Mi változott benne?
(Fordításkor a fuzzy sor ne maradjon benne!)

Megpróbálhatjuk, hogy az xgettextnek több fájlnevet adunk meg.

Pár megjegyzés:
Fordításnál formátumkarakterek sorrendje maradjon: %d %s.
_ karekterek grafikus felületen (pl. terminálban _File)
#~ jelzés: megszűnt szövegek
xgettext -c opciója: bemásolja a szöveget megelőző megjegyzést
gettextize program: felkészít egy programrenszert a gettext használatára ???


A vim.po fájllal érdemes kipróbálni a kbabel fordítástámogató programot.

Az Ubuntu fordítása a https://launchpad.net/ubuntu/ oldalon történik.
'''

import gettext
transl = gettext.translation("hi", "./locale")
# transl = gettext.translation("hi", "/usr/share/locale") #Ha rootként tudom elhelyezni.
_ = transl.ugettext

print _("Hello world!")
