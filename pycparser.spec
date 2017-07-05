#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycparser
Version  : 2.18
Release  : 30
URL      : http://pypi.debian.net/pycparser/pycparser-2.18.tar.gz
Source0  : http://pypi.debian.net/pycparser/pycparser-2.18.tar.gz
Summary  : C parser in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pycparser-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
===============
pycparser v2.18
===============
:Author: `Eli Bendersky <http://eli.thegreenplace.net>`_

%package python
Summary: python components for the pycparser package.
Group: Default

%description python
python components for the pycparser package.


%prep
%setup -q -n pycparser-2.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1499269076
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests/all_tests.py
%install
export SOURCE_DATE_EPOCH=1499269076
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
