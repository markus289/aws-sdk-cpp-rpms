Name:           aws-c-common
Version:        0.4.34
Release:        4%{?dist}
Summary:        Core c99 package for AWS SDK for C
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-add-modules-to-cmake-module-path.patch
Patch1:         0002-prefix-path-vars.patch

%if 0%{?el7}
BuildRequires:  cmake3 >= 3.0
%else
BuildRequires:  cmake >= 3.0
%endif

BuildRequires:  gcc

%description
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-common.

%prep
%autosetup -p1

%build
%if 0%{?el7}
%cmake3 \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DBUILD_SHARED_LIBS:BOOL=TRUE
%else
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DBUILD_SHARED_LIBS:BOOL=TRUE
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
%{_libdir}/libaws-c-common.so.*

%files devel
%{_libdir}/libaws-c-common.so
%{_libdir}/aws-c-common
%{_libdir}/cmake
%{_includedir}/aws

%changelog
* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-4
- Add patches to allow building of aws-c-event-stream package

* Mon Mar 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-3
- This package requires a C compiler, not a C++ compiler

* Mon Mar 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-2
- Fix building on EL 7

* Mon Mar 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-1
- Initial RPM release
