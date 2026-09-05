# Visual Studio Code와 WSL 개발 환경

2026년 9월 5일 기준으로 Visual Studio Code의 WSL 확장은 Windows 편집기에서 Linux 파일과 개발 도구를 사용할 수 있게 연결합니다.

Windows 설치, WSL 확장, 프로젝트 경로, 연결 검증, 컨테이너 연동을 다룹니다.

Windows에 편집기를 설치한 뒤 Ubuntu에서 프로젝트를 엽니다. [VS Code 공식 WSL 안내](https://code.visualstudio.com/docs/remote/wsl)를 기준으로 진행합니다.

## Windows용 편집기 설치

[Windows용 VS Code](https://code.visualstudio.com/docs/setup/windows)를 설치하면서 PATH 추가 옵션을 선택합니다. Linux GUI용 VS Code 패키지를 WSL 안에 설치하는 구성과 구분합니다.

## WSL 확장 설치

Windows VS Code의 확장 화면에서 Microsoft가 배포하는 [WSL 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)을 설치합니다. 확장 식별자는 `ms-vscode-remote.remote-wsl`입니다.

## Linux 파일 시스템에서 프로젝트 열기

[프로젝트 경로 안내](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#file-storage)에 따라 Linux 빌드 도구를 사용할 프로젝트를 Ubuntu 홈 아래에 둡니다. Ubuntu 터미널에서 빈 실습 폴더를 엽니다.

```bash
mkdir -p ~/projects/wsl-check
cd ~/projects/wsl-check
code .
```

첫 연결에서 VS Code가 WSL 쪽 서버 구성 요소를 설치할 수 있습니다.

## 편집기와 터미널 연결 검증

VS Code의 원격 상태 표시에서 대상 WSL 배포판을 확인합니다. [공식 개발 안내](https://code.visualstudio.com/docs/remote/wsl)처럼 통합 터미널도 Linux에서 실행되는지 확인합니다.

```bash
uname -s
pwd
which git
```

이어서 필요한 언어 확장은 확장 화면에서 해당 WSL 환경에 설치합니다. `code`를 찾을 수 없으면 Windows PATH 옵션, 터미널 재시작, WSL 상호 운용 설정을 확인합니다.

## 컨테이너 개발 연결

[Dev Containers 안내](https://code.visualstudio.com/docs/devcontainers/containers)에 따라 Docker Desktop과 컨테이너 개발을 구성할 수 있습니다. WSL 연결과 컨테이너 연결의 현재 대상을 상태 표시에서 구분합니다.

wslc의 미리 보기 연동은 [wslc 가이드](wslc.md)의 확장 버전과 호환성 범위를 기준으로 시험합니다.

## 연결 환경의 유지

여기까지 정리하면 Windows 편집기에서 Linux 프로젝트를 열고 Linux 도구로 빌드할 수 있습니다. 첫 연결에서는 배포판과 경로를 확인하고 장기적으로는 프로젝트가 사용하는 확장과 SDK 버전을 관리합니다.

일반 WSL 개발에는 WSL 확장을 사용합니다. 프로젝트별 컨테이너가 필요하다면 Dev Containers를 추가할 수 있습니다.
