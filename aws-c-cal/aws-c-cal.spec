# Copyright 2020 Markus Rothe
# Distributed under the terms of the Boost Software License 1.0
# SPDX-License-Identifier: BSL-1.0

Name:           aws-c-cal
Version:        0.5.12
Release:        1%{?dist}
Summary:        Amazon's Crypto Abstraction Layer
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-common-devel

%if 0%{?el7}
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif

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
%if 0%{?el7}
%cmake3
%else
%cmake
%endif
%if 0%{?el7}
%make_build
%else
%cmake_build
%endif

%install
%if 0%{?el7}
%make_install
%else
%cmake_install
%endif

%check
%if 0%{?el7}
ctest3 --output-on-failure --force-new-ctest-process %{?_smp_mflags}
%else
%ctest
%endif

%files
%{_bindir}/sha256_profile
%{_libdir}/libaws-c-cal.so.*

%files devel
%{_libdir}/libaws-c-cal.so
%{_libdir}/aws-c-cal
%{_includedir}/aws

%changelog
* Sun Oct 17 2021 Markus Rothe <markus.rothe@rite.cc> - 0.5.12-1
- Bump to 0.5.12, support EL7 and Amazon Linux 2

* Sat Nov 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.5-1
- Initial RPM release
