# WSL 시작하기

2026년 9월 5일 기준으로 WSL 설치와 초기 설정, 개발 도구 연결, 배포판 복사, wslc 컨테이너 실습을 정리했습니다. 정식 WSL과 공개 미리 보기 기능의 적용 범위를 각 문서에 표시했습니다.

이 가이드는 WSL 2 설치, Ubuntu 초기 설정, 개발 환경, 운영과 문제 해결을 다룹니다.

처음 사용하는 경우 설치와 Ubuntu 설정부터 순서대로 진행합니다. 기존 환경을 사용한다면 최신 변경 사항에서 적용할 항목을 선택할 수 있습니다.

## 설치부터 개발 환경까지의 순서

[Microsoft의 WSL 설치 흐름](https://learn.microsoft.com/en-us/windows/wsl/install)을 따라 다음 순서로 진행할 수 있습니다.

1. [WSL 2 설치와 업데이트](firststep/install.md)를 진행합니다.
2. [Ubuntu 초기 설정](firststep/ubuntu.md)을 적용합니다.
3. [Windows Terminal](firststep/winterm.md)과 [화면 분할 단축키](devsetup/multiplexer.md)를 확인합니다.
4. [Visual Studio Code](firststep/vscode.md)와 [Docker Desktop](firststep/docker.md)을 연결합니다.
5. 필요한 [.NET](devsetup/dotnet.md), [OpenJDK](devsetup/openjdk.md), [Go](devsetup/golang.md), [Ruby](devsetup/ruby.md) 환경을 구성합니다.

## PowerShell과 Ubuntu 명령 구분

`powershell` 코드 블록은 Windows PowerShell 5.1 또는 PowerShell 7에서 실행합니다. `bash` 코드 블록은 Ubuntu 터미널에서 실행합니다. 관리자 권한이 필요한 작업은 본문에 표시합니다.

WSL 안에서 Windows 도구를 부를 때에는 `wsl.exe`, `wslc.exe`처럼 확장자를 붙입니다. [Windows와 Linux 명령의 상호 운용](https://learn.microsoft.com/en-us/windows/wsl/filesystems#interoperability-between-windows-and-linux-commands)에 설명한 호출 규칙을 따릅니다.

## 정식 WSL과 wslc 미리 보기

[최신 변경 사항](firststep/latest.md)은 정식 WSL 2.7.13과 사전 릴리스 WSL 2.9.10을 구분합니다. [공식 릴리스 목록](https://github.com/microsoft/WSL/releases)에서 이후 버전과 공개 상태를 확인할 수 있습니다.

다만 [wslc 실습](firststep/wslc.md)은 WSL 2.9.3 이상의 공개 미리 보기를 사용합니다. 참여하려면 사전 릴리스 업데이트를 선택하며 정식 출시 시 명령과 지원 범위가 달라질 수 있습니다.

## 배포판 보관과 문제 해결

[배포판 복사와 복원](advanced/copy-distro.md), [.wsl 이미지와 RootFS 설치](advanced/install-from-rootfs.md), [네트워크](firststep/networking.md), [메모리](firststep/vmmem.md), [시간 동기화](troubleshoot/timesync.md)를 필요에 따라 적용합니다.

이어서 [Microsoft의 문제 해결 안내](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)와 실제 명령 출력을 비교하면 환경별 차이를 확인할 수 있습니다. 변경 전후의 WSL 버전과 재현 조건을 기록하면 문제를 좁히는 데 도움이 됩니다.

## 문서 기여와 한국 WSL 커뮤니티

[GitHub 저장소](https://github.com/wslhub/wsl-firststep)에서 이슈와 Pull Request로 내용을 보완할 수 있습니다. 로컬 빌드와 검증 절차는 [BUILD.md](https://github.com/wslhub/wsl-firststep/blob/master/BUILD.md)에 정리했습니다. 자료를 추가할 때에는 확인 날짜와 공식 출처, 실행할 셸을 함께 적습니다.

[한국 WSL 사용자 그룹](https://www.facebook.com/groups/wslhub/)에서 관련 경험과 질문을 공유할 수 있습니다. 기존에 소개한 국내 도서는 다음과 같으며 최신 명령과 지원 범위는 각 제품의 현재 문서를 기준으로 확인합니다.

- 처음 만나는 WSL: 개발자 및 IT 전문가를 위한 리눅스용 윈도우 하위 시스템 실무 안내서[^1], [교보문고](https://product.kyobobook.co.kr/detail/S000001810486)
- 효율성이 배가되는 WSL2 가이드북: 설치와 구성부터 비주얼 스튜디오 코드, 도커, 쿠버네티스에서의 활용까지, [교보문고](https://product.kyobobook.co.kr/detail/S000001952234)

[^1]: 한국 WSL 사용자 그룹 운영진이 직접 번역했습니다.

## 현재 작업에 맞는 문서 선택

여기까지 정리하면 WSL의 설치부터 개발 도구와 배포판 관리까지 같은 흐름으로 진행할 수 있습니다. 설치 직후의 실행 검증과 장기적인 버전 및 백업 관리를 구분해 적용합니다.

처음 시작하는 환경은 설치 가이드부터 진행합니다. 이미 개발 환경이 있다면 변경 사항과 문제 해결 문서에서 해당 조건을 선택할 수 있습니다.
