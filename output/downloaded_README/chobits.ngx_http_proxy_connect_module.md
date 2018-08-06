name
====

This module provides support for the "CONNECT" HTTP method.  
This method is mainly used to [tunnel SSL requests](https://en.wikipedia.org/wiki/HTTP_tunnel#HTTP_CONNECT_tunneling) through proxy servers.

Table of Contents
=================

   * [name](#name)
   * [Example](#example)
   * [Install](#install)
   * [Directive](#directive)
      * [proxy_connect](#proxy_connect)
      * [proxy_connect_allow](#proxy_connect_allow)
      * [proxy_connect_connect_timeout](#proxy_connect_connect_timeout)
      * [proxy_connect_read_timeout](#proxy_connect_read_timeout)
      * [proxy_connect_write_timeout](#proxy_connect_write_timeout)
      * [proxy_connect_address](#proxy_connect_address)
      * [proxy_connect_bind](#proxy_connect_bind)
   * [Variables](#variables)
      * [$connect_host](#connect_host)
      * [$connect_port](#connect_port)
      * [$connect_addr](#connect_addr)
   * [Nginx Compatibility](#nginx-compatibility)
   * [Tengine Compatibility](#tengine-compatibility)
   * [Author](#author)
   * [License](#license)

Example
=======

```
 server {
     listen                         3128;

     # dns resolver used by forward proxying
     resolver                       8.8.8.8;

     # forward proxy for CONNECT request
     proxy_connect;
     proxy_connect_allow            443 563;
     proxy_connect_connect_timeout  10s;
     proxy_connect_read_timeout     10s;
     proxy_connect_send_timeout     10s;

     # forward proxy for non-CONNECT request
     location / {
         proxy_pass http://$host;
         proxy_set_header Host $host;
     }
 }
```

With above configuration, you can get any https website via HTTP CONNECT tunnel.
A simple test with command `curl` is as following:

```
$ curl https://github.com/ -v -x 127.0.0.1:3128
*   Trying 127.0.0.1...                                           -.
* Connected to 127.0.0.1 (127.0.0.1) port 3128 (#0)                | curl creates TCP connection with nginx (with proxy_connect module).
* Establish HTTP proxy tunnel to github.com:443                   -'
> CONNECT github.com:443 HTTP/1.1                                 -.
> Host: github.com:443                                         (1) | curl sends CONNECT request to create tunnel.
> User-Agent: curl/7.43.0                                          |
> Proxy-Connection: Keep-Alive                                    -'
>
< HTTP/1.0 200 Connection Established                             .- nginx replies 200 that tunnel is established.
< Proxy-agent: nginx                                           (2)|  (The client is now being proxied to the remote host. Any data sent
<                                                                 '-  to nginx is now forwarded, unmodified, to the remote host)

* Proxy replied OK to CONNECT request
* TLS 1.2 connection using TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256  -.
* Server certificate: github.com                                   |
* Server certificate: DigiCert SHA2 Extended Validation Server CA  | curl sends "https://github.com" request via tunnel,
* Server certificate: DigiCert High Assurance EV Root CA           | proxy_connect module will proxy data to remote host (github.com).
> GET / HTTP/1.1                                                   |
> Host: github.com                                             (3) |
> User-Agent: curl/7.43.0                                          |
> Accept: */*                                                     -'
>
< HTTP/1.1 200 OK                                                 .-
< Date: Fri, 11 Aug 2017 04:13:57 GMT                             |
< Content-Type: text/html; charset=utf-8                          |  Any data received from remote host will be sent to client
< Transfer-Encoding: chunked                                      |  by proxy_connect module.
< Server: GitHub.com                                           (4)|
< Status: 200 OK                                                  |
< Cache-Control: no-cache                                         |
< Vary: X-PJAX                                                    |
...                                                               |
... <other response headers & response body> ...                  |
...                                                               '-
```

The sequence diagram of above example is as following:

```
  curl                     nginx (proxy_connect)            github.com
    |                             |                          |
(1) |-- CONNECT github.com:443 -->|                          |
    |                             |                          |
(2) |<- HTTP/1.1 200           ---|                          |
    |   Connection Established    |                          |
    |                             |                          |
    ~~  CONNECT tunnel has       ~~                          |
    ~~  been establesied.        ~~                          |
    |                             |                          |
    |                             |                          |
    |   [ SSL stream       ]      |                          |
(3) |---[ GET / HTTP/1.1   ]----->|   [ SSL stream       ]   |
    |   [ Host: github.com ]      |---[ GET / HTTP/1.1   ]-->.
    |                             |   [ Host: github.com ]   |
    |                             |                          |
    |                             |                          |
    |                             |                          |
    |                             |   [ SSL stream       ]   |
    |   [ SSL stream       ]      |<--[ HTTP/1.1 200 OK  ]---'
(4) |<--[ HTTP/1.1 200 OK  ]------|   [ < html page >    ]   |
    |   [ < html page >    ]      |                          |
    |                             |                          |
```

Also you can configure your browser to use this nginx as PROXY server (e.g. Google Chrome HTTP PROXY SETTING).

Here is another [guide & config](https://github.com/chobits/ngx_http_proxy_connect_module/issues/22#issuecomment-346941271) for how to configure this module working under SSL layer (for supporing Google Chrome HTTPS PROXY SETTING).

Install
=======

* Select right patch for building:

| nginx version | enable REWRITE phase | patch |
| --: | --: | --: |
| 1.4.x ~ 1.12.x  | NO  | [proxy_connect.patch](patch/proxy_connect.patch) |
| 1.4.x ~ 1.12.x  | YES | [proxy_connect_rewrite.patch](patch/proxy_connect_rewrite.patch) |
| 1.13.x ~ 1.14.x | NO  | [proxy_connect_1014.patch](patch/proxy_connect_1014.patch) |
| 1.13.x ~ 1.14.x | YES | [proxy_connect_rewrite_1014.patch](patch/proxy_connect_rewrite_1014.patch) |

This module disables nginx REWRITE phase for CONNECT request by default, which means `if`, `set`, `rewrite_by_lua` and other REWRITE phase directives cannot be used. To enable these, you should use `proxy_connect_rewrite.patch` instead of `proxy_connect.patch`. (`TODO`: merge two patches into one.)

* Install this module from Nginx source:

```
$ wget http://nginx.org/download/nginx-1.9.2.tar.gz
$ tar -xzvf nginx-1.9.2.tar.gz
$ cd nginx-1.9.2/
$ patch -p1 < /path/to/ngx_http_proxy_connect_module/patch/proxy_connect.patch
$ ./configure --add-module=/path/to/ngx_http_proxy_connect_module
$ make && make install
```

* Install this module from OpenResty source:

```
$ wget https://openresty.org/download/openresty-1.13.6.2.tar.gz
$ tar -zxvf openresty-1.13.6.2.tar.gz
$ cd openresty-1.13.6.2
$ ./configure --add-module=/path/to/ngx_http_proxy_connect_module
$ patch -d build/nginx-1.13.6/ -p 1 < /path/to/ngx_http_proxy_connect_module/patch/proxy_connect.patch
$ make && make install
```

Directive
=========

proxy_connect
-------------

Syntax: **proxy_connect**  
Default: `none`  
Context: `server`  

Enable "CONNECT" HTTP method support.

proxy_connect_allow
-------------------

Syntax: **proxy_connect_allow `all | [port ...] | [port-range ...]`**  
Default: `443 563`  
Context: `server`  

This directive specifies a list of port numbers or ranges to which the proxy CONNECT method may connect.  
By default, only the default https port (443) and the default snews port (563) are enabled.  
Using this directive will override this default and allow connections to the listed ports only.

The value `all` will allow all ports to proxy.

The value `port` will allow specified port to proxy.

The value `port-range` will allow specified range of port to proxy, for example:

```
proxy_connect_allow 1000-2000 3000-4000; # allow range of port from 1000 to 2000, from 3000 to 4000.
```

proxy_connect_connect_timeout
-----------------------------

Syntax: **proxy_connect_connect_timeout `time`**  
Default: `none`  
Context: `server`  

Defines a timeout for establishing a connection with a proxied server.


proxy_connect_read_timeout
--------------------------

Syntax: **proxy_connect_read_timeout `time`**  
Default: `60s`  
Context: `server`  

Defines a timeout for reading a response from the proxied server.  
The timeout is set only between two successive read operations, not for the transmission of the whole response.  
If the proxied server does not transmit anything within this time, the connection is closed.

proxy_connect_write_timeout
---------------------------

Syntax: **proxy_connect_write_timeout `time`**  
Default: `60s`  
Context: `server`  

Sets a timeout for transmitting a request to the proxied server.  
The timeout is set only between two successive write operations, not for the transmission of the whole request.  
If the proxied server does not receive anything within this time, the connection is closed.

proxy_connect_address
---------------------

Syntax: **proxy_connect_address `address [transparent] | off`**  
Default: `none`  
Context: `server`  

Specifiy an IP address of the proxied server. The address can contain variables.  
The special value off is equal to none, which uses the IP address resolved from host name of CONNECT request line.  

NOTE: If using `set $<nginx variable>` and `proxy_connect_address $<nginx variable>` together, you should use `proxy_connect_rewrite.patch` instead, see [Install](#install) for more details.

proxy_connect_bind
------------------

Syntax: **proxy_connect_bind `address | off`**  
Default: `none`  
Context: `server`  

Makes outgoing connections to a proxied server originate from the specified local IP address with an optional port.  
Parameter value can contain variables. The special value off is equal to none, which allows the system to auto-assign the local IP address and port.

The transparent parameter allows outgoing connections to a proxied server originate from a non-local IP address, for example, from a real IP address of a client:

```
proxy_connect_bind $remote_addr transparent;

```

NOTE: If using `set $<nginx variable>` and `proxy_connect_bind $<nginx variable>` together, you should use `proxy_connect_rewrite.patch` instead, see [Install](#install) for more details.

Variables
=========

$connect_host
-------------

host name from CONNECT request line.

$connect_port
-------------

port from CONNECT request line.

$connect_addr
-------------

IP address and port of the remote host, e.g. "192.168.1.5:12345".
IP address is resolved from host name of CONNECT request line.

Nginx Compatibility
===================

The latest module is compatible with the following versions of nginx:

* 1.14.0 (stable version of 1.14.x)
* 1.12.1 (stable version of 1.12.x)
* 1.10.3 (stable version of 1.10.x)
* 1.8.1 (stable version of 1.8.x)
* 1.6.3 (stable version of 1.6.x)
* 1.4.7 (stable version of 1.4.x)

OpenResty Compatibility
=======================

The latest module is compatible with the following versions of OpenResty:

* 1.13.6.2 (nginx version: 1.13.6)

Tengine Compatibility
=====================

This module will be merged into tengine soon, see [this pull request](https://github.com/alibaba/tengine/pull/335/).

Author
======
* [Peng Qi](https://github.com/jinglong): original author. He contributed this module to [Tengine](https://github.com/tengine) in this [pull request](https://github.com/alibaba/tengine/pull/335/).  
* [Xiaochen Wang](https://github.com/chobits): current maintainer. Rebuild this module for nginx.

LICENSE
=======

See [LICENSE](https://github.com/chobits/ngx_http_proxy_connect_module/blob/master/LICENSE) for details.
