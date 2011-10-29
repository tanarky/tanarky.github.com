.PHONY: install upload

install:
	rm -rf ./blog
	cp -pr ./_blogofile/_site/* ./

upload:
	git checkout master
	git commit -a -m "fixed something"
	git push origin master
