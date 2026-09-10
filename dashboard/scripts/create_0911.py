import os
import re

source_path = 'dashboard/news/kj_hanam_inside_20260910.html'
target_path = 'dashboard/news/kj_hanam_inside_20260911.html'
news_index_path = 'dashboard/news/index.html'
root_index_path = 'index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Title, Issue and Date updates
content = content.replace("37호 | 2026년 9월 10일 발행", "38호 | 2026년 9월 11일 발행")
content = content.replace("2026년 9월 10일 기준", "2026년 9월 11일 기준")

# 2. Section 1: 우리동네 국회의원 이광재
section1_content = """<!-- ===== 섹션 1: 이광재 국회의원 언론보도 & 현장일지 ===== -->
<div id="lawmaker">
<div class="section-title" style="display: flex; align-items: center; justify-content: center; gap: 10px;">
  <img src="./images/kjicon.png" alt="이광재 국회의원" style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; vertical-align: middle;">
  <span>우리동네 국회의원 이광재</span>
</div>

<!-- 기사 1 (언론보도 - 연합뉴스: 추미애, 국회 예결위원장 만나 2천446억 국비 요청) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.yna.co.kr/view/AKR20260910062500061?input=1195m" target="_blank" style="color: inherit; text-decoration: none;">[의정/예산] 추미애 지사, 이광재 국회 예결위원장 만나 2천446억 국비 지원 요청</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
경기도가 국회 예산결산특별위원회 이광재 위원장을 찾아 교산 신도시 AI 클러스터 조성, 지분형 주택 확대, 주요 교통망 구축 등 하남시 핵심 현안 해결과 내년도 10개 사업 총 2,446억 원 규모의 국비 확보를 위한 차질 없는 국회 협력을 요청했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.yna.co.kr/view/AKR20260910062500061?input=1195m" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (연합뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 연합뉴스 (최찬흥 기자)
</div>
</div>

<!-- 기사 2 (언론보도 - 디지털타임스: 이광재 예결위원장 "국가예산, AI 미래투자·복지 안전망 균형있게 확보할 것") -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.dt.co.kr/article/12083341?ref=naver" target="_blank" style="color: inherit; text-decoration: none;">[인터뷰] 이광재 예결위원장 "국가예산, AI 미래투자·복지 안전망 균형있게 확보할 것"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
더불어민주당 이광재 국회의원(예산결산특별위원장, 경기 하남갑)이 인터뷰를 통해 하남시 AI 바이오 클러스터 자족도시 도약 추진과 교산 3·9호선 연장 및 위례 교통대책 등 미래 성장동력 투자를 위한 국가 예산 확보 구상과 의정 방향을 상세히 밝혔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.dt.co.kr/article/12083341?ref=naver" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (디지털타임스) →</a></div>
</div>
<div class="source">
📌 출처: 디지털타임스 (강현철 기획제작부장)
</div>
</div>

<!-- 기사 3 (현장일지 - 네이버 블로그: [호르무즈에서 북극항로까지, 대한민국의 신질서 국가전략은?]) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224407507634" target="_blank" style="color: inherit; text-decoration: none;">[대정부질문] "호르무즈에서 북극항로까지, 대한민국의 신질서 국가전략은?"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
오늘 외교·통일·안보 분야 대정부질문 발언을 통해 호르무즈 해협 안보부터 북극항로 개척까지 대한민국의 신질서 국가전략과 미래 해양·에너지 안보 대응 방안을 제시하고 정부의 과감한 추진을 촉구했습니다.
<div style="margin-top: 14px; text-align: center;">
  <img src="./images/thumbnail0911.jpg" alt="호르무즈에서 북극항로까지, 대한민국의 신질서 국가전략은?" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid #cbd5e0; cursor: pointer; display: block; margin: 0 auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="margin-top: 14px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224407507634" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>
</div>"""

content = re.sub(r'<div id="lawmaker">.*?</div>\n</div>\n<hr/>', section1_content + '\n<hr/>', content, flags=re.DOTALL)

