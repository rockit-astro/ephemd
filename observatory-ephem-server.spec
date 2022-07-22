Name:      observatory-ephem-server
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/ephemd
Summary:   Exposes the current sun and moon positions for Warwick La Palma telescopes environment daemon
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common python3-astropy python3-numpy

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/var/tmp/daemon_home/astropy

%{__install} %{_sourcedir}/ephemd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/ephemd.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/ephemd
%defattr(-,root,root,-)
%{_unitdir}/ephemd.service
%dir /var/tmp/daemon_home/astropy

%changelog
