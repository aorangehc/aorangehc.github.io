---
layout: page
icon: fas fa-file-alt
order: 4
---

<div class="publications-container">
  <!-- 发表论文 -->
  <div class="publications-section">
    <h2><i class="fas fa-file-alt"></i> 发表论文</h2>
    <div class="publications-list">
      {% for pub in site.data.publications.publications %}
      <div class="publication-card">
        <div class="publication-header">
          <h3>{{ pub.title }}</h3>
          <div class="publication-meta">
            <span class="status status-{{ pub.status | replace: '已发表', 'published' | replace: '审稿中', 'reviewing' | replace: '准备投稿', 'preparing' }}">{{ pub.status }}</span>
            <span class="type">{{ pub.type }}</span>
            <span class="year">{{ pub.year }}</span>
          </div>
        </div>
        
        <div class="publication-body">
          <div class="authors">
            <strong>作者：</strong>
            {% for author in pub.authors %}
              {% if author == "orange" %}
                <span class="author-highlight">{{ author }}</span>
              {% else %}
                <span class="author">{{ author }}</span>
              {% endif %}
              {% unless forloop.last %}, {% endunless %}
            {% endfor %}
          </div>
          
          <div class="venue">
            <strong>发表于：</strong>{{ pub.venue }} ({{ pub.venue_short }})
            {% if pub.volume and pub.volume != "" %}
              , Vol. {{ pub.volume }}
              {% if pub.issue and pub.issue != "" %}, No. {{ pub.issue }}{% endif %}
              {% if pub.pages and pub.pages != "" %}, pp. {{ pub.pages }}{% endif %}
            {% endif %}
          </div>
          
          {% if pub.publisher and pub.publisher != "" %}
          <div class="publisher">
            <strong>出版社：</strong>{{ pub.publisher }}
          </div>
          {% endif %}
          
          <div class="abstract">
            <h5><i class="fas fa-quote-left"></i> 摘要</h5>
            <p>{{ pub.abstract }}</p>
          </div>
          
          <div class="keywords">
            <strong>关键词：</strong>
            {% for keyword in pub.keywords %}
            <span class="keyword-tag">{{ keyword }}</span>
            {% endfor %}
          </div>
          
          <div class="publication-stats">
            {% if pub.citation_count > 0 %}
            <div class="citation-count">
              <i class="fas fa-quote-right"></i> 被引用 {{ pub.citation_count }} 次
            </div>
            {% endif %}
          </div>
          
          <div class="publication-links">
            {% if pub.pdf and pub.pdf != "" %}
            <a href="{{ pub.pdf }}" target="_blank" class="btn-link pdf">
              <i class="fas fa-file-pdf"></i> PDF
            </a>
            {% endif %}
            {% if pub.doi and pub.doi != "" %}
            <a href="https://doi.org/{{ pub.doi }}" target="_blank" class="btn-link doi">
              <i class="fas fa-external-link-alt"></i> DOI
            </a>
            {% endif %}
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>

  <!-- 研究兴趣 -->
  <div class="research-interests-section">
    <h2><i class="fas fa-microscope"></i> 研究兴趣</h2>
    <div class="interests-grid">
      {% for interest in site.data.publications.research_interests %}
      <div class="interest-card">
        <h3>{{ interest.name }}</h3>
        <p>{{ interest.description }}</p>
        <div class="interest-keywords">
          {% for keyword in interest.keywords %}
          <span class="interest-tag">{{ keyword }}</span>
          {% endfor %}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>

  <!-- 学术活动 -->
  <div class="academic-activities-section">
    <h2><i class="fas fa-users"></i> 学术活动</h2>
    <div class="activities-list">
      {% for activity in site.data.publications.academic_activities %}
      <div class="activity-item">
        <div class="activity-header">
          <h3>{{ activity.activity }}</h3>
          <span class="year">{{ activity.year }}</span>
        </div>
        {% if activity.title %}
        <div class="activity-title">
          <strong>演讲题目：</strong>{{ activity.title }}
        </div>
        {% endif %}
        <div class="activity-description">
          {{ activity.description }}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>

  <!-- 获奖情况 -->
  <div class="awards-section">
    <h2><i class="fas fa-trophy"></i> 学术获奖</h2>
    <div class="awards-grid">
      {% for award in site.data.publications.awards_and_honors %}
      <div class="award-card">
        <div class="award-header">
          <h3>{{ award.name }}</h3>
          <span class="year">{{ award.year }}</span>
        </div>
        <div class="award-organization">
          <strong>颁发机构：</strong>{{ award.organization }}
        </div>
        <div class="award-description">
          {{ award.description }}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>

