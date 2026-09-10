# 🎨 하남 뉴스레터 디자인 시스템 & UI 가이드라인 (Design System Guide)

이 문서는 **KJ's 하남 인사이드 뉴스레터**의 디자인, UI 구성요소, 폰트 표준 및 배포 규칙을 정의합니다. 다음 뉴스레터 작성 및 발행 시 반드시 본 가이드라인을 준수합니다.

---

## 1. 🔤 폰트 체계 (Typography)

### 1.1 본문 및 공통 폰트 (Pretendard)
* **WebFont CDN 링크 (HTML `<head>` 상단 필수)**:
  ```html
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
  ```
* **전역 CSS 적용 (`*` 및 `body`)**:
  ```css
  * {
      font-family: 'Pretendard Variable', 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
  }
  body {
      font-family: 'Pretendard Variable', 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, 'Helvetica Neue', 'Segoe UI', 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif;
      line-height: 1.7;
      color: #333;
  }
  ```

### 1.2 주요 섹션 타이틀 폰트 (Gmarket Sans Bold) [고정/LOCKED]
* **WebFont CDN 링크 (HTML `<head>` 상단 필수)**:
  ```html
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSans.css" />
  ```
* **섹션 제목 클래스 (`.section-title`) CSS 적용 [고정/LOCKED]**:
  ```css
  .section-title {
      font-family: 'GmarketSansBold', 'GmarketSans', 'Pretendard', sans-serif !important;
      font-size: 1.33rem; /* PC 데스크톱 고정 (약 22.5px) */
  }
  @media (max-width: 600px) {
      .section-title {
          font-size: 1.22rem !important; /* 모바일 고정 (약 20.8px) */
      }
  }
  ```
* **적용 대상 5대 주요 섹션 제목**:
  1. `우리동네 국회의원 이광재` (`<img src="./images/kjicon.png" style="width:48px; height:48px; border-radius:50%;">` 프로필 아이콘 **48px 고정**)
  2. `📰 하남 지역 주요 뉴스`
  3. `☕ 하남 맘카페 HOT 이슈`
  4. `🎪 ALL IN 하남라이프`
  5. `🏛️ 공공기관 소식지`

---

## 2. 🖼️ 상단 헤더 배너 (`.header-box`)

### 2.1 메인 배너 이미지 규격 및 원본 해상도
* **권장 제작 규격**: `1400px × 320px ~ 360px` (2배수 고해상도 PNG/WebP)
* **이미지 파일명**: `./images/top.png`

### 2.2 레이아웃 (Full-Width 마진 제거)
* 컨테이너 카드 패딩 영역까지 꽉 채우는 풀-위드 디자인을 적용합니다.
* **CSS 규격**:
  ```css
  /* PC 데스크톱 기준 */
  .header-box {
      margin: -40px -40px 30px -40px;
      border-radius: 14px 14px 0 0;
      overflow: hidden;
      position: relative;
      box-shadow: 0 4px 15px rgba(0,0,0,0.05);
  }

  /* 모바일 미디어 쿼리 (@media (max-width: 600px)) */
  @media (max-width: 600px) {
      .header-box {
          margin: -12px -8px 20px -8px !important;
          border-radius: 8px 8px 0 0 !important;
          padding: 0 !important;
      }
  }
  ```

### 2.3 발행 정보 배지 (60% 투명도 Glassmorphic Badge)
* **위치**: 상단 배너 우측 하단 (`position: absolute; bottom: 12px; right: 16px;`)
* **HTML 구조 및 스타일**:
  ```html
  <div style="position: absolute; bottom: 12px; right: 16px; background: rgba(0, 0, 0, 0.3); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px); color: #ffffff; padding: 2px 8px; border-radius: 20px; font-size: 7px; font-weight: 600; border: 1px solid rgba(255, 255, 255, 0.3); opacity: 0.6;">
    {호수}호 | {발행일자} 발행
  </div>
  ```

---

## 3. 🎨 섹션 타이틀 배너 UI (`.section-title`)

* **가운데 정렬 및 흰색 테두리 필수 적용**:
  ```css
  .section-title {
      padding: 8px 16px;
      color: white;
      border-radius: 6px;
      font-size: 1.33rem;
      font-weight: bold;
      margin-bottom: 20px;
      background: linear-gradient(90deg, #2b6cb0, #4299e1);
      text-align: center;
      border: 1.5px solid #ffffff;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
      font-family: 'GmarketSansBold', 'GmarketSans', 'Pretendard', sans-serif !important;
  }
  ```

---

## 4. 📸 이미지 및 썸네일 처리 규칙

### 4.1 원본 비율 유지 (No-Cropping Policy)
* 이미지 텍스트 잘림을 방지하기 위해 `object-fit: cover` 및 고정 높이 지정을 금지합니다.
  ```css
  .flex-summary .img-box img {
      width: 100% !important;
      height: auto !important;
      object-fit: contain !important;
  }
  ```

### 4.2 카카오톡 & SNS 공유 Open Graph 메타 태그
* 카카오톡 및 SNS 스크랩 캐시 이슈를 방지하기 위해 일자별 전용 이미지 파일명(예: `thumbnail0910.png`)을 사용하거나 캐시 갱신 파라미터를 명시합니다.
  ```html
  <meta property="og:image" content="https://lee-kwang-jae.github.io/news_letter/images/thumbnail0910.png"/>
  <meta property="twitter:image" content="https://lee-kwang-jae.github.io/news_letter/images/thumbnail0910.png"/>
  <link rel="image_src" href="https://lee-kwang-jae.github.io/news_letter/images/thumbnail0910.png"/>
  ```

---

## 5. 🎥 유튜브 숏폼 비디오 플레이어 처리

* 유튜브 숏폼(`youtube.com/shorts`)의 외부 `<iframe>` 직접 임베드 시 발생하는 **오류 153** 방지를 위해 커스텀 포스터 비디오 카드로 표현합니다.
  ```html
  <a href="https://youtube.com/shorts/{VIDEO_ID}" target="_blank" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000; text-decoration: none;">
    <img src="https://img.youtube.com/vi/{VIDEO_ID}/hqdefault.jpg" alt="영상 제목" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.9;" />
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: #ff0000; border-radius: 14px; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(255,0,0,0.5);">
      <div style="width: 0; height: 0; border-top: 10px solid transparent; border-bottom: 10px solid transparent; border-left: 18px solid #ffffff; margin-left: 3px;"></div>
    </div>
    <div style="position: absolute; bottom: 16px; left: 14px; right: 14px; background: rgba(0,0,0,0.75); backdrop-filter: blur(4px); padding: 10px 12px; border-radius: 10px; color: #ffffff; font-size: 0.88rem; font-weight: bold; text-align: center; border: 1px solid rgba(255,255,255,0.2);">
      ▶ 클릭하여 숏폼 영상 재생
    </div>
  </a>
  ```
