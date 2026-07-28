%define modname	 ExtUtils-F77
%define modver 1.26

Summary:	Simple interface to F77 libs
Name:		perl-%{modname}
Version:	%{modver}
Release:	4
License:	GPLv2
Group:		Development/Perl
Url:		https://github.com/PDLPorters/extutils-f77
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETJ/ExtUtils-F77-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires:	gcc-gfortran
BuildRequires:	perl(File::Which)
Requires:	gcc-gfortran

%description
Simple interface to F77 libs.  Used to be in perl-PDL, but isn't anymore.

This module tries to figure out how to link C programs with
Fortran subroutines on your system. Basically one must add a list
of Fortran runtime libraries. The problem is their location
and name varies with each OS/compiler combination!

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test || :

%install
%makeinstall_std

%files
%doc README CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*

