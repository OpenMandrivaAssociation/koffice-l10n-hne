Name: koffice-l10n-hne
Version: 2.1.82
Release: %mkrel 2
Summary: Language files for KOffice Chhattisgarhi
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/unstable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-hne
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Chhattisgarhi translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.82-2mdv2011.0
+ Revision: 612640
- the mass rebuild of 2010.1 packages

* Sat Apr 17 2010 Funda Wang <fwang@mandriva.org> 2.1.82-1mdv2010.1
+ Revision: 535939
- new version 2.1.82

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 491262
- new version 2.1.1

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 469530
- new version 2.1.0

* Fri Nov 13 2009 Funda Wang <fwang@mandriva.org> 2.0.91-1mdv2010.1
+ Revision: 465550
- new version 2.0.91

* Thu Sep 17 2009 Funda Wang <fwang@mandriva.org> 2.0.82-1mdv2010.0
+ Revision: 443730
- import source and spec
- Created package structure for koffice-l10n-hne.

