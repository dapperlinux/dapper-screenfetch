Name:           dapper-screenfetch
Version:        3.8.1
Release:        1%{?dist}
Summary:        A "Bash Screenshot Information Tool"

License:        GPLv3+
URL:            https://github.com/dapperlinux/dapper-screenfetch
Source0:        %{name}-%{version}.tar.xz

BuildArch:      noarch
Provides:       screenfetch
Obsoletes:      screenfetch
Recommends:     scrot

%description
This handy Bash script can be used to generate one of
those nifty terminal theme information + ASCII distribution
logos you see in everyone's screen-shots nowadays. It will
auto-detect your distribution and display an ASCII version
of that distribution's logo and some valuable information
to the right. There are options to specify no ASCII art,
colors, taking a screen-shot upon displaying info, and even
customizing the screen-shot command! This script is very easy
to add to and can easily be extended.

%prep
%setup -q

%build
#Nothing to build

%install
install -m 755 -p -D screenfetch %{buildroot}%{_bindir}/screenfetch
install -m 644 -p -D screenfetch.1.gz %{buildroot}%{_mandir}/man1/screenfetch.1.gz

%files
%license LICENSE
%{_bindir}/screenfetch
%{_mandir}/man1/screenfetch.1.gz

%changelog
* Sun Jun 11 2017 Matthew Ruffell <msr50@uclive.ac.nz> - 3.8.0-1
- Initial release
