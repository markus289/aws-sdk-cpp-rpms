Name:           s2n
Version:        0.10.21
Release:        1%{?dist}
Summary:        Amazon's implementation of the TLS/SSL protocols
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  openssl-devel

Requires:       openssl-libs

%description
s2n is a C99 implementation of the TLS/SSL protocols that is designed to be
simple, small, fast, and with security as a priority.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use s2n.

%prep
%autosetup
# https://github.com/awslabs/s2n/issues/2401
sed -i -e 's/ -fvisibility=hidden//' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_libdir}/libs2n.so

%files devel
%{_includedir}
%{_libdir}/s2n

%changelog
* Sat Nov 28 16:19:46 UTC 2020 Markus Rothe <markus.rothe@rite.cc> - 0.10.21-1
- Initial RPM release
