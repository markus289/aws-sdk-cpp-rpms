# Copyright 2020 Markus Rothe
# Distributed under the terms of the Boost Software License 1.0
# SPDX-License-Identifier: BSL-1.0

Name:           s2n-tls
Version:        1.1.1
Release:        1%{?dist}
Summary:        Amazon's implementation of the TLS/SSL protocols
License:        ASL 2.0
URL:            https://github.com/aws/%{name}
Source0:        https://github.com/aws/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?el7}
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif

BuildRequires:  gcc
BuildRequires:  openssl-devel

Requires:       openssl-libs

%description
s2n-tls is a C99 implementation of the TLS/SSL protocols that is designed to be
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
sed -i -e 's/ -Werror//' CMakeLists.txt

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
%{_libdir}/libs2n.so

%files devel
%{_includedir}
%{_libdir}/s2n

%changelog
* Sun Oct 17 2021 Markus Rothe <markus.rothe@rite.cc> - 1.1.1-1
- Bump to 1.1.1, support EL7 and Amazon Linux 2

* Wed Jun 23 2021 Markus Rothe <markus.rothe@rite.cc> - 1.0.10-2
- Fixup URL to sources

* Wed Jun 23 2021 Markus Rothe <markus.rothe@rite.cc> - 1.0.10-1
- Rename, bump to 1.0.10

* Sat Nov 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.10.21-2
- Fixup URL to sources

* Sat Nov 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.10.21-1
- Initial RPM release
