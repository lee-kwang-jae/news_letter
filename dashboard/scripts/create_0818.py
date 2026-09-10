import re
import os

with open('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260817.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('2026년 8월 17일 발행', '2026년 8월 18일 발행')
content = content.replace('19호', '20호')
content = content.replace('2026.08.17', '2026.08.18')

new_articles = """<!-- 기사 1 -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.18 | 현장소식</div>
<h3>[전당대회를 마치며]</h3>
<div class="summary">
전당대회가 끝났습니다. 이번 대회의 주인공은 끝까지 경선을 지켜보고 참여해주신 당원 여러분입니다. 모든 후보의 약속인 '유능한 민주당'을 만들기 위해, 이제부터는 국민의 삶의 문제를 풀어주는 정당으로 거듭나겠습니다. 무거운 책임감을 안고 함께 이루어 나갑시다.
</div>
</div>
<!-- 기사 2 -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.18 | 현장소식</div>
<h3>[함께 만들어가는 새로운 하남]</h3>
<div class="summary">
하남은 녹지와 발전이 어우러지는 친환경 자족형 도시로 다시 태어납니다. 위례 성남골프장이 주택공급 대책에서 제외되었고, 3·9호선 등 철도망 확보와 교산신도시 추진에 속도를 내고 있습니다. 연구시설·기업 유치와 더불어 '생계조합' 입법 및 '집값 조정' 제도를 정비해 주민의 일자리와 주거 안정을 지키고 원도심 경제를 살리겠습니다.
</div>
</div>
<!-- 기사 3 -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.betanews.net/article/view/beta202608160005" target="_blank" style="color: inherit; text-decoration: none;">[김진명 경기도의원, 이광재 국회 예결위원장 만나 “운중동·대장동 교통난 대안은 경기남부광역철도뿐” 촉구]</a></h3>
<div class="summary">
김진명 더불어민주당 분당갑 지역위원장 겸 경기도의원이 이광재 국회 예산결산특별위원장을 만나 경기남부광역철도의 제5차 국가철도망 구축계획 반영을 위한 국회 차원의 협조를 요청했습니다. 김 의원은 서판교와 남판교 지역의 심각한 교통 문제를 해결하기 위해 경기남부광역철도가 유일한 대안임을 강조했습니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.betanews.net/article/view/beta202608160005" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 →</a></div>
</div>
<!-- 기사 4 -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.daejonilbo.com/news/articleView.html?idxno=2294907" target="_blank" style="color: inherit; text-decoration: none;">[세종시, 이광재 예결위원장 등 정치권 만나 '행정수도특별법' 연내 처리 총력 입법전]</a></h3>
<div class="summary">
행정수도특별법의 연내 국회 처리를 위해 세종시가 전국을 상대로 한 입법전에 뛰어들었습니다. 조상호 세종시장이 전국 시·도지사들에게 특별법 지지를 요청하고 이광재 국회 예결위원장 등 여야 정치권을 잇따라 만나며 9월 정기국회를 겨냥한 입법 지원을 촉구하고 있습니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.daejonilbo.com/news/articleView.html?idxno=2294907" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 →</a></div>
</div>"""

content = re.sub(r'(?s)<!-- 기사 1 -->.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)', new_articles + '\n', content)

new_local_news = """<!-- 지역 뉴스 기사 1 -->
<div class="article-card">
<div class="badge">📰 시정/행정</div>
<h3>하남도시공사 사장 재임용 논란, 시의회와 집행부 대립각</h3>
<div class="summary">
하남도시공사 사장 재임용을 둘러싸고 시의회와 하남시 집행부 간 갈등이 심화되고 있습니다. 시의회 일부 의원들은 절차적 문제와 무책임한 인사를 지적하며 강하게 비판하고 나섰으나, 하남시 측은 관계 법령과 내규에 따른 적법한 인사라며 반박해 논란이 계속되고 있습니다.
</div>
<div class="source">
📌 출처: 지역언론 종합
</div>
</div>

<!-- 지역 뉴스 기사 2 -->
<div class="article-card">
<div class="badge">📰 지역 경제</div>
<h3>하남시, 점심시간 주정차 단속 유예 시간 대폭 연장</h3>
<div class="summary">
지역 상권 활성화와 시민 편의 증진을 위해 하남시가 점심시간대 불법 주정차 단속 유예 시간을 기존보다 1시간 30분 늘렸습니다. 이에 따라 단속 유예 시간은 오전 11시부터 오후 3시까지 총 4시간으로 확대 적용되며, 지역 상인들과 시민들로부터 큰 호응을 얻고 있습니다.
</div>
<div class="source">
📌 출처: 하남시청 보도자료
</div>
</div>

<!-- 지역 뉴스 기사 3 -->
<div class="article-card">
<div class="badge">📰 교육/복지</div>
<h3>하남시 '성년 축하금 지원 조례안' 시의회 상임위 통과</h3>
<div class="summary">
새롭게 성년을 맞이하는 청년들을 응원하기 위한 '하남시 성년 축하금 지원 조례안'이 하남시의회 상임위원회를 통과했습니다. 이 조례안이 본회의를 최종 통과할 경우, 하남시 청년들은 성년이 되는 해에 지역화폐 등으로 소정의 축하금을 지원받을 수 있게 될 전망입니다.
</div>
<div class="source">
📌 출처: 하남시의회
</div>
</div>"""

content = re.sub(r'(?s)(<div class="section-title green">📰 하남 지역 주요 뉴스</div>\s*).*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 6: 하남 맘카페 HOT 이슈 TOP 3 ===== -->)', r'\1' + new_local_news + '\n', content)

new_mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 점심시간 주정차 단속 유예 시간 4시간으로 연장 환영 (미사맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 하남시가 8월 14일부터 점심시간 불법 주정차 단속 유예를 오전 11시부터 오후 3시까지 총 4시간으로 대폭 연장했습니다.</div>
<div class="mom-point">💡 주민 포인트: 점심시간에 식당가나 상가를 방문할 때 주차 스트레스가 크게 줄어들고 여유로운 일처리가 가능해졌습니다.</div>
<div class="mom-reaction">💬 주민 반응: "아이들 하원 전에 여유롭게 점심 먹고 장보기 너무 좋아졌어요", "주차비 부담도 덜고 상권도 살아나길 기대합니다" 등 환영하는 분위기입니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 하남시 '성년 축하금 지원 조례안' 상임위 통과 기대감 (위례맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 지역 청년들을 위해 성년이 되는 해에 축하금을 지원하는 조례안이 시의회 상임위를 통과해 본회의를 앞두고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 곧 성년이 되는 자녀를 둔 학부모들에게 지역화폐로 지급되는 축하금은 작지만 의미 있는 선물이 될 것입니다.</div>
<div class="mom-reaction">💬 주민 반응: "내년에 스무 살 되는 우리 아이도 받을 수 있겠네요!", "청년들을 위한 좋은 정책들이 더 많아졌으면 좋겠습니다"라며 긍정적인 반응을 보이고 있습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 연일 계속되는 폭염, 보육기관 야외활동 자제 현황 공유 (감일맘/미사맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 전국적인 폭염 경보가 며칠째 이어지면서, 지역 맘카페에서는 유치원과 어린이집의 야외활동 자제 및 실내 활동 현황을 공유하고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 아이들의 온열질환 예방이 최우선인 만큼, 안전하게 실내 활동 위주로 전환된 보육 기관들의 대처를 서로 확인하고 있습니다.</div>
<div class="mom-reaction">💬 주민 반응: "선생님들이 실내에서 재미있게 놀아주셔서 다행이에요", "이번 주말엔 아이들과 갈만한 시원한 실내 공간 추천해주세요"라며 안전과 놀거리를 공유하고 있습니다.</div>
</div>"""

content = re.sub(r'(?s)(<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\s*).*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 4: 네이버 인기 뉴스 Top 5 ===== -->)', r'\1\n' + new_mom_cafe_issues + '\n', content)

content = re.sub(r'(?s)(<div class="section-title orange">🔥 네이버 하남 관련 인기 뉴스 Top 5</div>\s*)<ul class="news-list">.*?</ul>', r'\1' + new_naver_news, content)

new_culture = """<div class="event-grid">
<div class="event-card">
<strong>[문화/전시] 한·불수교 140주년 기념 하남 아트 페스티벌 개최</strong>
<p>기간: 2026.08.21 ~ 08.27<br/>내용: 하남문화예술회관에서 한·불수교 140주년을 기념하는 특별 전시와 공연이 열립니다. 프랑스 작가들의 미디어아트 전시와 샹송 콘서트 등 다채로운 문화 행사를 시민 누구나 무료로 즐길 수 있습니다.</p>
</div>
<div class="event-card">
<strong>[체육/행사] 제5회 하남 미사강변 가족 걷기대회 참가자 모집</strong>
<p>접수 기간: 2026.08.18 ~ 08.31<br/>내용: 다가오는 초가을을 맞아 미사경정공원 일대에서 가족 걷기대회가 개최됩니다. 하남 시민이면 누구나 참가 신청이 가능하며, 완주 시 소정의 기념품과 지역 특산물 교환권이 제공됩니다.</p>
</div>
<div class="event-card">
<strong>[교육/강좌] 하남시립도서관 하반기 '달빛 인문학' 수강생 모집</strong>
<p>접수 기간: 2026.08.19 ~ 선착순 마감<br/>내용: 직장인과 학생을 위해 평일 저녁 시간에 진행되는 야간 인문학 강좌가 신장 및 미사도서관에서 개설됩니다. 문학, 역사 등 다양한 주제로 진행되며 도서관 홈페이지에서 신청할 수 있습니다.</p>
</div>
</div>"""

content = re.sub(r'(?s)(<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">한눈에 보는 하남시 문화·체육·축제 가이드</p>\s*)<div class="event-grid">.*?</div>\s*(?=</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)', r'\1' + new_culture + '\n', content)

new_public_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 공지사항 | 2026.08.18</div>
<h3>[하남시청] 하반기 지역공동체 일자리 사업 참여자 추가 모집</h3>
<div class="summary">
하남시청은 취약계층의 생계 안정과 지역 경제 활성화를 위해 '하반기 지역공동체 일자리 사업' 참여자를 추가 모집합니다. 근로 능력이 있는 만 18세 이상 하남 시민이라면 누구나 지원 가능하며, 선발된 인원은 9월부터 지역 환경 정비 및 공공 서비스 지원 업무에 투입됩니다.
</div>
<div class="source">
📌 출처: 하남시청 홈페이지 공고
</div>
</div>
<!-- 기사 2 -->
<div class="article-card">
<div class="badge">🏛️ 하남도시공사 | 2026.08.18</div>
<h3>[하남도시공사] 교산신도시 기업 이전 대책 마련 공청회 개최</h3>
<div class="summary">
하남도시공사는 교산신도시 조성에 따른 기존 입주 기업들의 안정적인 이전과 재정착을 돕기 위해 오는 8월 25일 공청회를 개최합니다. 이전 부지 조성 계획 및 세부 지원 대책을 안내하고 기업인들의 애로사항과 의견을 적극적으로 수렴할 계획입니다.
</div>
<div class="source">
📌 출처: 하남도시공사 보도자료
</div>
</div>
<!-- 기사 3 -->
<div class="article-card">
<div class="badge">🏛️ 하남소방서 | 2026.08.18</div>
<h3>[하남소방서] 추석 명절 대비 다중이용시설 화재 예방 특별 점검</h3>
<div class="summary">
하남소방서는 다가오는 추석 명절을 앞두고 대형 마트, 전통시장 등 시민들의 발길이 잦은 다중이용시설을 대상으로 화재 예방 특별 점검에 돌입합니다. 소방 설비 정상 작동 여부 및 피난로 확보 상태 등을 집중 점검하여 안전한 명절 환경 조성에 만전을 기할 예정입니다.
</div>
<div class="source">
📌 출처: 하남소방서 안전공지
</div>
</div>"""

content = re.sub(r'(?s)(<div class="section-title purple">🏛️ 공공기관 소식지</div>\s*).*?(?=</div>\s*<div class="bottom-nav")', r'\1\n' + new_public_news + '\n', content)

with open('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260818.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created 0818.html successfully.")
