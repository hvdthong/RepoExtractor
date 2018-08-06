# CXCORE-RaspberryPi3-ubuntu-18.04-aarch64    

![example1](https://assets.ubuntu.com/v1/c037fd75-ubuntu-logo.png)

****************

# [帮助文档 Help documentation （需要帮助戳这里If you need help）](https://github.com/chainsx/ubuntu64-rpi/wiki)
#### 这里提供一些问题的解决方案
##### Here are some solutions of some problems.

***************
## 使用说明
### Instructions

* 本系统是直接基于ubuntu-Base-18.04-arm64构建的根目录，所以稳定性有提升。
##### This system based on ubuntu-Base-18.04.
* `apt`的源默认为清华软件源
##### Default software sources : Tsinghua university tuna software source.
* 默认用户：`ubuntu`      密码：`ubuntu`
##### Default user: `ubuntu`.   Default password: `ubuntu`.
* 默认开启ssh，不想要的自己去关。
##### Open SSH by default, if you do not want, you can disable it.
* **第一次开机时会自动拓展根目录，然后会自动重启，重启后会配置系统，请耐心等待**。
##### This system will auto-expand rootfs at first boot, please be patient.
* 集成了`raspi-config`,`chainsx-tools`系统集成管理工具，使用方法：
##### There are two configure tools, you can use the following commands.
```
sudo raspi-config

sudo chainsx-tools
```

## 自行构建
### You can built by yourself.

### [Build documentation](https://github.com/chainsx/ubuntu64-rpi/wiki/Build-by-yourself)

## 关于内核
### About kernel.

- [X] wifi
- [X] bluetooth(蓝牙使用前需要配置。Bluetooth shuld configure before using)
- [X] GPIO


|  联系方式   |           |
|-----------|------------|
|QQ|1396219808(CX_dandelion)|
|E-mail|chainsx@outlook.com i@chainsx.cn|

**********************

## 预构建版本下载地址：
### Download Link.

| 版本Version | 下载链接Download link |
|--------|--------|
| ubuntu-18.04-developer-edition(ubuntu-18.04系统下载)  | [链接](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-18.04-arm64/Documentation/bionic-release.md)|
| cxcore系统核心(kernel,firmware,bootloader.....) | [链接](https://github.com/chainsx/ubuntu64-rpi/blob/ubuntu-18.04-arm64/Documentation/cxcore-sdk.md) |

## 特别鸣谢
##### [UMRnInside](https://github.com/UMRnInside)（提供了开机自动扩容方法)
##### [树莓派基金会](https://www.raspberrypi.org) (提供了开机自动扩容脚本)
##### [Armbian](https://armbian.com) (提供了chainsx-tools源码)
##### @ 束发少年 (提供论坛支持)
 
## 欢迎加入树莓派64位系统交流群，QQ群号码：697381661
## 论坛支持https://raspberrypi.party
### 感谢 @束发少年 的论坛支持

***************
######## 插播一段广告。。。。。
###### [ubuntu-16.04-arm64](https://github.com/chainsx/ubuntu64-rpi/tree/ubuntu-16.04.3-arm64)
##### [最新版mainline(4.16)内核（适用于所有树莓派3系统）](https://github.com/chainsx/firmware64-rpi)
###### [64位centos戳这里(做服务器建议使用此版本)](https://github.com/chainsx/centos64-rpi)
###### [64位debian(非pi64)](https://github.com/UMRnInside/RPi-arm64)
***************

