#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-Pg
Version  : 0.16013
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/DateTime-Format-Pg-0.16013.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/DateTime-Format-Pg-0.16013.tar.gz
Summary  : 'Parse and format PostgreSQL dates and times'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-DateTime-Format-Pg-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
# NAME
DateTime::Format::Pg - Parse and format PostgreSQL dates and times
# SYNOPSIS

%package dev
Summary: dev components for the perl-DateTime-Format-Pg package.
Group: Development
Provides: perl-DateTime-Format-Pg-devel = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-Pg package.


%package license
Summary: license components for the perl-DateTime-Format-Pg package.
Group: Default

%description license
license components for the perl-DateTime-Format-Pg package.


%prep
%setup -q -n DateTime-Format-Pg-0.16013

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Pg
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Pg/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1DateTime/Format/Pg.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::Pg.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-Pg/LICENSE
