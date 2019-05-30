# Makefile used by Copr to generate a srpm

setup:
	dnf install git-core python3-setuptools

tarball: setup
	python3 setup.py sdist --formats=tar

tarxz: tarball
	xz dist/*.tar

srpm: tarxz
	sed -i -e "s/^Release:.*/Release:        0.$$(date +%s).git$$(git log -1 --pretty=format:%h)%{?dist}/" *.spec
	rpmbuild --define "_sourcedir dist" --define "_srcrpmdir $(outdir)" -bs *.spec
