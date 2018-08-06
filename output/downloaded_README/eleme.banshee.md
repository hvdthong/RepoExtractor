Banshee
=======

Banshee is a real-time anomalies(outliers) detection system for periodic
metrics.

[![Build Status](https://travis-ci.org/eleme/banshee.svg?branch=master)](https://travis-ci.org/eleme/banshee)
[![GoDoc](https://godoc.org/github.com/eleme/banshee?status.svg)](https://godoc.org/github.com/eleme/banshee)
[![Join the chat at https://gitter.im/eleme/banshee](https://badges.gitter.im/eleme/banshee.svg)](https://gitter.im/eleme/banshee?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

![snap-01](docs/snap/01.png)

Case
----

For example, a website api's response time is reported to banshee from statsd
every 10 seconds:

```
20, 21, 21, 22, 23, 19, 18, 21, 22, 20, ..., 300
```

The latest `300` will be catched.

Features
--------

* Designed for periodic metrics.
* Dynamic threshold analyzation via 3-sigma.
* Also supports fixed-threshold alert option.
* Provides an alert rule management panel.
* No extra storage services required.

Requirements
------------

1. Go >= 1.5.
2. Node and gulp.
3. [Statsd](https://github.com/etsy/statsd).

It is strongly recommended to use statsd as banshee client.

Build
-----

1. Clone this repo and checkout to the latest release.
2. Build binary via `make`.
3. Build static files via `make static`.

Usage
-----

```bash
$ ./banshee -c <config-filename>
```

Example configuration file is [config/exampleConfig.yaml](config/exampleConfig.yaml).

Statsd Integration
------------------

1. Install [statsd-banshee](https://www.npmjs.com/package/statsd-banshee) to forward
   metrics to banshee.

   ```bash
   $ cd path/to/statsd
   $ npm install statsd-banshee
   ```

2. Add `statsd-banshee` to statsd backends in config.js:

   ```js
	{
	, backends: ['statsd-banshee']
	, bansheeHost: 'localhost'
	, bansheePort: 2015
	}
   ```

Supported Metrics
-----------------

* timers: `timer.mean_90.*`, `timer.upper_90.*`, `timer.count_ps.*`.
* counters: `counter.*`.
* gauge: `gauge.*`.

Detection should work for any metric delimited by dots, but above types are better
supported and are also recommended to use as banshee input.

*Statsd-banshee would format banshee metric names before data sent out.*

Web Panel Manual
----------------

Welcome to checkout the web panel manuals: [English](docs/web-manual.md), [简体中文](docs/web-manual.zh.md).

Deployment
----------

Banshee is a single-host program, its detection is fast enough in our case,
we don't have a plan to expand it now.

We are using a Python script ([deploy.py](deploy.py) via [fabric](http://www.fabfile.org/))
to deploy it to remote host:

```
python deploy.py -u hit9 -H remote-host:22 --remote-path "/service/banshee"
```

Upgrade
-------

Just pull the latest [tag release](https://github.com/eleme/banshee/releases).
*Please don't use master branch directly, checkout to a tag instead.*

Generally we won't release not-backward-compatiable versions, if any, related notes
would be added to the [changelog](changelog).

Alert Command
-------------

Banshee requires a command, normally a script to send alert messages.

It should be called from command line like this:

```bash
$ ./alert-command <JSON-String>
```

The JSON string example can be found at [alerter/exampleCommand/echo.go](alerter/exampleCommand/echo.go).

Philosophy
----------

But how do you really analyze the anomalous metrics? Via 3-sigma:

```python
>>> import numpy as np
>>> x = np.array([40, 52, 63, 44, 54, 43, 67, 54, 49, 45, 48, 54, 57, 43, 58])
>>> mean = np.mean(x)
>>> std = np.std(x)
>>> (80 - mean) / (3 * std)
1.2608052883472445 # anomaly, too big
>>> (20 - mean) / (3 * std)
-1.3842407711224991 # anomaly, too small
```

For further implementation introduction, please checkout [docs/algorithms.md](docs/algorithms.md).

Network Protocol
----------------

If you are using [statsd](https://github.com/etsy/statsd) as banshee client, please
checkout [statsd-banshee](https://www.npmjs.com/package/statsd-banshee).

The network protocol is line based:

```
<NAME> <STAMP> <VALUE> '\n'
```

Where the `NAME` should be a string, `STAMP` should be a timestamp integer in seconds, and
the `VALUE` should be a float number.

Web HTTP API
------------

Please checkout [docs/web-api.md](docs/web-api.md).

Docker Image
------------

Please checkout [docker/README.md](docker).

Authors
-------

Thanks to our [contributors](https://github.com/eleme/banshee/graphs/contributors).

License
-------

MIT Copyright (c) 2015 - 2016 Eleme, Inc.
