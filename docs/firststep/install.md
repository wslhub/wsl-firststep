# WSL 2 설치와 업데이트

2026년 9월 5일 기준으로 이 가이드는 업데이트된 Windows 11의 x64 또는 Arm64 환경을 다룹니다. WSL 2는 CPU 가상화와 가상 머신 플랫폼을 사용합니다.

설치 조건, 배포판 선택, 최초 사용자 생성, 업데이트, 오프라인 설치를 순서대로 안내합니다.

Windows에서 PowerShell을 열어 진행하며 관리자 권한이 필요한 위치는 해당 절차에 표시했습니다. WSL과 Ubuntu의 버전 차이는 [최신 변경 사항](latest.md)에서 확인할 수 있습니다.

## Windows와 가상화 조건

설치 환경부터 확인하겠습니다. [Microsoft 설치 문서](https://learn.microsoft.com/en-us/windows/wsl/install)는 Windows 10 버전 2004 빌드 19041 이상 또는 Windows 11을 명령 기반 설치 조건으로 안내합니다. Windows 10의 지원 수명은 [수명 주기 문서](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro)에서 따로 다룹니다.

PowerShell에서 Windows 버전 대화상자를 엽니다.

```powershell
winver.exe
```

작업 관리자의 CPU 화면에서 가상화 상태를 볼 수 있습니다. 가상 머신 안에 Windows를 설치했다면 호스트의 [중첩 가상화 지원](https://learn.microsoft.com/en-us/windows/wsl/faq)이 적용됩니다. Windows Server는 [서버용 설치 안내](https://learn.microsoft.com/en-us/windows/wsl/install-on-server)를 사용합니다.

## WSL 구성 요소와 배포판 설치

관리자 PowerShell에서 아래 명령으로 WSL 구성 요소를 설치합니다. 재시작 안내가 나오면 작업을 저장한 뒤 Windows를 재시작합니다. `--no-distribution`은 배포판 설치를 다음 단계로 미룹니다.

```powershell
wsl.exe --install --no-distribution
```

이 명령과 다운로드 옵션은 [WSL 기본 명령](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#install)에 설명되어 있습니다.

### 배포판 이름 선택

Windows 재시작 후 PowerShell에서 목록을 확인하고 설치합니다. 아래 예제는 Ubuntu 26.04 LTS를 사용합니다. 프로젝트가 Ubuntu 24.04를 요구하면 목록의 `Ubuntu-24.04`를 선택합니다.

```powershell
wsl.exe --list --online
wsl.exe --install -d Ubuntu-26.04
```

설치 목록은 서비스 제공 상황에 따라 달라집니다. [공식 배포판 정의](https://github.com/microsoft/WSL/blob/master/distributions/DistributionInfo.json)와 명령 출력의 `NAME`을 기준으로 선택합니다. 버전이 없는 `Ubuntu` 이름이 항상 특정 릴리스를 뜻하지는 않습니다.

## 최초 실행과 Linux 사용자

첫 실행에서 Linux 사용자 이름과 암호를 생성합니다. 암호를 입력할 때 화면에 문자가 나타나지 않아도 입력을 받습니다. Windows 계정과 Linux 계정은 각각 관리합니다. [Ubuntu 환경 설정 문서](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)에 초기화 과정을 설명했습니다.

PowerShell에서 등록 상태를 확인하고 Linux 홈 디렉터리로 진입합니다.

```powershell
wsl.exe --list --verbose
wsl.exe -d Ubuntu-26.04 --cd ~
```

`VERSION`이 `2`인지 확인한 뒤 [Ubuntu 초기 설정](ubuntu.md)으로 이어갑니다. 이 열은 Ubuntu 버전이나 WSL 패키지 버전을 표시하지 않습니다.

## WSL과 Ubuntu의 업데이트

WSL 구성 요소 업데이트는 PowerShell에서 실행합니다. 설치된 버전과 업데이트 결과는 [WSL 명령 참조](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#update-wsl)에서 설명하는 명령으로 확인합니다.

```powershell
wsl.exe --update
wsl.exe --version
wsl.exe --status
```

이어서 Ubuntu 패키지는 Ubuntu 안에서 `sudo apt update`와 `sudo apt upgrade`로 갱신합니다. Ubuntu 24.04를 Ubuntu 26.04로 바꾸는 릴리스 업그레이드는 별도 절차이며 [Canonical 업그레이드 안내](https://ubuntu.com/wsl/docs/stable/howto/upgrade-ubuntu/)에서 다룹니다.

wslc 실습의 사전 릴리스 설치는 [컨테이너 가이드](wslc.md)에서만 진행합니다.

## Store 접근 제한과 파일 설치

다운로드가 진행되지 않거나 Store 경로를 사용할 수 없다면 [Microsoft의 다운로드 옵션](https://learn.microsoft.com/en-us/windows/wsl/install)을 적용할 수 있습니다. 아래 명령은 인터넷 연결을 사용합니다.

```powershell
wsl.exe --install --web-download -d Ubuntu-26.04
```

완전한 오프라인 설치는 [WSL 릴리스](https://github.com/microsoft/WSL/releases)에서 아키텍처에 맞는 WSL MSI를 준비하고 가상 머신 플랫폼을 활성화한 뒤 배포판 이미지를 설치하는 순서로 진행합니다. 구형 커널 전용 MSI는 현재 WSL 전체 설치 패키지를 대신하지 않습니다. [.wsl 파일과 RootFS 설치](../advanced/install-from-rootfs.md)에 이미지 선택과 검증 절차를 정리했습니다.

## 설치 결과 점검

1. `wsl.exe --version`에서 WSL 구성 요소의 버전을 확인합니다.
2. `wsl.exe --list --verbose`에서 설치한 배포판과 WSL 2 실행 방식을 확인합니다.
3. Ubuntu에서 `whoami`와 `pwd`로 일반 사용자와 홈 디렉터리를 확인합니다.
4. [Ubuntu 초기 설정](ubuntu.md)으로 패키지 갱신을 진행합니다.

## 설치 이후의 작업 순서

여기까지 정리하면 WSL 구성 요소와 Linux 배포판은 각자 설치와 업데이트 절차를 사용합니다. 설치 직후에는 일반 사용자 진입과 패키지 갱신을 확인하고 장기적으로는 Windows와 Ubuntu의 지원 기간을 함께 관리합니다.

기본 개발 환경에는 정식 WSL을 사용할 수 있습니다. 별도 배포판이나 컨테이너를 실험할 때에는 기존 배포판 복제와 사전 릴리스 안내를 상황에 맞게 적용합니다.
