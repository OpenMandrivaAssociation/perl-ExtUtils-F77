%define modname	 ExtUtils-F77
%define modver 1.17

Summary:	Simple interface to F77 libs
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/ExtUtils-F77/
Source0:	http://www.perl.com/CPAN/authors/id/KGB/%{modname}-%{modver}.tar.gz
Patch0:		ExtUtils-F77-1.17-no-usrlib.patch
Patch1:		ExtUtils-F77-1.17-gfortran.patch
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	gcc-gfortran
Requires:	gcc-gfortran

%description
Simple interface to F77 libs.  Used to be in perl-PDL, but isn't anymore.

This module tries to figure out how to link C programs with
Fortran subroutines on your system. Basically one must add a list
of Fortran runtime libraries. The problem is their location
and name varies with each OS/compiler combination!

%prep
%setup -qn %{modname}-%{modver}
%apply_patches

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*

