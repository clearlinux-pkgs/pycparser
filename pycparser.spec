#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycparser
Version  : 2.18
Release  : 48
URL      : http://pypi.debian.net/pycparser/pycparser-2.18.tar.gz
Source0  : http://pypi.debian.net/pycparser/pycparser-2.18.tar.gz
Summary  : C parser in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pycparser-python3
Requires: pycparser-license
Requires: pycparser-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python-dev
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
pycparser is a complete parser of the C language, written in
                pure Python using the PLY parsing library.
                It parses C code into an AST and can serve as a front-end for
                C compilers or analysis tools.

%package legacypython
Summary: legacypython components for the pycparser package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pycparser package.


%package license
Summary: license components for the pycparser package.
Group: Default

%description license
license components for the pycparser package.


%package python
Summary: python components for the pycparser package.
Group: Default
Requires: pycparser-python3

%description python
python components for the pycparser package.


%package python3
Summary: python3 components for the pycparser package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pycparser package.


%prep
%setup -q -n pycparser-2.18

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530376092
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests/all_tests.py
%install
export SOURCE_DATE_EPOCH=1530376092
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/pycparser
cp LICENSE %{buildroot}/usr/share/doc/pycparser/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/pycparser/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
