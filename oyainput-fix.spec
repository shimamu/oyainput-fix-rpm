Name:           oyainput-fix
Version:        1.2
Release:        2.fcitx5fix.1.1%{?dist}
Summary:        Software to enable thumb-shift input for fcitx5

License:        GPL-3.0-or-later
URL:            https://github.com/shimamu/oyainput-fcitx5-fix
Source0:        https://github.com/shimamu/oyainput-fcitx5-fix/archive/refs/tags/v1.2-fcitx5-fix.1.1.tar.gz

BuildRequires:  gcc-c++, make
Recommends:     fcitx5

%description
OyaInput is a thumb-shift based Japanese input method inspired by the NICOLA layout.
This package provides a fixed and improved version for better compatibility with fcitx5,
but it can also work independently of fcitx5.

It enables efficient kana input for users familiar with thumb-shift typing,
supporting modern Linux desktops.

%prep
%setup -q -n oyainput-fcitx5-fix-1.2-fcitx5-fix.1.1

%build
make

%install
# install binary with setuid permission
mkdir -p %{buildroot}%{_bindir}
install -m 4755 oyainput %{buildroot}%{_bindir}/oyainput

# install .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 packaging/com.github.shimamu.oyainput-fcitx5-fix.desktop \
    %{buildroot}%{_datadir}/applications/com.github.shimamu.oyainput-fcitx5-fix.desktop

# install .desktop file for autostart
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
install -m 644 packaging/com.github.shimamu.oyainput-fcitx5-fix.desktop \
    %{buildroot}%{_sysconfdir}/xdg/autostart/com.github.shimamu.oyainput-fcitx5-fix.desktop

# install .svg icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 644 packaging/com.github.shimamu.oyainput-fcitx5-fix.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.github.shimamu.oyainput-fcitx5-fix.svg

%files
%license LICENSE
%doc README.md READMEJP.md
%{_bindir}/oyainput
%{_datadir}/applications/com.github.shimamu.oyainput-fcitx5-fix.desktop
%{_sysconfdir}/xdg/autostart/com.github.shimamu.oyainput-fcitx5-fix.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.github.shimamu.oyainput-fcitx5-fix.svg

%changelog
* Fri Sep 25 2026 shimamu <cooklecurry@gmail.com> - 1.2-2.fcitx5fix.1.1
- Add autostart entry for GNOME