# 3. Section 3: 하남 맘카페 HOT 이슈 (새로운 소식)
section3_content = """<!-- ===== 섹션 3: 하남 맘카페 HOT 이슈 ===== -->
<div id="mom-cafe">
<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>
<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 9월 11일 기준 하남 지역 인터넷 커뮤니티(맘카페)에서 가장 조회수와 댓글이 높았던 핫이슈 TOP 3 소식입니다.</p>

<div class="mom-issue-card">
<h4>1️⃣ 감일·위례 신도시 시내버스 및 마을버스 노선 증차 확정 소식에 맘카페 환호</h4>
<div class="mom-detail"><strong>현황:</strong> 감일 및 위례 신도시 주민들의 출퇴근 및 통학 불편 해소를 위해 주요 환승 거점 연결 시내버스 3개 노선 증차 및 마을버스 운행 횟수 대폭 확대 방안이 확정되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 출퇴근길 버스 대기시간 단축 및 지하철역 환승 편의 대폭 향상.</div>
<div class="mom-reaction">💬 주민 반응: "드디어 감일 노선 증차가 되는군요!", "아이들 학원 가고 등하교할 때 한결 수월해지겠어요" 감일·위례 맘카페 열띤 호응.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 하남 미사 한강공원 가을맞이 어린이 생태체험 및 힐링 주말 프로그램 신청 개시</h4>
<div class="mom-detail"><strong>현황:</strong> 미사 한강공원에서 가을철을 맞아 어린이와 학부모가 함께 참여하는 숲 체험, 야생화 관찰 및 주말 생태 교육 프로그램 선착순 접수가 시작되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 주말 아이들과 함께 멀리 나가지 않고 자연 속에서 즐기는 무료 생태체험활동.</div>
<div class="mom-reaction">💬 주민 반응: "주말에 아이들과 갈 만한 알찬 프로그램이 생겼네요!", "선착순 접수 바로 신청했습니다" 학부모 높은 관심.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 하남시 초·중·고 통학로 교통안전 시설(스마트 가온길·노란색 횡단보도) 전면 보강 소식</h4>
<div class="mom-detail"><strong>현황:</strong> 초등학교 및 중학교 주변 어린이 보호구역 내 바닥형 음성안내 보조장치 및 노란색 횡단보도 조성을 대폭 확대한다는 소식이 전해졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 등하굣길 스쿨존 안전사고 예방 및 학부모 안심 통학 환경 조성.</div>
<div class="mom-reaction">💬 주민 반응: "등하굣길 안전장치가 늘어나서 한시름 놓이네요", "우리 아이 학교 앞도 빨리 설치되면 좋겠습니다" 응원 댓글 속출.</div>
</div>
</div>"""

content = re.sub(r'<div id="mom-cafe">.*?</div>\n</div>\n\n<div id="culture">', section3_content + '\n\n<div id="culture">', content, flags=re.DOTALL)

# 4. Section 5: 공공기관 소식지 (새로운 소식)
section5_content = """<!-- ===== 섹션 5: 공공기관 소식지 ===== -->
<div id="public-news">
<div class="section-title purple">🏛️ 공공기관 소식지</div>

<!-- 신규: 청년 월세 한시 특별지원 2차 사업 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 | 2026.09</div>
<h3><a href="https://www.hanam.go.kr" target="_blank" style="color: inherit; text-decoration: none;">하남시 무주택 청년 주거비 지원 「청년 월세 한시 특별지원 2차」 신청 안내</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
하남시에서는 청년층의 주거비 부담 경감을 위해 월 최대 20만 원(최대 12회)의 월세를 지원하는 <b>『청년 월세 한시 특별지원 2차』</b> 사업 신청을 접수받고 있습니다.<br/><br/>
<b>지원 대상:</b> 만 19세 ~ 34세 이하 무주택 청년 (부모와 별도 거주하는 청년 독립 가구)<br/>
<b>지원 내용:</b> 실제 납부하는 임차료 범위 내 월 최대 20만 원(최대 12개월) 지급<br/>
<b>소득·재산 기준:</b> 청년가구 중위소득 60% 이하 및 원가구 중위소득 100% 이하 등<br/>
<b>신청 방법:</b> 복지로 홈페이지(<a href="https://www.bokjiro.go.kr" target="_blank" style="color:#3182ce; font-weight:bold;">bokjiro.go.kr</a>) 온라인 신청 또는 주소지 관할 행정복지센터 방문 접수<br/>
<b>문의:</b> 하남시청 청년이룸 삶지원팀 <a href="tel:031-790-5114" style="color:#3182ce; font-weight:bold;">031-790-5114</a>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.hanam.go.kr" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">공고문 자세히 보기 (하남시청) →</a></div>
</div>
<div class="source">
📌 출처: 하남시청 / 국토교통부
</div>
</div>
</div>"""

content = re.sub(r'<div id="public-news">.*?</div>\n</div>\n\n\n\n\n\n<!-- 하단', section5_content + '\n\n<!-- 하단', content, flags=re.DOTALL)

# Write to target_path
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Created {target_path}")

# Write to news_index_path & root_index_path
with open(news_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {news_index_path}")

with open(root_index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Updated {root_index_path}")
