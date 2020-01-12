.PHONY: all

all:
	latexmk mthesis.tex 1>/dev/null
	latexmk -c
	open -a Firefox mthesis.pdf

clean:
	rm -f *.bbl *.blg *.aux *.log *.dvi
