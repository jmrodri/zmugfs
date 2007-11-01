%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           zmugfs
Source1: version
Version: %(echo `awk '{ print $1 }' %{SOURCE1}`)
Release: %(echo `awk '{ print $2 }' %{SOURCE1}`)%{?dist}
Summary:        FUSE-based filesystem Smugmug client
Group:          Applications/Multimedia
License:        GPL
URL:            http://zmugtools.sourceforge.net/
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  python
Requires:       python >= 2.3
Requires:       zmugjson
Requires:       fuse-python

%description
FUSE-based filesystem to access Smugmug

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/zmugfs.*py*
%{_usr}/share/doc/%{name}-%{version}/LICENSE.TXT
%attr(755, root, root) %{_bindir}/zmugfs
%attr(644, root, root) /etc/zmugfs/logger.conf

%changelog
* Wed Oct 31 2007 Jesus Rodriguez <jmrodri at gmail dot com> 0.1-2
- first official release

* Tue Oct 30 2007 Jesus Rodriguez <jmrodri at gmail dot com> 0.1-1
- test rpm release
