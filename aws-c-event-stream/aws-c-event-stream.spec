Name:           aws-c-event-stream
Version:        0.1.5
Release:        6%{?dist}
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if 0%{?el7}
BuildRequires:  cmake3 >= 3.1
%else
BuildRequires:  cmake >= 3.1
%endif

BuildRequires:  gcc
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-checksums-devel

%description
Amazon Web Services use a format called event stream encoding. It encodes
binary data with header information that describes the contents of each event.
This data is transmitted over HTTP using the vnd.amazon.eventstream
content-type. This package implements encoder and decoder functions to work
with these streams.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# the cmake files included in this package search for the following two
# packages
Requires:       aws-c-common-devel
Requires:       aws-checksums-devel

%description devel
This package contains the header files, libraries and cmake supplementals
needed to develop applications that use aws-c-event-stream.

%prep
%autosetup

%build
%if 0%{?el7}
%cmake3
%else
%cmake
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
%{_libdir}/libaws-c-event-stream.so.*

%files devel
%{_libdir}/libaws-c-event-stream.so
%{_libdir}/aws-c-event-stream
%{_includedir}/aws

%changelog
* Tue Jun 23 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-4
- rebuilt

* Thu May 07 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-3
- rebuilt

* Tue Apr 28 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-2
- Delete patch, not strictly necessary, keep the package as close to upstream
  as possible

* Thu Apr 23 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.5-1
- Bump to 0.1.5

* Thu Apr 16 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-7
- rebuilt

* Thu Apr 09 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-6
- rebuilt

* Mon Mar 30 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-5
- rebuilt

* Fri Mar 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-4
- rebuilt

* Thu Mar 12 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-3
- Don't do a 'Release' build
- The devel package requires aws-c-common-devel and aws-checksums-devel

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-2
- rebuilt

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-1
- Initial RPM release
