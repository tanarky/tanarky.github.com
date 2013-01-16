.PHONY: install

NAMESPACE= tanarky
NAME     = cookie
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

uninstall:
	rm -rf $(VENVROOT)/lib/python$(PYVER)/site-packages/$(NAMESPACE)/$(NAME)*
	rm -rf $(VENVROOT)/lib/python$(PYVER)/site-packages/$(NAMESPACE).$(NAME)*
