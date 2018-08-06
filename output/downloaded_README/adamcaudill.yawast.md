## YAWAST [![Build Status](https://travis-ci.org/adamcaudill/yawast.svg?branch=master)](https://travis-ci.org/adamcaudill/yawast) [![Code Climate](https://codeclimate.com/github/adamcaudill/yawast/badges/gpa.svg)](https://codeclimate.com/github/adamcaudill/yawast) [![Test Coverage](https://codeclimate.com/github/adamcaudill/yawast/badges/coverage.svg)](https://codeclimate.com/github/adamcaudill/yawast/coverage) [![Gem Version](https://badge.fury.io/rb/yawast.svg)](https://badge.fury.io/rb/yawast) [![Docker Build](https://img.shields.io/docker/automated/adamcaudill/yawast.svg)](https://hub.docker.com/r/adamcaudill/yawast/)

**The YAWAST Antecedent Web Application Security Toolkit**

YAWAST is an application meant to simplify initial analysis and information gathering for penetration testers and security auditors. It performs basic checks in these categories:

* TLS/SSL - Versions and cipher suites supported; common issues.
* Information Disclosure - Checks for common information leaks.
* Presence of Files or Directories - Checks for files or directories that could indicate a security issue.
* Common Vulnerabilities
* Missing Security Headers

This is meant to provide a easy way to perform initial analysis and information discovery. It's not a full testing suite, and it certainly isn't Metasploit. The idea is to provide a quick way to perform initial data collection, which can then be used to better target further tests. It is especially useful when used in conjunction with Burp Suite (via the `--proxy` parameter).

Please see [the wiki](https://github.com/adamcaudill/yawast/wiki) for full documentation.

### Installing

YAWAST is packaged as a Ruby Gem & Docker container to make installing it as easy as possible. Details are available [on the wiki](https://github.com/adamcaudill/yawast/wiki/Installation).

The simplest options to install are:

As a Gem: `gem install yawast`

Via Docker: `docker pull adamcaudill/yawast`

It's strongly recommended that you review the [installation](https://github.com/adamcaudill/yawast/wiki/Installation) documentation, to make sure you have the proper dependencies.

### Tests

The following tests are performed:

* *(Generic)* Info Disclosure: X-Powered-By header present
* *(Generic)* Info Disclosure: X-Pingback header present
* *(Generic)* Info Disclosure: X-Backend-Server header present
* *(Generic)* Info Disclosure: X-Runtime header present
* *(Generic)* Info Disclosure: Via header present
* *(Generic)* Info Disclosure: PROPFIND Enabled
* *(Generic)* TRACE Enabled
* *(Generic)* X-Frame-Options header not present
* *(Generic)* X-Content-Type-Options header not present
* *(Generic)* Content-Security-Policy header not present
* *(Generic)* Public-Key-Pins header not present
* *(Generic)* X-XSS-Protection disabled header present
* *(Generic)* SSL: HSTS not enabled
* *(Generic)* Source Control: Common source control directories present
* *(Generic)* Presence of crossdomain.xml or clientaccesspolicy.xml
* *(Generic)* Presence of sitemap.xml
* *(Generic)* Presence of WS_FTP.LOG
* *(Generic)* Presence of RELEASE-NOTES.txt
* *(Generic)* Presence of readme.html
* *(Generic)* Missing cookie flags (Secure, HttpOnly, and SameSite)
* *(Generic)* Search for files (14,169) & common directories (21,332)
* *(Apache)* Info Disclosure: Module listing enabled
* *(Apache)* Info Disclosure: Server version
* *(Apache)* Info Disclosure: OpenSSL module version
* *(Apache)* Presence of /server-status
* *(Apache)* Presence of /server-info
* *(Apache Tomcat)* Presence of Tomcat Manager
* *(Apache Tomcat)* Presence of Tomcat Host Manager
* *(Apache Tomcat)* Tomcat Manager Weak Password
* *(Apache Tomcat)* Tomcat Host Manager Weak Password
* *(Apache Tomcat)* Tomcat version detection via invalid HTTP verb
* *(Apache Tomcat)* Tomcat PUT RCE (CVE-2017-12617)
* *(Apache Struts)* Sample files which may be vulnerable
* *(IIS)* Info Disclosure: Server version
* *(ASP.NET)* Info Disclosure: ASP.NET version
* *(ASP.NET)* Info Disclosure: ASP.NET MVC version
* *(ASP.NET)* Presence of Trace.axd
* *(ASP.NET)* Presence of Elmah.axd
* *(ASP.NET)* Debugging Enabled
* *(nginx)* Info Disclosure: Server version
* *(PHP)* Info Disclosure: PHP version

CMS Detection:

* Generic (Generator meta tag) *[Real detection coming as soon as I get around to it...]*

SSL Information:

* Certificate details
* Certificate chain
* Supported ciphers
* Maximum requests using 3DES in a single connection
* DNS CAA records

Checks for the following SSL issues are performed:

* Expired Certificate
* Self-Signed Certificate
* MD5 Signature
* SHA1 Signature
* RC4 Cipher Suites
* Weak (< 128 bit) Cipher Suites
* SWEET32

Certain DNS information is collected:

* IP Addresses
* IP Owner/Network (via [api.iptoasn.com](https://api.iptoasn.com/))
* TXT Records
* MX Records
* NS Records
* CAA Records (with CNAME chasing)
* Common Subdomains (2,354 subdomains) - optional, via `--subdomains`
* SRV Records - optional, via `--srv`

In addition to these tests, certain basic information is also displayed, such as IPs (and the PTR record for each IP), HTTP HEAD request, and others.

### Usage

The most common usage scenario is as simple as:

`yawast scan <url>`

Detailed [usage information](https://github.com/adamcaudill/yawast/wiki/Usage-&-Parameters) is available on the wiki.

### Sample

Sample output for a [scan](https://github.com/adamcaudill/yawast/wiki/Sample-Output) and [TLS-specific](https://github.com/adamcaudill/yawast/wiki/Scanning-TLS-(SSL)) checks are on the wiki.

### Special Thanks

* [SecLists](https://github.com/danielmiessler/SecLists) - Various lists are based on the resources collected by this project.
