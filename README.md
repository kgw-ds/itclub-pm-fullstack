# itclub-pm-fullstack
Full-stack learning log for PM readiness: FastAPI + SQLite (SSR &amp; JSON API) and Vue-based client rendering.

# IT Club PM Fullstack Lab

PM(프로덕트 매니저)로서 개발팀을 리드하기 위해, **DB → Backend(API/SSR) → Frontend(Rendering)** 흐름을 직접 구현하며 학습·기록하는 레포입니다.  
목표는 “개발을 잘하는 PM”이 아니라, **구조를 이해하고 요구사항을 개발 단위로 쪼개며, 팀원과 같은 언어(API/데이터/네트워크)로 소통할 수 있는 PM**이 되는 것입니다.

---

## Goals

### 1) Full-stack 구조 이해
- 같은 데이터(posts)를 **SSR(서버 렌더링 HTML)** 과 **API(JSON) + 프론트 렌더링(Vue)** 두 방식으로 표현
- DevTools(Network)로 요청/응답을 확인하며  
  - `document`(페이지 이동)  
  - `fetch/xhr`(데이터 요청)  
  을 구분하는 감각 만들기

### 2) PM 관점 산출물 만들기
- 기능 요구사항을 **DB / API / UI / 예외케이스**로 분해해 문서화
- 매일 “학습 로그 + 트러블슈팅 + 다음날 계획”을 남기기

---

## Tech Stack
- **Backend**: FastAPI (Python)
- **DB**: SQLite
- **SSR(템플릿)**: Jinja2
- **API**: JSON endpoints (`/api/*`)
- **Frontend Rendering**: Vue 3 (CDN, `fetch` 기반)

---

## Repository Structure
backend/ # FastAPI app (routes, db, templates)
docs/
day01.md # daily logs (Day01 ~ Day07)
screenshots/ # proof images (network, ui comparisons, etc.)
README.md

yaml
코드 복사

---

## How to Run (Windows)

### 1) 가상환경 생성 & 활성화
```powershell
cd C:\itclub_pm_a
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
2) 의존성 설치
(프로젝트에 requirements.txt가 있다면)

powershell
코드 복사
pip install -r requirements.txt
없다면(예시):

powershell
코드 복사
pip install fastapi uvicorn jinja2 python-multipart
3) 서버 실행
powershell
코드 복사
cd C:\itclub_pm_a\backend
python -m uvicorn app.main:app --reload
4) 접속
SSR 페이지: http://127.0.0.1:8000/

API(JSON): http://127.0.0.1:8000/api/posts

1-Week Plan (매일 3시간)
Day 01 — SSR vs API(JSON) + Front Rendering
 SSR(템플릿) 기반 목록/검색 흐름 체감

 /api/posts JSON API 구현(+ q 검색)

 Vue로 API 결과를 fetch해서 UI로 렌더링

 Jinja2 {{ }} vs Vue {{ }} 충돌 해결([[ ]])

Day 02 — CRUD를 API 중심으로 완성
 POST /api/posts (생성)

 DELETE /api/posts/{id} (삭제)

 Vue UI에서 생성/삭제 → 즉시 재렌더

Day 03 — DB 모델링 감각
 컬럼 추가(예: author / tag / is_done 등)

 정렬/필터/페이징(limit/offset) 맛보기

 “요구사항 → 스키마 변경 → API 반영” 흐름 정리

Day 04 — 인증/권한(개념+최소 구현)
 인증 vs 권한 구분

 “삭제는 특정 조건에서만 허용” 같은 정책을 서버에 적용(401/403 경험)

Day 05 — 품질(테스트/디버깅 루틴)
 API 최소 테스트 2~3개 작성

 재현→로그/Network→수정→재테스트 루틴 1회 완주

Day 06 — 배포/운영 감각
 환경변수(.env)로 설정 분리

 배포 후보 1곳에 올려서 접속(로그 확인 포함)

Day 07 — PM 산출물(개발 중심 문서) 완성
 API 명세(파라미터/응답 예시/에러)

 기능 목록을 DB/API/UI/예외케이스로 표 형태 정리

 다음 스프린트 계획(Must/Should/Could)

Logs
Day 01: docs/day01.md

Day 02: docs/day02.md (작성 예정)

각 Day 문서에는 다음을 포함합니다:

오늘 목표(Why)

구현한 기능(What)

데이터 흐름(How)

트러블슈팅(What happened / How solved)

증거(Proof: screenshot/API response)

내일 계획(Next)

What I Learned (PM 핵심 요약)
DB는 스스로 판단하지 않고, 백엔드가 만든 “질문(SQL/WHERE)”에 따라 결과를 반환한다.

JSON은 사용자에게 보여주기 위한 화면이 아니라, **프론트/앱/다른 서비스가 UI를 만들기 위한 “재료”**다.

DevTools(Network)에서 document(페이지)와 fetch/xhr(데이터)를 구분하면 문제를 빠르게 분해하고 팀원과 정확히 소통할 수 있다.

Next Milestone
Day02 목표: DELETE API + Vue 삭제 버튼으로 “API 기반 CRUD”를 완성하고, 기능 단위를 DB/API/UI/예외케이스로 분해해 문서화한다.
