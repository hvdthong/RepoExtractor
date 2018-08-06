# ![logo](https://raw.githubusercontent.com/Eastrall/Ether.Network/master/resources/banner.png)

[![forthebadge](http://forthebadge.com/images/badges/made-with-c-sharp.svg)](http://forthebadge.com)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

[![Build Status](https://travis-ci.org/Eastrall/Ether.Network.svg?branch=develop)](https://travis-ci.org/Eastrall/Ether.Network)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e84d77087d6940f79061799383cc1432)](https://www.codacy.com/app/Eastrall/Ether.Network?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Eastrall/Ether.Network&amp;utm_campaign=Badge_Grade)
[![NuGet Status](https://img.shields.io/nuget/v/Ether.Network.svg)](https://www.nuget.org/packages/Ether.Network/)

Ether.Network is a basic library to make quickly a simple server or client using sockets.

This library is coded with C# using .NET Core framework to target Windows and Linux operating systems.

## Framework support

- .NET Core 1.0 (netstandard1.3)
- .NET Core 2.0 (netstandard2.0)
- .NET Framework 4.5
- .NET Framework 4.6

## Features

### Server

- Client management
- Broadcast packets to all connected users or a list of connected users.
- Scalable configuration
	- Maximum of connected users
	- Bytes allocated per users

### Client

- Connect to a TCP server
- Disconnect from a server
- Send packets
- Receieve packets
- Scalable configuration
	- Bytes allocated per users

### Packets
- Create packet streams
- Read packet streams
- Create your own packet processor

## How to install

Create a .NETCore project and add the nuget package: `Ether.Network` or you can do it manually in you NuGet console package manager :

```
$> Install-Package Ether.Network
```
