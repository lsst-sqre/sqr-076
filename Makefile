.PHONY:
init:
	rm -rf .tox
	pip install -U tox pre-commit
	pre-commit install

.PHONY:
html:
	tox run -e lint,demo,html

.PHONY:
clean:
	rm -rf _build

.PHONY:
refresh-bib:
	tox run -e refresh-bib
	@echo
	@echo "Commit the new bibliographies: git add lsstbib && git commit -m \"Update bibliographies.\""
