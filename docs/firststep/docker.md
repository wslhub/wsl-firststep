# Docker Desktop과 WSL 2 연동

2026년 9월 5일 기준으로 Docker Desktop은 WSL 2 백엔드와 배포판 통합 기능을 제공합니다. 이 문서는 Windows에 Docker Desktop을 설치하는 구성을 다룹니다.

설치 조건, 백엔드 선택, 배포판 통합, 실행 검증, wslc와의 선택 기준을 설명합니다.

PowerShell에서 WSL 상태를 확인한 뒤 Docker Desktop과 Ubuntu 순서로 진행합니다. [Docker 공식 WSL 안내](https://docs.docker.com/desktop/features/wsl/)를 기준으로 작성했습니다.

## WSL과 Windows 설치 조건

PowerShell에서 현재 WSL과 배포판 상태를 확인합니다. Docker는 WSL 2.1.5 이상을 요구하며 최신 WSL 사용을 안내합니다. Windows 빌드와 아키텍처 조건은 [Docker Desktop 설치 문서](https://docs.docker.com/desktop/setup/install/windows-install/)에서 확인할 수 있습니다.

```powershell
wsl.exe --update
wsl.exe --version
wsl.exe --list --verbose
```

## Docker Desktop 설치와 백엔드

[공식 설치 프로그램](https://docs.docker.com/desktop/setup/install/windows-install/)으로 설치한 뒤 Docker Desktop을 실행합니다. 설정의 General에서 `Use the WSL 2 based engine`을 선택합니다.

Docker Desktop과 배포판 내부에 별도로 설치한 Docker Engine 또는 CLI가 충돌할 수 있습니다. [Docker WSL 안내](https://docs.docker.com/desktop/features/wsl/)에 따라 기존 설치와 데이터를 확인한 뒤 사용할 구성을 선택합니다. 회사에서 사용하는 경우 Docker Desktop 이용 조건은 설치 문서의 구독 안내를 기준으로 판단할 수 있습니다.

## 사용할 배포판의 WSL Integration

설정의 Resources에서 WSL Integration을 열어 개발에 사용할 배포판을 켜고 적용합니다. 해당 메뉴가 없다면 Linux 컨테이너 모드와 WSL 2 백엔드 상태를 확인합니다. [배포판 통합 절차](https://docs.docker.com/desktop/features/wsl/#turn-on-docker-desktop-wsl-2)를 참고할 수 있습니다.

통합 후 Ubuntu 터미널을 새로 열어 다음 검증을 진행합니다.

## 클라이언트와 서버 실행 검증

Ubuntu에서 아래 명령을 실행합니다. `docker version`의 Client와 Server가 모두 응답하고 `hello-world`가 완료되는지 확인합니다.

```bash
docker version
docker context show
docker run --rm hello-world
docker compose version
```

연결 오류가 나면 Desktop 실행 상태, 선택한 Docker context, 배포판 통합을 차례로 확인합니다. [Docker context 문서](https://docs.docker.com/engine/manage-resources/contexts/)에서 접속 대상을 구분하는 방법을 설명합니다.

## 프로젝트 파일과 wslc 선택

Linux 빌드 도구와 컨테이너 바인드 마운트를 사용할 프로젝트는 WSL 홈 아래에 둘 수 있습니다. [Docker의 WSL 파일 시스템 안내](https://docs.docker.com/desktop/features/wsl/)에서 경로에 따른 차이를 확인할 수 있습니다.

다만 [wslc](wslc.md)는 WSL에 포함된 별도 컨테이너 CLI이며 현재 공개 미리 보기로 제공합니다. 기존 Compose 구성이나 Docker Engine API 연동의 동작을 확인한 뒤 전환 범위를 판단합니다.

## 컨테이너 개발 환경의 유지

여기까지 정리하면 Docker Desktop에서 선택한 WSL 배포판으로 Docker 명령을 실행할 수 있습니다. 설치 직후에는 서버 응답과 실습 컨테이너를 확인하고 장기적으로는 WSL과 Desktop의 지원 조건을 함께 관리합니다.

기존 Docker 프로젝트에는 Desktop 통합을 사용할 수 있습니다. 내장 컨테이너 CLI 실험은 별도의 wslc 안내로 진행합니다.
