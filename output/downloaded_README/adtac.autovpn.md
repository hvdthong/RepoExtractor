# autovpn

`autovpn` is a tool to automatically connect you to a random VPN in a country
of your choice. It uses [openvpn][openvpn] to connect you to a server obtained
from [VPN Gate](http://www.vpngate.net/en/).

### Compiling

First clone the repo and `cd` into the directory:

```bash
$ git clone https://github.com/adtac/autovpn
$ cd autovpn
```

Then run this to generate the executable:

```bash
$ go build autovpn.go
```

It's Go. What do you expect?

### Requirements

This requires [openvpn][openvpn].

To install this on a `yum`-based distro:

```bash
$ sudo dnf install openvpn
```

If you're on a `apt`-based distro:

```bash
$ sudo apt-get install openvpn
```

And on Mac OSX:

```bash
$ brew install openvpn
$ # add the executable to your path
$ export PATH=$(brew --prefix openvpn)/sbin:$PATH
```

Tested and works on Fedora 23 and MacOS Sierra `10.12.6`. Dunno about
Windows. Patches welcome.

### Usage

Simply run:

```bash
$ ./autovpn
```

and you're done. You'll be connected to a server in the US. Welcome to the US!

You can give a country if you want. For example, if you want to connect to a server
in Japan:

```bash
$ ./autovpn JP
```

You may need superuser privileges. Don't worry, I'm not running `rm -rf --no-preserve-root /`
underneath. It's for `openvpn`.

### Contributing

All patches welcome!

### Disclaimer

This is completely insecure. Please do not use this for anything important. Get a
real and secure VPN. This is mostly a fun tool to get a VPN for a few minutes.

### License

```
    autovpn - simple automatic VPN in a country of your choice
    Copyright (C) 2017  Adhityaa Chandrasekar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
```


[openvpn]: https://github.com/OpenVPN/openvpn
