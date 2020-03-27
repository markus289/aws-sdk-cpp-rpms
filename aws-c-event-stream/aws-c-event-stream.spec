Name:           aws-c-event-stream
Version:        0.1.4
Release:        4%{?dist}
Summary:        C99 implementation of the vnd.amazon.eventstream content-type
License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        https://github.com/awslabs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-find-aws-c-common.patch

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
%autosetup -p1

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
%{_libdir}/libaws-c-event-stream.so.*

%files devel
%{_libdir}/libaws-c-event-stream.so
%{_libdir}/aws-c-event-stream
%{_includedir}/aws

%changelog
* Fri Mar 27 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-4
- rebuilt

* Thu Mar 12 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-3
- Don't do a 'Release' build
- The devel package requires aws-c-common-devel and aws-checksums-devel

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-2
- rebuilt

* Tue Mar 10 2020 Markus Rothe <markus.rothe@rite.cc> - 0.1.4-1
- Initial RPM release
