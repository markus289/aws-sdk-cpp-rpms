# Copyright 2020 Markus Rothe
# Distributed under the terms of the Boost Software License 1.0
# SPDX-License-Identifier: BSL-1.0

Name:           aws-c-event-stream
Version:        0.2.7
Release:        1%{?dist}
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-io-devel
BuildRequires:  aws-checksums-devel

%if 0%{?el7}
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif

BuildRequires:  gcc

Requires:       aws-c-io
Requires:       aws-checksums

%description
Amazon Web Services use a format called event stream encoding. It encodes
binary data with header information that describes the contents of each event.
This data is transmitted over HTTP using the vnd.amazon.eventstream
content-type. This package implements encoder and decoder functions to work
with these streams.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# the cmake files included in this package search for the following two
# packages
Requires:       aws-c-io-devel
Requires:       aws-checksums-devel

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-event-stream.

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
%{_libdir}/libaws-c-event-stream.so.*

%files devel
%{_libdir}/libaws-c-event-stream.so
%{_libdir}/aws-c-event-stream
%{_includedir}/aws

%changelog
* Sun Oct 17 2021 Markus Rothe <markus.rothe@rite.cc> - 0.2.7-1
- Bump to 0.2.7, support EL7 and Amazon Linux 2

* Sun Nov 29 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.5-5
- fixup dependency

* Sat Nov 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.5-4
- fixup last commit

* Sat Nov 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.5-3
- disable tests, as they require network access

* Sat Nov 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.5-2
- fix dependencies

* Tue Nov 24 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.5-1
- Bump to 0.2.5

* Sun Oct 25 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.6-4
- rebuilt

* Thu Sep 17 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.6-3
- rebuilt

* Fri Aug 21 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.6-2
- Stop supporting RHEL/CentOS, simplify

* Fri Jul 31 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.6-1
- Bump to 0.1.6

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-8
- Use cmake specific macros

* Wed Jul 15 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-7
- rebuilt

* Tue Jun 23 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-4
- rebuilt

* Thu May 07 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-3
- rebuilt

* Tue Apr 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-2
- Delete patch, not strictly necessary, keep the package as close to upstream
  as possible

* Thu Apr 23 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-1
- Bump to 0.1.5

* Thu Apr 16 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-7
- rebuilt

* Thu Apr 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-6
- rebuilt

* Mon Mar 30 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-5
- rebuilt

* Fri Mar 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-4
- rebuilt

* Thu Mar 12 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-3
- Don't do a 'Release' build
- The devel package requires aws-c-common-devel and aws-checksums-devel

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-2
- rebuilt

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-1
- Initial RPM release
