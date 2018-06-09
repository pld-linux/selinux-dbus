Summary:	DBus service to handle SELinux administration tasks
Summary(pl.UTF-8):	Usługa DBus do obsługi zadań administracyjnych SELinuksa
Name:		selinux-dbus
Version:	2.8
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/SELinuxProject/selinux/wiki/Releases
Source0:	https://raw.githubusercontent.com/wiki/SELinuxProject/selinux/files/releases/20180524/%{name}-%{version}.tar.gz
# Source0-md5:	23f0264df3ed123904a17d71f2a5b325
URL:		https://github.com/SELinuxProject/selinux/wiki
BuildRequires:	rpm-pythonprov
# /usr/bin/semodule
Requires:	policycoreutils >= 2.8
Requires:	python >= 2
Requires:	python-dbus
Requires:	python-modules >= 2
Requires:	python-pygobject3 >= 3
Requires:	python-selinux >= 2.8
Requires:	python-slip-dbus
# /usr/sbin/semanage
Requires:	selinux-python >= 2.8
Conflicts:	policycoreutils-sepolicy < 2.7
Conflicts:	system-config-selinux < 2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Security-enhanced Linux is a patch of the Linux kernel and a number of
utilities with enhanced security functionality designed to add
mandatory access controls to Linux. The Security-enhanced Linux kernel
contains new architectural components originally developed to improve
the security of the Flask operating system. These architectural
components provide general support for the enforcement of many kinds
of mandatory access control policies, including those based on the
concepts of Type Enforcement, Role-based Access Control, and
Multi-level Security.

This package contains DBus service to handle SELinux administration
tasks.

%description -l pl.UTF-8
Security-enhanced Linux jest prototypem jądra Linuksa i wielu
aplikacji użytkowych o funkcjach podwyższonego bezpieczeństwa.
Zaprojektowany jest tak, aby w prosty sposób ukazać znaczenie
obowiązkowej kontroli dostępu dla społeczności linuksowej. Ukazuje
również jak taką kontrolę można dodać do istniejącego systemu typu
Linux. Jądro SELinux zawiera nowe składniki architektury pierwotnie
opracowane w celu ulepszenia bezpieczeństwa systemu operacyjnego
Flask. Te elementy zapewniają ogólne wsparcie we wdrażaniu wielu typów
polityk obowiązkowej kontroli dostępu, włączając te wzorowane na: Type
Enforcement (TE), kontroli dostępu opartej na rolach (RBAC) i
zabezpieczeniach wielopoziomowych.

Ten pakiet zawiera usługę DBus do obsługi zadań administracyjnych
SELinuksa.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{_datadir}/system-config-selinux
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/system-config-selinux

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc selinux_client.py
/etc/dbus-1/system.d/org.selinux.conf
%{_datadir}/dbus-1/system-services/org.selinux.service
%{_datadir}/polkit-1/actions/org.selinux.policy
%dir %{_datadir}/system-config-selinux
%attr(755,root,root) %{_datadir}/system-config-selinux/selinux_server.py
%{_datadir}/system-config-selinux/selinux_server.py[co]
