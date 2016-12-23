#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycparser
Version  : 2.17
Release  : 26
URL      : http://pypi.debian.net/pycparser/pycparser-2.17.tar.gz
Source0  : http://pypi.debian.net/pycparser/pycparser-2.17.tar.gz
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
pycparser v2.17
===============
:Author: `Eli Bendersky <http://eli.thegreenplace.net>`_

%package python
Summary: python components for the pycparser package.
Group: Default

%description python
python components for the pycparser package.


%prep
%setup -q -n pycparser-2.17

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests/all_tests.py
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
