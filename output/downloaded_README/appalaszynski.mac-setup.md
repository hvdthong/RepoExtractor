<div align="center">
  <a href="https://github.com/appalaszynski/mac-setup">
    <img src="https://user-images.githubusercontent.com/35331661/37242209-c5d740cc-2465-11e8-92b3-e6d786e98dda.jpg" width="125px">
  </a>
  <br>
  <h1>Mac Setup</h1>
  <p>
    <em>Front End Web Development Setup for macOS</em>
  </p>
  <p>
    <a href="https://github.com/appalaszynski/mac-setup/stargazers">
      <img src="https://img.shields.io/github/stars/appalaszynski/mac-setup.svg" /> 
    </a>
    <a href="https://github.com/appalaszynski/mac-setup/network/members">
      <img src="https://img.shields.io/github/forks/appalaszynski/mac-setup.svg" /> 
    </a>
    <a href="https://github.com/appalaszynski/mac-setup">
      <img src="https://img.shields.io/badge/macOS-10.13.5-blue.svg" /> 
    </a>
    <a href="https://github.com/appalaszynski/mac-setup/commits/master">
      <img src="https://img.shields.io/github/last-commit/appalaszynski/mac-setup.svg" />
    </a>
  </p>
  <br>
  <br>
</div>

This document describes how I set up front end web development environment on my MacBook Air with macOS High Sierra 10.13.5.

---

## Table of Contents

