Name:      rockit-ephemeris
Version:   %{_version}
Release:   1
Summary:   Exposes the current sun and moon positions for the environment daemon
Url:       https://github.com/rockit-astro/ephemd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/var/tmp/daemon_home/astropy
mkdir -p %{buildroot}%{_sysconfdir}/ephemd

%{__install} %{_sourcedir}/ephemd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/ephemd@.service %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/lapalma.json %{buildroot}%{_sysconfdir}/ephemd
%{__install} %{_sourcedir}/warwick.json %{buildroot}%{_sysconfdir}/ephemd

%package server
Summary:  Ephemeris server
Group:    Unspecified
Requires: python3-rockit-common python3-astropy
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/ephemd
%defattr(-,root,root,-)
%{_unitdir}/ephemd@.service
%dir /var/tmp/daemon_home/astropy

%package data-lapalma
Summary: Ephemeris data for La Palma telescopes
Group:   Unspecified
%description data-lapalma

%files data-lapalma
%defattr(0644,root,root,-)
%{_sysconfdir}/ephemd/lapalma.json

%package data-warwick
Summary: Ephemeris data for Windmill Hill observatory
Group:   Unspecified
%description data-warwick

%files data-warwick
%defattr(0644,root,root,-)
%{_sysconfdir}/ephemd/warwick.json

%changelog
