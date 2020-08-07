report.pdf : report.tex output1.png output2.png output3.png articles.txt create_filestructure.py matrix.txt
	latexmk -pdf 

main.py: create_filestructure.py 
	python3 create_filestructure.py

output1.png : plots.py
	python3 plots.py

output2.png : plots.py
	python3 plots.py

output3.png: wordanalysis.py
	python3 wordanalysis.py
	fold -w80 article.txt > articles.txt && rm -f article.txt

articles.txt: wordanalysis.py
	python3 wordanalysis.py


	
.PHONY: cleanalmost_clean
clean: almost_clean
	rm report.pdf
	rm *.png
	rm articles.txt

	

almost_clean:
	latexmk -c