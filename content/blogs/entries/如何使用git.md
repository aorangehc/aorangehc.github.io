---
title: 如何使用git
date: 2025-01-11 09:58:39  +0800
categories: [技术, git, 指令]
---

<img src="../assets/images/如何使用git/git.png" alt="go" style="width: 40%; height: auto; display: block; margin-left: auto; margin-right: auto;">

**记录一下自己使用git容易忘记的指令和要学习遵守提交规范**

## git提交规范

<img src="../assets/images/如何使用git/git-commit规范.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

### 提交信息格式

每次提交应遵循以下格式：

```bash
<类型>(<范围>): <简短描述>

<更详细的描述>
```

* **类型**：提交的类型，表示本次提交的目的或类别，常见的类型包括：

  * `feat`：新特性（feature）

  * `fix`：修复 bug

  * `docs`：文档相关更新

  * `style`：代码风格的调整（空格、格式化等，不影响代码功能）

  * `refactor`：重构（既不修复 bug 也不添加新特性）

  * `test`：增加或修改测试代码

  * `ci`：持续集成相关的修改

  * `build`：构建系统（如打包工具等）

  * `revert`：回退提交

* **范围**：提交影响的模块或功能范围，对项目的哪个模块或者功能进行了修改，用圆括号括起来。例如：`feat(api)`, `fix(login)`。

* **简短描述**：简洁明了地描述本次提交的目的，首字母小写，不超过 50 个字符。

* **详细描述**：对提交的详细描述，包括原因、解决方案、关键点等。详细描述与简短描述之间空一行，内容可选但推荐提供，最大长度可以是 72 字符。

### 提交信息示例

* `feat(user-auth): add login API`

* `fix(api): fix invalid username validation`

* `docs(readme): update setup instructions`

* `refactor(auth): improve password hashing algorithm`

* `test(user): add unit tests for login functionality`

* `chore(deps): update dependency versions`

### 提交时的注意事项

* **避免**：

  * 使用模糊不清的提交信息，如 `fix`, `update`, `change` 等。

  * 提交过大的改动，建议将大改动拆分成多个小的提交。

  * 直接修改代码逻辑的提交没有详细描述。

* **务必**：

  * 保持提交信息简洁且有意义，能清晰地告诉他人此次修改的意图。

  * 每次提交前，请确保代码能够成功编译并通过测试，避免提交未通过测试的代码。

### demo

```bash
git add . # 添加修改的文件到暂存区
git commit -m "feat(user-auth): add login API" # 提交代码并写简短描述
git push origin main # 推送到远程仓库
```

```bash
# 新特性
git commit -m "feat(auth): 添加用户api"

# 修复 bug
git commit -m "fix(validation): ..."

# 代码重构
git commit -m "refactor(user): ...."

# 添加测试
git commit -m "test(user): 为登录添加单元测试"

# 文档更新
git commit -m "docs(readme): 更新安装指南"

```


## git常用指令

### 修改远程仓库地址

```bash
git remote set-url origin <new-url>
```

<img src="../assets/images/如何使用git/git-remote-change.png" alt="go" style="width: 50%; height: auto; display: block; margin-left: auto; margin-right: auto;">

### 同步远程仓库分支

```bash
# 同步远程仓库到main分支
git fetch origin main
```

## 参考资料

[Git 提交规范](https://my.feishu.cn/docx/COrVd46PDoPf7TxB1tZc0rcInTg)