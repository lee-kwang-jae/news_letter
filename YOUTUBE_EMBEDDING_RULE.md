# YouTube Video & Shorts Mobile-Compatible Embedding Directive

## 📌 목적 (Objective)
사용자가 유튜브 링크(Shorts 또는 일반 동영상)를 전달하면, 유튜브의 외부 임베드 제약 및 `Error 153`과 **iOS Safari / 카카오톡·네이버 인앱 브라우저 등 모바일 환경의 비디오 재생 차단을 완벽 방지**합니다. 모바일과 PC 모든 환경의 뉴스레터 웹페이지 내부에서 100% 매끄럽게 재생되는 자체 HTML5 미디어 플레이어 카드를 자동으로 구축합니다.

---

## 🛠️ 실행 단계별 워크플로우 (Step-by-Step Workflow)

### 1단계: 비디오 ID 추출 및 메타데이터 파싱
- 사용자가 입력한 유튜브 URL에서 `VIDEO_ID`를 추출합니다.
  - 예시: `https://youtube.com/shorts/3BlZC9feiyw` -> `3BlZC9feiyw`
- 유튜브 official oEmbed API를 통해 영상 제목 및 메타데이터를 수집합니다.
  - API: `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=VIDEO_ID&format=json`

### 2단계: 모바일 100% 호환 H.264/AAC MP4 다운로드 (iOS Safari/인앱 브라우저 필수)
- **중요**: iOS WebKit(Safari, 카카오톡/네이버 인앱 브라우저)은 `VP9` 코덱이나 오디오 스트림이 없는 미디어 파일 재생을 차단/오류 처리합니다.
- 반드시 `yt-dlp` 실행 시 **H.264(avc1) 비디오 코덱 + AAC(mp4a) 오디오 코덱**을 지정하여 MP4를 다운로드합니다.
- 실행 명령어:
  ```bash
  yt-dlp -f "bestvideo[vcodec^=avc1]+bestaudio[acodec^=mp4a]/best[ext=mp4]/mp4" "https://youtube.com/shorts/VIDEO_ID" -o "images/shorts_MMDD.mp4"
  ```
- 다운로드한 `.mp4` 파일을 아래 두 경로에 동시에 복사/저장합니다:
  - `images/shorts_MMDD.mp4`
  - `dashboard/news/images/shorts_MMDD.mp4`

### 3단계: 모바일 터치 호환 HTML5 비디오 플레이어 카드 작성 (Section 1 현장일지)
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

### 4단계: 모바일 터치 및 자바스크립트 연동 (Smooth Scroll & Play Promise Handling)
- 페이지 하단 스크립트의 `playNewsletterVideo()` 함수를 갱신합니다:
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

### 5단계: 뉴스레터 생성 스크립트 반영 및 로컬 Git 커밋 (No Auto-Push)
- `dashboard/scripts/create_MMDD.py` 파일의 현장일지 섹션에도 동일 비디오 카드를 포함시킵니다.
- 지침에 따라 `git add` 및 `git commit`만 실행하며, 사용자가 `/git에 배포해` 또는 `git push`를 명령하기 전에는 자동 `git push`를 하지 않습니다.
