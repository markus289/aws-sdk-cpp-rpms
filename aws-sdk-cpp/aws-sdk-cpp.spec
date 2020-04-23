Name:           aws-sdk-cpp
Version:        1.7.319
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
BuildRequires:  aws-c-event-stream-devel
BuildRequires:  aws-checksums-devel
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
%setup -q
sed -i -e 's/ "-Werror" "-pedantic"//' cmake/compiler_settings.cmake

%build
%if 0%{?el7}
%cmake3 \
    -DBUILD_SHARED_LIBS:BOOL=TRUE \
    -DBUILD_DEPS:BOOL=FALSE \
    -DAUTORUN_UNIT_TESTS:BOOL=FALSE \
    -DCUSTOM_MEMORY_MANAGEMENT:BOOL=FALSE
%else
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=TRUE \
    -DBUILD_DEPS:BOOL=FALSE \
    -DAUTORUN_UNIT_TESTS:BOOL=FALSE \
    -DCUSTOM_MEMORY_MANAGEMENT:BOOL=FALSE
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
