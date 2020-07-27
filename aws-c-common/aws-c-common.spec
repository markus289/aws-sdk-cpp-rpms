Name:           aws-c-common
Version:        0.4.50
Release:        1%{?dist}
Summary:        Core C99 package for AWS SDK for C
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?el7}
BuildRequires:  cmake3 >= 3.0
%else
BuildRequires:  cmake >= 3.0
%endif

BuildRequires:  gcc

%description
Core C99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-common.

%prep
%autosetup
sed -i -e "s/ -Werror//" cmake/AwsCFlags.cmake

%build
%if 0%{?el7}
%cmake3 -DCMAKE_BUILD_TYPE:STRING=Release
%else
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%endif
%make_build

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
* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.50-1
- Bump to 0.4.50

* Wed Jul 15 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.49-1
- Bump to 0.4.49

* Tue Jun 30 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.48-1
- Bump to 0.4.48

* Tue Jun 23 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.47-1
- Bump to 0.4.47

* Wed Jun 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.45-1
- Bump to 0.4.45

* Wed May 13 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.42-1
- Bump to 0.4.42

* Thu May 07 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.41-1
- Bump to 0.4.41

* Sat May 02 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.40-1
- Bump to 0.4.40

* Tue Apr 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.39-2
- Delete patch, not strictly necessary, keep the package as close to upstream
  as possible

* Thu Apr 16 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.39-1
- Bump to 0.4.39

* Thu Apr 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.37-1
- Bump to 0.4.37

* Tue Mar 31 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.36-1
- Bump to 0.4.36

* Mon Mar 30 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.35-2
- Update patch for CMake

* Fri Mar 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.35-1
- Bump to 0.4.35

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-7
- Nuke compiler option '-Werror'

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-6
- Set CMAKE_BUILD_TYPE to 'Release', as the tests fail otherwise

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-5
- Don't set CMAKE_BUILD_TYPE

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-4
- Add patches to allow building of aws-c-event-stream package

* Mon Mar 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-3
- This package requires a C compiler, not a C++ compiler

* Mon Mar 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-2
- Fix building on EL 7

* Mon Mar 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.34-1
- Initial RPM release
