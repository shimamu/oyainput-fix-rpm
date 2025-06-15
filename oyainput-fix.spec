Name:           oyainput-fix
Version:        1.2
Release:        1.fcitx5fix.1.1%{?dist}
Summary:        Software to enable thumb-shift input for fcitx5

License:        GPL-3.0-or-later
URL:            https://github.com/shimamu/oyainput-fcitx5-fix
Source0:        https://github.com/shimamu/oyainput-fcitx5-fix/archive/refs/tags/v1.2-fcitx5-fix.1.1.tar.gz

BuildRequires:  gcc-c++, make, pkg-config, fcitx5-devel
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
mkdir -p %{buildroot}/usr/bin
install -m 4755 oyainput %{buildroot}/usr/bin/oyainput

# install .desktop file
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 packaging/com.github.shimamu.oyainput-fcitx5-fix.desktop %{buildroot}%{_datadir}/applications/com.github.shimamu.oyainput-fcitx5-fix.desktop

# install .svg icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m 644 packaging/com.github.shimamu.oyainput-fcitx5-fix.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.github.shimamu.oyainput-fcitx5-fix.svg

%files
%license LICENSE
%doc README.md READMEJP.md
/usr/bin/oyainput
%{_datadir}/applications/com.github.shimamu.oyainput-fcitx5-fix.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.github.shimamu.oyainput-fcitx5-fix.svg

%changelog
* Sun Jun 15 2025 shimamu <cooklecurry@gmail.com> - 1.2-1.fcitx5fix.1.1
- Initial RPM release for oyainput-fcitx5-fix, including .desktop and icon