<style>
.publications-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.publications-container h2 {
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 30px;
}

.publications-container h2 i {
  margin-right: 10px;
  color: #3498db;
}

/* 论文卡片样式 */
.publication-card {
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  padding: 25px;
  margin-bottom: 25px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.publication-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

.publication-header h3 {
  margin: 0 0 15px 0;
  color: #2c3e50;
  font-size: 1.3em;
  line-height: 1.4;
}

.publication-meta {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.status {
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.85em;
  font-weight: 500;
}

.status-published {
  background: #d4edda;
  color: #155724;
}

.status-reviewing {
  background: #fff3cd;
  color: #856404;
}

.status-preparing {
  background: #d1ecf1;
  color: #0c5460;
}

.type {
  background: #e9ecef;
  color: #495057;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.85em;
}

.year {
  background: #3498db;
  color: white;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 0.85em;
}

.publication-body > div {
  margin-bottom: 15px;
}

.authors .author-highlight {
  font-weight: bold;
  color: #3498db;
}

.authors .author {
  color: #2c3e50;
}

.abstract {
  background: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  border-left: 4px solid #3498db;
}

.abstract h5 {
  margin: 0 0 10px 0;
  color: #2c3e50;
  font-size: 1em;
  display: flex;
  align-items: center;
  gap: 8px;
}

.abstract h5 i {
  color: #3498db;
}

.abstract p {
  margin: 0;
  line-height: 1.6;
  text-align: justify;
}

.keywords {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
}

.keyword-tag {
  background: #e3f2fd;
  color: #1976d2;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 0.85em;
}

.publication-stats {
  display: flex;
  align-items: center;
  gap: 15px;
}

.citation-count {
  color: #27ae60;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 5px;
}

.publication-links {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.btn-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9em;
  transition: background-color 0.2s ease;
}

.btn-link.pdf {
  background: #e74c3c;
  color: white;
}

.btn-link.pdf:hover {
  background: #c0392b;
  color: white;
  text-decoration: none;
}

.btn-link.doi {
  background: #9b59b6;
  color: white;
}

.btn-link.doi:hover {
  background: #8e44ad;
  color: white;
  text-decoration: none;
}

/* 研究兴趣样式 */
.interests-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.interest-card {
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.interest-card h3 {
  margin: 0 0 10px 0;
  color: #2c3e50;
  font-size: 1.1em;
}

.interest-card p {
  margin-bottom: 15px;
  line-height: 1.6;
  color: #555;
}

.interest-keywords {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.interest-tag {
  background: #f1c40f;
  color: #f39c12;
  background: #fff3cd;
  color: #856404;
  padding: 3px 8px;
  border-radius: 10px;
  font-size: 0.8em;
}

/* 学术活动样式 */
.activity-item {
  background: #ffffff;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.activity-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.activity-header h3 {
  margin: 0;
  color: #2c3e50;
  font-size: 1.1em;
}

.activity-title {
  margin-bottom: 10px;
  color: #555;
}

.activity-description {
  line-height: 1.6;
  color: #666;
}

/* 获奖情况样式 */
.awards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.award-card {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.award-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.award-header h3 {
  margin: 0;
  font-size: 1.1em;
}

.award-card .year {
  background: rgba(255,255,255,0.2);
  backdrop-filter: blur(10px);
}

.award-organization {
  margin-bottom: 10px;
  opacity: 0.9;
}

.award-description {
  line-height: 1.6;
  opacity: 0.9;
}

@media (max-width: 768px) {
  .publication-meta {
    flex-direction: column;
    gap: 8px;
  }
  
  .activity-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  
  .award-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  
  .interests-grid, .awards-grid {
    grid-template-columns: 1fr;
  }
  
  .publication-links {
    flex-direction: column;
  }
  
  .btn-link {
    text-align: center;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .publications-container {
    padding: 15px;
  }
  
  .publication-card, .interest-card, .activity-item, .award-card {
    padding: 15px;
  }
}
</style>