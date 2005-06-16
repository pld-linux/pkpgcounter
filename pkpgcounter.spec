#

Summary:	Page counter
Summary(pl):	Licznik stron
Name:		pkpgcounter
Version:	1.50
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://www.librelogiciel.com/software/pkpgcounter/tarballs/%{name}-%{version}.tar.gz
# Source0-md5:	94d70c07b82ca2f1374da135ba803bb5
URL:		http://www.librelogiciel.com/software/pkpgcounter
BuildRequires:	python
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pkpgcouter is a generic Page Description Language parser which main
feature is to count the number of pages in files ready to be printed.
It can currently compute the number of pages in several types of files
:
- PostScript (both DSC compliant and binary)
- PDF
- PCL3/4/5
- PCLXL (aka PCL6)
- ESC/P2

%description -l pl
Pkpgcouter jest ogólnym analizatorem jêzyków opisu stron (PCL
PostScript Esc/P2) którego g³ownym zadaniem jest zliczyæ ilo¶æ stron w
plikach gotowych do wydruku. Obecnie obs³uguje nastêpuj±ce formaty:
- PostScript (zgodny z DSC oraz binarny)
- PDF
- PCL3/4/5
- PCLXL (aka PCL6)
- ESC/P2

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README CREDITS BUGS 
%attr(755,root,root) %{_bindir}/*
/usr/share/python2.4/site-packages/pdlanalyzer/*.py
/usr/share/python2.4/site-packages/pdlanalyzer/*.pyc
%dir /usr/share/python2.4/site-packages/pdlanalyzer/
