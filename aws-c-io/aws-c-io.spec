# Copyright 2020 Markus Rothe
# Distributed under the terms of the Boost Software License 1.0
# SPDX-License-Identifier: BSL-1.0

Name:           aws-c-io
Version:        0.7.0
Release:        2%{?dist}
Summary:        I/O and TLS module for the AWS SDK for C
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-cal-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  s2n-devel

Requires:       aws-c-cal
Requires:       aws-c-common
Requires:       s2n

%description
This is a module for the Amazon Web Services (AWS) SDK for C. It handles all
I/O and TLS work for application protocols.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       aws-c-cal-devel
Requires:       aws-c-common-devel
Requires:       s2n-devel

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-common.

%prep
%autosetup

# tests require network access
%build
%cmake -DBUILD_TESTING:BOOL=FALSE
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libaws-c-io.so.*

%files devel
%{_libdir}/libaws-c-io.so
%{_libdir}/aws-c-io
%{_includedir}/aws

%changelog
* Sat Nov 28 20:17:50 UTC 2020 Markus Rothe <markus.rothe@rite.cc> - 0.7.0-2
- disable tests, as they require network access

* Sat Nov 28 19:03:52 UTC 2020 Markus Rothe <markus.rothe@rite.cc> - 0.7.0-1
- Initial RPM release
