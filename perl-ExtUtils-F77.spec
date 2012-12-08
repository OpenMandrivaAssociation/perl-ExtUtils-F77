%define upstream_name	 ExtUtils-F77
%define upstream_version 1.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Simple interface to F77 libs
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/ExtUtils-F77/
Source0:	http://www.perl.com/CPAN/authors/id/KGB/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		ExtUtils-F77-1.17-no-usrlib.patch
Patch1:		ExtUtils-F77-1.17-gfortran.patch
BuildRequires:	perl-devel
BuildRequires:	gcc-gfortran
Requires:	 gcc-gfortran
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/*/*
%doc README CHANGES

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.170.0-5mdv2012.0
+ Revision: 765232
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.170.0-4
+ Revision: 763739
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.170.0-3
+ Revision: 657893
- default to gfortran
- rebuild for updated spec-helper
- rebuild for updated spec-helper

* Sun Jan 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 627519
- new version

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.1
+ Revision: 393628
- renaming package to perl-ExtUtils-F77
- renaming package to perl-ExtUtils-F77
- update to 1.16
- rediff patches to match new version
- using %%perl_convert_version
- renamed package to perl-ExtUtils-F77 (instead of perl-ExtUtils_F77)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.14-14mdv2009.0
+ Revision: 223715
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.14-13mdv2008.1
+ Revision: 151276
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

