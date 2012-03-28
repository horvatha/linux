# ipython-nal és ipython3-mal is működik %ed fájlnévvel behívható
from __future__ import print_function

import re

urls = """http://bocs.hu http://arek.uni-obuda.hu https://elearning.uni-obuda.hu
   http://bocs.hu/ado/index.html""".split()

def keres(pattern, urls):
    for url in urls:
        print(url, end="\n ")
        search = re.search(pattern, url)
        if search:
            print(search.group())
        else:
            print("---------")

