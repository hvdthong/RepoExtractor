# pmbootstrap
[**Introduction**](https://postmarketos.org/blog/2017/05/26/intro/) | [**Security Warning**](https://ollieparanoid.github.io/post/security-warning/) | [**Devices**](https://wiki.postmarketos.org/wiki/Devices) | [![travis badge](https://api.travis-ci.org/postmarketOS/pmbootstrap.png?branch=master)](https://travis-ci.org/postmarketOS/pmbootstrap) | [![Coverage Status](https://coveralls.io/repos/github/postmarketOS/pmbootstrap/badge.svg?branch=master)](https://coveralls.io/github/postmarketOS/pmbootstrap?branch=master)

Sophisticated chroot/build/flash tool to develop and install [postmarketOS](https://postmarketos.org).

## Requirements
* 2 GB of RAM recommended for compiling
* Linux distribution (`x86`, `x86_64`, or `aarch64`)
  * [Windows subsystem for Linux (WSL)](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) does **not** work! Please use [VirtualBox](https://www.virtualbox.org/) instead.
  * Kernels based on the grsec patchset [do **not** work](https://github.com/postmarketOS/pmbootstrap/issues/107) *(Alpine: use linux-vanilla instead of linux-hardened, Arch: linux-hardened [is not based on grsec](https://www.reddit.com/r/archlinux/comments/68b2jn/linuxhardened_in_community_repo_a_grsecurity/))*
  * On Alpine Linux only: `apk add coreutils`
* Python 3.4+
* OpenSSL

## Usage Examples
Please refer to the [postmarketOS wiki](https://wiki.postmarketos.org) for in-depth coverage of topics such as [porting to a new device](https://wiki.postmarketos.org/wiki/Porting_to_a_new_device) or [installation](https://wiki.postmarketos.org/wiki/Installation_guide). The help output (`pmbootstrap -h`) has detailed usage instructions for every command. Read on for some generic examples of what can be done with `pmbootstrap`.

### Basics
Initial setup:
```
$ git clone https://github.com/postmarketOS/pmbootstrap
$ cd pmbootstrap
$ alias pmbootstrap=$PWD/pmbootstrap.py
$ pmbootstrap init
```

To make the `pmbootstrap` alias persistent, [see the wiki](https://wiki.postmarketos.org/wiki/Porting_to_a_new_device#Shortcut).

Run this in a second window to see all shell commands that get executed:
```
$ pmbootstrap log
```

### Packages
Build `aports/main/hello-world`:
```
$ pmbootstrap build hello-world
```

Cross-compile to `armhf`:
```
$ pmbootstrap build --arch=armhf hello-world
```

Build with source code from local folder:
```
$ pmbootstrap build linux-postmarketos-mainline --src=~/code/linux
```

Update checksums:
```
$ pmbootstrap checksum hello-world
```

Generate a template for a new package:
```
$ pmbootstrap newapkbuild "https://github.com/postmarketOS/osk-sdl/archive/0.51.tar.gz"
```

### Chroots
Enter the `armhf` building chroot:
```
$ pmbootstrap chroot -b armhf
```

Run a command inside a chroot:
```
$ pmbootstrap chroot -- echo test
```

Safely delete all chroots:
```
$ pmbootstrap zap
```

### Device Porting Assistance
Analyze Android [`boot.img`](https://wiki.postmarketos.org/wiki/Glossary#boot.img) files (also works with recovery OS images like TWRP):
```
$ pmbootstrap bootimg_analyze ~/Downloads/twrp-3.2.1-0-fp2.img
```

Check kernel configs:
```
$ pmbootstrap kconfig check
```

Edit a kernel config:
```
$ pmbootstrap kconfig edit --arch=armhf postmarketos-mainline
```

### System Image
Build the system image:
```
$ pmbootstrap install
```

Update existing installation on SD card (full disk encryption disabled):
```
$ pmbootstrap install --sdcard=/dev/mmcblk0 --no-fde --rsync
```

Run the image in Qemu:
```
$ pmbootstrap qemu --image-size=1G
```

Flash to the device:
```
$ pmbootstrap flasher flash_kernel
$ pmbootstrap flasher flash_rootfs --partition=userdata
```

Export the rootfs, kernel, initramfs, `boot.img` etc.:
```
$ pmbootstrap export
```

Extract the initramfs
```
$ pmbootstrap initfs extract
```

Build and flash Android recovery zip:
```
$ pmbootstrap install --android-recovery-zip
$ pmbootstrap flasher --method=adb sideload
```

### Repository Maintenance
Increase the `pkgrel` for each aport where the binary package has outdated dependencies (e.g. after soname bumps):
```
$ pmbootstrap pkgrel_bump --auto
```

Generate cross-compiler aports based on the latest version from Alpine's aports:
```
$ pmbootstrap aportgen binutils-armhf gcc-armhf
```

Manually rebuild package index:
```
$ pmbootstrap index
```

Delete local binary packages without existing aport of same version:
```
$ pmbootstrap zap -m
```

### Debugging
Use `-v` on any action to get verbose logging:
```
$ pmbootstrap -v build hello-world
```

Parse a single APKBUILD and return it as JSON:
```
$ pmbootstrap apkbuild_parse hello-world
```

Parse a package from an APKINDEX and return it as JSON:
```
$ pmbootstrap apkindex_parse $WORK/cache_apk_x86_64/APKINDEX.8b865e19.tar.gz hello-world
```

`ccache` statistics:
```
$ pmbootstrap stats --arch=armhf
```

`distccd` log:
```
$ pmbootstrap log_distccd
```

## Development
### Testing
Install `pytest` (via your package manager or pip) and run it inside the pmbootstrap folder.

## License
[GPLv3](LICENSE)
