#!/usr/bin/env python
# coding: utf-8
"""
1. You can start from command line::

    python keres.py

2. You can import it e.g in Jupyter notebook.

    from keres import *

    keres(
      r"^ http s? :// ([a-z-]+\.)+ [a-z]{2,3} (/[a-z-_\.]+)* $",
      urls )

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
    file:///var/www/index.html
    http://.hu
    http://arek..hu
    http://arek.uni-obuda.hungary
    http://bocs.hu//vimrc
    hhttp://bocs.hu
    """.split()

cars_number = """ABC-001
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
    SuperPandas@WesMcKinney.com
    horvaarp@morganstanley.com
    joci@csillagasz.at
    x_ypsilon@gmail.com
    very.common@example.gov
    bobebaba13@futrinka.mtv.hu
    BobeBaba13@futrinka.MTV.hu
    bobe@baba13@futrinka.mtv.hu
    abc.example.com
    bobebaba13@futrinka.mtv.
    bobebaba13@futrinka..hu
    """.split()

passwords = """AlMA99
7DonaldDuck
Game4Of2Thrones7
7years
7YEARS
Univers42Question
UniversQuestion""".split()


print("Examples: cars_number, IPs, urls, emails")


def search_list(regexp, words):
    """It searches a regular expression in more strings.

    regexp:
        The regular expression we are searching in.
        You can split into more lines (see re.VERBOSE).
    words:
        The list a words it searches in.

    Példa::

        search_list(
          r"^ http s? :// ([a-z-]+\.)+ [a-z]{2,3} (/[a-z-_\.]+)* $",
          urls )

    There might be useful to start the string by r in the form of
    r"pattern" because you don't need to excape the backslash (\) characters.

    """
    print('00 does not match at all, -- match a part,'
          ' ++ match the whole')
    for word in words:
        print('  ', word)
        search = re.search(regexp, word, re.VERBOSE)
        if search:
            if search.start() == 0 and search.end() == len(word):
                print('++ ', end='')
            else:
                print('-- ', end='')
            print(' '*search.start(), search.group(), sep='', end='')
            groupdict = search.groupdict()
            if groupdict:
                print(" "*(len(word)-search.end()),
                      ", ".join([
                          "{}={}".format(k, groupdict[k]) for k in groupdict
                      ])
                      )
            else:
                print()
        else:
            print("00")

if __name__ == '__main__':
    search_list(
        r"^ http s? :// ([a-z-]+\.)+ [a-z]{2,3} (/[a-z-_\.]+)* $",
        urls
    )
