---
title: golang学习记录（1）-在win搭建go环境
date: 2024-09-16 10:46:03  +0800
categories: [go,  环境搭建]
tags: [go,  环境搭建]
math: true
pin: true
mermaid: true
---

## Golong环境搭建
> SDK（Soft Development Kit, 软件开发工具包）：是一套工具得集合，方便开发者在特定的编程语言环境下进行开发
>
> 工具通常包含库、框架、文档和使用指导……

### 下载SDK工具包
[工具包下载网址](https://go.p2hp.com/dl/)

根据自己的需要可以选择不同的工具包，我的是Windows10 64位，选择下载“go1.17.3.windows-arm64.zip”
<img src="/assets/images/go/学习记录（1）/1.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

下载完成后，在电脑中选择一个地方解压文件即可，尽量解压在D盘中，解压后安装包删除即可，节省空间。

解压后的目录是下面这样，其中最重要的是bin目录下的“go.exe”，在我们的程序写完之后，需要通过它来编译运行.
<img src="/assets/images/go/学习记录（1）/2.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

进入到bin目录下，在上方输入cmd，回车进入命令行模式，输入指令,查看go的版本
```shell
go version
```
如果能够正常显示版本号，就表示安装成功
<img src="/assets/images/go/学习记录（1）/3.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

### 配置环境变量
> 在安装成功后还需要进行环境变量的配置
> 
> 在我的电脑，右击选择属性，之后点击右侧的高级系统设置，点击下方的环境变量，进入环境变量配置

go需要进行三个环境变量的配置，如下表

|环境变量名称|作用|
|-----|-----|
|GOROOT|表明go安装的位置|
|Path|表明go.exe的位置|
|GOPATH|表明go项目的位置|

配置示例如下：

GOROOT
<img src="/assets/images/go/学习记录（1）/4.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

Path
<img src="/assets/images/go/学习记录（1）/5.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

GOPATH
<img src="/assets/images/go/学习记录（1）/6.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

测试环境变量是否配置成功：
win+R 输入cmd，打开命令行，输入命令查看
```shell
go version
```
<img src="/assets/images/go/学习记录（1）/7.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">
如果能够正常显示版本号，就表示环境变量配置成功。

#### IDE配置
这是我们使用的是“宇宙最强IDE”--VsCode
直接在插件市场选择插件就行，这里我们安装了下面几个：
<img src="/assets/images/go/学习记录（1）/8.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

在这了我们使用ctrl+shift+p，输入Go: install/update tools后回车即可自动安装。