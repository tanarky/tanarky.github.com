.PHONY: install upload

install:
	rm -rf ./blog
	cp -pr ./_blogofile/_site/* ./

upload:
	git branch master
	git push origin master
