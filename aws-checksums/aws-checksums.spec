Name:           aws-checksums
Version:        0.1.5
Release:        5%{?dist}
Summary:        Amazon's CRC32c and CRC32 implementations
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?el7}
BuildRequires:  cmake3 >= 3.1
%else
BuildRequires:  cmake >= 3.1
%endif

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
%setup -q

%build
%if 0%{?el7}
%cmake3 -DBUILD_SHARED_LIBS:BOOL=TRUE
%else
%cmake -DBUILD_SHARED_LIBS:BOOL=TRUE
%endif
make %{?_smp_mflags}

%install
%make_install

%check
%if 0%{?el7}
ctest3 -V %{?_smp_mflags}
%else
ctest -V %{?_smp_mflags}
%endif

%files
%{_libdir}/libaws-checksums.so

%files devel
%{_libdir}/aws-checksums
%{_includedir}/aws

%changelog
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
