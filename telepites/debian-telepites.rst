====================================================
  Debian GNU/Linux telepítése
====================================================
    
Kísérletezés céljából érdemes a Linuxot virtuális gépre telepíteni.
Erre a Virtualbox vagy a VMWare megfelelő. Ezek beszerzéséről és
beállításáról a fájl végén van szó.

Telepítés
===============

A `debian.org <http://debian.org>`_-on keressük meg, hol lehet letölteni képfájlokat, és hol találunk
leírásokat. Ez otthoni házi.

Gyakorláshoz a helyi szerverről is leszedhetjük::

 wget http://arek.uni-obuda.hu/repo/linux/extra/debian-6.0.2.1-i386-netinst.iso

Virtuális gépben:
CD-ROM-nál megfelelő meghatót ki kellett jelölni vagy szedjük le
linux/telepitesbol a iso filet, és azt állítsuk be.
Indítsuk el a virtuális gépet. Ha van telepítő-CD bent legyen.

Miután megjelent az Debian felirat+csiga lépjünk be az ablakba (katt
oda) hogy tudjunk dolgozni ott.

(Virtualboxban Jobb Ctrl, WMWare alatt Ctrl-Alt a kilépés,
bal-alul mindkettőben ki van írva.)

Válasszunk szakértő módot. (Advanced options/Expert install)

Ha CD-ről telepítünk,
ellenőrizzük a CD integritását. Lehet, hogy a telepítés
vége felé derül ki, hogy nem ép és akkor kezdhetjük előről.

Legyen hu_HU.utf-8 az alapértelmezett nyelvi beállítás.
Adjunk meg pár más helyi beállítást is: pl. en_GB.utf-8 de_DE.utf-8 a
későbbi gyakorláshoz.

A telepítendő összetevőket átnézhetjük, most nem kell semmi.

!!!!! A hálózat beállítását az órán elmondottak szerint állítsuk !!!!!

Ha nem DHCP, akkor ezek a címek hasznosak a ROIK-ban.
IP-cím:
192.168.3.232 - 192.168.3.243 (12 db IP-cím)
Mindenkié legyen a 192.168.3.x ahol x=231+ gépsorszám.

mask, átjáró, jó ahogy van,
de DNS-nek még jobb a 193.224.148.2 (az ns.szerver közvetlen címe).

gépnévnek ne mindeni debiant adjon hanem pl. debian<gépsorszám>-ot
tartomány roik.bmf.hu

Particionálás
---------------

Kézzel particionáljunk, az alábbi partíciókat hozzuk létre:

1. Fat32 terület (20% méret /windowsra csatolva)
   (képzeletbeli Windows, vagy egy olyan terület, amit
   közösen használ a Win és Linux adatoknak).
  
2. ext3 3 GB,  hely /     Boot "zászlóval"
  
3. cserehely (swap) 256 MB (amekkora a RAM)
  
4. ext3 maradék  /home

   jellemző_használat beállítása úgy: hogy várhatóan nagy fájlokat - pl.
   nagyfelbontású képeket és filmeket - tárolnak a felhasználók (csak példa)

Rendszeróra nem UTC szerint jár, ha van Windows, ha csak Linux akkor
igen.

Felhasználók:

- root (jelszó:most legyen root, de éles rendszeren számok-kis-nagybetűk legyenek benne)

- diak (diak jelszóval; amivel majd beléphetnek a gépünkre másik gépről)

Szoftverválasztás: csak szabvány rendszer

GRUB-ot a  master boot record-ba

Feladatok a kész Linuxon
===========================

Töltsük le a feladatokat a frissen telepített gépre::
 
 apt-get install git vim

 git clone git://github.com/horvatha/linux.git

 cd linux/telepites

 vim debian-telepites.txt

ha ez nem megy, akkor::

 wget http://arek.uni-obuda.hu/repo/linux/telepites/debian-telepites.txt

Telepítés befejezése után indítsuk újra. Ilyenkor megtalálnánk minden
Windowsos indítható partíciót és korábbi linuxainkat a GRUB menüjében.
De most nincs ilyen.

Rendszergazdává válás és visszatérés
--------------------------------------

Lépjünk be root-ként (SuperUserként)::

   su
   <jelszó megadása>

Ekkor # alakú promptot kapunk a $ helyett, a továbbiakban ahol #-tel kezdek
sort rendszergazdaként kell futtatni.

Ha vissza akarunk térni, akkor  az alábbi billentyűkombinációt üssük le
(Most még ne.)::

  <Ctrl+d>

Használhatunk külön ablakot is a normál és a su felhasználónak.
Lásd lejjebb.

Programtelepítés
---------------------------

Telepítsünk egy postgresql szervert:

1. Parancssorban:

  a. Keressük meg, milyen csomag::

	apt-cache search postgresql

   Így sok, szűrjünk::

	apt-cache search postgresql |grep postgresql

   nézzük meg egy kiválasztott csomag adatait::

	apt-cache show postgresql
 
  b. Telepítsük::

	apt-get install postgresql

    Mielőtt igent mondunk, nézzük meg hány csomag, mennyit kell leszedni,
    mekkora területet használ.

2. Aptitude felületén (ezt nem fogom kérdezni)

  aptitude indítása:

	aptitude

  Keressünk rá a csomagra::

	/postgre

  Ez így túl sok, reguláris kifejezéssel keressünk::

	/^postgre<Enter>

  Következő előfordulás::

	n

3. Grafikus felület alatt synaptic is használható.


