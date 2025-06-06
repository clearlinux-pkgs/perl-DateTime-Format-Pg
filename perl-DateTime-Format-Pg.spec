#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-DateTime-Format-Pg
Version  : 0.16014
Release  : 32
URL      : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/DateTime-Format-Pg-0.16014.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DM/DMAKI/DateTime-Format-Pg-0.16014.tar.gz
Summary  : 'Parse and format PostgreSQL dates and times'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-DateTime-Format-Pg-license = %{version}-%{release}
Requires: perl-DateTime-Format-Pg-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Getopt::Long)
BuildRequires : perl(Module::Build::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
DateTime::Format::Pg - Parse and format PostgreSQL dates and times
# SYNOPSIS

%package dev
Summary: dev components for the perl-DateTime-Format-Pg package.
Group: Development
Provides: perl-DateTime-Format-Pg-devel = %{version}-%{release}
Requires: perl-DateTime-Format-Pg = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-Pg package.


%package license
Summary: license components for the perl-DateTime-Format-Pg package.
Group: Default

%description license
license components for the perl-DateTime-Format-Pg package.


%package perl
Summary: perl components for the perl-DateTime-Format-Pg package.
Group: Default
Requires: perl-DateTime-Format-Pg = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-Pg package.


%prep
%setup -q -n DateTime-Format-Pg-0.16014
cd %{_builddir}/DateTime-Format-Pg-0.16014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Pg
cp %{_builddir}/DateTime-Format-Pg-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Pg/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::Pg.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-Pg/f235ba4160673bcb7c9d58c2f09dbc7fc0efadea

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
