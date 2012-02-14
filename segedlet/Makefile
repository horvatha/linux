linalk.pdf: linalk.tex psqljegyzet.tex bank_rovid.tex debian-telepites.tex
	pdflatex linalk.tex
	pdflatex linalk.tex

upload:
	scp -p -P 122 linalk.pdf horvatha@arek.uni-obuda.hu:/home/AREK/horvatha/public_html/repo/linux/extra


psqljegyzet.tex: ../postgresql/README.rst
	./bin/verbatim.py ../postgresql/README.rst psqljegyzet.tex

# bank_rovid.tex: ../postgresql/bank/bank_rovid.py
# 	pygmentize -f tex  ../postgresql/bank/bank_rovid.py > bank_rovid.tex

debian-telepites.tex: ../telepites/debian-telepites.rst
	./bin/verbatim.py ../telepites/debian-telepites.rst debian-telepites.tex

feladatok.pdf: feladatok.tex
	pdflatex feladatok.tex
	pdflatex feladatok.tex

clean:
	rm *.log *.aux *.out *.toc
