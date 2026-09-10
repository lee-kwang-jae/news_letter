import re
import os

with open('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260818.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('2026년 8월 18일 발행', '2026년 8월 19일 발행')
content = content.replace('20호', '21호')
content = content.replace('2026.08.18', '2026.08.19')

import re
# Remove the SECTION 1 and 2 overview block
overview_pattern = r'\s*<div style="background-color: #f8fafc; padding: 20px; border-radius: 8px; margin-top: 15px; margin-bottom: 25px; border: 1px solid #e2e8f0; color: #334155; line-height: 1.6; font-size: 0.95rem;">\s*<div style="font-weight: bold; color: #1e293b; margin-bottom: 8px; font-size: 1.05rem;">SECTION 1 : 현장소식</div>.*?</div>\s*</div>'
content = re.sub(overview_pattern, '', content, flags=re.DOTALL)

# Increase overall font size by 1px
content = content.replace('<style>', '<style>\n        html {\n            font-size: 17px;\n        }')

new_articles = """<!-- 기사 1 -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.19 | 현장소식</div>
<h3>[하남 광역버스 개선을 위한 간담회 개최 및 의견 수렴]</h3>
<div class="summary">
<img src="./images/bus_poster.png" alt="하남 광역버스 교통 대책 간담회 포스터" style="max-width: 160px; height: auto; float: left; margin: 5px 15px 5px 0; border-radius: 8px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
이번 주 금요일 오전 10시 30분, 「하남 광역버스 교통 대책 간담회」를 개최합니다. 하남시민 여러분이 겪고 계신 광역버스 불편을 직접 듣고, 실질적인 해결책을 마련하겠습니다. 📌 간담회 전, 시민 여러분의 의견을 받고 있습니다. 평소 광역버스를 이용하며 느끼셨던 불편이나 개선 의견을 자유롭게 남겨주세요. 여러분의 의견을 간담회에서 꼼꼼히 챙기겠습니다.<br><br>📍 의견 제출: 포스터 QR코드 또는 <a href="https://docs.google.com/forms/d/e/1FAIpQLSdf2GIkBSLSAHE9-H7URsTSgELCQqkIxcmeM74pVmplTeZChQ/viewform?usp=dialog" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: underline;">[설문조사 링크]</a><br>📺 현장 참석이 어려우신 분들은 유튜브 생중계로 함께해 주세요.<br>하남 주민 여러분의 많은 관심과 참여 부탁드립니다.
<div style="margin-top: 10px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224382386343" target="_blank" style="color: #718096; text-decoration: underline;">[출처] 하남 광역버스 개선을 위한 주민 여러분의 의견을 듣습니다🚌 | 작성자 이광재</a></div>
</div>
</div>
<!-- 기사 2 -->
<div class="article-card card-field">
<div class="badge badge-field">📰 2026.08.19 | 현장소식</div>
<h3>[8월 2주차 의정활동 보고]</h3>
<div class="summary">
안녕하세요, 우리동네 국회의원 이광재입니다. 하남시민 여러분을 위해 발로 뛴 8월 둘째 주 의정활동 소식을 전해드립니다. 지역 현안 해결을 위한 간담회부터 국회에서의 주요 입법 활동까지, 주민 여러분의 더 나은 내일을 위해 치열하게 고민하고 행동했습니다. 아래 버튼을 눌러 자세한 주간 활동 내역을 확인해 보세요.
</div>
<div style="margin-top: 15px; text-align: center;">
<a href="https://blog.naver.com/lee_kwang_jae/224382096966" target="_blank" style="display: inline-block; padding: 12px 24px; background: linear-gradient(135deg, #ff9900, #ff5e00); color: #ffffff; text-decoration: none; border-radius: 6px; font-weight: bold; width: 55%; box-sizing: border-box; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">🔍 8월 2주차 의정보고 자세히 보기 →</a>
</div>
</div>
<!-- 기사 3 -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.sisajournal-e.com/news/articleView.html?idxno=423104" target="_blank" style="color: inherit; text-decoration: none;">[[DX브리핑] KOSA, 국회에 피지컬AI 예산 지원 요청]</a></h3>
<div class="summary">
한국인공지능·소프트웨어산업협회(KOSA) 조준희 협회장이 이광재 예산결산특별위원장과 만나 3대 메가프로젝트 추진에 필요한 국회 차원의 예산 지원을 요청했습니다. 이광재 위원장은 "AI를 국가 주권의 관점에서 키워야 한다는 문제의식에 깊이 공감한다"며 예산 심의 과정에서 업계의 건의를 면밀히 살피겠다고 답했습니다.
</div>
<div style="margin-top: 10px;"><a href="https://www.sisajournal-e.com/news/articleView.html?idxno=423104" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 →</a></div>
</div>
<!-- 기사 4 -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://dgmbc.com/NewsArticle/857149" target="_blank" style="color: inherit; text-decoration: none;">[민주당 대구시당, 국회 예결특위위원장에 대구 국립뮤지컬콤플렉스 예타 선정 지원 요청]</a></h3>
<div class="summary">
박형룡 민주당 대구시당위원장 등이 국회를 방문해 이광재 예산결산특별위원장을 만나 대구 국립뮤지컬콤플렉스 조성 사업이 예비타당성조사 대상에 선정되도록 지원을 요청했습니다. 이광재 위원장은 "차별성 있는 시설 운영 방안 등을 첨부하면 긍정적으로 검토해 정부에 전달하겠다"고 밝혔습니다.
</div>
<div style="margin-top: 10px;"><a href="https://dgmbc.com/NewsArticle/857149" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 →</a></div>
</div>"""

content = re.sub(r'(?s)<!-- 기사 1 -->.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)', new_articles + '\n', content)

new_local_news = """<!-- 지역 뉴스 기사 4 -->
<div class="article-card">
<div class="badge">📰 환경/시정</div>
<h3>하남시, 반려견 목줄 미착용·배설물 방치 등 야간 단속 실시</h3>
<div class="summary" style="display: flex; align-items: center; gap: 15px;">
<img src="./images/hanam_dog.png" alt="하남시 반려견 야간 단속 이미지" style="max-width: 160px; height: auto; border-radius: 8px; border: 1px solid #e2e8f0; cursor: pointer; flex-shrink: 0;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
<div>하남시는 성숙한 반려동물 문화 정착과 민원 예방을 위해 오는 9월까지 동물보호법 위반 행위에 대한 야간 집중 단속을 실시합니다. 반려견 목줄(2m 이내) 및 인식표 미착용, 배설물 미수거 등을 중점 단속하며 위반 시 최대 60만 원의 과태료가 부과됩니다. 9~10월 동물등록 자진신고 기간도 함께 운영됩니다.</div>
</div>
<div class="source">
📌 출처: 하남시청 보도자료
</div>
</div>

<!-- 지역 뉴스 기사 5 -->
<div class="article-card">
<div class="badge">📰 부동산/시정</div>
<h3>하남시, 24개 법정동 녹지지역 '토지거래허가구역' 신규 지정</h3>
<div class="summary">
하남시는 국토교통부의 신규 주택공급 후보지 투기 방지 대책에 따라 관내 자연녹지지역 전역이 토지거래허가구역으로 신규 지정됐다고 밝혔습니다. 이번 지정은 공공주택지구 주변 지역의 지가 상승을 억제하고 투기성 토지 거래를 사전에 차단하기 위한 조치로, 하남시 관내 24개 법정동이 대상에 포함됩니다.
</div>
<div class="source">
📌 출처: 누리일보
</div>
</div>

<!-- 지역 뉴스 기사 6 -->
<div class="article-card">
<div class="badge">📰 치안/시정</div>
<h3>하남시, 체납차량 번호판 영치 24일 일제단속 실시</h3>
<div class="summary">
하남시는 오는 24일 자동차세 2회 이상 체납 또는 체납액 30만 원 이상인 체납차량 15,250대(체납액 16.2억 원)를 대상으로 경찰과 협업하여 번호판 영치 일제단속에 들어갑니다. 이번 단속은 다수 체납자 거주지와 복합쇼핑몰, 지식산업센터 등 차량 밀집지역을 중심 타깃으로 집중 실시됩니다.
</div>
<div class="source">
📌 출처: 시티뉴스 | <a href="https://m.ctnews.co.kr/40721" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 →</a>
</div>
</div>"""

content = re.sub(r'(?s)(<div class="section-title green">📰 하남 지역 주요 뉴스</div>\s*).*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 6: 하남 맘카페 HOT 이슈 TOP 3 ===== -->)', r'\1' + new_local_news + '\n', content)

new_mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 하남시 8월 물놀이장(미사호수공원·종합운동장 등) 막바지 피서 인기 (미사맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 극심한 폭염 속에서 하남시 관내 무료 야외 물놀이장(미사호수공원, 하남종합운동장, 백제어린이공원 등)이 주말 및 방학 피서지로 큰 인기를 끌고 있습니다.</div>
<div class="mom-point">💡 주민 포인트: 무더위 속 아이들과 함께 가성비 높은 물놀이를 즐기기 위한 개장 시간, 주차 팁, 쉼터 명당 자리가 실시간으로 공유되고 있습니다.</div>
<div class="mom-reaction">💬 주민 반응: "미사호수공원 물놀이장 아침 오픈런 필수네요!", "수질 관리도 잘 되어 있고 안전요원분들 계셔서 아이와 가기 좋습니다"라며 호평이 이어지고 있습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 위례복합체육센터 8월 정식 개관 "수영·아이돌봄 신청 문의 폭주" (위례맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 13일 위례지구 내 실내수영장과 유아/어린이 체육관, 아이돌봄센터를 갖춘 '위례복합체육센터'가 정식 개관하여 본격 운영에 들어갔습니다.</div>
<div class="mom-point">💡 주민 포인트: 신도시 내 부족했던 영유아·어린이 수영 교실과 다목적 돌봄 공간이 확충되어 맘카페 내 강좌 수강 신청 팁이 빠르게 공유되고 있습니다.</div>
<div class="mom-reaction">💬 주민 반응: "어린이 수영장 수강신청 첫날부터 오픈런 해야겠어요", "돌봄센터랑 체육시설이 붙어 있어 최고입니다"라며 큰 반응을 얻고 있습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 하남 24개 법정동 녹지 '토지거래허가구역' 신규 지정 이슈 (감일맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 18일부터 국토부 투기 방지 대책으로 하남시 관내 자연녹지지역 전역이 토지거래허가구역으로 전격 신규 지정되었습니다.</div>
<div class="mom-point">💡 주민 포인트: 기획부동산 투기 사전 차단에 대한 긍정적 평가와 함께 실거주 주택 거래 및 교산·감일 주변 개발 영향에 대해 관심이 쏠렸습니다.</div>
<div class="mom-reaction">💬 주민 반응: "난개발 방지에는 도움 되겠네요", "감일·초이 일대 대출이나 매매에 영향은 없는지 정보 공유 부탁드려요" 등 활발한 토론이 펼쳐졌습니다.</div>
</div>"""

content = re.sub(r'(?s)(<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\s*).*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 4: 네이버 인기 뉴스 Top 5 ===== -->)', r'\1\n' + new_mom_cafe_issues + '\n', content)

content = re.sub(r'(?s)(<div class="section-title orange">🔥 네이버 하남 관련 인기 뉴스 Top 5</div>\s*)<ul class="news-list">.*?</ul>', r'\1' + new_naver_news, content)

new_culture = """<div class="event-grid">
<div class="event-card">
<strong>[전시/체험] 하남역사박물관 가을 특별전 '하남의 기억을 걷다'</strong>
<p>기간: 2026.08.25 ~ 10.31<br/>내용: 하남의 과거와 현재를 조명하는 가을 특별 전시가 열립니다. 미사리 유적부터 현대 신도시 개발까지 하남의 변천사를 한눈에 볼 수 있는 다채로운 사진과 유물이 전시됩니다.</p>
</div>
<div class="event-card">
<strong>[공연/행사] 미사호수공원 주말 야외 버스킹 '별빛 선율'</strong>
<p>일시: 8월 넷째 주~9월 둘째 주 매주 토/일 저녁 7시<br/>내용: 선선해진 저녁, 미사호수공원 수변 무대에서 지역 예술인들이 참여하는 다채로운 버스킹 공연이 펼쳐집니다. 어쿠스틱 밴드, 마술 쇼 등 온 가족이 즐길 수 있는 무대가 마련됩니다.</p>
</div>
<div class="event-card">
<strong>[공연/예술] 하남문화예술회관 기획 가족 뮤지컬 '정글북'</strong>
<p>일시: 2026.08.29 ~ 08.30<br/>내용: 화려한 무대 연출과 역동적인 안무가 돋보이는 명작 가족 뮤지컬 '정글북'이 하남을 찾아옵니다. 하남 시민 대상 특별 할인 혜택이 제공되며, 예매는 문화예술회관 홈페이지에서 가능합니다.</p>
</div>
</div>"""

content = re.sub(r'(?s)(<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">한눈에 보는 하남시 문화·체육·축제 가이드</p>\s*)<div class="event-grid">.*?</div>\s*(?=</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)', r'\1' + new_culture + '\n', content)

new_public_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시청 공지사항 | 2026.08.19</div>
<h3>[하남시청] 2026년 하반기 청년 창업 지원금 사업 참여자 모집</h3>
<div class="summary">
하남시는 지역 청년들의 참신한 아이디어 발굴과 초기 창업의 어려움을 돕기 위해 하반기 창업 지원금 사업 참여자를 모집합니다. 선발된 청년 창업가에게는 최대 1,000만 원의 사업화 자금과 맞춤형 컨설팅이 지원됩니다.
</div>
<div class="source">
📌 출처: 하남시청 홈페이지 공고
</div>
</div>
<!-- 기사 3 -->
<div class="article-card">
<div class="badge">🏛️ 하남경찰서 | 2026.08.19</div>
<h3>[하남경찰서] 2학기 개학 맞이 스쿨존 교통안전 집중 캠페인 전개</h3>
<div class="summary">
하남경찰서는 초등학교 2학기 개학 시즌을 맞아 어린이 보호구역(스쿨존) 내 교통사고 예방을 위한 집중 캠페인과 불법 주정차 특별 단속을 실시합니다. 운전자들의 각별한 주의와 서행 운전을 당부드립니다.
</div>
<div class="source">
📌 출처: 하남경찰서 보도자료
</div>
</div>

<!-- 기사 4 -->
<div class="article-card">
<div class="badge">🏛️ 하남시보건소 | 2026.08.19</div>
<h3>[하남시보건소] 2026년 걷기 프로그램 '하남 88워킹 2기' 참가자 모집</h3>
<div class="summary" style="display: flex; align-items: center; gap: 15px;">
<img src="https://www.hanam.go.kr/DATA/bbs/109/20260811034702145_KUah.jpg" alt="하남 88워킹 2기 포스터" style="max-width: 150px; height: auto; border-radius: 8px; border: 1px solid #e2e8f0; cursor: pointer; flex-shrink: 0;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
<div>
하남시보건소(건강증진과)에서 60세 이상 어르신을 대상으로 주 1회, 총 8주간 진행되는 걷기 프로그램 '하남 88워킹 2기' 참가자를 모집합니다.<br><br>
• <strong>모집기간</strong>: 2026. 8. 18.(화) 09:00 ~ 8. 26.(수) 17:00 (선착순 전화 모집 ☎ 031-790-6436)<br>
• <strong>모집대상</strong>: 60세 이상 하남시민 구역별 20명<br>
• <strong>운영장소 및 일정</strong>: 감일동 수변 산책로(매주 화 10:00~11:30) / 신장동 덕풍천 산책로(매주 목 10:00~11:30)
</div>
</div>
<div class="source">
📌 출처: 하남시보건소 (건강증진과)
</div>
</div>"""

content = re.sub(r'(?s)(<div class="section-title purple">🏛️ 공공기관 소식지</div>\s*).*?(?=</div>\s*<div class="bottom-nav")', r'\1\n' + new_public_news + '\n', content)

modal_code = """
<!-- 이미지 팝업 모달 -->
<div id="imageModal" style="display:none; position:fixed; z-index:9999; left:0; top:0; width:100%; height:100%; background-color:rgba(0,0,0,0.8); text-align:center; flex-direction:column; justify-content:center; align-items:center;" onclick="this.style.display='none'">
    <img id="modalImage" src="" style="max-width:90%; max-height:90%; border-radius:8px; box-shadow:0 4px 20px rgba(0,0,0,0.5);">
    <span style="color:white; margin-top:15px; font-size:1.1rem; cursor:pointer;">닫기 (아무 곳이나 클릭하세요)</span>
</div>
<script>
function openImageModal(src) {
    document.getElementById('imageModal').style.display = 'flex';
    document.getElementById('modalImage').src = src;
}
</script>
</body>"""
content = content.replace('</body>', modal_code)

with open('d:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260819.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Created 0819.html successfully.")
