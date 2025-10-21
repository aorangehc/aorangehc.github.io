---
layout: page
icon: fas fa-user-graduate
order: 1
---

<div class="resume-container">
  <!-- 个人信息 -->
  <div class="personal-info">
    <h2><i class="fas fa-user"></i> 个人信息</h2>
    <div class="info-grid">
      <div class="info-item">
        <strong>姓名：</strong>{{ site.data.resume.personal.name }}
      </div>
      <div class="info-item">
        <strong>职位：</strong>{{ site.data.resume.personal.title }}
      </div>
      <div class="info-item">
        <strong>邮箱：</strong><a href="mailto:{{ site.data.resume.personal.email }}">{{ site.data.resume.personal.email }}</a>
      </div>
      <div class="info-item">
        <strong>GitHub：</strong><a href="{{ site.data.resume.personal.github }}" target="_blank">{{ site.data.resume.personal.github }}</a>
      </div>
      <div class="info-item">
        <strong>地址：</strong>{{ site.data.resume.personal.location }}
      </div>
    </div>
    <div class="summary">
      <p>{{ site.data.resume.personal.summary }}</p>
    </div>
  </div>

  <!-- 教育背景 -->
  <div class="education-section">
    <h2><i class="fas fa-graduation-cap"></i> 教育背景</h2>
    {% for edu in site.data.resume.education %}
    <div class="education-item">
      <div class="edu-header">
        <h3>{{ edu.degree }} - {{ edu.major }}</h3>
        <span class="period">{{ edu.period }}</span>
      </div>
      <div class="edu-details">
        <p><strong>学校：</strong>{{ edu.school }}</p>
        <p><strong>GPA：</strong>{{ edu.gpa }}</p>
        <p>{{ edu.description }}</p>
      </div>
    </div>
    {% endfor %}
  </div>

  <!-- 技能 -->
  <div class="skills-section">
    <h2><i class="fas fa-code"></i> 技能</h2>
    
    <div class="skill-category">
      <h3>编程语言</h3>
      <div class="skills-grid">
        {% for skill in site.data.resume.skills.programming %}
        <div class="skill-item">
          <strong>{{ skill.name }}</strong> ({{ skill.level }})
          <p>{{ skill.description }}</p>
        </div>
        {% endfor %}
      </div>
    </div>

    <div class="skill-category">
      <h3>框架与库</h3>
      <div class="skills-tags">
        {% for framework in site.data.resume.skills.frameworks %}
        <span class="skill-tag">{{ framework }}</span>
        {% endfor %}
      </div>
    </div>

    <div class="skill-category">
      <h3>工具与技术</h3>
      <div class="skills-tags">
        {% for tool in site.data.resume.skills.tools %}
        <span class="skill-tag">{{ tool }}</span>
        {% endfor %}
      </div>
    </div>
  </div>

  <!-- 项目经历 -->
  <div class="projects-section">
    <h2><i class="fas fa-project-diagram"></i> 项目经历</h2>
    {% for project in site.data.resume.projects %}
    <div class="project-item">
      <div class="project-header">
        <h3>{{ project.name }}</h3>
        <span class="period">{{ project.period }}</span>
      </div>
      <div class="project-details">
        <p><strong>角色：</strong>{{ project.role }}</p>
        <div class="technologies">
          <strong>技术栈：</strong>
          {% for tech in project.technologies %}
          <span class="tech-tag">{{ tech }}</span>
          {% endfor %}
        </div>
        <p>{{ project.description }}</p>
        {% if project.repository %}
        <p><strong>代码仓库：</strong><a href="{{ project.repository }}" target="_blank">{{ project.repository }}</a></p>
        {% endif %}
      </div>
    </div>
    {% endfor %}
  </div>

  <!-- 实习经历 -->
  <div class="internships-section">
    <h2><i class="fas fa-briefcase"></i> 实习经历</h2>
    {% for internship in site.data.resume.internships %}
    <div class="internship-item">
      <div class="internship-header">
        <h3>{{ internship.position }}</h3>
        <span class="period">{{ internship.period }}</span>
      </div>
      <div class="internship-details">
        <p><strong>公司：</strong>{{ internship.company }}</p>
        <p><strong>地点：</strong>{{ internship.location }}</p>
        <ul>
          {% for desc in internship.description %}
          <li>{{ desc }}</li>
          {% endfor %}
        </ul>
        <div class="technologies">
          <strong>技术栈：</strong>
          {% for tech in internship.technologies %}
          <span class="tech-tag">{{ tech }}</span>
          {% endfor %}
        </div>
      </div>
    </div>
    {% endfor %}
  </div>

  <!-- 发表论文 -->
  <div class="publications-section">
    <h2><i class="fas fa-file-alt"></i> 发表论文</h2>
    {% for pub in site.data.resume.publications %}
    <div class="publication-item">
      <h3>{{ pub.title }}</h3>
      <p><strong>作者：</strong>{{ pub.authors | join: ", " }}</p>
      <p><strong>发表于：</strong>{{ pub.venue }} ({{ pub.year }})</p>
      <p><strong>类型：</strong>{{ pub.type }}</p>
      <p>{{ pub.description }}</p>
      {% if pub.pdf %}
      <p><a href="{{ pub.pdf }}" target="_blank" class="btn-link"><i class="fas fa-file-pdf"></i> 查看PDF</a></p>
      {% endif %}
    </div>
    {% endfor %}
  </div>

  <!-- 荣誉奖项 -->
  <div class="honors-section">
    <h2><i class="fas fa-trophy"></i> 荣誉奖项</h2>
    <div class="honors-grid">
      {% for honor in site.data.resume.honors %}
      <div class="honor-item">
        <h3>{{ honor.name }}</h3>
        <p><strong>年份：</strong>{{ honor.year }}</p>
        <p><strong>颁发机构：</strong>{{ honor.organization }}</p>
      </div>
      {% endfor %}
    </div>
  </div>

  <!-- 语言能力 -->
  <div class="languages-section">
    <h2><i class="fas fa-language"></i> 语言能力</h2>
    <div class="languages-grid">
      {% for lang in site.data.resume.languages %}
      <div class="language-item">
        <h3>{{ lang.name }}</h3>
        <p><strong>水平：</strong>{{ lang.level }}</p>
        {% if lang.description %}
        <p>{{ lang.description }}</p>
        {% endif %}
      </div>
      {% endfor %}
    </div>
  </div>
