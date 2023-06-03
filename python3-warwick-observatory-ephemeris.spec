Name:           python3-warwick-observatory-ephemeris
Version:        20230603
Release:        0
License:        GPL3
Summary:        Common backend code for the Warwick telescopes ephemeris daemon
Url:            https://github.com/warwick-one-metre/ephemd
BuildArch:      noarch

%description

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
