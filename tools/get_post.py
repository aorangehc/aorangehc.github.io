# python脚本，添加信息自动生成post文件
# -*- coding: utf-8 -*-
import datetime
import os

# 获取用户输入
title = input("请输入post题目：")
date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %z") + ' +0800'
categories = input("请输入文章类别（多个通过“，”分割）：").split(',')
tags = input("请输入文章标签（多个通过“，”分割）：").split(',')

# 将列表转换为字符串
categories_str = ', '.join(categories)
tags_str = ', '.join(tags)

# 创建 Jekyll front matter
front_matter = f"---\n" \
               f"title: {title}\n" \
               f"date: {date_str}\n" \
               f"categories: [{categories_str}]\n" \
               f"tags: [{tags_str}]\n" \
               f"render_with_liquid: false\n" \
               f"---\n"

# 创建 Markdown 文件名
filename = f"{datetime.datetime.now().strftime('%Y-%m-%d')}-{title.replace(' ', '-')}.md"

filename = "../_posts/" + filename

# 确保文件路径存在
dir_path = os.path.dirname(filename)
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# 写入文件，使用 UTF-8 编码
with open(filename, 'w', encoding='utf-8') as file:
    file.write(front_matter)

print("文件创建完成")
