# Copyright 2020 Markus Rothe
# Distributed under the terms of the Boost Software License 1.0
# SPDX-License-Identifier: BSL-1.0

Name:           aws-c-common
Version:        0.6.14
Release:        2%{?dist}
Summary:        Core C99 package for AWS SDK for C
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?el7}
BuildRequires:  cmake3
%else
BuildRequires:  cmake
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
ctest3 -V %{?_smp_mflags} --exclude-regex 'test_stack_trace_decoding|test_memtrace_stacks|promise_test_multiple_waiters'
%else
%{ctest --exclude-regex 'test_stack_trace_decoding|test_memtrace_stacks|promise_test_multiple_waiters'}
%endif

%files
%{_libdir}/libaws-c-common.so.*

%files devel
%{_libdir}/libaws-c-common.so
%{_libdir}/aws-c-common
%{_libdir}/cmake
%{_includedir}/aws

%changelog
* Sun Oct 17 2021 Markus Rothe <markus.rothe@rite.cc> - 0.6.14-2
- Support EL7

* Sun Oct 17 2021 Markus Rothe <markus.rothe@rite.cc> - 0.6.14-1
- Bump to 0.6.14

* Wed Jun 23 2021 Markus Rothe <markus.rothe@rite.cc> - 0.6.2-1
- Bump to 0.6.2

* Sun Oct 25 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.59-1
- Bump to 0.4.59

* Thu Sep 17 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.57-1
- Bump to 0.4.57

* Thu Sep 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.56-1
- Bump to 0.4.56

* Fri Sep 04 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.55-1
- Bump to 0.4.55

* Sat Aug 29 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.54-1
- Bump to 0.4.54

* Fri Aug 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.53-1
- Bump to 0.4.53

* Fri Aug 21 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.52-2
- Stop supporting RHEL/CentOS, simplify

* Thu Aug 20 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.52-1
- Bump to 0.4.52

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.50-4
- Use %ctest on dists other than el7/el8

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.50-3
- Don't use %cmake_build on el7/el8
- Use %cmake_install on dists other than el7/el8

* Mon Jul 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.4.50-2
- Use %cmake_build instead of %make_build

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
