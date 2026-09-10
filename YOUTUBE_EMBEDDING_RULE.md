# YouTube Video & Shorts Embedding Directive

## 📌 목적 (Objective)
사용자가 유튜브 링크(Shorts 또는 일반 동영상)를 전달하면, 유튜브의 외부 임베드 제약 및 `Error 153 (동영상 플레이어 구성 오류)`을 완전 차단하고, 웹페이지 내부에서 100% 매끄럽게 재생되는 자체 HTML5 미디어 플레이어 카드를 자동으로 구축합니다.

---

## 🛠️ 실행 단계별 워크플로우 (Step-by-Step Workflow)

### 1단계: 비디오 ID 추출 및 메타데이터 파싱
- 사용자가 입력한 유튜브 URL에서 `VIDEO_ID`를 추출합니다.
  - 예시: `https://youtube.com/shorts/3BlZC9feiyw` -> `3BlZC9feiyw`
- 유튜브 official oEmbed API를 통해 영상 제목 및 메타데이터를 수집합니다.
  - API: `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json`

### 2단계: yt-dlp 활용 고화질 MP4 자동 다운로드 (오류 153 완벽 예방)
- 유튜브 iframe 임베드는 브라우저 보안 정책, file:// 환경, 텔레그램 미리보기 등에서 차단(오류 153)을 일으키므로, **반드시 `yt-dlp`로 로컬 미디어 파일(.mp4)을 다운로드**합니다.
- 실행 명령어:
  ```bash
  yt-dlp -f "bestvideo[vcodec^=avc1]+bestaudio[acodec^=mp4a]/best[ext=mp4]/mp4" "https://youtube.com/shorts/VIDEO_ID" -o "images/shorts_MMDD.mp4"
  ```
- 다운로드한 `.mp4` 파일을 아래 두 경로에 동시에 복사/저장합니다:
  - `images/shorts_MMDD.mp4`
  - `dashboard/news/images/shorts_MMDD.mp4`

### 3단계: HTML5 비디오 플레이어 카드 작성 (Section 1 현장일지)
- `index.html`, `dashboard/news/index.html`, `dashboard/news/kj_hanam_inside_YYYYMMDD.html` 파일의 현장일지 섹션에 아래 구조로 카드를 만듭니다:

```html
<!-- 기사 (현장일지 - 유튜브 숏폼 영상) -->
<div class="article-card card-field">
<div class="badge badge-field">🎥 현장일지 (영상)</div>
<h3><a href="javascript:void(0)" onclick="playNewsletterVideo()" style="color: inherit; text-decoration: none;" title="클릭하여 페이지에서 영상 재생">"[영상 제목]" 현장 숏폼</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
[영상 요약 내용]
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container-VIDEO_ID" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-VIDEO_ID" poster="https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="./images/shorts_MMDD.mp4" type="video/mp4">
      <iframe src="https://www.youtube.com/embed/VIDEO_ID?feature=oembed" title="[영상 제목]" style="width: 100%; height: 100%; border: 0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </video>
  </div>
</div>
<div style="margin-top: 12px; font-size: 0.9em; color: #718096;"><a href="[유튜브URL]" target="_blank" style="color: #3182ce; font-weight: bold; text-decoration: none;">유튜브에서 보기 (이광재 TV) →</a></div>
</div>
<div class="source">
📌 출처: 이광재 공식 유튜브 (이광재 TV)
</div>
</div>
```

### 4단계: 자바스크립트 연동
- 페이지 하단 스크립트의 `playNewsletterVideo()` 함수를 갱신합니다:
  ```javascript
  function playNewsletterVideo() {
      var v = document.getElementById('video-VIDEO_ID');
      if (v) { v.play(); }
  }
  ```

### 5단계: 로컬 Git 커밋만 수행 (No Auto-Push)
- 지침에 따라 `git add` 및 `git commit`만 실행하며, 사용자가 `/git에 배포해` 라고 명령하기 전에는 `git push`를 하지 않습니다.
