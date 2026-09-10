# Project-Scoped Rules for Hanam Newsletter Agent

## 1. 지역 정치인 관련 뉴스 수집 및 언급 규칙
하남지역 주요 뉴스 수집 시, 아래에 기재된 의원들의 동정이나 주요 활동이 포함된 뉴스를 우선적으로 발굴하고 뉴스레터 기사 요약문에 해당 의원의 이름을 반드시 명시하여 요약하십시오.

- **하남시의원**: `정혜영`, `최승태`
- **경기도의원**: `오민영`, `강성삼`

## 2. GitHub 배포 규칙 (Git Deployment Rule)
- 기본 작업(뉴스레터 작성 및 수정) 시에는 **로컬 파일 저장**까지만 진행합니다.
- 사용자가 채팅에서 **`/git에 배포해`** 라고 명시적으로 명령할 때만 `git push`를 실행합니다.

## 3. 고정 디자인 수칙 (Locked Design System)
- 상단 배너 이미지: `./images/top01.png` (`onerror="this.src='./images/top.png'"` 지참)
- 5대 섹션 순서, GmarketSansBold 타이틀, 카드 디자인 및 48px 프로필 아이콘(`kjicon.png`)을 엄격히 고정 유지합니다.
- 메타태그 제목: `매일전하는 이광재의원의 하남인사이드`

## 4. 유튜브 링크 처리 지침 (YouTube Embedding Rule)
- 사용자가 유튜브 링크(Shorts 또는 일반 동영상)를 가져오면 [YOUTUBE_EMBEDDING_RULE.md](file:///d:/github/newsletter/newsletter/YOUTUBE_EMBEDDING_RULE.md) 지침을 **무조건 자동 실행**합니다.
- `yt-dlp`로 로컬 `.mp4` 동영상을 자동 다운로드하고, 외부 차단(오류 153) 없는 인라인 HTML5 `<video>` 플레이어로 현장일지 카드를 구축합니다.

