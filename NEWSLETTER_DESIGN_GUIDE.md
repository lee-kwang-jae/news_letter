# 🎨 하남 뉴스레터 디자인 시스템 & 표준 가이드라인 (Newsletter Design System Guide)

본 가이드라인은 **매일전하는 이광재의원의 하남인사이드** 뉴스레터의 레이아웃, 헤더 배너, 섹션 5대 구조, 카드 디자인, 폰트 및 OpenGraph 메타태그 규격을 정의합니다. 향후 모든 뉴스레터 생성 및 수정 시 본 스타일과 구조를 그대로 유지해야 합니다.

---

## 1. 🏷️ 표준 명칭 & Open Graph 메타 태그 [고정/LOCKED]

* **공식 뉴스레터 제목**: `매일전하는 이광재의원의 하남인사이드`
* **HTML Head OpenGraph 태그 규격**:
  ```html
  <title>매일전하는 이광재의원의 하남인사이드</title>
  <meta property="og:type" content="website"/>
  <meta property="og:locale" content="ko_KR"/>
  <meta property="og:url" content="https://lee-kwang-jae.github.io/news_letter/"/>
  <meta property="og:site_name" content="매일전하는 이광재의원의 하남인사이드"/>
  <meta property="og:title" content="매일전하는 이광재의원의 하남인사이드"/>
  <meta property="og:description" content="이광재 국회의원 의정활동, 하남 지역 주요 뉴스, 하남 맘카페 HOT 이슈, ALL IN 하남라이프 &amp; 공공기관 소식지"/>
  <meta property="og:image" content="https://lee-kwang-jae.github.io/news_letter/images/thumb.jpg"/>
  <meta property="og:image:url" content="https://lee-kwang-jae.github.io/news_letter/images/thumb.jpg"/>
  <meta property="og:image:secure_url" content="https://lee-kwang-jae.github.io/news_letter/images/thumb.jpg"/>
  <meta property="og:image:type" content="image/jpeg"/>
  <meta property="og:image:width" content="1200"/>
  <meta property="og:image:height" content="630"/>
  <meta property="og:image:alt" content="매일전하는 이광재의원의 하남인사이드"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="매일전하는 이광재의원의 하남인사이드"/>
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
    <img src="./images/top01.png" alt="매일전하는 이광재의원의 하남인사이드" style="width: 100%; height: auto; display: block;" onerror="this.src='./images/top.png'">
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
   - 구성: 언론보도 카드 (`card-press`) + 현장일지 카드 (`card-field`)
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
