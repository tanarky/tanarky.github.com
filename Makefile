.PHONY: install upload

install:
	./install.sh

upload:
	git checkout master
	git push origin master
