%global srcname fedmsg_meta_umb
%global rpmname fedmsg-meta-umb

Name:           python-%{rpmname}
Version:        0.0.1
Release:        1%{?dist}
Summary:        fedmsg metadata provider plugins for the Unified Message Bus

License:        LGPLv2+
URL:            https://github.com/release-engineering/%{srcname}
Source0:        %{srcname}-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python2-devel python3-devel
BuildRequires:  python2-nose python3-nose
BuildRequires:  python2-fedmsg python3-fedmsg
BuildRequires:  python2-mako python3-mako
BuildRequires:  python2-cloud-sptheme python3-cloud-sptheme

%description
This package contains plugins to the fedmsg metadata provider for internal
Red Hat services attached to the Unified Message Bus.


%package -n python2-%{rpmname}
Summary:        %{summary}
Requires:       python2-fedmsg
%{?python_provide:%python_provide python2-%{rpmname}}

%description -n python2-%{rpmname}
This package contains plugins to the fedmsg metadata provider for internal
Red Hat services attached to the Unified Message Bus.


%package -n python3-%{rpmname}
Summary:        %{summary}
Requires:       python3-fedmsg
%{?python_provide:%python_provide python3-%{rpmname}}

%description -n python3-%{rpmname}
This package contains plugins to the fedmsg metadata provider for internal
Red Hat services attached to the Unified Message Bus.


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{rpmname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%files -n python3-%{rpmname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Thu Jun  7 2018 Mike Bonnet <mikeb@redhat.com> - 0.0.1-1
- Initial build
