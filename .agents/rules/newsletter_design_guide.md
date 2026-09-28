# 🎨 하남 뉴스레터 디자인 시스템 & 표준 가이드라인 (Newsletter Design System Guide)

본 가이드라인은 **매일전하는 이광재의원의 우리동네 하남소식** 뉴스레터의 레이아웃, 헤더 배너, 섹션 5대 구조, 카드 디자인, 폰트 및 OpenGraph 메타태그 규격을 정의합니다. 향후 모든 뉴스레터 생성 및 수정 시 본 스타일과 구조를 그대로 유지해야 합니다.

---

## 1. 🏷️ 표준 명칭 & Open Graph 메타 태그 [고정/LOCKED]

* **공식 뉴스레터 제목**: `매일전하는 이광재의원의 우리동네 하남소식`
* **HTML Head OpenGraph 태그 규격**:
  ```html
  <title>매일전하는 이광재의원의 우리동네 하남소식</title>
  <meta property="og:type" content="website"/>
  <meta property="og:locale" content="ko_KR"/>
  <meta property="og:url" content="https://lee-kwang-jae.github.io/news_letter/"/>
  <meta property="og:site_name" content="매일전하는 이광재의원의 우리동네 하남소식"/>
  <meta property="og:title" content="매일전하는 이광재의원의 우리동네 하남소식"/>
  <meta property="og:description" content="이광재 국회의원 의정활동, 하남 지역 주요 뉴스, 하남 맘카페 HOT 이슈, ALL IN 하남라이프 &amp; 공공기관 소식지"/>
  <meta property="og:image" content="https://lee-kwang-jae.github.io/news_letter/images/thumb.jpg"/>
  <meta property="og:image:url" content="https://lee-kwang-jae.github.io/news_letter/images/thumb.jpg"/>
  <meta property="og:image:secure_url" content="https://lee-kwang-jae.github.io/news_letter/images/thumb.jpg"/>
  <meta property="og:image:type" content="image/jpeg"/>
  <meta property="og:image:width" content="1200"/>
  <meta property="og:image:height" content="630"/>
  <meta property="og:image:alt" content="매일전하는 이광재의원의 우리동네 하남소식"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="매일전하는 이광재의원의 우리동네 하남소식"/>
  <meta name="twitter:description" content="이광재 국회의원 의정활동, 하남 지역 주요 뉴스, 하남 맘카페 HOT 이슈, ALL IN 하남라이프 &amp; 공공기관 소식지"/>
  <meta name="twitter:image" content="https://lee-kwang-jae.github.io/news_letter/images/thumb.jpg"/>
  <meta name="twitter:image:width" content="1200"/>
  <meta name="twitter:image:height" content="630"/>
  <link rel="image_src" href="https://lee-kwang-jae.github.io/news_letter/images/thumb.jpg"/>
  ```

---

## 2. 🖼️ 상단 헤더 배너 (`.header-box`) [고정/LOCKED]

* **상단 배너 이미지 경로**: `./images/top01.png` (fallback: `./images/top.png`)
* **HTML 구조**:
  ```html
  <div class="header-box">
    <img src="./images/top01.png" alt="매일전하는 이광재의원의 우리동네 하남소식" style="width: 100%; height: auto; display: block;" onerror="this.src='./images/top.png'">
    <div style="position: absolute; bottom: 12px; right: 16px; background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); color: #ffffff; padding: 2px 8px; border-radius: 20px; font-size: 7px; font-weight: 600; border: 1px solid rgba(255, 255, 255, 0.3); opacity: 0.6;">
      {호수}호 | {발행일자} 발행
    </div>
  </div>
  ```

---

## 3. 📚 뉴스레터 5대 핵심 섹션 구조 [고정/LOCKED]

뉴스레터 본문은 반드시 다음 5개 섹션 순서를 준수합니다:

1. **`우리동네 국회의원 이광재` (`#lawmaker`)**
   - 프로필 아이콘: `<img src="./images/kjicon.png" style="width:48px; height:48px; border-radius:50%;">`
   - 구성: 현장일지 카드 (`card-field`) [선배치] + 언론보도 카드 (`card-press`) [후배치]
2. **`📰 하남 지역 주요 뉴스` (`#local-news`)**
   - 제목 스타일: `<div class="section-title green">📰 하남 지역 주요 뉴스</div>`
