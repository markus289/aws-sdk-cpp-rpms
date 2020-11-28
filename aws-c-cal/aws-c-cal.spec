Name:           aws-c-cal
Version:        0.4.5
Release:        1%{?dist}
Summary:        Amazon's Crypto Abstraction Layer
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-common-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  openssl-devel

Requires:       aws-c-common
Requires:       openssl-libs

%description
Amazon Web Services (AWS) Crypto Abstraction Layer that is a cross-platform C99
wrapper for cryptography primitives.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       aws-c-common-devel

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-common.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_bindir}/sha256_profile
%{_libdir}/libaws-c-cal.so.*

%files devel
%{_libdir}/libaws-c-cal.so
%{_libdir}/aws-c-cal
%{_includedir}/aws

%changelog
* Sat Nov 28 16:42:18 UTC 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.5-1
- Initial RPM release
