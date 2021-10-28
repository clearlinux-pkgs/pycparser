#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycparser
Version  : 2.20
Release  : 76
URL      : https://files.pythonhosted.org/packages/0f/86/e19659527668d70be91d0369aeaa055b4eb396b0f387a4f92293a20035bd/pycparser-2.20.tar.gz
Source0  : https://files.pythonhosted.org/packages/0f/86/e19659527668d70be91d0369aeaa055b4eb396b0f387a4f92293a20035bd/pycparser-2.20.tar.gz
Summary  : C parser in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pycparser-license = %{version}-%{release}
Requires: pycparser-python = %{version}-%{release}
Requires: pycparser-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
pycparser is a complete parser of the C language, written in
                pure Python using the PLY parsing library.
                It parses C code into an AST and can serve as a front-end for
                C compilers or analysis tools.

%package license
Summary: license components for the pycparser package.
Group: Default

%description license
license components for the pycparser package.


%package python
Summary: python components for the pycparser package.
Group: Default
Requires: pycparser-python3 = %{version}-%{release}

%description python
python components for the pycparser package.


%package python3
Summary: python3 components for the pycparser package.
Group: Default
Requires: python3-core
Provides: pypi(pycparser)

%description python3
python3 components for the pycparser package.


%prep
%setup -q -n pycparser-2.20
cd %{_builddir}/pycparser-2.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603399952
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests/all_tests.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycparser
cp %{_builddir}/pycparser-2.20/LICENSE %{buildroot}/usr/share/package-licenses/pycparser/3a3d1c2cf8d81b9a4a823d5f3a865480f9b64977
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycparser/3a3d1c2cf8d81b9a4a823d5f3a865480f9b64977

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
