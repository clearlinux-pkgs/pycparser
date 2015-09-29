#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycparser
Version  : 2.14
Release  : 16
URL      : https://pypi.python.org/packages/source/p/pycparser/pycparser-2.14.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pycparser/pycparser-2.14.tar.gz
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
pycparser v2.14
===============
:Author: `Eli Bendersky <http://eli.thegreenplace.net>`_

%package python
Summary: python components for the pycparser package.
Group: Default

%description python
python components for the pycparser package.


%prep
%setup -q -n pycparser-2.14

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
python tests/all_tests.py
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
