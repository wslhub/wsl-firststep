# WSL 정식 릴리스와 컨테이너 미리 보기

2026년 9월 5일에 Microsoft의 릴리스 목록을 확인했습니다. 정식 채널은 WSL 2.7.13을 제공하며 사전 릴리스 채널은 WSL 2.9.10을 제공합니다. 두 릴리스 모두 MDE 플러그인 오류로 WSL을 시작하지 못하는 문제를 수정했습니다.

이 문서에서는 릴리스 채널, 설치 방식, systemd와 WSLg, 네트워크와 메모리, wslc의 적용 범위를 다룹니다.

먼저 현재 버전을 구분한 뒤 기존 배포판에 적용할 변경과 컨테이너 실험 절차를 순서대로 살펴보겠습니다.

확인 시점과 미리 보기의 범위는 다음과 같습니다.

> 2026년 9월 5일 기준입니다. WSL 컨테이너는 공개 미리 보기이며 `wsl.exe --update --pre-release`로 설치합니다. 정식 출시 시 요구 조건과 명령이 달라질 수 있습니다.

## 정식 채널과 사전 릴리스 채널

[WSL 공식 릴리스](https://github.com/microsoft/WSL/releases)의 `Latest`와 `Pre-release` 표시로 배포 상태를 구분합니다. 아래 공개 날짜는 GitHub의 UTC 시각을 기준으로 적었습니다.

| 채널 | 확인한 버전 | 공개 날짜 | 업데이트 명령 |
| --- | --- | --- | --- |
| 정식 | [WSL 2.7.13](https://github.com/microsoft/WSL/releases/tag/2.7.13) | 2026년 9월 4일 | `wsl.exe --update` |
| 사전 릴리스 | [WSL 2.9.10](https://github.com/microsoft/WSL/releases/tag/2.9.10) | 2026년 9월 4일 | `wsl.exe --update --pre-release` |

PowerShell에서 설치된 패키지 버전과 배포판 실행 방식을 함께 확인합니다.

```powershell
wsl.exe --version
wsl.exe --status
wsl.exe --list --verbose
```

`--version`의 WSL 2.7.13 같은 제품 버전과 `--list --verbose`의 `VERSION` 열에 표시되는 WSL 1 또는 WSL 2는 서로 다른 값을 나타냅니다. `wsl.exe --update`는 Ubuntu 패키지나 Ubuntu 릴리스까지 업그레이드하지 않습니다.

## 설치 명령과 .wsl 배포 형식

현재 설치 절차는 `wsl.exe --install`과 `wsl.exe --list --online`을 중심으로 구성합니다. Ubuntu 26.04 LTS와 Ubuntu 24.04 LTS의 실제 배포 이름은 [Microsoft 배포판 목록](https://github.com/microsoft/WSL/blob/master/distributions/DistributionInfo.json)에서도 확인할 수 있습니다.

이어서 이미지 설치 방식을 짚어보겠습니다. `.wsl` 파일은 WSL 2.4.10 이상에서 설치할 수 있는 배포 형식입니다. [Canonical의 설치 안내](https://ubuntu.com/wsl/docs/stable/howto/install-ubuntu-wsl2/)에 따라 파일을 두 번 클릭하거나 `wsl.exe --install --from-file`로 설치합니다. 기존 배포판 복제에는 [내보내기와 가져오기](../advanced/copy-distro.md)를 사용합니다.

## systemd와 Linux GUI 앱

[systemd](https://learn.microsoft.com/en-us/windows/wsl/systemd)는 WSL 0.67.6 이상에서 지원합니다. 기존에 가져온 이미지까지 자동으로 활성화된다고 가정하지 않고 `ps -p 1 -o comm=`으로 실제 PID 1을 확인합니다. 설정 절차는 [Ubuntu 초기 설정](ubuntu.md)에 정리했습니다.

[WSLg](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps)는 WSL 2에서 Linux GUI 앱을 Windows 데스크톱과 통합합니다. 지원 범위는 Windows 10 빌드 19044 이상 또는 Windows 11이며 GPU 드라이버와 WSL 업데이트도 영향을 줍니다. Windows 10의 일반 지원은 2025년 10월 14일에 종료되었으며 [ESU와 제품별 수명 주기](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro)는 별도로 확인할 수 있습니다.

## 네트워크와 메모리 설정의 적용 범위

[WSL 설정 참조](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)는 배포판별 `/etc/wsl.conf`와 Windows 사용자별 `.wslconfig`를 구분합니다. DNS, 프록시, 방화벽 옵션은 `[wsl2]`에 두며 `autoMemoryReclaim`은 `[experimental]`에 둡니다.

다만 [컨테이너 발표](https://devblogs.microsoft.com/commandline/wsl-container-is-now-available-for-public-preview/)에서 소개한 virtiofs와 consomme 기본값을 일반 WSL 배포판의 기본값으로 적용하지 않습니다. [네트워크 설정](networking.md)과 [메모리 설정](vmmem.md)은 일반 배포판을 기준으로 설명합니다.

## wslc CLI와 Windows 앱용 API

[WSL 컨테이너](https://learn.microsoft.com/en-us/windows/wsl/wsl-container)는 `wslc.exe`와 Windows 앱용 API를 제공합니다. 최소 요구 버전은 WSL 2.9.3입니다. 정식 WSL 2.7.13을 설치하는 것만으로 해당 기능을 사용할 수 있지는 않습니다.

사전 릴리스 WSL 2.9.10은 `wslc system info`, 컨테이너 이벤트, 여러 CLI 호환성 수정을 포함합니다. 실제 실습은 [wslc 가이드](wslc.md)에서 진행할 수 있습니다. Docker Desktop 기반 작업은 [기존 Docker 가이드](docker.md)에서 다룹니다.

## 업데이트 전후 점검 항목

1. PowerShell에서 WSL 패키지 버전과 배포판 이름을 기록합니다.
2. 보존할 배포판을 내보내고 복사본으로 복원 가능 여부를 확인합니다.
3. 일반 작업에는 정식 업데이트를 적용하고 컨테이너 실험에는 사전 릴리스를 선택합니다.
4. 업데이트 후 사용 중인 VPN, 개발 서버, 컨테이너 도구의 동작을 확인합니다.

## 현재 환경에 맞춘 적용 순서

여기까지 정리하면 WSL 정식 업데이트와 wslc 미리 보기는 서로 다른 채널을 사용합니다. 설치된 배포판의 실행 여부와 개발 도구 연결은 업데이트 직후 확인할 수 있으며 미리 보기의 정식 전환 일정은 이후 릴리스에서 달라질 수 있습니다.

기존 개발 환경을 유지하려면 정식 채널을 기준으로 진행합니다. Windows에서 내장 컨테이너 CLI나 API를 실험하려면 별도로 백업한 환경에서 wslc 절차를 적용할 수 있습니다.
