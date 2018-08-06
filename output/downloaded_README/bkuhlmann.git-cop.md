# Git Cop

[![Gem Version](https://badge.fury.io/rb/git-cop.svg)](https://badge.fury.io/rb/git-cop)
[![Code Climate Maintainability](https://api.codeclimate.com/v1/badges/d312f4724004dc691afc/maintainability)](https://codeclimate.com/github/bkuhlmann/git-cop/maintainability)
[![Code Climate Test Coverage](https://api.codeclimate.com/v1/badges/d312f4724004dc691afc/test_coverage)](https://codeclimate.com/github/bkuhlmann/git-cop/test_coverage)
[![Circle CI Status](https://circleci.com/gh/bkuhlmann/git-cop.svg?style=svg)](https://circleci.com/gh/bkuhlmann/git-cop)

Enforces Git rebase workflow with consistent Git commits for a clean and easy to read/debug project
history.

<!-- Tocer[start]: Auto-generated, don't remove. -->

## Table of Contents

  - [Features](#features)
  - [Screencasts](#screencasts)
  - [Requirements](#requirements)
  - [Setup](#setup)
    - [Install](#install)
    - [Upgrade](#upgrade)
    - [Configuration](#configuration)
      - [Enablement](#enablement)
      - [Severity Levels](#severity-levels)
      - [Regular Expressions](#regular-expressions)
    - [Rake](#rake)
  - [Usage](#usage)
    - [Command Line Interface (CLI)](#command-line-interface-cli)
    - [Git Hooks](#git-hooks)
      - [Commit Message](#commit-message)
      - [Post Commit](#post-commit)
    - [Continuous Integration (CI)](#continuous-integration-ci)
      - [Circle CI](#circle-ci)
      - [Travis CI](#travis-ci)
  - [Cops](#cops)
    - [Commit Author Email](#commit-author-email)
    - [Commit Author Name Capitalization](#commit-author-name-capitalization)
    - [Commit Author Name Parts](#commit-author-name-parts)
    - [Commit Body Bullet](#commit-body-bullet)
    - [Commit Body Bullet Capitalization](#commit-body-bullet-capitalization)
    - [Commit Body Bullet Delimiter](#commit-body-bullet-delimiter)
    - [Commit Body Issue Tracker Link](#commit-body-issue-tracker-link)
    - [Commit Body Leading Line](#commit-body-leading-line)
    - [Commit Body Line Length](#commit-body-line-length)
    - [Commit Body Paragraph Capitalization](#commit-body-paragraph-capitalization)
    - [Commit Body Phrase](#commit-body-phrase)
    - [Commit Body Presence](#commit-body-presence)
    - [Commit Body Single Bullet](#commit-body-single-bullet)
    - [Commit Subject Length](#commit-subject-length)
    - [Commit Subject Prefix](#commit-subject-prefix)
    - [Commit Subject Suffix](#commit-subject-suffix)
  - [Style Guide](#style-guide)
    - [General](#general)
    - [Commits](#commits)
    - [Branches](#branches)
    - [Tags](#tags)
    - [Rebases](#rebases)
    - [Pull Requests](#pull-requests)
    - [GitHub](#github)
  - [Tests](#tests)
  - [Versioning](#versioning)
  - [Code of Conduct](#code-of-conduct)
  - [Contributions](#contributions)
  - [License](#license)
  - [History](#history)
  - [Credits](#credits)

<!-- Tocer[finish]: Auto-generated, don't remove. -->

## Features

- Enforces a [Git Rebase Workflow](http://www.bitsnbites.eu/a-tidy-linear-git-history).
- Enforces a clean and consistent Git commit history.
- Provides Continuous Integration (CI) build server support.
- Provides Git Hook support for local use.
- Provides a customizable suite of style cops.

## Screencasts

[![asciicast](https://asciinema.org/a/131420.png)](https://asciinema.org/a/131420)

## Requirements

0. [Ruby 2.5.x](https://www.ruby-lang.org) (or higher)

## Setup

### Install

Type the following to install:

    gem install git-cop

### Upgrade

If upgrading from 1.x.x to 2.x.x, please take note of the following changes:

- The `whitelist` configuration option has been removed and is no longer supported. Please update
  any custom configurations by replacing `:whitelist:` keys with `:includes:` keys. See the
  *Configuration* section, below, for further details.
- The `blacklist` configuration option has been removed and is no longer supported. Please update
  any custom configurations by replacing `:blacklist:` keys with `:excludes:` keys. See the
  *Configuration* section, below, for further details.

### Configuration

This gem can be configured via a global configuration:

    ~/.config/git-cop/configuration.yml

It can also be configured via [XDG environment variables](https://github.com/bkuhlmann/runcom#xdg)
as provided by the [Runcom](https://github.com/bkuhlmann/runcom) gem. Check out the [Runcom
Examples](https://github.com/bkuhlmann/runcom#examples) for project specific usage.

The default configuration is:

    :commit_author_email:
      :enabled: true
      :severity: :error
    :commit_author_name_capitalization:
      :enabled: true
      :severity: :error
    :commit_author_name_parts:
      :enabled: true
      :severity: :error
      :minimum: 2
    :commit_body_bullet:
      :enabled: true
      :severity: :error
      :excludes:
        - "\\*"
        - "•"
    :commit_body_bullet_capitalization:
      :enabled: true
      :severity: :error
      :includes: "\\-"
    :commit_body_bullet_delimiter:
      :enabled: true
      :severity: :error
      :includes: "\\-"
    :commit_body_issue_tracker_link:
      :enabled: true,
      :severity: :error
      :excludes:
        - "(f|F)ix(es|ed)?\\s\\#\\d+"
        - "(c|C)lose(s|d)?\\s\\#\\d+"
        - "(r|R)esolve(s|d)?\\s\\#\\d+"
        - "github\\.com\\/.+\\/issues\\/\\d+"
    :commit_body_leading_line:
      :enabled: false
      :severity: :warn
    :commit_body_line_length:
      :enabled: true
      :severity: :error
      :length: 72
    :commit_body_paragraph_capitalization:
      :enabled: true
      :severity: :error
    :commit_body_phrase:
      :enabled: true
      :severity: :error
      :excludes:
        - "absolutely",
        - "actually",
        - "all intents and purposes",
        - "along the lines",
        - "at this moment in time",
        - "basically",
        - "each and every one",
        - "everyone knows",
        - "fact of the matter",
        - "furthermore",
        - "however",
        - "in due course",
        - "in the end",
        - "last but not least",
        - "matter of fact",
        - "obviously",
        - "of course",
        - "really",
        - "simply",
        - "things being equal",
        - "would like to",
        - "/\\beasy\\b/",
        - "/\\bjust\\b/",
        - "/\\bquite\\b/",
        - "/as\\sfar\\sas\\s.+\\sconcerned/",
        - "/of\\sthe\\s(fact|opinion)\\sthat/"
    :commit_body_presence:
      :enabled: false
      :severity: :warn
      :minimum: 1
    :commit_body_single_bullet:
      :enabled: true
      :severity: :error
      :includes: "\\-"
    :commit_subject_length:
      :enabled: true
      :severity: :error
      :length: 72
    :commit_subject_prefix:
      :enabled: true
      :severity: :error
      :includes:
        - Fixed
        - Added
        - Updated
        - Removed
        - Refactored
    :commit_subject_suffix:
      :enabled: true
      :severity: :error
      :includes:
        - "\\."

Feel free to take this default configuration, modify, and save as your own custom
`configuration.yml`.

#### Enablement

By default, most cops are enabled. Accepted values are `true` or `false`. If you wish to disable a
cop, set it to `false`.

#### Severity Levels

By default, most cops are set to `error` severity. If you wish to reduce the severity level of a
cop, you can set it to `warn` instead. Here are the accepted values and what each means:

- `warn`: Will count as an issue and display a warning but will not cause the program/build to
  fail. Use this if you want to display issues as reminders or cautionary warnings.
- `error`: Will count as an issue, display error output, and cause the program/build to fail. Use
  this setting if you want to ensure bad commits are prevented.

#### Regular Expressions

Some cops support *include* or *exclude* lists. These lists can consist of strings, regular
expressions, or a combination thereof. Regardless of your choice, all lists are automatically
converted to regular expression for use by the cops. This means a string like `"example"` becomes
`/example/` and a regular expression of `"\\AExample.+"` becomes `/\AExample.+/`.

If you need help constructing complex regular expressions for these lists, try launching an IRB
session and using `Regexp.new` or `Regexp.escape` to experiment with the types of words/phrases you
want to turn into regular expressions. *For purposes of the YAML configuration, these need to be
expressed as strings with special characters escaped properly for internal conversion to a regular
expression.*

### Rake

This gem provides optional Rake tasks. They can be added to your project by adding the following
requirement to the top of your `Rakefile`:

    require "git/cop/rake/setup"

Now, when running `bundle exec rake -T`, you'll see `git_cop` included in the list.

If you need a concrete example, check out the [Rakefile](Rakefile) of this project for details.

## Usage

### Command Line Interface (CLI)

From the command line, type: `git-cop --help`

    git-cop --hook                # Add Git Hook support.
    git-cop -c, [--config]        # Manage gem configuration.
    git-cop -h, [--help=COMMAND]  # Show this message or get help for a command.
    git-cop -p, [--police]        # Check feature branch for issues.
    git-cop -v, [--version]       # Show gem version.

To check if your Git commit history is clean, run: `git-cop --police`. It will exit with a failure
if at least one issue, with error severity, is detected.

This gem does not check commits on `master`. This is intentional as you would, generally, not want
to rewrite or fix commits on `master`. This gem is best used on feature branches as it automatically
detects all commits made since `master` on the feature branch.

Here is an example workflow, using gem defaults with issues detected:

    cd example
    git checkout -b test
    touch text.txt
    git add --all .
    git commit --message "This is a bogus commit message that is also terribly long and will word wrap"
    git-cop --police

    # Output:
    Running Git Cop...

    83dbad531d84a184e55cbb38c5b2a4e5fa5bcaee (Brooke Kuhlmann, 0 seconds ago): This is a bogus commit message that is also terribly long and will word wrap
      Commit Body Presence Warning. Use minimum of 1 line (non-empty).
      Commit Subject Length Error. Use 72 characters or less.
      Commit Subject Prefix Error. Use: /Fixed/, /Added/, /Updated/, /Removed/, /Refactored/.
      Commit Subject Suffix Error. Use: /\./.

    1 commit inspected. 4 issues detected (1 warning, 3 errors).

### Git Hooks

This gem supports
[Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

It is *highly recommended* you manage Git Hooks as global scripts as it'll reduce project
maintenance costs for you. To configure global Git Hooks, add the following to your `~/.gitconfig`:

    [core]
      hooksPath = ~/.git_template/hooks

Then you can customize Git Hooks for all of your projects.
[Check out these examples](https://github.com/bkuhlmann/dotfiles/tree/master/home_files/.config/git/hooks).

If using a global configuration is not desired, you can add Git Hooks at a per project level by
editing any of the scripts within the `.git/hooks` directory of the repository.

#### Commit Message

The *commit-msg* hook, which is the best way to use this gem as a Git Hook, is provided as a
`--hook` option. Run `git-cop --help --hook` for usage:

    Usage:
      git-cop --hook

    Options:
      [--commit-message=PATH]  # Check commit message.

    Add Git Hook support.

As shown above, the `--commit-message` option accepts a file path (i.e. `.git/COMMIT_EDITMSG`) which
is provided to you by Git within the `.git/hooks/commit-msg` script. Here is a working example of
what that script might look like:

    #! /usr/bin/env bash

    set -o nounset
    set -o errexit
    set -o pipefail
    IFS=$'\n\t'

    if ! command -v git-cop > /dev/null; then
       printf "%s\n" "[git]: Git Cop not found. To install, run: gem install git-cop."
       exit 1
    fi

    git-cop --hook --commit-message "${BASH_ARGV[0]}"

Whenever you attempt to add a commit, Git Cop will check your commit for issues prior to saving it.

#### Post Commit

The *post-commit* hook is possible via the `--police --commits` option. Usage:

    Usage:
      git-cop -p, [--police]

    Options:
      -c, [--commits=one two three]  # Check specific commit SHA(s).

    Check feature branch for issues.

The *post-commit* hook can be used multiple ways but, if you want it to check each commit after it
has been made, here is a working example which can be used as a `.git/hooks/post-commit` script:

    #! /usr/bin/env bash

    set -o nounset
    set -o errexit
    set -o pipefail
    IFS=$'\n\t'

    if ! command -v git-cop > /dev/null; then
       printf "%s\n" "[git]: Git Cop not found. To install, run: gem install git-cop."
       exit 1
    fi

    git-cop --police --commits $(git log --pretty=format:%H -1)

Whenever a commit has been saved, this script will run Git Cop to check for issues.

### Continuous Integration (CI)

This gem automatically configures itself for known CI build servers.

Calculation of commits is done by reviewing all commits made on the feature branch since branching
from `master`. Below are the build servers which are supported and *tested*. If you have a build
server that is not listed, please open a pull request with support.

#### Circle CI

This gem automatically detects and configures itself for [Circle CI](https://circleci.com) builds by
checking the `CIRCLECI` environment variable. No additional setup required!

#### Travis CI

This gem automatically detects and configures itself for [Travis CI](https://travis-ci.org) builds
by checking the `TRAVIS` environment variable. No additional setup required!

## Cops

The following details the various cops provided by this gem to ensure a high standard of commits for
your project.

### Commit Author Email

| Enabled | Severity | Defaults |
|---------|----------|----------|
| true    | error    | none     |

Ensures author email address exists. Git requires an author email when you use it for the first time
too. This takes it a step further to ensure the email address loosely resembles an email address.

    # Disallowed
    mudder_man

    # Allowed
    jayne@serenity.com

### Commit Author Name Capitalization

| Enabled | Severity | Defaults |
|---------|----------|----------|
| true    | error    | none     |

Ensures auther name is properly capitalized. Example:

    # Disallowed
    jayne cobb
    dr. simon tam

    # Allowed
    Jayne Cobb
    Dr. Simon Tam

### Commit Author Name Parts

| Enabled | Severity |  Defaults  |
|---------|----------|------------|
| true    | error    | minimum: 2 |

Ensures author name consists of, at least, a first and last name. Example:

    # Disallowed
    Kaylee

    # Allowed
    Kaywinnet Lee Frye

### Commit Body Bullet

| Enabled | Severity |          Defaults        |
|---------|----------|--------------------------|
| true    | error    | excludes: `["\\*", "•"]` |

Ensures commit message bodies use a standard Markdown syntax for bullet points. Markdown supports
the following syntax for bullets:

    *
    -

It's best to use `-` for bullet point syntax as `*` are easier to read when used for *emphasis*.
This makes parsing the Markdown syntax easier when reviewing a Git commit as the syntax used for
bullet points and *emphasis* are now, distinctly, unique.

### Commit Body Bullet Capitalization

| Enabled | Severity |       Defaults      |
|---------|----------|---------------------|
| true    | error    | includes: `["\\-"]` |

Ensures commit body bullet lines are capitalized. Example:

    # Disallowed

    - an example bullet.

    # Allowed

    - An example bullet.

### Commit Body Bullet Delimiter

| Enabled | Severity |       Defaults      |
|---------|----------|---------------------|
| true    | error    | includes: `["\\-"]` |

Ensures commit body bullets are delmited by a space. Example:

    # Disallowed

    -An example bullet.

    # Allowed

    - An example bullet.

### Commit Body Issue Tracker Link

| Enabled | Severity |                       Defaults                      |
|---------|----------|-----------------------------------------------------|
| true    | error    | excludes: (see configuration list, mentioned above) |

Ensures commit body doesn't contain a link to an issue tracker. The exclude list defaults to GitHub
Issue links but can be customized for any issue tracker.

There are several reasons for exluding issue tracker links from commit bodies:

0. Not all issue trackers preserve issues (meaning they can be deleted). This makes make reading
   historic commits much harder to understand why the change was made when the link no longer works.
0. When not connected to the internet or working on a laggy connection, it's hard to understand why
   a commit was made when all you have is a link to an issue with no other supporting context.
0. During the course of a repository's life, issue trackers can be replaced (rare but it does
   happen). If the old issue tracker service is no longer paid for, none of the links within the
   commit will be of any relevance.
0. An issue might span several commits in order to resolve it. Including a link in each commit is
   tedious and can create noise within the issue's history which is distracting.

Instead of linking to issues, take the time to write a short summary as to *why* the commit was
made. Doing this will make it easier to understand *why* the commit was made, keeps the commit self-
contained, and makes learning about/debugging the commit faster.

Issue tracker links are best used at the pull request level due to an issue usually spanning
multiple commits in order to complete the work. When reading a pull request, this is a great
opportunity to link to an issue in order to provide a high level overview and reason why the pull
request exists.

### Commit Body Leading Line

| Enabled | Severity | Defaults |
|---------|----------|----------|
| true    | error    | none     |

Ensures there is a leading, empty line, between the commit subject and body. Generally, this isn't
an issue but sometimes the Git CLI can be misued or a misconfigured Git editor will smash the
subject line and start of the body as one run-on paragraph. Example:

    # Disallowed

    Curabitur eleifend wisi iaculis ipsum.
    Pellentque morbi-trist sentus et netus et malesuada fames ac turpis egestas. Vestibulum tortor
    quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu_libero sit amet quam
    egestas semper. Aenean ultricies mi vitae est. Mauris placerat's eleifend leo. Quisque et sapien
    ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, orn si amt wit.

    # Allowed

    Curabitur eleifend wisi iaculis ipsum.

    Pellentque morbi-trist sentus et netus et malesuada fames ac turpis egestas. Vestibulum tortor
    quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu_libero sit amet quam
    egestas semper. Aenean ultricies mi vitae est. Mauris placerat's eleifend leo. Quisque et sapien
    ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, orn si amt wit.

### Commit Body Line Length

| Enabled | Severity |  Defaults  |
|---------|----------|------------|
| true    | error    | length: 72 |

Ensures each line of the commit body is no longer than 72 characters in length for consistent
readabilty and word-wrap prevention on smaller screen sizes. For further details, read Tim Pope's
original [article](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) on the
subject.

### Commit Body Paragraph Capitalization

| Enabled | Severity | Defaults |
|---------|----------|----------|
| true    | error    | none     |

Ensures each paragraph of the commit body is capitalized. Example:

    # Disallowed

    curabitur eleifend wisi iaculis ipsum.

    # Allowed

    Curabitur eleifend wisi iaculis ipsum.

### Commit Body Phrase

| Enabled | Severity |                       Defaults                      |
|---------|----------|-----------------------------------------------------|
| true    | error    | excludes: (see configuration list, mentioned above) |

Ensures non-descriptive words/phrases are avoided in order to keep commit message bodies informative
and specific. The exclude list is case insensitive. Detection of excluded words/phrases is case
insensitve as well. Example:

    # Disallowed

    Obviously, the existing implementation was too simple for my tastes. Of course, this couldn't be
    allowed. Everyone knows the correct way to implement this code is to do just what I've added in
    this commit. Easy!

    # Allowed

    Necessary to fix due to a bug detected in production. The included implentation fixes the bug
    and provides the missing spec to ensure this doesn't happen again.

### Commit Body Presence

| Enabled | Severity |  Defaults  |
|---------|----------|------------|
| false   | warn     | minimum: 1 |

Ensures a minimum number of lines are present within the commit body. Lines with empty characters
(i.e. whitespace, carriage returns, etc.) are considered to be empty.

Automatically ignores *fixup!* commits as they are not meant to have bodies.

### Commit Body Single Bullet

| Enabled | Severity |      Defaults    |
|---------|----------|------------------|
| true    | error    | includes: `"\\-"` |

Ensures a single bullet is never used when a paragraph could be used instead. Example:

    # Disallowed

    - Pellentque morbi-trist sentus et netus et malesuada fames ac turpis egestas. Vestibulum tortor
      quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu_libero sit amet quam.

    # Allowed

    Pellentque morbi-trist sentus et netus et malesuada fames ac turpis egestas. Vestibulum tortor
    quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu_libero sit amet quam.

### Commit Subject Length

| Enabled | Severity |  Defaults  |
|---------|----------|------------|
| true    | error    | length: 72 |

Ensures the commit subject length is no more than 72 characters in length. This default is more
lenient than the [50/72 rule](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
as it gives one the ability to formulate a more descriptive subject line without being too wordy or
suffer being word wrapped.

Automatically ignores *fixup!* or *squash!* commit prefixes when calculating subject length.

### Commit Subject Prefix

| Enabled | Severity |        Defaults       |
|---------|----------|-----------------------|
| true    | error    | includes: (see below) |

Ensures the commit subject uses consistent prefixes that help explain *what* is being commited. The
include list *is* case sensitive. The default include list consists of the following prefixes:

- *Fixed* - Existing code that has been fixed.
- *Removed* - Code that was once added and is now removed.
- *Added* - New code that is an enhancement, feature, etc.
- *Updated* - Existing code that has been modified.
- *Refactored* - Existing code that has been cleaned up and does not change functionality.

In practice, using a prefix other than what has been detailed above to explain *what* is being
committed is never needed. This include list is not only short and easy to remember but also has the
added benefit of categorizing the commits for building release notes, change logs, etc. This becomes
handy when coupled with another tool, [Milestoner](https://github.com/bkuhlmann/milestoner), for
producing consistent project milestones and Git tag histories.

Automatically ignores *fixup!* or *squash!* commit prefixes when used as a Git Hook in order to not
disturb interactive rebase workflows.

### Commit Subject Suffix

| Enabled | Severity |       Defaults      |
|---------|----------|---------------------|
| true    | error    | includes: `["\\."]` |

Ensures commit subjects are suffixed consistently. The include list *is* case sensitive and only
allows for periods (`.`) to ensure each commit is sentance-like when generating release notes, Git
tags, change logs, etc. This is handy when coupled with a tool, like
[Milestoner](https://github.com/bkuhlmann/milestoner), which automates project milestone releases.

## Style Guide

In addition to what is described above and automated for you, the following style guide is also
worth considering:

### General

- Use a [Git rebase workflow](http://www.bitsnbites.eu/a-tidy-linear-git-history) instead of a Git
  merge workflow.
- Use `git commit --fixup` when fixing a previous commit, addressing pull request feedback, etc.,
  and don't need to modifiy the original commit message.
- Use `git commit --squash` when fixing a previous commit, addressing pull request feedback, etc.,
  and want to combine the original commit message with the squash commit message into a single
  message.
- Use `git rebase --interactive` when cleaning up commit history, order, messages, etc. Should be
  done prior to submitting a pull request or when pull request feedback has been addressed and you
  are ready to merge to `master`.
- Use `git push --force-with-lease` instead of `git push --force` when pushing changes after an
  interactive rebasing session.
- Avoid checking in development-specific configuration files (add to `.gitignore` instead).
- Avoid checking in sensitive information (i.e. security keys, passphrases, etc).
- Avoid "WIP" (a.k.a. "Work in Progress") commits and/or pull requests. Be confident with your code
  and collegues' time. Use branches, stashes, etc. instead -- share a link to a diff if you have
  questions/concerns during development.

### Commits

- Use small, atomic commits:
  - Easier to review and provide feedback.
  - Easier to review implementation and corresponding tests.
  - Easier to document with detailed subject messages (especially when grouped together in a pull
    request).
  - Easier to reword, edit, squash, fix, or drop when interactively rebasing.
  - Easier to merge together versus tearing apart a larger commit into smaller commits.
- Use commits in a logical order:
  - Each commit should tell a story and be a logical building block to the next commit.
  - Each commit, when reviewed in order, should be able to explain *how* the feature or bug fix was
    completed and implemented properly.
- Use a commit subject that explains *what* is being commited.
- Use a commit message body that explains *why* the commit is necessary. Additional considerations:
  - If the commit has a dependency to the previous commit or is a precursor to the commit that will
    follow, make sure to explain that.
  - Include links to dependent projects, stories, etc. if available.

### Branches

- Use feature branches for new work.
- Maintain branches by rebasing upon `master` on a regular basis.

### Tags

- Use tags to denote milestones/releases:
  - Makes it easier to record milestones and capture associated release notes.
  - Makes it easier to compare differences between versions.
  - Provides a starting point for debugging production issues (if any).

### Rebases

- Avoid rebasing a shared branch. If you must do this, clear communcation should be used to warn
  those ahead of time, ensure that all of their work is checked in, and that their local branch is
  deleted first.

### Pull Requests

- Avoid authoring and reviewing your own pull request.
- Keep pull requests short and easy to review:
  - Provide a high level overview that answers *why* the pull request is necessary.
  - Provide a link to the story/task that prompted the pull request.
  - Provide screenshots/screencasts if possible.
  - Ensure all commits within the pull request are related to the purpose of the pull request.
- Review and merge pull requests quickly:
  - Maintain a consistent but reasonable pace -- Review morning, noon, and night.
  - Avoid letting pull request linger more than a day. Otherwise, you risk hampering moral and
    dimishing the productivity of the team.
- Use emojis to help identify the types of comments added during the review process:
  - Generally, an emoji should prefix all feedback. Format: `<emoji> <feedback>`.
  - :tea: - Signifies you are reviewing the pull request. This is *non-blocking* and is meant to be
    informational. Useful when reading over a pull request with a large number of commits, reviewing
    complex code, requires additional testing by the reviewer, etc.
  - :information_source: - Signifies informational feedback that is *non-blocking*. Can also be used
    to let one know you are done reviewing but haven't approved yet (due to feedback that needs
    addressing), rebasing a pull request and then merging, waiting for a blocking pull request to be
    resolved, status updates to the pull request, etc.
  - :art: - Signifies an issue with code style and/or code quality. This can be *blocking* or *non-
    blocking* feedback but is feedback generally related to the style/quality of the code,
    implementation details, and/or alternate solutions worth considering.
  - :bulb: - Indicates a helpful tip or trick for improving the code. This can be *blocking* or
    *non-blocking* feedback and is left up to the author to decide (generally, it is a good idea to
    address and resolve the feedback).
  - :star: - Signifies code that is liked, favorited, remarkable, etc. This feedback is *non-
    blocking* and is always meant to be positive/uplifting.
  - :white_check_mark: - Signifies approval of a pull request. The author can merge to `master` and
    delete the feature branch at this point.
- If the pull request discussion gets noisy, stop typing and switch to face-to-face chat.
- If during a code review, additional features are discovered, create stories for them and return to
  reviewing the pull request.
- The author, not the reviewer, should merge the feature branch upon approval.
- Ensure the following criteria is met before merging your feature branch to master:
  - Ensure all `fixup!` and `squash!` commits are interactively rebased and merged. *Avoid letting
    these get onto the `master` branch!*
  - Ensure your feature branch is rebased upon `master`.
  - Ensure all tests and code quality checks are passing.
  - Ensure the feature branch is deleted after being successfully merged.

### GitHub

When using GitHub, make sure to enforce a rebase workflow for all of your GitHub projects (*highly
recommended*). You can do this via your project options (i.e.
`https://github.com/<username/organization>/<project>/settings`) and editing your merge options for
pull requests as follows:

![GitHub Merge Options](doc/github-settings-options.png)

Doing this will help maintain a clean Git history.

## Tests

To test, run:

    bundle exec rake

## Versioning

Read [Semantic Versioning](http://semver.org) for details. Briefly, it means:

- Major (X.y.z) - Incremented for any backwards incompatible public API changes.
- Minor (x.Y.z) - Incremented for new, backwards compatible, public API enhancements/fixes.
- Patch (x.y.Z) - Incremented for small, backwards compatible, bug fixes.

## Code of Conduct

Please note that this project is released with a [CODE OF CONDUCT](CODE_OF_CONDUCT.md). By
participating in this project you agree to abide by its terms.

## Contributions

Read [CONTRIBUTING](CONTRIBUTING.md) for details.

## License

Copyright 2017 [Alchemists](https://www.alchemists.io).
Read [LICENSE](LICENSE.md) for details.

## History

Read [CHANGES](CHANGES.md) for details.
Built with [Gemsmith](https://github.com/bkuhlmann/gemsmith).

## Credits

Developed by [Brooke Kuhlmann](https://www.alchemists.io) at
[Alchemists](https://www.alchemists.io).
