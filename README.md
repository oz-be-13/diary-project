# Diary Project – 나만의 일기장

이번 프로젝트는 팀플로 진행됩니다. 부담 없이 팀원들과 즐겁게 진행해 주세요!

“나만의 일기장”은 매일 일기를 작성하며 자신의 생각을 정리하고, 명언과 자기성찰 질문을 랜덤으로 제공하는 개인 일기 관리 서비스입니다. 사용자는 JWT 인증으로 로그인하며, 자신만의 일기를 CRUD 할 수 있습니다. 명언은 웹 스크래핑으로 한 번 저장 후 DB에서 랜덤으로 불러오며, 자기성찰 질문 또한 랜덤으로 제공됩니다.

- 패키지명: `diary-project`
- 런타임: Python 3.13.5
- 의존성/가상환경: Poetry

## 💫 주요 기능

- 회원가입
- 로그인/로그아웃 (JWT 인증)
- 일기 CRUD
- 일기 검색 및 정렬
- 명언 랜덤 제공
- 명언 북마크
- 자기성찰 질문 랜덤 제공

## 🏃 프로젝트 목표

- 팀 협업 경험 (GitHub 브랜치 전략 & 코드 리뷰)
- 의존성 관리 및 실행 환경 구성
- FastAPI 기반 API 설계와 JWT 인증 구현 능력 강화
- 웹 스크래핑과 DB 연동 실습
- 실전 프로젝트 구조 설계 및 배포 경험
- AWS EC2 + Nginx + Gunicorn + Uvicorn 배포

## 👥 (추천) 팀원의 역할

처음 협업을 진행하는 여러분을 위해 간단하게 역할을 제안합니다. 팀 상황에 맞게 자유롭게 조정해도 됩니다.

- 팀장
  - FastAPI 프로젝트 초기 세팅
  - GitHub 레포 생성 및 브랜치 전략 관리
  - 전체 일정/작업 조율 및 코드 리뷰 총괄
- 공통 작업 (모두 참여)
  - Git 브랜치 전략 수립
  - 프로젝트 세부 기획(질문 콘텐츠, 스크래핑 대상 선정 등)
  - DB 모델링 및 ORM 설계(부분 설계 후 통합 또는 전원 공동 설계)
  - API Spec 작성 및 리뷰
  - 코드 리뷰 및 테스트
- 담당 API 파트
  1) 인증 & 사용자 관리: JWT 회원가입/로그인/로그아웃, 권한 처리  
  2) 일기 CRUD & 검색: 작성/조회/수정/삭제, 검색/정렬/페이징  
  3) 명언 스크래핑 & 질문: 스크래핑/저장, 랜덤 제공, 명언 북마크

배포는 1명이 전담하되, 학습을 위해 각자 한 번씩 직접 배포해 보길 권장합니다.

---

## ⚙️ 개발 환경

- Python: 3.13.5
- 패키지 및 가상환경: Poetry

### 사전 준비

1) Python 3.13.5 설치  
2) Poetry 설치  
   - 공식 문서: https://python-poetry.org/docs/#installation

### 프로젝트 설정 및 의존성 설치


## 🔀 Git Flow 브랜치 전략

본 프로젝트는 Git Flow 전략을 기반으로 브랜치를 운영합니다.

### 주요 브랜치
- **main** : 운영/배포용 브랜치 (항상 안정 상태 유지)
- **develop** : 개발 통합 브랜치 (기능 개발 결과물을 모음)

### 보조 브랜치
- **feature/\*** : 새로운 기능 개발 시 `develop` 에서 분기 → 완료 후 `develop` 으로 머지
- **release/\*** : 배포 준비 시 `develop` 에서 분기 → QA 및 안정화 후 `main` 과 `develop` 에 머지
- **hotfix/\*** : 운영 중 긴급 버그 수정 시 `main` 에서 분기 → 수정 후 `main` 과 `develop` 에 머지

### 브랜치 흐름 예시
```mermaid
gitGraph
   commit id: "v1.0"
   branch develop
   commit id: "init"
   branch feature/featA
   commit id: "featA-1"
   commit id: "featA-2"
   checkout develop
   merge feature/featA
   branch release/1.0.1
   commit id: "QA fix"
   checkout main
   merge release/1.0.1
   commit id: "v1.0.1"
   checkout develop
   merge release/1.0.1
