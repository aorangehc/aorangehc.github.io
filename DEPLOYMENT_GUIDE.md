# 求职增强功能部署指南

## 概述
由于Windows环境下Jekyll本地安装较为复杂，我们推荐直接使用GitHub Pages进行在线预览和部署。

## 部署步骤

### 1. 推送到GitHub仓库

```bash
# 添加所有更改
git add .

# 提交更改
git commit -m "Add job-seeking enhancements: resume, projects, experience, publications pages"

# 推送到GitHub
git push origin enhancement
```

### 2. 在GitHub上合并分支

1. 访问你的GitHub仓库：`https://github.com/aorangehc/aorangehc.github.io`
2. 点击 "Compare & pull request" 按钮
3. 创建Pull Request，标题：`Add job-seeking enhancements`
4. 描述中可以包含：
   ```
   ## 新增功能
   - ✅ 简历页面 (Resume)
   - ✅ 项目展示页面 (Projects) 
   - ✅ 工作经历页面 (Experience)
   - ✅ 学术成果页面 (Publications)
   - ✅ 增强联系方式配置
   - ✅ SEO优化设置
   ```
5. 合并到main分支

### 3. 启用GitHub Pages

1. 在仓库设置中找到 "Pages" 选项
2. Source选择 "Deploy from a branch"
3. Branch选择 "main"
4. 文件夹选择 "/ (root)"
5. 点击Save

### 4. 访问网站

- 网站将在几分钟内部署完成
- 访问地址：`https://aorangehc.github.io`
- GitHub会自动使用Jekyll构建网站

## 个性化数据配置

部署完成后，你需要根据个人情况修改以下文件中的数据：

### 简历数据 (`_data/resume.yml`)
- 个人信息、教育背景、技能、证书等

### 项目数据 (`_data/projects.yml`)
- 项目名称、描述、技术栈、链接等

### 工作经历 (`_data/experience.yml`)
- 实习和工作经历、职责、成就等

### 学术成果 (`_data/publications.yml`)
- 论文、研究兴趣、学术活动等

### 联系方式 (`_data/contact.yml`)
- LinkedIn、Stack Overflow等社交媒体链接

## 优势

### 对求职者的优势
1. **专业展示**：结构化展示技能、项目和经历
2. **易于分享**：一个链接展示所有信息
3. **SEO优化**：提高在搜索引擎中的可见性
4. **移动友好**：响应式设计适配各种设备
5. **持续更新**：随时更新最新信息

### 对招聘者的优势
1. **快速了解**：一站式查看候选人信息
2. **技术验证**：通过GitHub仓库验证技术能力
3. **项目展示**：直观了解项目经验和技术栈
4. **联系便捷**：多种联系方式一目了然

## 注意事项

1. **数据隐私**：确保不包含敏感个人信息
2. **定期更新**：保持信息的时效性
3. **链接有效性**：定期检查外部链接是否有效
4. **移动端测试**：确保在手机上显示正常

## 故障排除

如果网站无法正常显示：
1. 检查GitHub Pages设置是否正确
2. 查看Actions标签页的构建日志
3. 确保所有YAML文件格式正确
4. 检查图片和文件路径是否正确

## 后续优化建议

1. 添加Google Analytics进行访问统计
2. 配置自定义域名（可选）
3. 添加更多项目案例
4. 优化页面加载速度
5. 添加多语言支持（中英文）