Summary:	Speech Recognition Scoring Toolkit (SCTK)
Name:		sctk
Version:	2.4.0
Release:	%mkrel 0
License:	GPL
Group:		Text tools
Source:		ftp://jaguar.ncsl.nist.gov/pub/%{name}-%{version}-20091110-0958.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Speech Recognition Scoring Toolkit (SCTK)
Includes the SCLITE, ASCLITE, tranfilt, hubscr, SLATreport and utf_filt scoring tools

%prep
%setup -q

%build
rm -fr %{buildroot}
make config
make all

%install
make install
mkdir -p %{buildroot}%{_sbindir}
cp bin/* %{buildroot}%{_sbindir}/

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_sbindir}/*
