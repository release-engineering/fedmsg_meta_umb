%global srcname fedmsg_meta_umb
%global rpmname fedmsg-meta-umb

Name:           python-%{rpmname}
Version:        0.1.0
Release:        1%{?dist}
Summary:        fedmsg metadata provider plugins for the Unified Message Bus

License:        LGPLv2+
URL:            https://github.com/release-engineering/%{srcname}
Source0:        %{srcname}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-fedmsg
BuildRequires:  python3-mako
BuildRequires:  python3-cloud-sptheme
BuildRequires:  python3-sphinx

%description
This package contains plugins to the fedmsg metadata provider for internal
Red Hat services attached to the Unified Message Bus.


%package -n python3-%{rpmname}
Summary:        %{summary}
Requires:       python3-fedmsg
%{?python_provide:%python_provide python3-%{rpmname}}

%description -n python3-%{rpmname}
This package contains plugins to the fedmsg metadata provider for internal
Red Hat services attached to the Unified Message Bus.

%package doc
Summary:        Documentation for datagrepper running on the Unified Message Bus

%description doc
This package contains documentation for datagrepper running on the Unified
Message Bus. This includes web pages with a customized theme, and descriptions
of the message topics and formats that are specific to the Unified Message Bus.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
PYTHONPATH=. sphinx-build-3 doc/ htmldocs/

%install
%py3_install
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -pr datagrepper-docs htmldocs %{buildroot}%{_datadir}/%{name}

%check
%{__python3} -m unittest

%files -n python3-%{rpmname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%files doc
%{_datadir}/%{name}

%changelog
* Mon Dec 11 2023 Mike Bonnet <mikeb@redhat.com> - 0.1.0-1
- migrate to pyproject.toml
- compatibility with Python 3.12

* Thu Dec  3 2020 Mike Bonnet <mikeb@redhat.com> - 0.0.4-1
- snitch: handle inconsistent IDs
- errata: improved message handling
- replace references to external icons with local copies
- add CodeQL analysis and update tests to run on Python 3.9
- clair: handle messages from Clair v4
- messagebusd: new processor

* Fri Jan 17 2020 Mike Bonnet <mikeb@redhat.com> - 0.0.3-1
- remove python2 support, since fedmsg no longer supports it as of Fedora 31

* Tue Jul  3 2018 Mike Bonnet <mikeb@redhat.com> - 0.0.2-3
- install doesn't handle directories, use cp instead

* Tue Jul  3 2018 Mike Bonnet <mikeb@redhat.com> - 0.0.2-2
- Rename subpackage to -doc in accordance with Fedora recommendations
- Don't install docs as %%doc files, because dnf in a container runs with tsflags=nodocs

* Wed Jun 27 2018 Mike Bonnet <mikeb@redhat.com> - 0.0.2-1
- Build -docs subpackage

* Thu Jun  7 2018 Mike Bonnet <mikeb@redhat.com> - 0.0.1-1
- Initial build
