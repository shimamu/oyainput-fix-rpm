# oyainput-fix-rpm

This repository contains the RPM packaging files for **oyainput-fix**,
a thumb-shift based Japanese input method that works with fcitx5 and other input method frameworks.

## Fedora COPR Repository

The built RPM packages are available from the Fedora COPR repository:

[https://copr.fedorainfracloud.org/coprs/shimamu/oyainput-fix/](https://copr.fedorainfracloud.org/coprs/shimamu/oyainput-fix/)

You can enable and install the package on Fedora using the following commands:

```bash
sudo dnf copr enable shimamu/oyainput-fix
sudo dnf install oyainput-fix
```

## Description

This package provides fixes to improve compatibility with multiple input method frameworks,
including but not limited to fcitx5.

## License

This project is licensed under the GNU General Public License v3.0 or later. See [LICENSE](LICENSE) for details.

## Development / Maintenance

For maintainers or future contributors:

- The RPM package is built automatically on Fedora COPR from the [`oyainput-fix.spec`](oyainput-fix.spec) file in this repository.
- Running `make` locally to create RPM files is intended only for testing purposes.

