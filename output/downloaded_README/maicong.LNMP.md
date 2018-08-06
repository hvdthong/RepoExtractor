CentOS 7 Install LNMP Environment
=======

[中文版使用说明](README.zh-CN.md)

### The version list is available to install

Using YUM packages:

```
Nginx 1.12/1.13
MySQL 5.5/5.6/5.7/8.0
MariaDB 5.5/10.0/10.1/10.2/10.3
PHP 5.4/5.5/5.6/7.0/7.1/7.2
phpMyAdmin
Adminer
```

Using source code compile

```
OpenSSL 1.1.0f
Nginx 1.13.7
PHP 7.2.0
```

### Installing

Using YUM packages:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/maicong/LNMP/master/lnmp.sh)"
```

Using source code compile:

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/maicong/LNMP/master/source.sh)"
```

### Using

**Service management**

```bash
# MySQL
systemctl {start,stop,status,restart} mysqld.service

# MariaDB
systemctl {start,stop,status,restart} mariadb.service

# PHP
systemctl {start,stop,status,restart} php-fpm.service

# Nginx
systemctl {start,stop,status,restart,reload} nginx.service
```

**Site management**

```bash
# list
service vhost list

# start(restart), stop
service vhost {start,stop} [<domain>]

# add, edit
service vhost {add, edit} [<domain>] [<server_name>] [<index_name>] [<rewrite_file>] [<host_subdirectory>]

# delete
service vhost del [<domain>]
```

Parameter declaration

- `start` start|restart
- `stop` stop
- `add` add
- `edit` edit
- `del` delete
- `<domain>` site sign, default: `domain`
- `<server_name>` domain list, use `,` partition, default: `domain.com,www.domain.com`
- `<index_name>` the file of home page, take effect in proper order, default: `index.html,index.htm,index.php`
- `<rewrite_file>` rewrite rule file, save in `/etc/nginx/rewrite/`, default: `nomal.conf`
- `<host_subdirectory>` whether support subdirectory bind, `on` or `off`, default: `off`

Example

```bash
# start or restart all site
service vhost start

# stop all site
service vhost stop

# list all site
service vhost list

# add a sign of `mysite`, domain list is `mysite.com`
service vhost add mysite mysite.com

# start or restart the site which is sign `mysite`
service vhost start mysite

# stop the site which is sign `mysite`
service vhost stop mysite

# edit the site which is sign `mysite`
service vhost edit mysite

# delete the site which is sign `mysite`
service vhost del mysite
```

**Backup**

```bash
# create a new backup
service vbackup start

# delete a new backup
service vbackup del [<file>.tar.gz]

# list all backup
service vbackup list
```

### Agreement

The MIT License (MIT)
