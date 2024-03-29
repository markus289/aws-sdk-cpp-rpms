# Copyright 2020 Markus Rothe
# Distributed under the terms of the Boost Software License 1.0
# SPDX-License-Identifier: BSL-1.0

Name:           aws-sdk-cpp
Version:        1.8.186
Release:        6%{?dist}
Summary:        Amazon Web Services SDK for C++
License:        ASL 2.0
URL:            https://github.com/aws/%{name}
Source0:        https://github.com/aws/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         f7c1d1691991995a97b8d120cc1668212e1025b3.patch
Patch1:         0001-add-missing-header.patch

BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-event-stream-devel
BuildRequires:  aws-checksums-devel

%if 0%{?el7}
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zlib-devel

Requires:       aws-c-common
Requires:       aws-c-event-stream
Requires:       aws-checksums
Requires:       libcurl
Requires:       openssl-libs
Requires:       pulseaudio-libs
Requires:       zlib

%description
The Amazon Web Services (AWS) SDK for C++ provides a modern C++ interface for
AWS. It is meant to be performant and fully functioning with low- and
high-level SDKs, while minimizing dependencies and providing platform
portability (Windows, OSX, Linux, and mobile).

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       aws-c-common-devel
Requires:       aws-c-event-stream-devel
Requires:       aws-checksums-devel
Requires:       libcurl-devel
Requires:       openssl-devel
Requires:       zlib-devel

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-sdk-cpp.

%prep
%autosetup -p1
sed -i -e 's/ "-Werror" "-pedantic"//' cmake/compiler_settings.cmake

%build
%if 0%{?el7}
%cmake3 \
    -DBUILD_DEPS:BOOL=FALSE \
    -DAUTORUN_UNIT_TESTS:BOOL=FALSE \
    -DCUSTOM_MEMORY_MANAGEMENT:BOOL=FALSE
%else
%cmake \
    -DBUILD_DEPS:BOOL=FALSE \
    -DAUTORUN_UNIT_TESTS:BOOL=FALSE \
    -DCUSTOM_MEMORY_MANAGEMENT:BOOL=FALSE
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
%{_libdir}/lib*.so

%files devel
%{_includedir}/aws
%{_libdir}/cmake
%{_libdir}/pkgconfig

%changelog
* Wed Oct 20 2021 Markus Rothe <markus.rothe@rite.cc> - 1.8.186-6
- update patch

* Tue Oct 19 2021 Markus Rothe <markus.rothe@rite.cc> - 1.8.186-5
- update patch

* Tue Oct 19 2021 Markus Rothe <markus.rothe@rite.cc> - 1.8.186-4
- update patch

* Mon Oct 18 2021 Markus Rothe <markus.rothe@rite.cc> - 1.8.186-3
- update patch

* Mon Oct 18 2021 Markus Rothe <markus.rothe@rite.cc> - 1.8.186-2
- Add patches for security and to solve a compile error

* Sun Oct 17 2021 Markus Rothe <markus.rothe@rite.cc> - 1.8.186-1
- Bump/downgrade to 1.8.186

* Sun Oct 17 2021 Markus Rothe <markus.rothe@rite.cc> - 1.9.123-1
- Bump to 1.9.123, support EL7 and Amazon Linux 2

* Sun Nov 29 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.95-2
- rebuilt

* Sat Nov 28 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.95-1
- Bump to 1.8.95

* Wed Nov 11 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.85-1
- Bump to 1.8.85

* Sun Nov  1 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.79-1
- Bump to 1.8.79

* Fri Oct 30 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.78-1
- Bump to 1.8.78

* Tue Oct 27 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.75-1
- Bump to 1.8.75

* Sun Oct 25 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.74-1
- Bump to 1.8.74

* Mon Oct 05 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.61-1
- Bump to 1.8.61

* Sat Aug 29 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.37-1
- Bump to 1.8.37

* Fri Aug 21 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.32-2
- Stop supporting RHEL/CentOS, simplify

* Thu Aug 20 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.32-1
- Bump to 1.8.32

* Fri Jul 31 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.18-1
- Bump to 1.8.18

* Thu Jul 30 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.17-1
- Bump to 1.8.17

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.14-2
- Use cmake specific macros

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.14-1
- Bump to 1.8.14

* Thu Jul 16 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.8-1
- Bump to 1.8.8

* Wed Jul 15 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.7-2
- rebuilt

* Sat Jul 11 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.7-1
- Bump to 1.8.7

* Tue Jul 07 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.4-1
- Bump to 1.8.4

* Sat Jul 04 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.3-1
- Bump to 1.8.3

* Thu Jul 02 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.2-1
- Bump to 1.8.2

* Wed Jul 01 2020 Markus Rothe <markus.rothe@rite.cc> - 1.8.1-1
- Bump to 1.8.1

* Tue Jun 30 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.365-1
- Bump to 1.7.365

* Wed Jun 24 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.361-2
- remove unknown component

* Wed Jun 24 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.361-1
- Bump to 1.7.361
- Build everything except 'fsx' to work around a temporary build failue in that
  component

* Tue Jun 23 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.360-1
- Bump to 1.7.360

* Thu Jun 11 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.353-1
- Bump to 1.7.353

* Wed Jun 10 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.351-1
- Bump to 1.7.351
- Remove patch, that has been commited upstream

* Wed May 13 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.333-1
- Bump to 1.7.333

* Thu May 07 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.329-2
- Really apply patch

* Thu May 07 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.329-1
- Bump to 1.7.329, add patch for EPEL 7

* Wed May 06 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.328-1
- Bump to 1.7.328

* Sat May 02 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.326-1
- Bump to 1.7.326

* Thu Apr 30 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.324-1
- Bump to 1.7.324

* Wed Apr 29 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.323-1
- Bump to 1.7.323

* Tue Apr 28 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.322-1
- Bump to 1.7.322

* Sun Apr 26 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.321-1
- Bump to 1.7.321

* Fri Apr 24 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.320-1
- Bump to 1.7.320

* Thu Apr 23 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.319-1
- Bump to 1.7.319

* Mon Apr 20 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.316-1
- Bump to 1.7.316

* Thu Apr 16 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.314-2
- rebuilt

* Thu Apr 09 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.314-1
- Bump to 1.7.314

* Wed Apr 08 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.313-2
- Disable custom memory management

* Wed Apr 08 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.313-1
- Bump to 1.7.313

* Thu Apr 02 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.309-1
- Bump to 1.7.309

* Mon Mar 30 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.306-1
- Bump to 1.7.306

* Fri Mar 27 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.305-1
- Bump to 1.7.305

* Sat Mar 21 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.301-1
- Bump to 1.7.301

* Thu Mar 19 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.299-1
- Bump to 1.7.299

* Wed Mar 18 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.298-1
- Bump to 1.7.298

* Tue Mar 17 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.297-1
- Bump to 1.7.297

* Sun Mar 15 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.296-1
- Bump to 1.7.296

* Thu Mar 12 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.294-1
- Bump to 1.7.294
- Don't do a 'Release' build
- The cmake files in the devel package search for several packages. Account for
  this in the dependencies.

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.292-2
- Nuke compiler options '-Werror' and '-pedantic'

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.292-1
- Initial RPM release
