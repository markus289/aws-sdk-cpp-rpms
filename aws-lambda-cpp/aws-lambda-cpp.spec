Name:           aws-lambda-cpp
Version:        0.2.6
Release:        1%{?dist}
Summary:        C++ implementation of the AWS Lambda runtime
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-include-64-bit-glibc.patch
Patch1:         0002-use-proper-libdir.patch

%if 0%{?el7}
BuildRequires:  cmake3 >= 3.9
%else
BuildRequires:  cmake >= 3.9
%endif

BuildRequires:  gcc-c++
# the AWS SDK for C++ is required to build and execute the tests
BuildRequires:  aws-sdk-cpp-devel
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
%autosetup -p1

%build
%if 0%{?el7}
%cmake3 \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DENABLE_TESTS:BOOL=TRUE
%else
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DENABLE_TESTS:BOOL=TRUE
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
%{_libdir}/libaws-lambda-runtime.so.*

%files devel
%{_libdir}/libaws-lambda-runtime.so
%{_libdir}/aws-lambda-runtime
%{_includedir}/aws

%changelog
* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.2.6-1
- Initial RPM release