Nézzük meg mekkora szabad hely van a rendszeren, hány % foglalt
(jegyezzük meg)::

  df
  df -h

Nézzük meg milyen csomagok töltődtek le eddig (telepítés során és után)::

  ls /var/cache/apt/archives

Ezek valószínűleg nem kellenek már, ha csak újra nem kell telepíteni
ezeket, töröljük::

  # apt-get clean (a # jelzi, hogy ezt rootként kell)

Most mekkora szabad hely van a rendszeren::

  df 

Vim beállítása
----------------
Másik ablakon jelentkezzünk be diákként::

  <Alt><F2> ...

Nézzük meg a .bashrc-t::

  vim .bashrc

Nem színez::
  :syntax on

Alapból a Debian és Ubuntu csak egy minimális csomagot telepít a Vimből
(vim-tiny) ami nem tud szintaxiskiemelést, de szerencsére már
telepítettük a vim csomagot nemrég.

Állítsuk be, hogy alapból színezzen. De hol vannak a Vim rendszerszintű
beállításai? ...

Keressünk gyorsan fájlokat locate-tel.

a) Ehhez először telepítsük a locate csomagot::

     # apt-get install locate

b) Ehhez frissítsük a locate adatbázisát (rootként)::

     # updatedb

c) Mostmár kereshetünk::

     locate vimrc


Állítsuk be, hogy alapból színezzen a Vim!

a) Váltsunk rendszergazdára::

      su
      <jelszó megadása>

b) szerkesszük a beállítási fájlt::

     # vim /etc/vim/vimrc
     :syntax on 	# Így jobban átlátható
     /syntax on    # rákeres a megfelelő sorra
     <syntax on sor elől " kivétele>
     <a set mouse=a sor elől is>
     :wq      # Kilépés mentéssel

c) Lépjünk vissza normál felhasználóra::

     <Ctrl+d>

Próbáljuk ki újra diákként::

     vim .bashrc

Otthon kipróbálhatjuk (vagy ha sikerül megtalálni,
hogy lehet karakteres felületen bekapcsolni az
egeret vmware alatt)::

   :sp .bash_profile
   (a két ablak határát egérrel húzkodhatjuk)

ssh és futási szintek
-------------------------

Nézzük meg melyik szintek milyen be-(ki-)lépéshez tartoznak és melyik
alapértelmezett::

  vim /etc/inittab
  (úgy tudom újabb Ubuntukon az inittab helyét más vette át)

Mik indulnak el az alapértelmezett szinten::

  ls /etc/rc2.d

Mentsük fájlba későbbre (gondoljuk át, hová)!

::
  ls /etc/rc2.d > lsrc2

Nézzük meg a gépünk hálózati adatait::

  # ifconfig    (# a root promtot jelöli, nem kell beírni)

Telepítsünk ssh szervert (keresés, telepítés)!

Ismételten listázzuk az rc2.d könyvtárat, mi változott?

::

  ls /etc/rc2.d > lsrc2_
  vimdiff lsrc*

Milyen típusú fájlok ezek?

::
  ls -l /etc/rc2.d

Milyen program indul el az indításakor? Nézzünk bele az S20ssh
tartalmába!

::
  vim /etc/rc2.d/S20ssh

..
  Ez valószínű, hogy nem fog menni:
  | Próbáljunk bejelentkezni egy másik friss Debianra:
  | 
  |   ssh diak@192.168.3.2xx  (pl: xx=08)
  | 
  | Ki (és mit) dolgozik ott?
  | 
  |   w

A legvégén állítsuk le a gépet (root)::

  # halt

Újraindítás::

  # reboot

Virtualbox beszerzése és beállítása
===================================

Telepítsük Debian/Ubuntu alá a Virtualboxot:
virtualbox csomag és virtualbox-ose-modules megfelelő változata.

Rakjuk bele a felhasználót a vboxusers csoportba rootként vagy sudoval::

  # adduser diak vboxusers

diak felhasználóként ellenőrizhetük, hogy benne van::

  $ groups

Rootként betöltjük a kernelbe a vboxdrv modult::

  # modprobe vboxdrv

Ellenőrizzük, hogy megvan::

  # lsmod |grep vbox

Ez elveszik újabb indításkor, ezért rakjuk be a
/etc/modules fájlba a vboxdrv sort.

Linux 2.6 kernel kijelölése

Memóriaméret: 256MB elég karakteres szerverhez

4GB merevlemez-méret legyen a változó méretű jó nekünk.

Ellenőrizhetjük, hogy mekkora helyünk van a gépünkön::

  $ df

VMWare beszerzése és beállítása
===============================

VMware Workstation lelőhelye (lehet, hogy már nincs ott):
hirdet/szakcs/szamitogep_rendszerek/B.Z./wmware (88M)
ez a telepítéshez kell csak, mert a létrehozott fájlrendszer az
ingyenesen jogtisztán használható VMware Playerrel használható.
Regisztráció után telepítésre alkalmas VMWare verzió is beszerezhető
ingyenesen a honlapjukról.

Indítsuk a VMWare-t!

Hozzunk létre új virtuális gépet!

Configuration: Custom
V. machine format: New - Workstation 5
Networking: Bridged

Linux/Other Linux 2.6 kernel kijelölése

Memóriaméret: 256MB elég karakteres szerverhez

4GB merevlemez-méret legyen
és ugyanabban az ablakban foglaljuk le a diszkterületet előre
(Allocate all disk space)

