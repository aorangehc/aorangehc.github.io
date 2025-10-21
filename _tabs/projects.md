---
layout: page
icon: fas fa-project-diagram
order: 2
---

<div class="projects-container">
  <!-- 精选项目 -->
  <div class="featured-section">
    <h2><i class="fas fa-star"></i> 精选项目</h2>
    <div class="featured-grid">
      {% for featured_name in site.data.projects.featured_projects %}
        {% for project in site.data.projects.projects %}
          {% if project.name == featured_name %}
          <div class="featured-project-card">
            {% if project.image %}
            <div class="project-image">
              <img src="{{ project.image }}" alt="{{ project.name }}" loading="lazy">
            </div>
            {% endif %}
            <div class="project-content">
              <h3>{{ project.name }}</h3>
              <p class="project-description">{{ project.description }}</p>
              <div class="project-links">
                {% if project.repository and project.repository != "" %}
                <a href="{{ project.repository }}" target="_blank" class="btn-link">
                  <i class="fab fa-github"></i> 代码仓库
                </a>
                {% endif %}
                {% if project.demo and project.demo != "" %}
                <a href="{{ project.demo }}" target="_blank" class="btn-link demo">
                  <i class="fas fa-external-link-alt"></i> 在线演示
                </a>
                {% endif %}
              </div>
            </div>
          </div>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </div>
  </div>

  <!-- 所有项目 -->
  <div class="all-projects-section">
    <h2><i class="fas fa-folder-open"></i> 所有项目</h2>
    <div class="projects-grid">
      {% for project in site.data.projects.projects %}
      <div class="project-card">
        <div class="project-header">
          <div class="project-title-section">
            <h3>{{ project.name }}</h3>
            <div class="project-meta">
              <span class="period">{{ project.period }}</span>
              <span class="status status-{{ project.status | replace: '已完成', 'completed' | replace: '进行中', 'ongoing' | replace: '持续更新', 'updating' | replace: '持续维护', 'maintaining' }}">{{ project.status }}</span>
            </div>
          </div>
        </div>
        
        <div class="project-body">
          {% if project.image %}
          <div class="project-thumbnail">
            <img src="{{ project.image }}" alt="{{ project.name }}" loading="lazy">
          </div>
          {% endif %}
          
          <div class="project-details">
            <p><strong>角色：</strong>{{ project.role }}</p>
            
            <div class="technologies">
              <strong>技术栈：</strong>
              <div class="tech-tags">
                {% for tech in project.technologies %}
                <span class="tech-tag">{{ tech }}</span>
                {% endfor %}
              </div>
            </div>
            
            <div class="project-description">
              <p>{{ project.description }}</p>
            </div>
            
            {% if project.features %}
            <div class="project-features">
              <strong>主要功能：</strong>
              <ul>
                {% for feature in project.features %}
                <li>{{ feature }}</li>
                {% endfor %}
              </ul>
            </div>
            {% endif %}
          </div>
        </div>
        
        <div class="project-footer">
          <div class="project-links">
            {% if project.repository and project.repository != "" %}
            <a href="{{ project.repository }}" target="_blank" class="btn-link">
              <i class="fab fa-github"></i> 代码仓库
            </a>
            {% endif %}
            {% if project.demo and project.demo != "" %}
            <a href="{{ project.demo }}" target="_blank" class="btn-link demo">
              <i class="fas fa-external-link-alt"></i> 在线演示
            </a>
            {% endif %}
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>

<style>
.projects-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.projects-container h2 {
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 30px;
}

.projects-container h2 i {
  margin-right: 10px;
  color: #3498db;
}

/* 精选项目样式 */
.featured-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 30px;
  margin-bottom: 50px;
}

.featured-project-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  color: white;
}

.featured-project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}

.featured-project-card .project-image {
  height: 200px;
  overflow: hidden;
}

.featured-project-card .project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.featured-project-card .project-content {
  padding: 25px;
}

.featured-project-card h3 {
  margin: 0 0 15px 0;
  font-size: 1.3em;
  font-weight: bold;
}

.featured-project-card .project-description {
  margin-bottom: 20px;
  line-height: 1.6;
  opacity: 0.9;
}

/* 所有项目样式 */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
  gap: 25px;
}

.project-card {
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.project-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.project-header {
  padding: 20px 20px 0 20px;
}

.project-title-section h3 {
  margin: 0 0 10px 0;
  color: #2c3e50;
  font-size: 1.2em;
  line-height: 1.3;
}

.project-meta {
  display: flex;
  gap: 10px;
  align-items: center;
}

.period {
  background: #3498db;
  color: white;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.85em;
}

.status {
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.85em;
  font-weight: 500;
}

.status-completed {
  background: #d4edda;
  color: #155724;
}

.status-ongoing {
  background: #fff3cd;
  color: #856404;
}

.status-updating, .status-maintaining {
  background: #d1ecf1;
  color: #0c5460;
}

.project-body {
  padding: 20px;
}

.project-thumbnail {
  width: 100%;
  height: 180px;
  overflow: hidden;
  border-radius: 8px;
  margin-bottom: 15px;
}

.project-thumbnail img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-details p {
  margin-bottom: 12px;
  line-height: 1.6;
}

.technologies {
  margin-bottom: 15px;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 8px;
}

.tech-tag {
  background: #e9ecef;
  color: #495057;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.85em;
}

.project-description {
  margin-bottom: 15px;
}

.project-features {
  margin-bottom: 15px;
}

.project-features ul {
  margin: 8px 0 0 0;
  padding-left: 20px;
}

.project-features li {
  margin-bottom: 5px;
  line-height: 1.5;
}

.project-footer {
  padding: 0 20px 20px 20px;
}

.project-links {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.btn-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #3498db;
  color: white;
  padding: 8px 16px;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9em;
  transition: background-color 0.2s ease;
}

.btn-link:hover {
  background: #2980b9;
  color: white;
  text-decoration: none;
}

.btn-link.demo {
  background: #27ae60;
}

.btn-link.demo:hover {
  background: #219a52;
}

.featured-project-card .btn-link {
  background: rgba(255,255,255,0.2);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.3);
}

.featured-project-card .btn-link:hover {
  background: rgba(255,255,255,0.3);
}

@media (max-width: 768px) {
  .featured-grid {
    grid-template-columns: 1fr;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .project-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  
  .project-links {
    flex-direction: column;
  }
  
  .btn-link {
    text-align: center;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .projects-container {
    padding: 15px;
  }
  
  .project-card {
    margin-bottom: 20px;
  }
  
  .project-header, .project-body, .project-footer {
    padding-left: 15px;
    padding-right: 15px;
  }
}
</style>