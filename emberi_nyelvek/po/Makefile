hi.po: ../hi.py
	xgettext --package-name=hi -d hi ../hi.py

hu-init:
	msginit -l hu_HU -i hi.po

hu.po: hi.po
	msgmerge -U hu.po hi.po

hi.mo: hu.po
	msgfmt -c -v -o hi.mo hu.po
	cp hi.mo ../locale/hu/LC_MESSAGES
