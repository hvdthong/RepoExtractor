# DailyProgrammerChallenges

This repo contains all of the challenges from [**r/dailyprogrammer**](http://reddit.com/r/dailyprogrammer) and also scripts used to pull challenges from the subreddit 3 times per week and to cleanup directories & remove unnecessary posts.

## Requirements

- Python 3
  - praw
  - pprint

## Installation

  ```bash
  $ pip3 install -r etc/requirements.txt
  ```

## How to use

The script can also be run via the command line by running `./post-challenges.py <number_of_challenges>`
It will look for a copy of `praw.ini`, an example is in `etc/praw.ini.example`

You may wish to run this in a temporary directory, to avoid adding folders directly to the top directory of the repo. Move the various levels of challenges into their respective end points.

### Example full run

  ```bash
  $ cd DailyProgrammerChallenges
  $ mkdir tmp
  $ cp etc/praw.ini.example tmp/praw.ini
  $ cd tmp
  # Edit praw.ini with the correct info
  $ ../post-challenges.py
  # Take a look at what was downloaded for any 'problems'
  $ mv *Easy* "Easy Challenges/."
  $ mv *Intermediate* "Intermediate Challenges/."
  $ mv *Hard* "Hard Challenges/."
  $ cd ..
  $ ./transform.py
  ```

  Examine the changes that `transform.py` performed and check that they seem okay.

## Challenges & Solutions

See a missing challenge & missing selftext? Want to add a solution to a challenge? See the [**CONTRIBUTING.md**](https://github.com/FreddieV4/DailyProgrammerChallenges/blob/master/CONTRIBUTING.md) file for how to submit changes.

-------------------------------------
**Creator:** [**Freddie Vargus**](http://github.com/FreddieV4)

Uses the [**MIT License**](https://github.com/FreddieV4/DailyProgrammerChallenges/blob/master/LICENSE)

This project was inspired by [**LewisJohnson**](https://github.com/LewisJohnson/dailyprogrammer), whom I collaborated with on a similar repository.
