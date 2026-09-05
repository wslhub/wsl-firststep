# 문서 빌드와 검증

2026년 9월 5일 기준으로 이 저장소는 MkDocs 1.6.1과 Material for MkDocs 9.7.7로 문서를 빌드합니다. 직접 사용하는 Markdown 렌더러와 확장도 requirements.txt에서 버전을 고정합니다.

가상 환경 준비, 미리 보기, 자동 검증, 기여 절차, 배포 동작을 설명합니다.

Python 3.11 이상에서 저장소 루트를 작업 디렉터리로 사용합니다. CI는 Python 3.13을 사용하며 Windows 명령 실습과 문서 빌드 검증을 구분합니다.

## 가상 환경과 의존성 설치

[Python venv](https://docs.python.org/3/library/venv.html)로 격리 환경을 생성합니다. Ubuntu와 macOS에서 다음 명령을 실행합니다.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Windows PowerShell에서는 `py -3.13 -m venv .venv`로 만들고 아래 명령의 `.venv/bin/python`을 `.venv\Scripts\python.exe`로 바꿉니다. 활성화 스크립트를 실행하지 않아도 해당 Python 경로로 작업할 수 있습니다.

## 브라우저 미리 보기

[MkDocs 개발 서버](https://www.mkdocs.org/user-guide/cli/#mkdocs-serve)를 실행합니다.

```bash
.venv/bin/python -m mkdocs serve
```

표시된 로컬 주소를 브라우저로 엽니다. Ubuntu 문서의 목록 안 코드 블록, Terminal 단축키 표, wslc 코드 복사 버튼과 탐색 메뉴를 확인합니다.

## 엄격한 빌드와 렌더링 검사

경고를 실패로 처리하는 [strict 빌드](https://www.mkdocs.org/user-guide/cli/#mkdocs-build) 뒤에 생성된 HTML을 검사합니다.

```bash
.venv/bin/python -m mkdocs build --strict
.venv/bin/python scripts/check_docs.py
```

검사는 문서별 생성 HTML, 제목, 원문 코드 펜스 노출, 내부 링크와 앵커, 정적 자원, 검색 인덱스를 확인합니다. Ubuntu 목록 안의 코드 블록도 별도로 검사해 이슈 #8의 재발을 탐지합니다. 원문의 JSON과 INI 코드 블록도 파싱합니다. 외부 사이트의 일시 장애와 Windows 명령의 실제 실행 결과는 이 검사에 포함하지 않습니다.

## 문서 변경과 근거 기록

기능을 추가할 때에는 실행할 셸, 확인 날짜, 정식 또는 미리 보기 상태, 공식 출처를 함께 적습니다. [Material의 SuperFences 확장](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/#superfences)이 중첩 코드 블록을 처리하며 목록 안 코드는 네 칸 들여씁니다.

1. 문서와 mkdocs.yml의 탐색 경로를 함께 수정합니다.
2. 엄격한 빌드와 HTML 검사를 실행합니다.
3. 브라우저에서 표, 코드 블록, 링크를 확인합니다.
4. Pull Request에 수정 범위와 실제 검증 결과를 기록합니다.

README.md와 docs/index.md는 각각 GitHub와 웹사이트용 진입점을 제공합니다. 상대 링크 기준이 달라 별도 파일로 관리합니다.

## 검증한 산출물의 Pages 배포

Pull Request에서는 저장소 읽기 권한으로 문서를 빌드하고 검증한 뒤 Pages 산출물을 업로드합니다. master 반영 후에는 같은 검증을 통과한 산출물을 [공식 Pages Actions](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)로 배포합니다. 배포 작업만 Pages 쓰기 권한과 OIDC 토큰 발급 권한을 사용하며 공식 Actions는 확인한 커밋으로 고정합니다.

이 워크플로를 처음 적용할 때 저장소 Settings의 Pages에서 Build and deployment의 Source를 GitHub Actions로 지정합니다. [GitHub 문서](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)에 따르면 GITHUB_TOKEN으로 푸시한 커밋은 Pages 빌드를 시작하지 않습니다. 따라서 배포용 커밋을 만드는 대신 검증한 산출물을 직접 배포합니다. 기존 gh-pages 브랜치는 이전 배포 기록으로 남습니다.

프로젝트 주소는 `https://wslhub.com/wsl-firststep/`이며 이 저장소에 도메인 루트용 CNAME을 추가하지 않습니다. 브랜치 보호 규칙에 필요한 PR 승인은 저장소 설정을 따릅니다.

## 빌드 검증과 실행 검증의 범위

여기까지 정리하면 로컬과 CI에서 같은 문서 빌드 및 HTML 검사를 사용할 수 있습니다. 바로 확인할 수 있는 문서 표시와 링크 오류를 먼저 해결하고 외부 출처와 제품 버전은 이후 업데이트에서도 다시 확인합니다.

Windows에서 WSL, wslc, Docker를 직접 실행한 경우에는 버전과 결과를 PR에 기록합니다. macOS나 Linux에서 문서만 빌드한 결과를 WSL 실행 검증으로 표시하지 않습니다.
