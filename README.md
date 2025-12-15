# itclub-pm-fullstack
Full-stack learning log for PM readiness: FastAPI + SQLite (SSR &amp; JSON API) and Vue-based client rendering.

# IT Club PM Fullstack Lab

PM(프로덕트 매니저)로서 개발팀을 리드하기 위해, **DB → Backend(API/SSR) → Frontend(Rendering)** 흐름을 직접 구현하며 학습·기록하는 레포입니다.  
“개발을 잘하는 PM”이 아니라, **구조를 이해하고 요구사항을 개발 단위로 쪼개고, 팀원과 같은 언어(API/데이터/네트워크)로 소통할 수 있는 PM**이 되는 것이 목표입니다.

---

## 목표

### 1) 풀스택 구조 이해(핵심)
- 같은 데이터(posts)를 **SSR(서버 렌더링 HTML)** 과 **API(JSON) + 프론트 렌더링(Vue)** 두 방식으로 표현
- 요청/응답의 실체를 DevTools(Network)로 확인하며
  - `document`(페이지 이동)
  - `fetch/xhr`(데이터 요청)
  를 구분할 수 있게 만들기

### 2) PM 관점 산출물 생성
- 기능 요구사항을 **DB / API / UI / 예외케이스**로 쪼개어 정리
- 매일 학습 로그 + 트러블슈팅 로그 + 다음날 계획을 문서로 남기기

---

## Tech Stack
- **Backend**: FastAPI (Python)
- **DB**: SQLite
- **SSR(템플릿)**: Jinja2
- **API**: JSON endpoints (`/api/*`)
- **Frontend Rendering**: Vue 3 (CDN, fetch 기반)

---

## Repository Structure
