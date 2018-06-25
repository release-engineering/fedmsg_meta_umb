# Makefile used by Copr to generate a srpm

tarball:
	python3 setup.py sdist --formats=tar

tarxz: tarball
	xz dist/*.tar

srpm: tarxz
	rpmbuild --define "_sourcedir dist" --define "_srcrpmdir $(outdir)" -bs *.spec
