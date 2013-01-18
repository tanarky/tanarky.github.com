.PHONY: install

NAMESPACE= tanarky
NAME     = login
VENVROOT = /usr/share/pyenv/$(NAMESPACE)
VENVBIN  = $(VENVROOT)/bin
PYVER    = 2.7
PYTHON   = $(VENVBIN)/python
PIP      = $(VENVBIN)/pip

clean:
	rm -rf dist build src/*.egg-info

activate:
	$(PIP) install -r requirements.txt

install: activate clean uninstall
	$(PYTHON) setup.py test
	$(PYTHON) setup.py sdist
	$(PIP) install dist/*tar.gz

init:
	scripts/init_env_for_mac

freeze: uninstall
	$(PIP) freeze | tee requirements.txt

babel_extract:
	pybabel extract -F babel.cfg -o messages.pot .

babel_init:
	pybabel init -i messages.pot -d src/tanarky/login/translations -l ja_JP
	pybabel init -i messages.pot -d src/tanarky/login/translations -l en_US

babel_update:
	pybabel update -i messages.pot -d src/tanarky/login/translations -l ja_JP
	pybabel update -i messages.pot -d src/tanarky/login/translations -l en_US

babel_compile:
	pybabel compile -d src/tanarky/login/translations

uninstall:
	rm -rf $(VENVROOT)/lib/python$(PYVER)/site-packages/$(NAMESPACE)/$(NAME)*
	rm -rf $(VENVROOT)/lib/python$(PYVER)/site-packages/$(NAMESPACE).$(NAME)*
