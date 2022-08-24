#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : igsc
Version  : 0.8.4
Release  : 1
URL      : https://github.com/intel/igsc/archive/refs/tags/V0.8.4.tar.gz
Source0  : https://github.com/intel/igsc/archive/refs/tags/V0.8.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: igsc-bin = %{version}-%{release}
Requires: igsc-lib = %{version}-%{release}
Requires: igsc-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : doxygen
BuildRequires : metee-dev
BuildRequires : pkgconfig(libudev)

%description
# Intel(R) Graphics System Controller Firmware Update Library (IGSC FU)
--------------------------------------------------------------------------

%package bin
Summary: bin components for the igsc package.
Group: Binaries
Requires: igsc-license = %{version}-%{release}

%description bin
bin components for the igsc package.


%package dev
Summary: dev components for the igsc package.
Group: Development
Requires: igsc-lib = %{version}-%{release}
Requires: igsc-bin = %{version}-%{release}
Provides: igsc-devel = %{version}-%{release}
Requires: igsc = %{version}-%{release}

%description dev
dev components for the igsc package.


%package lib
Summary: lib components for the igsc package.
Group: Libraries
Requires: igsc-license = %{version}-%{release}

%description lib
lib components for the igsc package.


%package license
Summary: license components for the igsc package.
Group: Default

%description license
license components for the igsc package.


%prep
%setup -q -n igsc-0.8.4
cd %{_builddir}/igsc-0.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661378969
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1661378969
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/igsc
cp %{_builddir}/igsc-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/igsc/a8f3e29d5eab4420318de979754f5637d4bf2c3f
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/igsc

%files dev
%defattr(-,root,root,-)
/usr/include/igsc_lib.h
/usr/lib/cmake/igsc/igscConfig.cmake
/usr/lib/cmake/igsc/igscConfigVersion.cmake
/usr/lib/cmake/igsc/igscTargets-relwithdebinfo.cmake
/usr/lib/cmake/igsc/igscTargets.cmake
/usr/lib64/libigsc.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libigsc.so.0
/usr/lib64/libigsc.so.0.8.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/igsc/a8f3e29d5eab4420318de979754f5637d4bf2c3f
