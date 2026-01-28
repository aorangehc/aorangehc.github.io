---
title: golang学习记录（12）
date: 2024-10-20 15:01:03  +0800
categories: [golang, golang基础学习]
---

# go 中的 package 和 gomodules

## 1、package的定义和导入

> 在go中，package是一个非常重要的概念，它是go语言中的一个基本单位，它可以包含多个.go文件，每个.go文件都必须属于一个package，这也是代码复用的基础，其中fmt、os、io等都是一个包
>
> 每个源码文件的第一行都是package xxx，xxx就是这个文件所属的包名
>
> 同一目录之下的源码可以直接使用，不需要import

## 2、import的方式

> 1、import "路径名称"
>
> 2、import 别名 "路径名称"
>
> 3、import ."路径名称"
>

注意包名称不能重复

## 3、go.mod

> 1、go.mod是go语言中的一个文件，它是go语言的一个依赖管理文件，它的作用是管理go语言的依赖关系
>
> 2、这个文件的内容是自动维护的
>
> 3、go.mod维护内容下载到一个固定位置中


## 4、设置GOProxy的国内镜像

> 在命令行中设置成国内镜像即可

<img src="../assets/images/go/学习记录（12）/1.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

## 5、goget与gomod相关指令

> go get 指令用于下载包，它会自动下载包的依赖包
>
> go get 依赖地址
>
> go get - u 指令用于更新包，它会自动更新包的依赖包
>
> go get -u=patch 指令用于更新包到修订版本


> go mod help查看能使用的指令，如下：

<img src="../assets/images/go/学习记录（12）/2.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

> go mod tidy

## 6、gomodreplace

> go mod replace 指令用于替换包，它会自动替换包的依赖包

## 7、go的一些编码规范

<img src="../assets/images/go/学习记录（12）/3.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

<img src="../assets/images/go/学习记录（12）/4.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

<img src="../assets/images/go/学习记录（12）/5.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">
