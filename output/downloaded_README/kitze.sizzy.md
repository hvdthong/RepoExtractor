<p align="center">
<img src="http://i.imgur.com/DmmJV3Z.png" alt="Sizzy" width="200"/>
</p>

## Sizzy

A tool for developing responsive websites crazy-fast, made by [@thekitze](http://kitze.io)

---
[![OpenCollective](https://opencollective.com/sizzy/backers/badge.svg)](#backers)
[![OpenCollective](https://opencollective.com/sizzy/sponsors/badge.svg)](#sponsors)


![gif](http://i.imgur.com/BtyqVle.gif)

## Sharing with an url
Add ```?url=http://your-url.com``` at the end of the url to share it with a preloaded url.

Example: <a href="http://sizzy.co?url=https://preactjs.com" target="_blank">http://sizzy.co?url=https://preactjs.com</a>

## Chrome extension
Adds a Sizzy button in the Chrome toolbar, which on click opens any page directly into Sizzy.

[Chrome Extension](https://chrome.google.com/webstore/detail/sizzy/nfhlbmjiiogoelaflfclodlkncbdiefo)  
[Source](https://github.com/kitze/sizzy/tree/master/chrome-extension)

## Getting Started

1. Install the dependencies:
```
yarn install
```

2. Start the server:

```sh
yarn start
```

3. Open it in your browser http://localhost:3033/

Tip: You can also use ```npm``` instead of ```yarn```, and if you want to use ```yarn``` but you don't have it on your machine, [here's how to install it](https://yarnpkg.com/lang/en/docs/install/).

## Dev issues

### Getting ```module not found``` errors
![error](http://i.imgur.com/45S4JsF.png)

Files are imported from their absolute paths instead of their relative paths to avoid repeating ```../../../../``` when requiring files. Unfortunately on some machines, the ```NODE_PATH=./src``` rule from the [.env](https://github.com/kitze/sizzy/blob/master/.env#L4) file doesn't get applied, as mentioned [in this issue](https://github.com/kitze/sizzy/issues/31).

Temporary solution is to run ```export NODE_PATH=./src``` in the terminal, before running ```yarn start```.



## Backers

Support us with a monthly donation and help us continue our activities. [[Become a backer](https://opencollective.com/sizzy#backer)]

<a href="https://opencollective.com/sizzy/backer/0/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/0/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/1/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/1/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/2/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/2/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/3/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/3/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/4/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/4/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/5/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/5/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/6/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/6/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/7/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/7/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/8/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/8/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/9/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/9/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/10/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/10/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/11/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/11/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/12/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/12/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/13/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/13/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/14/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/14/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/15/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/15/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/16/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/16/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/17/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/17/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/18/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/18/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/19/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/19/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/20/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/20/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/21/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/21/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/22/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/22/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/23/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/23/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/24/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/24/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/25/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/25/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/26/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/26/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/27/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/27/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/28/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/28/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/backer/29/website" target="_blank"><img src="https://opencollective.com/sizzy/backer/29/avatar.svg"></a>

### Sponsors

Become a sponsor and get your logo on our README on Github with a link to your site. [[Become a sponsor](https://opencollective.com/sizzy#sponsor)]

<a href="https://opencollective.com/sizzy/sponsor/0/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/0/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/1/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/1/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/2/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/2/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/3/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/3/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/4/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/4/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/5/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/5/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/6/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/6/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/7/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/7/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/8/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/8/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/9/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/9/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/10/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/10/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/11/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/11/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/12/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/12/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/13/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/13/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/14/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/14/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/15/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/15/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/16/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/16/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/17/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/17/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/18/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/18/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/19/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/19/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/20/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/20/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/21/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/21/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/22/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/22/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/23/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/23/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/24/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/24/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/25/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/25/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/26/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/26/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/27/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/27/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/28/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/28/avatar.svg"></a>
<a href="https://opencollective.com/sizzy/sponsor/29/website" target="_blank"><img src="https://opencollective.com/sizzy/sponsor/29/avatar.svg"></a>
