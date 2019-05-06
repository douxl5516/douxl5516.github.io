---
title: Windows远程桌面连接阿里云Ubuntu服务器
date: 2018-08-02 19:06:10
description: 使用Windows远程桌面工具连接管理阿里云Ubuntu服务器
tags: [云服务器,Linux,Ubuntu]
category: 云服务器
---

本地Windows远程桌面连接阿里云Ubuntu 16.04服务器:

1、目的:希望通过本地的Windows远程桌面连接到阿里云的Ubuntu服务器,通过远程桌面图形界面的方式操作服务器。

2、条件:申请的阿里云Ubuntu服务器一台,本地Windows操作系统电脑一台。

3、如何远程桌面连接:

(1)首先通过Windows系统下连接Linux系统的命令行工具连接Ubuntu服务器,(工具:xshell,securecrt,putty等)。

(2)通过Windows下工具连接到linux操作系统,之后打开命令窗口,切换到root权限。

(3)先安装更新:apt-get upate。

(4)安装xrdp:输入apt-get install xrdp-->回车-->输入"y"-->回车,安装完成。

       (xrdp: An open source remote desktop protocol(rdp) server)

(5)安装vnc4server:输入apt-get install vnc4server"-->回车-->输入"y"-->回车,安装完成。

       (VNC (Virtual Network Console)是虚拟网络控制台的缩写)

(6)安装xfce4:输入apt-get install xubuntu-desktop"-->回车-->输入"y"-->回车。

> -->输入echo "xfce4-session" >~/.xsession-->回车-->输入 service xrdp restart-->回车,安装完成。

> (Xfce是一个自由软件,运行在类Unix操作系统 (如Linux、FreeBSD 和 Solaris)上,提供轻量级桌面环境。)

(7)在本地Windows电脑上,使用"窗口键+R"打开"运行对话框"-->输入"mstsc"-->回车-->输入Ubuntu主机的IP地址-->"连接"。

(8)选择"sesman-Xvnc"-->输入"用户名和密码"-->回车,成功登录到Ubuntu桌面,现在可以进行远程操作了。
