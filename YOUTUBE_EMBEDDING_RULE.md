# YouTube Video & Shorts Mobile-Compatible Embedding Directive

## 📌 목적 (Objective)
사용자가 유튜브 링크(Shorts 또는 일반 동영상)를 전달하면, 유튜브의 외부 임베드 제약(`Error 153`) 및 **모바일(iOS Safari/카카오톡/네이버 인앱 브라우저) 환경의 재생 오류를 완벽 차단**합니다. 모바일과 PC 모든 환경에서 매끄럽게 인라인 재생되는 HTML5 미디어 플레이어 카드를 자동으로 구축합니다.

---

## 🚨 핵심 원칙 (Core Rules - MANDATORY)

1. **요약글 절대 금지 (No Summary Text Rule)**:
   - 영상 카드 내에 **텍스트 요약글(설명 문구)을 절대로 넣지 않습니다.**
   - `<div class="summary">` 내부에는 오직 **영상 플레이어 컨테이너**와 **'유튜브에서 보기' 링크**만 작성합니다.

2. **로컬 MP4 동영상 및 포스터 이미지 필수 동기화**:
   - 유튜브 영상의 재생 오류(`Error 153`)를 방지하기 위해 `yt-dlp`로 모바일 호환 H.264/AAC MP4 파일(`shorts_MMDD.mp4`) 및 포스터 썸네일(`shorts_MMDD_poster.jpg`)을 다운로드합니다.
   - MP4 비디오 및 포스터 이미지는 반드시 `images/`와 `dashboard/news/images/` 양쪽 폴더에 동시에 복사/동기화합니다.

---

## 🛠️ 실행 단계별 워크플로우 (Step-by-Step Workflow)

### 1단계: 비디오 ID 추출 및 메타데이터 수집
- URL에서 `VIDEO_ID` 추출 (예: `https://youtube.com/shorts/lhLfoDigJc4` -> `lhLfoDigJc4`).
- oEmbed API 또는 페이지 메타태그에서 영상 제목을 파싱합니다:
  - `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json`

### 2단계: MP4 비디오 및 썸네일 포스터 저장
- `yt-dlp`로 iOS Safari 및 모바일 호환 H.264/AAC MP4 비디오를 다운로드합니다 (AV1 코덱은 모바일 재생 불가):
  ```bash
  yt-dlp -f "bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]/mp4" -o "images/shorts_MMDD.mp4" "https://youtube.com/shorts/VIDEO_ID"
  ```
  - 만약 다운로드된 비디오가 AV1 코덱인 경우 `ffmpeg`로 H.264/AAC로 변환합니다:
  ```bash
  ffmpeg -y -i images/shorts_MMDD.mp4 -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k -movflags +faststart images/shorts_MMDD_h264.mp4
  ```
- 썸네일 포스터 이미지(`shorts_MMDD_poster.jpg`)를 `https://img.youtube.com/vi/VIDEO_ID/maxresdefault.jpg` (또는 `hqdefault.jpg`)에서 다운로드합니다.
- 동영상과 포스터를 `images/` 및 `dashboard/news/images/` 양쪽 폴더에 모두 복사합니다.

### 3단계: 현장일지 영상 카드 마크업 (요약글 없음)
- `create_MMDD.py`, `index.html`, `dashboard/news/index.html`, `dashboard/news/kj_hanam_inside_YYYYMMDD.html`에 아래 표준 HTML 카드 마크업을 적용합니다:

```html
<!-- [현장일지] (유튜브 숏폼 영상) -->
<div class="article-card card-field" style="margin-top: 16px;">
<div class="badge badge-field">🎥 현장일지 (영상)</div>
<h3><a href="javascript:void(0)" onclick="playNewsletterVideo()" style="color: inherit; text-decoration: none;" title="클릭하여 페이지에서 영상 재생">"[영상 제목]" 현장 숏폼</a></h3>
<div class="summary" style="text-align: left; word-break: keep-all; letter-spacing: -0.3px;">
<div style="margin-top: 14px; margin-bottom: 12px; display: flex; justify-content: center;">
  <div id="yt-container-VIDEO_ID" style="position: relative; width: 100%; max-width: 320px; aspect-ratio: 9/16; border-radius: 16px; overflow: hidden; border: 1px solid #cbd5e0; box-shadow: 0 8px 24px rgba(0,0,0,0.2); display: block; background: #000;">
    <video id="video-VIDEO_ID" poster="images/shorts_MMDD_poster.jpg" controls playsinline webkit-playsinline="true" x5-playsinline="true" preload="metadata" style="width: 100%; height: 100%; object-fit: cover; border-radius: 16px;">
      <source src="images/shorts_MMDD.mp4" type="video/mp4">
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

### 4단계: `playNewsletterVideo()` 함수 연동
- 페이지 하단 스크립트에 `video-VIDEO_ID` 요소를 포함한 `playNewsletterVideo()` 재생 함수를 연동합니다:
  ```javascript
  function playNewsletterVideo() {
      var v = document.getElementById('video-VIDEO_ID');
      if (v) {
          v.scrollIntoView({ behavior: 'smooth', block: 'center' });
          if (v.paused) {
              var promise = v.play();
              if (promise !== undefined) {
                  promise.catch(function(error) {
                      console.log("Autoplay blocked:", error);
                      v.muted = true;
                      v.play();
                  });
              }
          } else {
              v.pause();
          }
      }
  }
  ```
