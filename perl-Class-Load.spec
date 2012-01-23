#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Class
%define		pnam	Load
%include	/usr/lib/rpm/macros.perl
Summary:	Class::Load - a working (require "Class::Name") and more
Summary(pl.UTF-8):	Class::Load - działające (require "Klasa::Nazwa") i inne
Name:		perl-Class-Load
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d26a8c6da4e12d72d9f06a47c89c6a73
URL:		http://search.cpan.org/dist/Class-Load/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Test-Fatal
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
require EXPR only accepts Class/Name.pm style module names, not
Class::Name. How frustrating! For that, we provide load_class
'Class::Name'.

It's often useful to test whether a module can be loaded, instead of
throwing an error when it's not available. For that, we provide
try_load_class 'Class::Name'.

Finally, sometimes we need to know whether a particular class has been
loaded. Asking %%INC is an option, but that will miss inner packages
and any class for which the filename does not correspond to the
package name. For that, we provide is_class_loaded 'Class::Name'.

%description -l pl.UTF-8
require EXPR przyjmuje tylko nazwy modułów w stylu Klasa/Nazwa.pm, a
nie Klasa::Nazwa - jest to frustrujące. Dlatego moduł ten udostępnia
funkcję load_class 'Klasa::Nazwa'.

Często przydaje się sprawdzić, czy moduł może być załadowany, zamiast
rzucania błędu, kiedy jest niedostępny. Dlatego modułu ten udostępnia
funkcję try_load_class 'Klasa::Nazwa'.

W końcu - czasem trzeba sprawdzić, czy dana klasa została załadowana.
Sprawdzanie %%INC jest jakąś opcją, ale pominie pakiety i klasy, dla
których nazwa pliku nie zgadza się z nazwą pakietu. Dlatego moduł ten
udostępnia funkcję is_class_loaded 'Klasa::Nazwa'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/Load.pm
%{perl_vendorlib}/Class/Load
%{_mandir}/man3/Class::Load.3pm*
