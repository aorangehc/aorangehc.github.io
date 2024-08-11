---
title: Jekyll Test
date: 2024-08-09 16:17:09 +0800
categories: [Test, Hello]
tags: [jekyll, hello world] 
render_with_liquid: false
---
## 1.测试

在Markdown中添加PDF链接的格式如下：

[pdf测试](/assets/pdf/An Efficient Man-Machine Recognition Method Based On Mouse.pdf)

<embed src="/assets/pdf/An Efficient Man-Machine Recognition Method Based On Mouse.pdf" type="application/pdf" width="100%" height="500px" />

![能显示图片吗？](/assets/images/2020-03-29-jekyll-test/图片测试.png)


视频播放测试

可播放

可播放的视频对大小有要求，还是上传到哔哩哔哩账号比较合适




<video width="320" height="240" controls autoplay loop>
  <source src="/assets/video/test.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


播放视频的方法：将视频上传bilibili，然后通过之前配置的bilibili播放控件播放视频
<iframe src="//player.bilibili.com/player.html?bvid=BV1EH4y1c7XY" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%" height="500px"> </iframe>
