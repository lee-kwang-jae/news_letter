import os
import re

source_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260827.html'
target_path = 'd:/github/newsletter/newsletter/dashboard/news/kj_hanam_inside_20260828.html'
index_path = 'd:/github/newsletter/newsletter/dashboard/news/index.html'

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Date and Issue number updates
content = content.replace("KJ's 하남 인사이드 - 2026년 8월 27일", "KJ's 하남 인사이드 - 2026년 8월 28일")
content = content.replace('27호 | 2026년 8월 27일 발행', '28호 | 2026년 8월 28일 발행')
content = content.replace('📅 발행일: 2026년 8월 27일', '📅 발행일: 2026년 8월 28일')

# Remove weather widget HTML and weather script if any remnant
content = re.sub(r'(?s)<!-- 실시간 날씨 위젯 -->\s*<div class="weather-widget" id="weather-widget">.*?</div>', '', content)
content = re.sub(r'(?s)<!-- 실시간 날씨 데이터 Fetch 스크립트 -->\s*<script>.*?</script>', '', content)

# Section 1: 우리동네 국회의원 이광재
lawmaker_articles = """<!-- 기사 1 (언론보도 - 뉴스1) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.news1.kr/politics/assembly/6271892" target="_blank" style="color: inherit; text-decoration: none;">이광재, 임대주택 분쟁조정 '당사자 참석' 보장 법안 발의</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
이광재 더불어민주당 국회의원(경기 하남시갑, 국회 예산결산특별위원장)이 공공·민간 임대주택 분쟁 조정의 실효성을 획기적으로 높이기 위한 「민간 임대주택에 관한 특별법 일부개정법률안」을 대표 발의했습니다. 임대주택 분쟁조정위원회 개최 시 임차인과 사업자 등 분쟁 당사자의 출석 및 의견 진술권을 법적으로 실질 보장하고, 서면 위주나 사업자 편향 조정을 방지하여 갈등을 공정하게 중재하도록 제도적 장치를 마련했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.news1.kr/politics/assembly/6271892" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (뉴스1) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0828_kj_01.jpg" alt="이광재 의원 임대주택 분쟁조정 당사자 참석 보장 법안 발의" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>

<!-- 기사 2 (언론보도 - 지디넷코리아) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://zdnet.co.kr/view/?no=20260827131712" target="_blank" style="color: inherit; text-decoration: none;">[이광재 칼럼] 문화에 투자하라 - 한류를 대한민국의 자산으로 만드는 법</a></h3>
<div class="summary flex-summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="flex: 1;">
국회 예산결산특별위원장 이광재 의원이 ZDNet Korea 칼럼을 통해 대한민국 미래 투자 핵심 인프라로 '문화 콘텐츠'를 제시했습니다. 이 의원은 K-콘텐츠가 세계인의 호응과 신뢰를 먼저 구축하면 K-푸드, 화장품, 패션을 거쳐 첨단 기술과 제도·표준으로 확산되는 '신뢰의 사다리' 수출 모델을 구상하며, 콘텐츠 투자는 단순 지원이 아닌 국가 브랜드를 만드는 강력한 산업 투자임을 강조했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://zdnet.co.kr/view/?no=20260827131712" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (지디넷코리아) →</a></div>
</div>
<div class="img-box" style="width: 240px; flex-shrink: 0;">
<img src="./images/0828_kj_02.jpg" alt="[이광재 칼럼] 문화에 투자하라" style="width: 100%; height: 170px; object-fit: cover; border-radius: 12px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
<div class="source">
📌 출처: 지디넷코리아
</div>
</div>

<!-- 기사 3 (언론보도 - 강원도민일보) -->
<div class="article-card card-press">
<div class="badge badge-press">📰 언론보도</div>
<h3><a href="https://www.kado.net/news/articleView.html?idxno=2069020" target="_blank" style="color: inherit; text-decoration: none;">이광재 국회의원, 불확실성 가중 시대 '정책제안서' 『국민을 부자로 만드는 나라』 발간</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 의원이 미래 국가 비전과 국민 삶의 실질적 개선을 담은 신간 『국민을 부자로 만드는 나라』를 출간했습니다. 책에서는 출생 시 국가 1억 원 지원을 시드머니로 만 20세 청년 마중물 1억 원 지급 및 65세 시 60억 원 규모 노후 자산을 운용하는 '미래펀드' 구상을 비롯해 일자리·주거·의료·재정 등 40대 실용주의 정책 과제를 구체적으로 다루고 있습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.kado.net/news/articleView.html?idxno=2069020" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (강원도민일보) →</a></div>
</div>
<div class="source">
📌 출처: 강원도민일보
</div>
</div>

<!-- 기사 4 (현장일지 - 네이버 블로그) -->
<div class="article-card card-field">
<div class="badge badge-field">📝 현장일지</div>
<h3><a href="https://blog.naver.com/lee_kwang_jae/224392350500" target="_blank" style="color: inherit; text-decoration: none;">[현장일지] "하남을 위해, 하루를 꽉 채웠습니다"</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
이광재 국회의원이 하남 지역 현안 해결과 민생 소통을 위해 하루 동안 소상공인연합회 간담회, 학부모폴리스·녹색어머니연합회 간담회, 하남경찰서 및 한국토지주택공사(LH) 현장 면담 등을 연속으로 가졌습니다. 지역 자영업자의 애로사항을 청취하고 어린이 안전 통학로 조성 및 교통·주거 인프라 개선을 위해 현장에서 직접 발로 뛰는 소통 행보를 이어갔습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://blog.naver.com/lee_kwang_jae/224392350500" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">현장일지 전문 보기 (이광재 블로그) →</a></div>
<div class="img-grid" style="display: flex; gap: 12px; margin-top: 14px;">
<div style="flex: 1;">
<img src="./images/0828_kj_03.jpg" alt="이광재 의원 하남 소통 현장일지 1" style="width: 100%; height: 160px; object-fit: cover; border-radius: 10px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
<div style="flex: 1;">
<img src="./images/0828kj_03.jpg" alt="이광재 의원 하남 소통 현장일지 2" style="width: 100%; height: 160px; object-fit: cover; border-radius: 10px; border: 1px solid #e2e8f0; cursor: pointer;" onclick="openImageModal(this.src)" title="클릭하여 원본 보기">
</div>
</div>
</div>
<div class="source">
📌 출처: 이광재 공식 네이버 블로그
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="lawmaker">\s*<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션 2: 하남 지역 주요 뉴스 ===== -->)',
    '<div id="lawmaker">\n<div class="section-title">🗣️ 우리동네 국회의원 이광재</div>\n' + lawmaker_articles + '\n',
    content
)

# Section 2: 하남 지역 주요 뉴스 (하남일보 부동산 및 하남타임즈 교육청 신설 기사 반영)
local_news_articles = """<!-- 지역 뉴스 기사 1 (교육/정책 - 2026.08.28 추가) -->
<div class="article-card">
<div class="badge">📰 교육/정책</div>
<h3><a href="https://www.joongboo.com/news/articleView.html?idxno=363734810" target="_blank" style="color: inherit; text-decoration: none;">광주하남교육지원청, 학생 주도 '폰 프리 스쿨(Phone-Free School)' 정책설명회 개최</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
광주하남교육지원청이 26일 학생·학부모·교직원 등 250여 명이 참석한 가운데 '2026 광주하남 학생 주도 폰 프리 스쿨 정책설명회'를 열었습니다. 단순한 사용 통제를 넘어 학생들이 스스로 스마트폰 이탈 시간을 독서·예술·체육(RAS) 활동으로 채우는 디지털 웰빙 프로젝트로, 이현재 하남시장 등 지자체와 연계해 지역 체육·문화 인프라를 전폭 지원합니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.joongboo.com/news/articleView.html?idxno=363734810" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (중부일보) →</a></div>
</div>
<div class="source">
📌 출처: 중부일보 (김지백·김동욱 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (교육/진로 - 2026.08.28 추가) -->
<div class="article-card">
<div class="badge">📰 교육/진로</div>
<h3><a href="https://www.vision21.kr/news/article.html?no=611839" target="_blank" style="color: inherit; text-decoration: none;">하남 감일고, 고1 대상 ‘2026 진로진학 로드맵 컨설팅’ 운영…고교학점제 맞춤 설계 집중 지원</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남 감일고등학교가 8월 25일과 27일 1학년 학생 160명과 학부모를 대상으로 ‘2026 진로진학 로드맵 컨설팅’을 개최했습니다. 고교학점제 전면 시행에 발맞춰 1:1 전문 컨설팅을 통해 성적 분석 및 희망 진로별 과목 선택, 대입 전형 준비 전략을 체계적으로 지원하여 학업 설계 능력과 대입 경쟁력을 대폭 강화했습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.vision21.kr/news/article.html?no=611839" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (비전21뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 비전21뉴스 (정서영 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (환경/상수도 - 2026.08.28 추가) -->
<div class="article-card">
<div class="badge">📰 환경/상수도</div>
<h3><a href="https://www.ctnews.co.kr/40746" target="_blank" style="color: inherit; text-decoration: none;">하남정수장 고도정수처리시설 준공…9월부터 신장·덕풍동 원도심 13만 명 고품질 수돗물 공급</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 총사업비 약 446.7억 원을 투입해 하남정수장 고도정수처리시설(1일 70,000톤 규모) 조성을 준공하고 오는 9월부터 본격 통수에 들어갑니다. 오존 처리 및 입상활성탄(숯) 여과 공정을 도입해 기존 표준 공정으로 완전 제거가 어렵던 맛·냄새 유발 물질과 소독부산물, 미량 유해 유기물을 깔끔히 제거합니다. 신장동·덕풍동 등 원도심 시 전역 약 13만 주민에게 양질의 고품질 수돗물이 안정적으로 공급될 예정입니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="https://www.ctnews.co.kr/40746" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (시티뉴스) →</a></div>
</div>
<div class="source">
📌 출처: 시티뉴스 (고승선 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (체육/복지 - 2026.08.28 추가) -->
<div class="article-card">
<div class="badge">📰 체육/복지</div>
<h3>하남시 당정근린공원 18홀 파크골프장 조성 완료…오는 10월 전격 시범운영</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 당정근린공원 내 1만 4,000㎡ 부지에 총사업비 16억 원을 투입해 18홀 규격의 파크골프장 및 부대시설 조성을 8월 말 마무리하고 오는 10월부터 본격 시범운영에 돌입합니다. 이용객 접근성 개선을 위해 2억 원을 별도 투입해 조정경기장 진입경사로(100m) 정비 공사도 병행 추진하며, 어르신 및 생활체육 동호인들의 원정 불편 해소와 한강 변 생활체육 랜드마크 조성이 기대됩니다.
</div>
<div class="source">
📌 출처: 하남일보
</div>
</div>

<!-- 지역 뉴스 기사 2 (교육/행정 - 2026.08.28 추가) -->
<div class="article-card">
<div class="badge">📰 교육/행정</div>
<h3>하남교육지원청 신설 긍정신호…안민석 교육감 "준비된 하남부터 추진"</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
3만 하남시민과 4만 학생의 오랜 숙원인 '하남교육지원청' 분리·신설이 탄력을 받게 되었습니다. 26일 동부권 지자체장 간담회에서 안민석 경기도교육감은 이현재 하남시장의 교육청 분리 촉구에 "준비된 곳부터 추진하는 원칙에 따라 하남시가 우선 추진될 가능성이 높다"고 밝히며, "광주와 하남이 함께하는 행사는 오늘이 마지막일 것"이라 언급해 독립 개청 가시화에 대한 큰 호응을 얻었습니다. 하남시는 종합복지타운 내 무상 임시청사 공간 및 한홀중 부지 제공 등 선제적 지원 노력을 펼치고 있습니다.
</div>
<div class="source">
📌 출처: 하남타임즈 (박필기 기자)
</div>
</div>

<!-- 지역 뉴스 기사 2 (부동산/동향 - 2026.08.27 추가) -->
<div class="article-card">
<div class="badge">📰 부동산/시장</div>
<h3><a href="http://www.hanamilbo.net/news/articleView.html?idxno=12568" target="_blank" style="color: inherit; text-decoration: none;">하남, 아파트 매매·전세 75주 동반 '수직 상승' 대기록</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
한국부동산원의 8월 넷째 주(24일 기준) 주간 아파트 가격 동향에 따르면, 하남시 매매가와 전세가가 무려 <b>75주 연속 동반 상승</b> 대기록을 작성했습니다. 강남 인접 입지와 지하철 3·9호선·GTX 교통 호재, 보유세 개편 논의에 따른 '똘똘한 한 채' 매물 잠김 현상이 주원인으로 분석됩니다. 미사강변도시(12.3억 원), 감일지구(11.1억 원), 위례신도시(14.5억 원) 등 84㎡ 국민평형 실거래가가 역대급 신고가 행진을 펼치고 있으며, 전셋값 상승(미사 6.5억~7억, 위례 7.5억~8억 원)이 매매가를 밀어올리는 상승 피드백 구도를 형성하고 있습니다.
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="http://www.hanamilbo.net/news/articleView.html?idxno=12568" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">기사 원문 보기 (하남일보) →</a></div>
</div>
<div class="source">
📌 출처: 하남일보
</div>
</div>

<!-- 지역 뉴스 기사 3 (민생/생활 - 2026.08.26~27) -->
<div class="article-card">
<div class="badge">📰 민생/복지</div>
<h3>하남시, '고유가 피해지원금' 8월 31일 사용 마감 안내…스미싱 사기 주의 당부</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시가 관내 소상공인 및 취약계층에 지급된 '고유가 피해지원금'의 사용 기한이 오는 8월 31일(월) 종료됨에 따라 기한 내 미사용액 소멸 방지를 위한 소비를 당부했습니다. 아울러 최근 시청을 사칭해 지원금 환수를 빙자한 결제 유도 스미싱 문자가 기승을 부리고 있어 주민 주의를 촉구했습니다.
</div>
<div class="source">
📌 출처: 서울매일 / 경기매일
</div>
</div>

"""

content = re.sub(
    r'(?s)<div id="local-news">\s*<div class="section-title green">📰 하남 지역 주요 뉴스</div>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="local-news">\n<div class="section-title green">📰 하남 지역 주요 뉴스</div>\n\n' + local_news_articles + '\n',
    content
)

# Section 3: 하남 맘카페 HOT 이슈
mom_cafe_issues = """<div class="mom-issue-card">
<h4>1️⃣ 초·중·고 2학기 개학 준비 및 학원가 하반기 셔틀버스 노선 공유 (미사맘스클럽/감일맘/위례맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 26일 기준 개학을 앞두고 하남 관내 초·중·고교 2학기 개학 준비물과 학원가 셔틀버스 노선 개편 소식이 맘카페 주요 게시글로 연이어 올라왔습니다.</div>
<div class="mom-point">💡 주민 포인트: 미사·감일·위례 신도시 내 학원가 신규 셔틀 운행 시간표와 방과후 교실 신청 안내 꿀팁 정보가 주민들 간에 활발히 소통되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "긴 여름방학이 끝나서 시원섭섭하지만 개학 준비로 바쁘네요!", "변경 학원 셔틀 노선 미리 공유해 주셔서 정말 유용했습니다" 등의 반응이 올랐습니다.</div>
</div>

<div class="mom-issue-card">
<h4>2️⃣ 하남시 고유가 피해지원금 8월 31일 사용 마감 및 주민세 납부 팁 (미사맘/감일맘/하남맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 정기분 주민세 납부 기간과 함께 하남시 고유가 피해지원금 사용 마감일(8/31)이 다가옴에 따라 사용처 정보 및 위택스 납부 방법이 카페 핫 이슈로 떠올랐습니다.</div>
<div class="mom-point">💡 주민 포인트: 잔여 지원금 사용이 가능한 동네 마트, 병·의원, 미용실 등 생활 밀착 가맹점 목록과 지원금 사칭 스미싱 주의 경고글이 활발히 공유되었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "남은 지원금으로 동네 마트에서 주말 장 알뜰하게 봤어요", "8월 31일 지나면 소멸되니 아직 남아있는 분들은 꼭 쓰세요!" 등의 반응이 달렸습니다.</div>
</div>

<div class="mom-issue-card">
<h4>3️⃣ 스타필드 하남 '2026 더 좋은소비 페스타' 주말 가족 체험 부스 오픈 기대감 (미사맘/위례맘/감일맘)</h4>
<div class="mom-detail"><strong>현황:</strong> 8월 28일(금)부터 30일(일)까지 스타필드 하남 센트럴 아트리움에서 열리는 사회적경제 기업 팝업 페스타 개최 소식이 맘카페에 전해졌습니다.</div>
<div class="mom-point">💡 주민 포인트: 아이들과 함께 참여할 수 있는 친환경 체험 공예 부스, 유기농 식품 장터, 가족 공연 및 방문객 선착순 사은품 정보가 큰 호응을 얻었습니다.</div>
<div class="mom-reaction">💬 주민 반응: "주말에 아이들과 스타필드 나들이 가는데 꼭 들러봐야겠네요", "지역 친환경 제품도 사고 아이 체험도 할 수 있어서 기대됩니다" 등의 기대평이 올랐습니다.</div>
</div>"""

content = re.sub(
    r'(?s)<div id="mom-cafe">\s*<div class="section-title pink">💬 하남 맘카페 HOT 이슈.*?</div>\s*<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>.*?(?=</div>\s*<hr/>\s*<!-- ===== 섹션)',
    '<div id="mom-cafe">\n<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">하남 지역 인터넷 커뮤니티에서 가장 화두가 되었던 우리 동네 소식을 모았습니다.</p>\n\n' + mom_cafe_issues + '\n',
    content
)

# Section 4: ALL IN 하남라이프
culture_events = """<div class="event-card" style="border-left: 4px solid #319795; background-color: #f0fdf4; padding: 14px 16px;">
<strong style="display: block; font-size: 0.98rem; color: #2b6cb0; margin-bottom: 8px;">[축제/행사] 스타필드 하남 '2026 더 좋은소비 페스타 in 하남' (8월 28일~30일)</strong>
<p style="margin: 0; font-size: 0.88rem; color: #4a5568; line-height: 1.6;">
<b>일시:</b> 2026년 8월 28일(금) ~ 8월 30일(일) (3일간)<br/>
<b>장소:</b> 스타필드 하남 센트럴 아트리움<br/>
<b>내용:</b> 경기·하남 지역 우수 사회적경제기업 38개사의 친환경 공예, 유기농 식품 유통 및 가족 만들기 체험 부스 운영 (방문객 선착순 사은품 증정)
</p>
</div>

<div class="event-card">
<strong>[보건/생활] 하남시 보건소 9월 '성인·노인 만성질환 예방 운동교실' 수강생 모집</strong>
<p>기간: 2026년 8월 27일(목)부터 선착순 모바일/방문 접수 (하남시보건소)<br/>내용: 늦더위 폭염 장기화 대응 어르신 및 고혈압·당뇨 만성질환자 맞춤형 근력 및 유산소 운동 프로그램이 9월부터 가동됩니다.</p>
</div>

<div class="event-card">
<strong>[교육/도서관] 하남시립도서관 2026년 가을학기 어린이·청소년 독서강좌 수강생 모집</strong>
<p>기간: 2026년 8월 27일(목)부터 선착순 접수 (하남시립도서관 홈페이지)<br/>내용: 미사·나룰도서관 동화 창작, AI 디지털 웹툰, 주말 독서 토론 교실 등 9월 맞춤형 강좌 운영.</p>
</div>

<div class="event-card">
<strong>[청년/지원] 2026년 청년드림, 제주애(愛) 올레(Olle)? 참가자 모집 중 (8월 31일까지)</strong>
<p>기간: 2026년 8월 25일(화) ~ 8월 31일(월)<br/>내용: 하남 만 19~34세 청년 대상 제주시 한달살이 숙박비 지원 사업 (이메일 cnr2013@korea.kr 접수)</p>
</div>"""

content = re.sub(
    r'(?s)<div id="culture">\s*<div class="section-title".*?>🎭 ALL IN 하남라이프</div>\s*<p.*?>.*?</p>\s*<div class="event-grid">.*?(?=</div>\s*</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->|</div>\s*<hr/>\s*<!-- ===== 섹션 3: 공공기관 소식지 ===== -->)',
    '<div id="culture">\n<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>\n<p style="color:#4a5568; font-size:0.93rem; margin-bottom:18px;">2026년 8월 28일 기준 한눈에 보는 하남시 최신 문화·공연·청년 지원 가이드</p>\n<div class="event-grid">\n' + culture_events + '\n</div>',
    content
)

# Section 5: 공공기관 소식지
public_agency_news = """<!-- 기사 1 -->
<div class="article-card">
<div class="badge">🏛️ 하남시 보건소 | 2026.08.28</div>
<h3>[하남시보건소] 2026년 가을맞이 성인·어르신 맞춤형 만성질환 예방 운동교실 모집 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px; line-height: 1.6;">
<b>모집기간:</b> 2026.8.27.(목) ~ 선착순 마감 | <b>대상:</b> 관내 성인 및 노인<br/>
<b>주요내용:</b> 폭염 지속에 따른 기력 회복 및 고혈압·당뇨 맞춤 운동지도, 체성분 측정 지원<br/>
<b>접수방법:</b> 하남시보건소 모바일 앱 또는 현장 방문 (문의: 보건사업과)
</div>
<div class="source">
📌 출처: 하남시 보건소 공지사항
</div>
</div>

<!-- 기사 2 -->
<div class="article-card">
<div class="badge">🏛️ 하남시립도서관 | 2026.08.28</div>
<h3>[하남시립도서관] 2026년 가을학기 어린이·청소년 독서문화 강좌 수강생 모집 안내</h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
하남시 미사·나룰·덕풍도서관에서 9월 개강하는 초·중학생 맞춤형 동화 창작, AI 웹툰, 독서토론 교실 수강생을 8월 27일부터 도서관 홈페이지에서 선착순 모집합니다.
</div>
<div class="source">
📌 출처: 하남시립도서관 공지사항
</div>
</div>"""

content = re.sub(
    r'(?s)<div id="public-news">\s*<div class="section-title purple">🏛️ 공공기관 소식지</div>.*?(?=\s*<div class="bottom-nav")',
    '<div id="public-news">\n<div class="section-title purple">🏛️ 공공기관 소식지</div>\n\n' + public_agency_news + '\n</div>\n\n',
    content
)

# Clean up any leftover duplicate event cards or double empty lines
content = re.sub(r'</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<div class="event-card">.*?</div>\s*<hr/>', '</div>\n</div>\n<hr/>', content)
content = re.sub(r'\n{3,}', '\n\n', content)

# Write to kj_hanam_inside_20260828.html
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Write to index.html
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully added Hanam Ilbo real estate article to Section 2!")