</div>

<style>
.resume-container {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.resume-container h2 {
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 20px;
}

.resume-container h2 i {
  margin-right: 10px;
  color: #3498db;
}

.personal-info .info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 10px;
  margin-bottom: 15px;
}

.info-item {
  padding: 8px 0;
}

.summary {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
  margin-top: 15px;
}

.education-item, .project-item, .internship-item, .publication-item {
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.edu-header, .project-header, .internship-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.edu-header h3, .project-header h3, .internship-header h3 {
  margin: 0;
  color: #2c3e50;
}

.period {
  background: #3498db;
  color: white;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.9em;
}

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 15px;
  margin-bottom: 20px;
}

.skill-item {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
}

.skills-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 20px;
}

.skill-tag, .tech-tag {
  background: #e9ecef;
  color: #495057;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.9em;
}

.tech-tag {
  background: #d4edda;
  color: #155724;
}

.technologies {
  margin: 10px 0;
}

.honors-grid, .languages-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 15px;
}

.honor-item, .language-item {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
}

.btn-link {
  display: inline-block;
  background: #3498db;
  color: white;
  padding: 8px 16px;
  text-decoration: none;
  border-radius: 5px;
  margin-top: 10px;
}

.btn-link:hover {
  background: #2980b9;
  color: white;
  text-decoration: none;
}

@media (max-width: 768px) {
  .edu-header, .project-header, .internship-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .period {
    margin-top: 10px;
  }
  
  .info-grid {
    grid-template-columns: 1fr;
  }
}
</style>