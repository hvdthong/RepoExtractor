[//]: # (This file is generated by the documentation build process.)
[//]: # (DO NOT modify it directly!)
[//]: # (See gulp configuration and the `docs` folder for more.)

# Timestrap

[![Travis](https://img.shields.io/travis/overshard/timestrap.svg?style=flat-square)](https://travis-ci.org/overshard/timestrap) [![Coveralls](https://img.shields.io/coveralls/overshard/timestrap.svg?style=flat-square)](https://coveralls.io/github/overshard/timestrap) [![license](https://img.shields.io/github/license/overshard/timestrap.svg?style=flat-square)](https://github.com/overshard/timestrap/blob/master/LICENSE.md) [![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg?style=flat-square)](https://gitter.im/overshard/timestrap)

Time tracking you can host anywhere. Full export support in
multiple formats and easily extensible.

![Timestrap](screenshot.png)

### :warning: Warning

This app is currently very unstable. Everything may, and probably will, change.

## Demo

There is a [demo instance of Timestrap](https://timestrap.herokuapp.com/) on
Heroku that resets every 10 minutes. The default credentials are:

- Username: `admin`
- Password: `admin`

## Quickstart

Want to get up and running quickly? :rocket:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/overshard/timestrap)

For manual deployments to Heroku without using the deploy button, make sure to
create two settings before pushing using `heroku config:set`:

    heroku config:set DJANGO_SETTINGS_MODULE=timestrap.settings.heroku
    heroku config:set SECRET_KEY=ChangeMeToSomethingRandom

After a successful push, log in with the default credentials (below)
and **change the admin password**

:lock: Heroku deployments use a default username and password with superuser 
access, please change it via the admin panel after initial login:

- Username: `admin`
- Password: `admin`

## Docker Installation

Follow the steps below to install Timestrap locally or on any server. This
process installs the minimal requirements to *run* Timestrap. For development
requirements and procedures, see [Development Installation](#development-installation).

1. Install the requirements:
    - Docker
    - Docker Compose

1. Set any custom configuration options you need and run

        docker-compose up -d

1. Bootstrap the database and creates the initial site and user
(username: admin, password: admin)

        docker-compose exec web python3 manage.py migrate --settings=timestrap.settings.docker

The Timestrap application should now be running at [http://localhost/](http://localhost/).
If it is not, feel free to [create an issue](https://github.com/overshard/timestrap/issues)
to seek assistance or report a bug! :bug:

## Development Installation

**:exclamation: Important Note:** Node is not required for Timestrap to function. Node is
used for building Timestrap's static files and improving the development
workflow. This installation procedure is only necessary for making changes to
static files.

1. Install the requirements:
    - Python 3.4+
    - Node 8+

1. Initiate a virtual environment with the development requirements.

        pip install pipenv && pipenv install --dev

1. Install Node dependencies.

        npm install -g gulp-cli && npm install

1. Bootstrap the database and creates the initial site and user
(username: admin, password: admin)

        gulp manage:migrate

1. Run the server!

        gulp

The Timestrap application should now be running at [http://localhost:8000](http://localhost:8000).
Gulp will automatically recognize and recompile changes to any static
files, allowing quick modification and review without starting and stopping
the application.

[Pull requests](https://github.com/overshard/timestrap/pulls) are :+1: welcome
and :clap: encouraged!

## Further Reading

For additional documentation on [configuration](https://docs.gettimestrap.com/en/latest/#configuration), 
[installation](https://docs.gettimestrap.com/en/latest/#installation), 
[testing](https://docs.gettimestrap.com/en/latest/development/testing.html) and
more, please see [https://docs.getTimestrap.com](https://docs.gettimestrap.com).