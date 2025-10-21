---
layout: page
icon: fas fa-briefcase
order: 3
---

<div class="experience-container">
  <!-- 实习经历 -->
  <div class="work-experience-section">
    <h2><i class="fas fa-briefcase"></i> 实习经历</h2>
    <div class="timeline">
      {% for exp in site.data.experience.experiences %}
      <div class="timeline-item">
        <div class="timeline-marker">
          <div class="timeline-dot"></div>
        </div>
        <div class="timeline-content">
          <div class="experience-card">
            <div class="experience-header">
              <div class="company-info">
                <h3>{{ exp.position }}</h3>
                <h4>{{ exp.company }}</h4>
                <div class="experience-meta">
                  <span class="period">{{ exp.period }}</span>
                  <span class="location">{{ exp.location }}</span>
                  <span class="type type-{{ exp.type }}">{{ exp.type }}</span>
                </div>
              </div>
            </div>
            
            <div class="experience-body">
              <div class="department">
                <strong>部门：</strong>{{ exp.department }}
              </div>
              
              <div class="description">
                <p>{{ exp.description }}</p>
              </div>
              
              <div class="responsibilities">
                <h5><i class="fas fa-tasks"></i> 主要职责</h5>
                <ul>
                  {% for responsibility in exp.responsibilities %}
                  <li>{{ responsibility }}</li>
                  {% endfor %}
                </ul>
              </div>
              
              <div class="achievements">
                <h5><i class="fas fa-trophy"></i> 主要成就</h5>
                <ul>
                  {% for achievement in exp.achievements %}
                  <li>{{ achievement }}</li>
                  {% endfor %}
                </ul>
              </div>
              
              <div class="technologies">
                <h5><i class="fas fa-code"></i> 技术栈</h5>
                <div class="tech-tags">
                  {% for tech in exp.technologies %}
                  <span class="tech-tag">{{ tech }}</span>
                  {% endfor %}
                </div>
              </div>
              
              <div class="skills-gained">
                <h5><i class="fas fa-lightbulb"></i> 技能收获</h5>
                <ul>
                  {% for skill in exp.skills_gained %}
                  <li>{{ skill }}</li>
                  {% endfor %}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>

  <!-- 志愿服务经历 -->
  <div class="volunteer-section">
    <h2><i class="fas fa-hands-helping"></i> 志愿服务经历</h2>
    <div class="volunteer-grid">
      {% for volunteer in site.data.experience.volunteer_experience %}
      <div class="volunteer-card">
        <div class="volunteer-header">
          <h3>{{ volunteer.position }}</h3>
          <h4>{{ volunteer.organization }}</h4>
          <span class="period">{{ volunteer.period }}</span>
        </div>
        
        <div class="volunteer-body">
          <div class="description">
            <p>{{ volunteer.description }}</p>
          </div>
          
          <div class="responsibilities">
            <h5><i class="fas fa-tasks"></i> 主要工作</h5>
            <ul>
              {% for responsibility in volunteer.responsibilities %}
              <li>{{ responsibility }}</li>
              {% endfor %}
            </ul>
          </div>
          
          <div class="achievements">
            <h5><i class="fas fa-star"></i> 主要成果</h5>
            <ul>
              {% for achievement in volunteer.achievements %}
              <li>{{ achievement }}</li>
              {% endfor %}
            </ul>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>

<style>
.experience-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.experience-container h2 {
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 30px;
}

.experience-container h2 i {
  margin-right: 10px;
  color: #3498db;
}

/* 时间线样式 */
.timeline {
  position: relative;
  padding-left: 30px;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 15px;
  top: 0;
  bottom: 0;
  width: 2px;
  background: #3498db;
}

.timeline-item {
  position: relative;
  margin-bottom: 40px;
}

.timeline-marker {
  position: absolute;
  left: -22px;
  top: 20px;
}

.timeline-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: #3498db;
  border: 3px solid #ffffff;
  box-shadow: 0 0 0 3px #3498db;
}

.timeline-content {
  margin-left: 20px;
}

/* 经历卡片样式 */
.experience-card {
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.experience-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.experience-header h3 {
  margin: 0 0 5px 0;
  color: #2c3e50;
  font-size: 1.3em;
  font-weight: bold;
}

.experience-header h4 {
  margin: 0 0 15px 0;
  color: #7f8c8d;
  font-size: 1.1em;
  font-weight: normal;
}

.experience-meta {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.period {
  background: #3498db;
  color: white;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.9em;
}

.location {
  background: #95a5a6;
  color: white;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.9em;
}

.type {
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.9em;
  font-weight: 500;
}

.type-实习 {
  background: #d4edda;
  color: #155724;
}

.experience-body {
  margin-top: 20px;
}

.department {
  margin-bottom: 15px;
  padding: 10px;
  background: #f8f9fa;
  border-radius: 5px;
}

.description {
  margin-bottom: 20px;
  line-height: 1.6;
}

.experience-body h5 {
  color: #2c3e50;
  margin: 20px 0 10px 0;
  font-size: 1.1em;
  display: flex;
  align-items: center;
  gap: 8px;
}

.experience-body h5 i {
  color: #3498db;
  font-size: 0.9em;
}

.experience-body ul {
  margin: 10px 0;
  padding-left: 20px;
}

.experience-body li {
  margin-bottom: 8px;
  line-height: 1.5;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 10px;
}

.tech-tag {
  background: #e9ecef;
  color: #495057;
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.9em;
}

/* 志愿服务样式 */
.volunteer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 25px;
}

.volunteer-card {
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  padding: 25px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.volunteer-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.volunteer-header h3 {
  margin: 0 0 5px 0;
  color: #2c3e50;
  font-size: 1.2em;
  font-weight: bold;
}

.volunteer-header h4 {
  margin: 0 0 10px 0;
  color: #7f8c8d;
  font-size: 1em;
  font-weight: normal;
}

.volunteer-header .period {
  background: #27ae60;
}

.volunteer-body {
  margin-top: 15px;
}

.volunteer-body h5 {
  color: #2c3e50;
  margin: 15px 0 8px 0;
  font-size: 1em;
  display: flex;
  align-items: center;
  gap: 6px;
}

.volunteer-body h5 i {
  color: #27ae60;
  font-size: 0.9em;
}

.volunteer-body ul {
  margin: 8px 0;
  padding-left: 18px;
}

.volunteer-body li {
  margin-bottom: 6px;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .timeline {
    padding-left: 20px;
  }
  
  .timeline::before {
    left: 10px;
  }
  
  .timeline-marker {
    left: -17px;
  }
  
  .timeline-content {
    margin-left: 15px;
  }
  
  .experience-meta {
    flex-direction: column;
    gap: 8px;
  }
  
  .volunteer-grid {
    grid-template-columns: 1fr;
  }
  
  .experience-card, .volunteer-card {
    padding: 20px;
  }
}

@media (max-width: 480px) {
  .experience-container {
    padding: 15px;
  }
  
  .timeline {
    padding-left: 15px;
  }
  
  .timeline::before {
    left: 7px;
  }
  
  .timeline-marker {
    left: -15px;
  }
  
  .timeline-content {
    margin-left: 10px;
  }
  
  .experience-card, .volunteer-card {
    padding: 15px;
  }
}
</style>