Summary:	Page counter
Summary(pl.UTF-8):	Licznik stron
Name:		pkpgcounter
Version:	1.81
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	http://www.librelogiciel.com/software/pkpgcounter/tarballs/%{name}-%{version}.tar.gz
# Source0-md5:	8af34c6fa843bee198f97658f97279ed
URL:		http://www.librelogiciel.com/software/pkpgcounter
BuildRequires:	python 
BuildRequires:	python-devel
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pkpgcouter is a generic Page Description Language parser whose main
feature is to count the number of pages in files ready to be printed.
It can currently compute the number of pages in several types of
files:
- PostScript (both DSC compliant and binary)
- PDF
- PCL3/4/5
- PCLXL (aka PCL6)
- ESC/P2

%description -l pl.UTF-8
Pkpgcouter jest ogólnym programem do analizowania języków opisu stron
(PCL, PostScript, Esc/P2), którego głównym zadaniem jest zliczyć
liczbę stron w plikach gotowych do wydruku. Obecnie obsługuje
następujące formaty:
- PostScript (zgodny z DSC oraz binarny)
- PDF
- PCL3/4/5
- PCLXL (aka PCL6)
- ESC/P2

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/*/*.py
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README CREDITS BUGS 
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/pkpgpdls
%{py_sitescriptdir}/pkpgpdls/*.py[co]
%{_mandir}/man1/*
