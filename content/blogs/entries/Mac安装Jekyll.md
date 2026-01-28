---
title: Mac安装Jekyll
date: 2025-10-24 21:11:11  +0800
categories: [GitHub,  Blog, Jekyll]
---

# 在macOS上轻松安装Jekyll：打造你的个人博客

更新了在Windows的Jekyll教程。顺便把环境在Mac上重新配置了一遍，把完整流程记录下来，给正在折腾博客的你一份可直接照做的macOS安装指南。

> 本文默认你使用 **zsh** 终端（macOS 默认），并通过 **rbenv** 管理 Ruby 版本，避免系统自带 Ruby 的权限与兼容问题。

---

## 第一步：准备基础环境

### 1. 安装 Homebrew（已装可跳过）

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

安装完成后，根据提示把 `brew` 加入 PATH，并重新打开终端或执行 `source ~/.zshrc`。

### 2. 安装 rbenv 与 ruby-build

```shell
brew update
brew install rbenv ruby-build
```

### 3. 初始化 rbenv（zsh）

```shell
echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
source ~/.zshrc
```

---

## 第二步：安装 Ruby 与 Jekyll

### 1. 安装较新的 Ruby（示例使用 3.3.5）

```shell
rbenv install 3.3.5
rbenv global 3.3.5
ruby -v
```

### 2. 安装 Bundler 和 Jekyll

```shell
gem install bundler jekyll
```

---

## 第三步：在项目中安装依赖并启动

在你的博客主目录下运行：

```shell
bundle install
bundle exec jekyll serve
```

看到成功提示后，在浏览器访问：

```
http://127.0.0.1:4000
```


<img src="../assets/images/2025-10-24-Mac-install-Jekyll/run_success.png" alt="mac_jekyll" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

## 安装完成！🎉

恭喜！现在你已经在 **macOS** 上成功安装并运行了 Jekyll。后续可以在 `_config.yml` 中调整主题与配置、在 `_posts` 中编写文章，用 `bundle exec jekyll build` 生成静态文件进行部署。
