.PHONY: all

all:
	platex mthesis.tex
	platex mthesis.tex 1>/dev/null
	platex mthesis.tex 1>/dev/null
	dvipdfmx mthesis.dvi 1>/dev/null
	open -a skim mthesis.pdf
