# Kenneth Reitz's Dotfiles

I keep these stored in iCloud, and synced across all machines (including Linux machines).

    $ ln -s '~/Library/Mobile Documents/com~apple~CloudDocs' ~/iCloud
    $ cd ~/iCloud/dotfiles
    $ ./install.sh | ./update.sh

### Fish Shell

I use the [Fish Shell](https://fishshell.com). It's excellent software. I use [fisherman](https://github.com/fisherman/fisherman) to manage my shell plugins:

    $ fisher ls
    anicode		    	grc
    autojump	    	humanize_duration
    bang-bang	    	osx
    bass		    	pipenv-fish
    bd		        	pisces
    choices		    	pyenv
    docker-completion	python
    done		    	segment
    extract		    	spin
    get		        	ssh
    getopts		    	ssh-term-helper
    git_util	    	tab

### Homebrew Packages
    
List of [installed packages](https://github.com/kennethreitz/dotfiles/blob/master/install.sh).

### Useful MacOS Utilities

    $ battery
    <displays battery state>

    $ cpu
    Intel(R) Core(TM) i5-4690 CPU @ 3.50GHz

    $ lock
    (locks screen)

    $ icloud
    observing in /Volumes/KR/Library/Mobile Documents/com~apple~CloudDocs for the docs|data|external scope(s)
    2018-03-07 13:21:29 +0000 total:10
     o /Lightroom ☁
     o /repos ☁
     o /Apps ☁
     o /Sublime Text 3 ↑ 229 KB (229350) 12.2%  ↓ 384 KB (384337) 100.0%  server edit to download
     o /dotfiles ↑ 1.9 MB (1924925) 95.0%  ↓ 4 KB (3801) 100.0%  server edit to download
     o /.Trash ☁
     o /go ☁
     o /Lightroom CC ☁
     o /Sketches Pro ☁
     o /OpenEmu ☁

    $ icloud-logs
    <incredible set of realtime logs>

    $ mate
    <opens Sublime Text 3>

    $ vlc
    <opens given file in VLC>

### Generally Useful Utilities

    $ up
    PING 8.8.8.8 (8.8.8.8): 56 data bytes
    64 bytes from 8.8.8.8: icmp_seq=0 ttl=58 time=23.997 ms

    $ fresh
    [master 5778044] empty commit

    $ cake
    Copied! ✨ 🍰 ✨

    $ super-cake
    Copied! 💫 ✨ 🍰 ✨ 💫

    $ pyc
    <removes all .pyc files from current working directory and subdirs>

    $ svn
    <removes all .svn files from current working directory and subdirs>
