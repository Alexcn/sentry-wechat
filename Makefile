SHELL=/bin/sh
BUILDDIR=./build
DISTDIR=./dist

.PHONY: clean dist

clean:
	rm -rf $(BUILDDIR) $(DISTDIR)

dist: clean
	python setup.py sdist bdist_wheel

format: 
	yapf --recursive --in-place --parallel sentry_wechat/
