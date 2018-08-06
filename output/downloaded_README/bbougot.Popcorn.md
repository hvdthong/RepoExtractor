<h1 align="center">
  <img src="https://raw.githubusercontent.com/bbougot/Popcorn/master/Popcorn/icon.ico" height="128" width="128" alt="Logo" />
  <br />
  Popcorn
</h1>

<h3 align="center">A Powerful and Fast Popcorn Time Client</h3>

<div align="center">
  
  [![Gitter](https://img.shields.io/badge/Gitter-Join%20Chat-green.svg?style=flat-square)](https://gitter.im/popcorn-app/popcorn) <a href="https://popcorn-slack.azurewebsites.net" target="_blank">
    <img alt="Slack" src="http://popcorn-slack.azurewebsites.net/badge.svg">
  </a>
   [![Releases](https://img.shields.io/github/release/bbougot/Popcorn.svg)](https://github.com/bbougot/Popcorn/releases)
  [![Build status](https://ci.appveyor.com/api/projects/status/mjnfwck6otg9c5wj/branch/master?svg=true)](https://ci.appveyor.com/project/bbougot/popcorn/branch/master)
  [![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=Popcorn&metric=ncloc)](https://sonarcloud.io/dashboard?id=Popcorn)
  [![Coverage Status](https://coveralls.io/repos/github/bbougot/Popcorn/badge.svg?branch=master)](https://coveralls.io/github/bbougot/Popcorn?branch=master) 
  <a target="_blank" href="https://github.com/bbougot/Popcorn/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" />
  </a>
</div>

# Popcorn
Popcorn is a simple application which lets you watch any movie or TV show instantly.

## Features

* Huge database
    * The API collects most of known movies (7000+) and shows (3000+)

* Performance
    * A strong effort has been made to get the best performance from UI navigation and downloading

* Capabilities
    * Popcorn offers a wide set of functionalities (Trailer, subtitles, Chromecast support, filtering by genre and rating, ...)

## How does it work

### Frontend
* Framework
    * The app is a .NET 4.7.1 application using WPF framework. 

* Basics
    * It communicates with its own [API](https://github.com/bbougot/PopcornAPI) to query movies, shows, trailers, cast, assets and torrents. The app includes a video player ([ffmediaelement](https://github.com/unosquare/ffmediaelement)) and a torrent handler ([libtorrent](https://github.com/bbougot/libtorrent-net)) and is also able to cast to a Chromecast device.

* Advanced
    * The app can update by itself automatically using an incremental update system.
    * Popcorn also sends usage data to Azure Application Insights.

### Backend
* The backend is powered by a Microsoft stack
    * The [API](https://github.com/bbougot/PopcornAPI) is a ASP.NET Core app which serves movies and shows from SQL Server database. It also supports caching using Redis database.
    * The assets (images and torrent files) are stored on Azure Blob Storage.

## Supported platforms
Windows 7+ is supported (Windows 7, 8, 8.1, 10).

## Installation
Download installer [here](https://github.com/bbougot/Popcorn/releases/download/v5.0.1/PopcornInstaller.exe) 

## Todos
See the [roadmap](https://github.com/bbougot/Popcorn/projects/1) for the full list.

## Mockups

### Home Page
![Home Page](https://github.com/bbougot/Popcorn/blob/master/Screenshots/Screen1.jpg)

### Movie Page
![Movie Page](https://github.com/bbougot/Popcorn/blob/master/Screenshots/Screen2.jpg)

### Show Page
![Show Page](https://github.com/bbougot/Popcorn/blob/master/Screenshots/Screen3.jpg)

### Actor Page
![Show Page](https://github.com/bbougot/Popcorn/blob/master/Screenshots/Screen4.jpg)

## License
If you distribute a copy or make a fork of the project, you have to credit this project as source.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

**This project and the distribution of this project is not illegal, nor does it violate any DMCA laws. The use of this project, however, may be illegal in your area. Check your local laws and regulations regarding the use of torrents to watch potentially copyrighted content. The maintainers of this project do not condone the use of this project for anything illegal, in any state, region, country, or planet. Please use at your own risk.**
