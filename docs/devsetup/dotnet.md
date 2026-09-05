# Ubuntu에서 .NET SDK 설치

2026년 9월 5일 기준으로 이 문서는 Ubuntu 26.04 LTS와 Ubuntu 24.04 LTS에서 .NET 10 SDK를 설치하는 방법을 다룹니다. Microsoft의 현재 Ubuntu 안내는 두 릴리스의 Ubuntu 저장소에서 .NET 10을 제공합니다.

배포판 확인, 저장소 선택, SDK 설치, 실행 검증, 프로젝트 버전 관리를 설명합니다.

Ubuntu 터미널에서 진행합니다. [Microsoft Ubuntu 설치 안내](https://learn.microsoft.com/en-us/dotnet/core/install/linux-ubuntu-install)의 해당 Ubuntu 릴리스 조건을 기준으로 적용합니다.

## Ubuntu 릴리스와 아키텍처

현재 Ubuntu 정보와 아키텍처를 확인합니다.

```bash
cat /etc/os-release
dpkg --print-architecture
```

Windows용 SDK와 Linux용 SDK는 별도로 설치합니다. WSL에서 Linux 빌드를 할 때에는 Linux용 `dotnet` 실행 파일을 사용합니다. [.NET 설치 확인](https://learn.microsoft.com/en-us/dotnet/core/install/how-to-detect-installed-versions)에서 SDK와 런타임을 구분할 수 있습니다.

## Ubuntu 패키지 공급원 선택

[Ubuntu 24.04와 26.04 설치 표](https://learn.microsoft.com/en-us/dotnet/core/install/linux-ubuntu-install)는 Ubuntu 피드에서 .NET 10을 설치하도록 안내합니다. 해당 릴리스에 Microsoft 저장소 등록 패키지를 추가하는 것을 기본 절차로 사용하지 않습니다.

기존 Microsoft 피드와 Ubuntu 피드가 섞인 환경은 [.NET 패키지 혼합 문제](https://learn.microsoft.com/en-us/dotnet/core/install/linux-package-mixup)를 기준으로 먼저 정리합니다. 이전 Ubuntu 릴리스의 명령을 배포판 숫자만 바꾸어 적용하지 않습니다.

## .NET 10 SDK 설치

Ubuntu 터미널에서 패키지 목록을 갱신하고 SDK를 설치합니다. SDK에는 해당 런타임도 포함됩니다.

```bash
sudo apt update
apt-cache policy dotnet-sdk-10.0
sudo apt install dotnet-sdk-10.0
```

설치 후보가 없다면 [현재 Ubuntu 버전의 공급원](https://learn.microsoft.com/en-us/dotnet/core/install/linux-ubuntu-install)을 다시 확인합니다. 수동 설치가 필요한 경우 [공식 설치 스크립트](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-install-script)를 사용할 수 있지만 운영체제 의존성과 업데이트 관리는 별도로 진행합니다.

## SDK와 실행 경로 확인

Ubuntu에서 실행 파일과 SDK 정보를 확인합니다.

```bash
command -v dotnet
dotnet --info
dotnet --list-sdks
dotnet --list-runtimes
```

[설치 확인 문서](https://learn.microsoft.com/en-us/dotnet/core/install/how-to-detect-installed-versions)에 따라 SDK 목록과 런타임 목록을 각각 확인합니다. 원하는 SDK가 보여도 프로젝트의 `global.json`이 다른 버전을 선택할 수 있습니다.

## 프로젝트의 SDK 선택

프로젝트가 이미 [global.json](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json)을 갖고 있다면 그 버전과 roll-forward 정책을 적용합니다. 새 프로젝트에서는 팀이 검증한 SDK 버전을 기록할 수 있습니다.

이어서 [.NET 지원 정책](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core)에서 지원 기간을 확인합니다. 예전 문서의 .NET 8 예제를 모든 새 프로젝트의 최신 기준으로 적용하지 않습니다.

## SDK 설치 이후의 확인

여기까지 정리하면 Ubuntu의 공급원으로 .NET SDK를 설치하고 실제 실행 경로를 확인할 수 있습니다. 설치 직후에는 프로젝트 빌드를 실행하고 장기적으로는 SDK 선택 정책과 지원 기간을 관리합니다.

기존 프로젝트에는 해당 프로젝트가 요구하는 버전을 사용합니다. 새 프로젝트는 지원 중인 SDK와 팀의 배포 조건을 함께 기준으로 선택합니다.
