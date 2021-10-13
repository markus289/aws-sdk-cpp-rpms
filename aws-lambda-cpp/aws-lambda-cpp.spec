# Copyright 2020 Markus Rothe
# Distributed under the terms of the Boost Software License 1.0
# SPDX-License-Identifier: BSL-1.0

Name:           aws-lambda-cpp
Version:        0.2.7
Release:        1%{?dist}
Summary:        C++ implementation of the AWS Lambda runtime
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel

Requires:       libcurl
Requires:       zip

%description


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-lambda-cpp.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libaws-lambda-runtime.so.*

%files devel
%{_libdir}/libaws-lambda-runtime.so
%{_libdir}/aws-lambda-runtime
%{_includedir}/aws

%changelog
* Sun Oct 25 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.7-1
- Bump to 0.2.7

* Thu Sep 17 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.6-8
- rebuilt

* Fri Aug 21 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.6-7
- Stop supporting RHEL/CentOS, simplify

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.6-6
- Depend on git to apply patches

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.6-5
- Use cmake specific macros

* Wed Mar 11 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.6-3
- Really disable tests

* Wed Mar 11 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.6-2
- Make libdir patch apply
- Disable tests as they want to make HTTP requests to remote hosts

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.6-1
- Initial RPM release
