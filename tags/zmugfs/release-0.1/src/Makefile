VERSION		= $(shell echo `awk '{ print $$1 }' version`)
RELEASE		= $(shell echo `awk '{ print $$2 }' version`)
NEWRELEASE	= $(shell echo $$(($(RELEASE) + 1)))

TOPDIR = $(shell pwd)
PYFILES     = $(wildcard *.py)
EXAMPLEDIR = 
INITDIR	= 
PYCHECKER       = /usr/bin/pychecker
PYFLAKES    = /usr/bin/pyflakes

all: rpms

bumprelease:	
	-echo "$(VERSION) $(NEWRELEASE)" > version

setversion: 
	-echo "$(VERSION) $(RELEASE)" > version

build: clean
	python setup.py build -f

clean:
	-rm -f  MANIFEST
	-rm -rf dist/ build/
	-rm -rf *~
	-rm -rf rpm-build/
	-rm -rf docs/*.gz

clean_hard:
	-rm -rf $(shell python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")/zmugfs

clean_hardest: clean_rpms


install: build 
	python setup.py install -f

install_hard: clean_hard install

install_hardest: clean_hardest rpms install_rpm restart

install_rpm:
	-rpm -Uvh rpm-build/zmugfs-$(VERSION)-$(RELEASE)$(shell rpm -E "%{?dist}").noarch.rpm

restart:
	-/usr/bin/zmugfs /tmp/fuse

recombuild: install_harder restart

clean_rpms:
	-rpm -e zmugfs

sdist:
	python setup.py sdist

new-rpms: bumprelease rpms

pychecker:
	@$(PYCHECKER) $(PYFILES) || exit 0

pyflakes:
	@$(PYFLAKES) $(PYFILES) || exit 0

money: clean
	-sloccount --addlang "makefile" $(TOPDIR) $(PYDIRS) $(EXAMPLEDIR) $(INITDIR)
 
rpms: build sdist
	mkdir -p rpm-build
	cp dist/*.gz rpm-build/
	cp version rpm-build/
	rpmbuild --define "_topdir %(pwd)/rpm-build" \
	--define "_builddir %{_topdir}" \
	--define "_rpmdir %{_topdir}" \
	--define "_srcrpmdir %{_topdir}" \
	--define '_rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm' \
	--define "_specdir %{_topdir}" \
	--define "_sourcedir  %{_topdir}" \
	-ba zmugfs.spec
