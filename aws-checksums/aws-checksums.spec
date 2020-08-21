Name:           aws-checksums
Version:        0.1.9
Release:        2%{?dist}
Summary:        Amazon's CRC32c and CRC32 implementations
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  aws-c-common-devel
BuildRequires:  cmake
BuildRequires:  gcc

%description
Cross-platform hardware accelerated CRC32c and CRC32 with fallback to efficient
software implementations. C interface with language bindings for each of
Amazon's SDKs.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-checksums.

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
%{_libdir}/libaws-checksums.so.*

%files devel
%{_libdir}/libaws-checksums.so
%{_libdir}/aws-checksums
%{_includedir}/aws

%changelog
* Fri Aug 21 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.9-2
- Stop supporting RHEL/CentOS, simplify

* Thu Aug 20 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.9-1
- Bump to 0.1.9

* Fri Jul 31 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.8-3
- Libraries are now symlinked correctly

* Fri Jul 31 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.8-2
- This package now requires cmake macros from aws-c-common

* Fri Jul 31 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.8-1
- Bump to 0.1.8

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.7-4
- Use cmake specific macros

* Wed Jun 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.7-1
- Bump to 0.1.7

* Wed Apr 08 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-5
- Do build as a shared library
- As it turns out, I want to turn of CUSTOM_MEMORY_MANAGEMENT in aws-sdk-cpp
  instead

* Wed Apr 08 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-4
- Build as a static library

* Thu Mar 12 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-3
- Don't do a 'Release' build

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-2
- rebuilt

* Mon Mar 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-1
- Initial RPM release
