linalk.pdf: linalk.tex psqljegyzet.tex bank_rovid.tex debian-telepites.tex
	pdflatex linalk.tex
	pdflatex linalk.tex

psqljegyzet.tex: ../postgresql/README.txt
	./bin/verbatim.py ../postgresql/README.txt psqljegyzet.tex

# bank_rovid.tex: ../postgresql/bank/bank_rovid.py
# 	pygmentize -f tex  ../postgresql/bank/bank_rovid.py > bank_rovid.tex

debian-telepites.tex: ../telepites/debian-telepites.txt
	./bin/verbatim.py ../telepites/debian-telepites.txt debian-telepites.tex

feladatok.pdf: feladatok.tex
	pdflatex feladatok.tex
	pdflatex feladatok.tex

clean:
	rm *.log *.aux *.out *.toc
