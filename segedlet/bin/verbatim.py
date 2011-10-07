#! /usr/bin/python
# coding: utf-8

import os
import sys


l = len(sys.argv)
if l==1:
    print >>sys.stderr,  "Használat: ektelen.py forrásfájl [célfájl]"
    exit(1)
if l==2:
    input = sys.argv[1]
    output="temp"
elif l==3:
    input = sys.argv[1]
    output = sys.argv[2] 

if l>3:
    print >>sys.stderr,  "Használat: ektelen.py forrásfájl [célfájl]"
    exit(1)

#os.system("ektelen %s >%s" % (input, output) )

f=open(input)
lines = f.readlines()
f.close()

lines.insert(0, "\\begin{verbatim}\n")
lines.append("\\end{verbatim}\n")

f=open(output, "w")
f.writelines(lines)
f.close()


if __name__ == '__main__':
    pass
