# encoding: utf-8
# ipython-nal és ipython3-mal is működik %ed fájlnévvel behívható
from __future__ import print_function

import re

urls = """http://bocs.hu
    http://arek.uni-obuda.hu
    https://elearning.uni-obuda.hu
    http://bocs.hu/ado/index.html
    https://github.com/horvatha/linux/blob/master/regexp/keres_ipy.py
    http://.hu
    http://arek..hu
    http://arek.uni-obuda.hungary
    http://bocs.hu//vimrc
    hhttp://bocs.hu
    """.split()

rendszamok = """ABC-001
AAA-000
TRA-548
KISAPA-01
-01
AAA-
""".split()

IPs = """192.168.3.26
    1.5.222.54
    192.168.3.026
    1992.168.3.26
    184..233.45
    011.12.022.03
    560.370.13.25
    """.split()

emails = """horvath.arpad@arek.uni-obuda.hu
    x_ipszilon@gmail.com
    """

def keres(regexp, szavak):
    """A regexp reguláris kifejezést keres több szóban.

    regexp:
        Több sorba szétszedhető (lásd re.VERBOSE).
    szavak:
        Szavak listája, amiben keres.

    """
    for szo in szavak:
        print(szo, end="\n ")
        search = re.search(regexp, szo, re.VERBOSE)
        if search:
            print(search.group())
        else:
            print("---------")

