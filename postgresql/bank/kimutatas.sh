#!/bin/bash

#### Fájlba ####

TEX="kimutatas.tex"

echo '\documentclass[a4paper]{article}
\usepackage[utf8x]{inputenc}
\usepackage{ucs}
\usepackage[magyar]{babel}
\begin{document}' > $TEX

psql -q -P format=latex -P border=3 \
	-c "SELECT * FROM betétesek;" >> $TEX

echo '\end{document}' >> $TEX


#### Képernyőre ####

echo
echo "**** Hagyományos formátum ****"

psql -q  \
	-c "SELECT * FROM betétesek;"

echo "**** Hagyományos formátum, vastagabb keret ****"

psql -q -P border=3 \
	-c "SELECT * FROM betétesek;"

echo "**** LaTeX formátum ****"

psql -q -P format=latex -P border=3 \
	-c "SELECT * FROM betétesek;"


# pdflatex $TEX
# rm $TEX
# evince kimutatas.pdf
