Name:           aws-sdk-cpp
Version:        1.7.292
Release:        1%{?dist}
Summary:        Amazon Web Services SDK for C++
License:        ASL 2.0
URL:            https://github.com/aws/%{name}
Source0:        https://github.com/aws/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?el7}
BuildRequires:  cmake3 >= 3.1
%else
BuildRequires:  cmake >= 3.1
%endif

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-checksums-devel
BuildRequires:  aws-c-event-stream-devel
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zlib-devel

Requires:       aws-c-common
Requires:       aws-checksums
Requires:       aws-c-event-stream
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

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-sdk-cpp.

%prep
%setup -q

%build
%if 0%{?el7}
%cmake3 \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DBUILD_SHARED_LIBS:BOOL=TRUE \
    -DBUILD_DEPS:BOOL=FALSE \
    -DAUTORUN_UNIT_TESTS:BOOL=FALSE
%else
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DBUILD_SHARED_LIBS:BOOL=TRUE \
    -DBUILD_DEPS:BOOL=FALSE \
    -DAUTORUN_UNIT_TESTS:BOOL=FALSE
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
%{_libdir}/lib*.so

%files devel
%{_includedir}/aws
%{_libdir}/cmake
%{_libdir}/pkgconfig

%changelog
* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 1.7.292-1
- Initial RPM release