- [Installation](#installation)
- [System Preferences](#system-preferences)
- [Terminal](#terminal)
- [Bash](#bash)
- [Homebrew](#homebrew)
- [Git](#git)
- [Node.js](#nodejs)
- [Node Package Manager](#node-package-manager)
- [Web Browsers](#web-browsers)
- [Visual Studio Code](#visual-studio-code)

---

## Installation

You can follow the instructions below or use shell script to configure settings automatically.
There are two ways to do it:

- clone/download the repository into your computer and then execute ```mac-setup.sh``` script,
- one line installation - open your terminal and paste the following code:
 
```shell
$ curl -L https://github.com/appalaszynski/mac-setup/archive/master.tar.gz | tar -xvz; cd mac-setup-master; chmod +x mac-setup.sh; ./mac-setup.sh
```

<div align="center">
  <img src="https://user-images.githubusercontent.com/35331661/40432542-3d8a4370-5eaa-11e8-88ea-b9974ae13e82.png">
</div>

---

## System Preferences

After a clean install of operating system, there are a couple tweaks I like to make to the System Preferences. Some of them are not strictly related to web development environment - I use them because of my personal habits.


- General > User dark menu bar and Dock
- General > Ask to keep changes when closing documents
- General > Close windows when quitting an app
- Dock > Automatically hide and show the Dock
- Keyboard > Key Repeat > Fast (all the way to the right)
- Keyboard > Delay Until Repeat > Short (all the way to the right)

### Set Dock size

```shell
$ defaults write com.apple.dock tilesize -int 35; killall Dock
```

### Disable "Press and hold"

```shell
$ defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false
```

### Reset icons in Launchpad

I usually use this command after installing every application that I need - it keeps Apple applications on the first page and moves the rest to the next pages.

```shell
$ defaults write com.apple.dock ResetLaunchPad -bool true; killall Dock
```

### Show hidden files

This can also be done by pressing `Command ⌘` + `Shift ⇧` + `.`.

```shell
$ defaults write com.apple.finder AppleShowAllFiles YES
```

### Show path bar in Finder

```shell
$ defaults write com.apple.finder ShowPathbar -bool true
```

### Show status bar in Finder

```shell
$ defaults write com.apple.finder ShowStatusBar -bool true
```

### Set firmware password

Setting a firmware password prevents your Mac from starting up from any device other than your startup disk. It may also be set to be required on each boot.

```shell
$ firmwarepasswd -setpasswd -setmode command
```

You can find a lot more settings in [defaults.sh](https://github.com/appalaszynski/mac-setup/blob/master/api/defaults.sh).

---

## Terminal

I use my custom Terminal profile which I called **Flat**. You can download it by typing:

```shell
$ curl -O https://raw.githubusercontent.com/appalaszynski/mac-setup/master/Flat.terminal
```

To use it as default profile open downloaded `Flat.terminal` file and click **Shell** > **Use settings as default** option.

---

## Bash

```shell
# Update Homebrew itself, upgrade all packages, remove dead symlinks, remove old versions
# of installed formulas, clean old downloads from cache, remove versions of formulas, which
# are downloaded, but not installed, check system for potential problems, remove cached
# Homebrew-Cask downloads
alias brewup='brew update; brew upgrade; brew prune; brew cleanup; brew doctor; brew cask cleanup'

# Remove bash history and exit bash shell
alias rmhis='rm .bash_history; history -c; logout'

# Easier navigation
alias ..="cd .."
alias ....="cd ../.."

# Shortcuts
alias p="cd ~/Projects"
alias d="cd ~/Desktop"

# Enable ANSI colors sequences to distinguish file types
export CLICOLOR=1

# Value of this variable describes what color to use for which attribute
export LSCOLORS=GxFxCxDxBxegedabagaced

# Color definitions
RED='\[\033[1;31m\]'
GREEN='\[\033[1;32m\]'
YELLOW='\[\033[1;33m\]'
PURPLE='\[\033[1;35m\]'
GRAY='\[\033[1;30m\]'
DEFAULT='\[\033[0m\]'

# Function which prints current Git branch name
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

# Set up prompt
PS1="${RED}\u" # Username
PS1+=" ${GRAY}• " # Separator
PS1+="${GREEN}\h" # Hostname
PS1+=" ${GRAY}• " # Seprataor
PS1+="${YELLOW}\w" # Working directory
PS1+=" ${GRAY}\$([[ -n \$(git branch 2> /dev/null) ]] && echo \"•\") " # Separator
PS1+="${PURPLE}\$(parse_git_branch)" # Git branch
PS1+="\n" # New line
PS1+="${GRAY}\$ " # Dollar sign
PS1+="${DEFAULT}" # Get back default color

export PS1;
```

In my `.bash_profile` file I create, among others, a `brewup` alias to keep Homebrew (which we are going to install in a second) up to date. I also set color scheme for `ls` command output and for custom prompt which contains username, computer name, working directory and current Git branch.

To download `.bash_profile` and execute its content, use:

```shell
$ cd ~
$ curl -O https://raw.githubusercontent.com/appalaszynski/mac-setup/master/.bash_profile
$ source ~/.bash_profile
```

---

## Homebrew

[Homebrew](http://brew.sh/) package manager allows to install almost any app right from the command line.

### Installation

```shell
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Usage

To install specific package use ```brew install <package>``` e.g.

```shell
$ brew install git
```

### Brewfile

Installing each package separately may take some time. That's why I use [Homebrew Bundle](https://github.com/Homebrew/homebrew-bundle), which allows to automatically install all packages and applications listed in the `Brewfile` file.

Here are all the programs I install with a brief description.

- [Cask](https://caskroom.github.io) - an extension to Homebrew which allows to install almost any program that exists for a Mac
- [Git](https://git-scm.com) - version control system
- [mas-cli](https://github.com/mas-cli/mas) - Mac App Store command line interface
- [AppCleaner](https://freemacsoft.net/appcleaner/) - apps uninstaller
- [Filezilla](https://filezilla-project.org) - FTP client
- [Firefox](https://www.mozilla.org/firefox/new/) - web browser
- [Flux](https://justgetflux.com) - screen color temperature adjusting app
- [Fork](https://git-fork.com) - Git GUI client
- [Google Chrome](https://www.google.pl/chrome/browser/desktop/index.html) - web browser
- [Kap](https://getkap.co/) - screen recorder
- [KeepingYouAwake](https://github.com/newmarcel/KeepingYouAwake) - app which prevents Mac from entering sleep mode
- [Keka](http://www.kekaosx.com) - file archiver
- [MAMP](https://www.mamp.info/en/) - Apache, MySQL and PHP package
- [Opera](http://www.opera.com) - web browser
- [Postman](https://www.getpostman.com) - API testing tool
- [Sequel Pro](http://www.sequelpro.com) - MySQL GUI tool
- [Skype](https://www.skype.com) - voice and video chat
- [Slack](https://slack.com) - team collaboration tools
- [Spectacle](https://www.spectacleapp.com) - window manager
- [Transmission](https://transmissionbt.com) - BitTorrent client
- [Tunnelblick](https://tunnelblick.net/) - GUI for OpenVPN
- [Visual Studio Code](https://code.visualstudio.com) - code editor
- [VLC](https://www.videolan.org/vlc/) - media player
- [iMovie](https://www.apple.com/imovie/) - video editor
- [Pages](https://www.apple.com/pages/) - text editor
- [Numbers](https://www.apple.com/numbers/) - spreadsheet editor

Below are the entire contents of my `Brewfile`, which will install all the above programs with a single command.

```ruby
tap 'caskroom/cask'

brew 'git'
brew 'mas'

cask 'appcleaner'
cask 'filezilla'
cask 'firefox'
cask 'flux'
cask 'fork'
cask 'google-chrome'
cask 'kap'
cask 'keepingyouawake'
cask 'keka'
cask 'mamp'
cask 'opera'
cask 'postman'
cask 'sequel-pro'
cask 'skype'
cask 'slack'
cask 'spectacle'
cask 'transmission'
cask 'tunnelblick'
cask 'visual-studio-code'
cask 'vlc'

mas "iMovie", id: 408981434
mas "Numbers", id: 409203825
mas "Pages", id: 409201541
```

To check App Store application's IDs use:

```shell
$ mas search <app name>
```

To download my `Brewfile` file type:

```shell
$ curl -O https://raw.githubusercontent.com/appalaszynski/mac-setup/master/Brewfile
```

To install applications listed in `Brewfile` use:

```shell
$ brew bundle
```

in directory that contains `Brewfile`.

---

## Git

You can set Git global configuration two ways. The first is to run a bunch of commands which will update the Git configuration file, e.g.

```shell
$ git config --global user.name "First Last"
$ git config --global user.email "email@email.com"
```

The other and faster way is creating the Git configuration file and input it all ourselves.

```shell
$ cd ~
$ curl -O https://raw.githubusercontent.com/appalaszynski/mac-setup/master/.gitconfig
$ open .gitconfig
```

```properties
[user]
  name = First Last
  email = email@email.com
[github]
  user = username
[core]
  editor = editor
[credential]
  helper = osxkeychain
```

Here I set my name, email, GitHub username, core editor and connect Git to the macOS Keychain so I don’t have to type my username and password every time I want to push to GitHub.

### SSH

You can also authenticate GiHub using SSH public key. You must generate one if they don’t already have one. To do is use following code:

```shell
$ ssh-keygen -t rsa -b 4096 -C "your_email_used_in_github@example.com"
```

but first make sure that there is a `~/.ssh` directory on your computer.

Above command will create a private key (`id_rsa`) and public key (`id_rsa.pub`) in `~/.ssh` directory.
Next add your newly created SSH key to the ssh-agent to be able to manage your keys.

```shell
$ ssh-add <path to private key>
```

Now just login into your Github account and paste content of `id_rsa.pub` file in **Settings** > **SSH and GPG keys** > **New SSH key**.

After you've set up your SSH key and added it to your GitHub account, you can test your connection. Open Terminal and paste following code:

```shell
$ ssh -T git@github.com
```

After verifying figerprint by typing `yes` you should see the following message:

```shell
Hi <your username>! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## Node.js

For installation of Node.js I like to use [Node Version Manager](https://github.com/creationix/nvm) (nvm). To download it type:

```shell
$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
```

You can check all available Node.js versions by:

```shell
$ nvm list-remote
```

To install specific version type:

```shell
$ nvm install <version>
```

---

## Node Package Manager

Packages which I use globally at the moment are:
* [Gulp](https://gulpjs.com)
* [Webpack](https://webpack.js.org)
* [npm-upgrade](https://www.npmjs.com/package/npm-upgrade)

To install them use:

```shell
$ npm install -g gulp-cli webpack npm-upgrade
```

---

## Web Browsers

Currently I have installed all major web browsers:

- [Chrome](https://www.google.com/chrome/)
- [Safari](https://www.apple.com/safari/)
- [Opera](https://www.opera.com/)
- [Firefox](https://www.mozilla.org/en-US/firefox/)

For main development I use Google Chrome.

### Chrome extensions

- [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) - block ads
- [Privacy Badger](https://chrome.google.com/webstore/detail/privacy-badger/pkehgijcmpdhfbdbbnkijodmdjhbjlgp) - block spying ads and invisible trackers
- [Nano Defender](https://chrome.google.com/webstore/detail/nano-defender/ggolfgbegefeeoocgjbmkembbncoadlb) - anti-adblock defuser
- [HTTPS Everywhere](https://chrome.google.com/webstore/detail/https-everywhere/gcbommkclmclpchllfjekcdonpmejbdp?hl=pl) - automatically switch from "http" to "https"
- [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc) - validate and view JSON documents
- [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) - inspect component hierarchies and states
- [Redux DevTools](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd) - debug state changes
- [Pesticide](https://chrome.google.com/webstore/detail/pesticide-for-chrome/bblbgcheenepgnnajgfpiicnbbdmmooh) - toggle different colored outlines on every element for quick CSS layout debug

---

## Visual Studio Code

All default settings changes are stored in `settings.json` file. You can open it by pressing `Command ⌘` + `,` going to Code > Preferences > Settings.
Here are my `settings.json` contents: 

```json
{
  "workbench.startupEditor": "newUntitledFile",
  "workbench.colorTheme": "Monokai",
  "workbench.activityBar.visible": false,
  "workbench.iconTheme": "material-icon-theme",
  "workbench.statusBar.feedback.visible": false,
  "editor.fontSize": 12,
  "editor.tabSize": 2,
  "editor.multiCursorModifier": "ctrlCmd",
  "editor.minimap.enabled": false,
  "editor.formatOnPaste": true,
  "editor.detectIndentation": false,
  "problems.decorations.enabled": false,
  "explorer.openEditors.visible": 0,
  "explorer.decorations.colors": false,
  "files.insertFinalNewline": true,
  "html.autoClosingTags": false,
  "files.exclude": {
    "**/node_modules/": true,
    "**/.vscode/": true,
  },
  "material-icon-theme.folders.theme": "classic",
  "material-icon-theme.hidesExplorerArrows": true,
  "material-icon-theme.folders.color": "#90a4ae",
  "material-icon-theme.opacity": 0.8,
  "eslint.autoFixOnSave": true,
  "todohighlight.isEnable": true,
  "todohighlight.keywords": [
    {
      "text": "TODO:",
      "color": "black",
      "backgroundColor": "yellow",
      "overviewRulerColor": "yellow"
    },
    {
      "text": "FIXME:",
      "color": "white",
      "backgroundColor": "red",
      "overviewRulerColor": "red"
    }
  ],
  "todohighlight.exclude": [
    "**/public/"
  ],
  "auto-rename-tag.activationOnLanguage": [
    "html",
    "xml",
    "javascript",
    "javascriptreact"
  ],
  "bracketPairColorizer.activeScopeCSS": [
    "borderStyle : solid",
    "borderWidth : 1px",
    "borderColor : {color}; opacity: 0.5",
    "backgroundColor : {color}"
  ],
  "bracketPairColorizer.highlightActiveScope": true,
  "debug.allowBreakpointsEverywhere": true,
}
```

You can copy and paste them or just download whole file by:

```shell
$ cd /Users/Your Username/Library/Application Support/Code/User
$ curl -O https://raw.githubusercontent.com/appalaszynski/mac-setup/master/settings.json
```

### Extensions

- [Auto Rename Tag](https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag) - automatically rename paired HTML tag
- [Bracket Pair Colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer) - match brackets to be identified with colours
- [Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome) - debug JavaScript code running in Google Chrome from VS Code
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) - integrate ESLint into VS Code
- [JavaScript (ES6) code snippets](https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets) - code snippets for JavaScript in ES6 syntax
- [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme) - icons based on Material Design
- [open in browser](https://marketplace.visualstudio.com/items?itemName=techer.open-in-browser) - open any file in browser right from VS Code explorer
- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) -  autocomplete filenames
- [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager) - manage projects right inside VS Code
- [Reactjs code snippets](https://marketplace.visualstudio.com/items?itemName=xabikos.ReactSnippets) - code snippets for React development
- [SCSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-scss) - autocomplete variables, mixins, functions etc.
- [TODO Highlight](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight) - highlight and list TODO, FIXME or any annotations within code

To install all extensions by one command use:

```shell
$ code --install-extension CoenraadS.bracket-pair-colorizer --install-extension PKief.material-icon-theme --install-extension alefragnani.project-manager --install-extension christian-kohler.path-intellisense --install-extension dbaeumer.vscode-eslint --install-extension formulahendry.auto-rename-tag --install-extension mrmlnc.vscode-scss --install-extension msjsdiag.debugger-for-chrome --install-extension techer.open-in-browser --install-extension wayou.vscode-todo-highlight --install-extension xabikos.ReactSnippets --install-extension xabikos.JavaScriptSnippets
```