3. **`💬 하남 맘카페 HOT 이슈` (`#mom-cafe`)**
   - 제목 스타일: `<div class="section-title pink">💬 하남 맘카페 HOT 이슈</div>`
   - 카드 스타일: `<div class="mom-issue-card">` (현황, 주민 포인트, 주민 반응 💬)
4. **`🎪 ALL IN 하남라이프` (`#culture`)**
   - 제목 스타일: `<div class="section-title" style="background: linear-gradient(90deg, #319795, #4fd1c5);">🎭 ALL IN 하남라이프</div>`
   - 카드 스타일: `<div class="article-card" style="background-color: #f0fdf4; border-left: 4px solid #319795;">`
5. **`🏛️ 공공기관 소식지` (`#public-news`)**
   - 제목 스타일: `<div class="section-title purple">🏛️ 공공기관 소식지</div>`

---

## 4. 🔤 폰트 체계 (Typography) [고정/LOCKED]

* **Pretendard WebFont**: 본문 및 공통 UI
* **Gmarket Sans Bold**: 주요 섹션 타이틀 (`.section-title`)


---

## 부록: 기사 카드 파스텔 디자인 (Article Card Design)

앞으로 하남 뉴스레터를 생성하거나 수정할 때, 기사 카드(Article Card) 부분은 반드시 다음의 파스텔 톤 디자인 스타일과 구조를 유지해야 합니다. HTML/CSS 생성 시 이 가이드를 반영하세요.

## 1. HTML 구조 (클래스 부여)
- 국회의원 소식 섹션에서 **현장소식** 기사는 `<div class="article-card card-field">`를 사용합니다.
- 국회의원 소식 섹션에서 **언론보도** 기사는 `<div class="article-card card-press">`를 사용합니다.

## 2. 기사 카드 공통 스타일 (.article-card)
- 테두리(border) 제거 (`border: none;`)
- 모서리 둥글게 (`border-radius: 14px;`)
- 옅고 부드러운 그림자 효과 적용 (`box-shadow: 0 4px 15px rgba(0,0,0,0.04);`)
- 마우스 오버(Hover) 시 입체 효과 (`transform: translateY(-4px); box-shadow: 0 10px 25px rgba(0,0,0,0.09);`)

## 3. 섹션별 파스텔 톤 배경색
각 기사 카드의 배경은 시각적 구분을 위해 다음의 파스텔 색상을 사용합니다:
- **현장소식** (`#lawmaker .article-card.card-field`): 연한 파스텔 블루 (`#f0f7ff`)
- **언론보도** (`#lawmaker .article-card.card-press`): 현장소식보다 좀 더 진한 스카이블루 (`#e0f2fe`)
- **지역 주요 뉴스** (`#local-news .article-card`): 연한 민트/초록색 (`#f2fbf5`)
- **공공기관 소식** (`#public-news .article-card`): 차분한 연한 보라색 (`#f8f5ff`)
- **맘카페 핫이슈** (`#mom-cafe .article-card`, `.mom-issue-card`): 따뜻한 연한 분홍색 (`#fff5f8`), 테두리 없음

## 4. 요약 텍스트 박스 스타일 (.summary)
- 각 파스텔 톤 배경에 잘 어울리도록 텍스트 박스는 반투명한 흰색 배경(`background: rgba(255, 255, 255, 0.55);`)을 사용합니다.
- 테두리 역시 은은한 반투명 색상을 적용합니다.
  - 현장소식/언론보도: `border: 1px solid rgba(144, 205, 244, 0.4);`
  - 지역 뉴스: `border: 1px solid rgba(198, 246, 213, 0.4);`
  - 공공기관 소식: `border: 1px solid rgba(233, 216, 253, 0.4);`

## 5. 타이틀 바 상단 고정 (Sticky Header) 및 맨위로 버튼
- `🗣️ 우리동네 국회의원 이광재` 섹션 타이틀 바 (`#lawmaker .section-title`)는 스크롤을 내릴 때 화면 상단(`top: 0`)에 지속 고정(`position: fixed;`)되는 스티키 헤더 기능(`.fixed-title`)을 유지합니다.
- 하단 푸터 영역(`© 2026 우리동네 진짜일꾼 이광재`) 중앙에 배치된 동그란 화살표 아이콘 버튼(`⬆️`) 클릭 시 (`scrollToTop()`), 최상단 스크롤 이동과 함께 타이틀 바의 고정이 즉시 해제(Unfix)되어 본래 위치로 복귀하도록 스크립트를 구성합니다.



