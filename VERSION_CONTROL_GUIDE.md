# 🔄 版本控制和回滚指南

## 📋 当前状态

### 分支结构
- **main**: 原始版本（生产环境）
- **enhancement**: 求职增强功能分支
- **backup-original-20251021-2108**: 原始版本备份分支

### 已推送到GitHub的分支
✅ `main` - 原始版本  
✅ `enhancement` - 求职增强功能  
✅ `backup-original-20251021-2108` - 备份分支  

## 🚀 部署到GitHub Pages

### 方法1: 合并到main分支（推荐）

```bash
# 1. 切换到main分支
git checkout main

# 2. 合并enhancement分支
git merge enhancement

# 3. 推送到GitHub
git push origin main
```

### 方法2: 直接使用enhancement分支

1. 访问 GitHub 仓库设置
2. 进入 **Settings** → **Pages**
3. 在 **Source** 中选择 `enhancement` 分支
4. 点击 **Save**

## 🔙 版本回滚方案

### 情况1: 如果合并到main后有问题

#### 方案A: 重置到原始版本
```bash
# 1. 切换到main分支
git checkout main

# 2. 重置到备份分支的状态
git reset --hard backup-original-20251021-2108

# 3. 强制推送（⚠️ 谨慎使用）
git push origin main --force
```

#### 方案B: 创建回滚提交（更安全）
```bash
# 1. 切换到main分支
git checkout main

# 2. 创建回滚提交
git revert HEAD

# 3. 推送回滚
git push origin main
```

### 情况2: 如果使用enhancement分支部署有问题

#### 直接切换回main分支部署
1. 访问 GitHub 仓库设置
2. 进入 **Settings** → **Pages**
3. 在 **Source** 中选择 `main` 分支
4. 点击 **Save**

## 📊 GitHub Pages 配置步骤

### 1. 启用GitHub Pages
1. 访问: `https://github.com/aorangehc/aorangehc.github.io/settings/pages`
2. 在 **Source** 部分选择分支:
   - 选择 `main` (原始版本)
   - 或选择 `enhancement` (求职增强版本)
3. 点击 **Save**

### 2. 等待部署
- 部署通常需要1-5分钟
- 可以在 **Actions** 标签页查看部署状态
- 访问: `https://aorangehc.github.io`

### 3. 自定义域名（可选）
如果有自定义域名，在 **Custom domain** 中输入域名

## ⚠️ 重要注意事项

### 安全备份
- ✅ 原始版本已备份到 `backup-original-20251021-2108` 分支
- ✅ 所有分支都已推送到GitHub远程仓库
- ✅ 可以随时恢复到任何版本

### 推荐流程
1. **测试**: 先使用 `enhancement` 分支部署测试
2. **确认**: 确认功能正常后再合并到 `main`
3. **备份**: 重要更改前总是创建备份分支

### 紧急回滚
如果网站出现严重问题：
```bash
# 立即切换到备份版本
git checkout backup-original-20251021-2108
git checkout -b emergency-rollback
git push origin emergency-rollback
```
然后在GitHub Pages设置中切换到 `emergency-rollback` 分支。

## 🔗 相关链接

- **GitHub仓库**: https://github.com/aorangehc/aorangehc.github.io
- **GitHub Pages设置**: https://github.com/aorangehc/aorangehc.github.io/settings/pages
- **网站地址**: https://aorangehc.github.io
- **Actions状态**: https://github.com/aorangehc/aorangehc.github.io/actions

## 📞 问题排查

### 部署失败
1. 检查 **Actions** 标签页的构建日志
2. 确认 `_config.yml` 配置正确
3. 检查是否有语法错误

### 网站无法访问
1. 确认GitHub Pages已启用
2. 检查分支选择是否正确
3. 等待DNS传播（最多24小时）

### 功能异常
1. 检查浏览器控制台错误
2. 确认所有文件都已正确推送
3. 对比本地预览和线上版本差异