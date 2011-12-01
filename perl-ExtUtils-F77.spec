%define upstream_name	 ExtUtils-F77
%define upstream_version 1.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 3

Summary:	Simple interface to F77 libs
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/ExtUtils-F77/
Source0:    http://www.perl.com/CPAN/authors/id/KGB/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		ExtUtils-F77-1.17-no-usrlib.patch
Patch1:		ExtUtils-F77-1.17-gfortran.patch
BuildRequires: gcc-gfortran
Requires:  gcc-gfortran
Obsoletes: perl-ExtUtils_F77
Provides:  perl-ExtUtils_F77
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Simple interface to F77 libs.  Used to be in perl-PDL, but isn't anymore.

This module tries to figure out how to link C programs with
Fortran subroutines on your system. Basically one must add a list
of Fortran runtime libraries. The problem is their location
and name varies with each OS/compiler combination!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1 -b .no-usrlib
%patch1 -p1 -b .gfortran

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/*/*
%doc README CHANGES

