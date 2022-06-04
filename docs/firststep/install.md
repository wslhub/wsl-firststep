# 커맨드라인으로 WSL v2 설치하기

커맨드라인으로 WSL v2를 설치하면 간단하고 빠르게 WSL v2를 시작할 수 있습니다.

## 프로세서 아키텍처 확인하기

내가 사용하는 컴퓨터의 프로세서의 종류와 지원 범위를 확인해야 합니다.

| CPU 종류      | 아키텍처    | WSL v1 | WSL v2 |
| ------------  | ----------- | ------ | ------ |
| 인텔 프로세서 | 32비트 전용 |        |        |
| 인텔 프로세서 | 64비트 지원 | O      | O[^A]  |
| ARM 프로세서  | 32비트 전용 |        |        |
| ARM 프로세서  | 64비트 지원 | O      | O[^B]  |

## 지원되는 윈도우 버전 확인하기

내가 실행하는 윈도우 10 버전이 정확히 어떻게 되는지 확인하려면 PowerShell에서 다음과 같이 실행합니다.

```powershell
cmd.exe /c ver
```

### 32비트 인텔 프로세서

32비트 인텔 프로세서에서는 WSL v1, v2 모두 지원되지 않습니다.

### 64비트 인텔 프로세서

| OS 버전    | 실행 가능한 WSL 버전 | WSL v2 필요 조건              | 커맨드라인을 통한 설치 지원[^G] | WSLg 지원 |
| ---------- | -------------------- | ----------------------------- | ------------------------------- | --------- |
| 10.0.10240 |                      |                               |                                 |           |
| 10.0.10586 |                      |                               |                                 |           |
| 10.0.14393 | 레거시 WSL[^C]       |                               |                                 |           |
| 10.0.14393 | 레거시 WSL[^C]       |                               |                                 |           |
| 10.0.15063 | 레거시 WSL[^C]       |                               |                                 |           |
| 10.0.16299 | WSL v1               |                               |                                 |           |
| 10.0.17134 | WSL v1               |                               |                                 |           |
| 10.0.17763 | WSL v1               |                               |                                 |           |
| 10.0.18362 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트[^D] |                                 |           |
| 10.0.18363 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트[^D] |                                 |           |
| 10.0.19041 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트[^E] | O                               |           |
| 10.0.19042 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트[^E] | O                               |           |
| 10.0.19043 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트[^E] | O                               |           |
| 10.0.19044 | WSL v1, WSL v2       | CPU 가상화                    | O                               |           |
| 10.0.20348 | WSL v1, WSL v2       | CPU 가상화 [^F]               | O                               |           |
| 10.0.22000 | WSL v1, WSL v2       | CPU 가상화                    | O                               | O         |

### 32비트 ARM 프로세서

32비트 프로세서에서는 WSL v1, v2 모두 지원되지 않습니다.

### 64비트 ARM 프로세서

| OS 버전    | 실행 가능한 WSL 버전 | WSL v2 필요 조건          | 커맨드라인을 통한 설치 지원 | WSLg 지원 |
| ---------- | -------------------- | ------------------------- | --------------------------- | --------- |
| 10.0.17134 | WSL v1               |                           |                             |           |
| 10.0.17763 | WSL v1               |                           |                             |           |
| 10.0.18362 | WSL v1               |                           |                             |           |
| 10.0.18363 | WSL v1               |                           |                             |           |
| 10.0.19041 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트 | O                           |           |
| 10.0.19042 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트 | O                           |           |
| 10.0.19043 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트 | O                           |           |
| 10.0.19044 | WSL v1, WSL v2       | CPU 가상화, 최신 업데이트 | O                           |           |
| 10.0.22000 | WSL v1, WSL v2       | CPU 가상화                | O                           | O         |

## Windows Terminal 설치하기

WSL v2를 사용하면서 기존의 내장 터미널을 사용해도 문제 없지만, 좀 더 풍부하고 다양한 기능을 사용하려면 Windows Terminal을 설치해서 사용하는 것이 좋습니다.

PowerShell을 열고 아래 명령어를 붙여넣으세요.

```powershell
Start-Process 'https://aka.ms/terminal'
```

그러면 Windows Terminal을 설치할 수 있는 스토어 페이지로 접근할 수 있고, 바로 설치를 시작할 수 있습니다.

## 자동 설치

위의 지원되는 윈도우 버전 확인하기 표에서 **커맨드라인을 통한 설치 지원**을 사용할 수 있는 OS에 해당하는 경우, 다음의 명령어를 PowerShell에서 실행하면 간편하게 설치할 수 있습니다. 아래 명령어로 WSL v2 실행에 필요한 구성 요소 (가상 머신 플랫폼, WSL v2 전용 커널)를 한 번에 설치합니다.

```powershell
wsl.exe --install
```

컴퓨터 재시작이 필요하다는 안내가 나올 경우 안내에 따라 재시작하도록 합니다. WSL 설치가 완료된 후에는 다음의 명령어를 실행하여 커맨드라인으로 설치할 수 있는 배포판의 종류를 확인합니다.

```powershell
wsl.exe --list --online
```

원하는 배포판을 찾으면, 다음과 같이 명령어를 입력합니다. 여기서는 `Ubuntu-20.04`를 설치한다고 가정하겠습니다.

```powershell
wsl.exe --install -d Ubuntu-20.04
```

설치가 끝나면 자동으로 새 배포판이 실행되어 초기화 과정이 실행됩니다.

Windows Terminal에는 자동으로 새 항목이 등록됩니다.

## 수동 설치

### WSL, HCS 옵션 켜기

**NOTE: 윈도우, 리눅스, 맥, 그리고 퍼블릭 클라우드 환경에서 가상 컴퓨터 안에서 WSL을 사용하려고 Windows 10이나 Windows Server 2019 이상의 OS를 설치한 경우, 사용하는 가상 컴퓨터가 중첩 가상화 기능을 제공하는지 확인한 다음 이 단계를 따라하세요. 중첩 가상화가 작동하지 않는 가상 컴퓨터 상에 설치된 Windows 10에서는 WSL v1만 사용할 수 있습니다.**

WSL v1과 v2를 모두 사용하려면 관리자 모드로 PowerShell을 열고 아래 명령어를 붙여넣으세요. 컴퓨터가 재부팅될 수 있습니다.

```powershell
If ((Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform, Microsoft-Windows-Subsystem-Linux).RestartNeeded) { Restart-Computer -Force }
```

설치가 끝난 다음에는 아래 명령어를 붙여넣으세요. 재부팅이 되었다면 다시 한 번 관리자 모드로 PowerShell을 열고 아래 명령어를 붙여넣으세요.

```powershell
wsl --set-default-version 2
```

### WSL v2용 최신 리눅스 커널 업데이트하기

WSL v2를 실행하려면 마이크로소프트가 배포하는 최신 버전의 리눅스 커널 패키지를 설치해야 합니다. 이 커널 패키지는 HCS 위에서 실행되는 WSL v2를 위한 전용 리눅스 커널입니다.

x64 프로세서를 쓰는 시스템에서는 아래와 같이 명령어를 실행합니다.

```powershell
Set-Location -Path $env:USERPROFILE\Downloads
$TargetUri = "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi"
Invoke-WebRequest -Uri $TargetUri -OutFile .\wsl_update_x64.msi
.\wsl_update_x64.msi
```

Surface Pro X처럼 ARM 프로세서를 쓰는 시스템에서는 아래와 같이 명령어를 실행합니다.

```powershell
Set-Location -Path $env:USERPROFILE\Downloads
$TargetUri = "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_arm64.msi"
Invoke-WebRequest -Uri $TargetUri -OutFile .\wsl_update_arm64.msi
.\wsl_update_arm64.msi
```

> NOTE: 2020년 9월 현재 배포되는 MSI 패키지는 msiexec.exe를 사용하여 MSI 패키지를 설치하는 것이 지원되지 않아서 커맨드라인으로 리눅스 커널 패키지 설치를 자동/무인 설치 방식으로 진행하는 것에 제한이 있는 상태입니다.

### Ubuntu 20.04 설치하기

WSL용 리눅스를 설치하는 방법은 스토어를 이용하는 방법과 직접 설치를 하는 방법이 있습니다. 스토어를 이용하면 설치와 관리가 간편하지만 스토어 앱을 초기화할 경우 WSL 설정이 날아가는 문제가 생길 수 있어 수동으로 설치하는 방법을 추천합니다.

PowerShell을 열고 아래 명령어를 붙여 넣습니다.

```powershell
Set-Location -Path $env:USERPROFILE\Downloads
$TargetUri = "https://aka.ms/wslubuntu2004"
Invoke-WebRequest -Uri $TargetUri -OutFile .\ubuntu.zip
New-Item -Type Container -Path $env:SYSTEMDRIVE\Distro\Ubuntu2004
Expand-Archive -Path .\ubuntu.zip -DestinationPath $env:SYSTEMDRIVE\Distro\Ubuntu2004
Remove-Item -Path .\ubuntu.zip
Set-Location -Path $env:SYSTEMDRIVE\Distro\Ubuntu2004
.\ubuntu2004.exe
```

설치를 끝내고나면 Windows Terminal에는 자동으로 새 항목이 등록됩니다.

만약에 Ubuntu 20.04 대신 다른 배포판을 설치하고 싶다면, 아래 부록을 참고하세요.

### 다른 리눅스 패키지 찾아보기

amd64 지원 호환 프로세서를 쓰시는 분들은 아래 패키지를 사용하실 수 있습니다.

* [Ubuntu 최신 버전](https://aka.ms/wslubuntu)
* [Ubuntu 20.04](https://aka.ms/wslubuntu2004)
* [Ubuntu 18.04](https://aka.ms/wsl-ubuntu-1804)
* [Ubuntu 16.04](https://aka.ms/wsl-ubuntu-1604)
* [Debian GNU/Linux](https://aka.ms/wsl-debian-gnulinux)
* [Kali Linux](https://aka.ms/wsl-kali-linux-new)
* [SUSE Linux Enterprise Server 12](https://aka.ms/wsl-sles-12)
* [SUSE Linux Enterprise Server 15 SP2](https://aka.ms/wsl-SUSELinuxEnterpriseServer15SP2)
* [SUSE Linux Enterprise Server 15 SP3](https://aka.ms/wsl-SUSELinuxEnterpriseServer15SP3)
* [openSUSE Tumbleweed](https://aka.ms/wsl-opensuse-tumbleweed)
* [openSUSE Leap 15.3](https://aka.ms/wsl-opensuseleap15-3)
* [openSUSE Leap 15.2](https://aka.ms/wsl-opensuseleap15-2)
* [Oracle Linux 8.5](https://aka.ms/wsl-oraclelinux-8-5)
* [Oracle Linux 7.9](https://aka.ms/wsl-oraclelinux-7-9)
* [Fedora Remix for WSL](https://github.com/WhitewaterFoundry/WSLFedoraRemix/releases/)

arm64 호환 프로세서를 쓰시는 분들은 아래 패키지를 사용하실 수 있습니다.

* [Ubuntu 20.04 ARM](https://aka.ms/wslubuntu2004arm)
* [Ubuntu 18.04 ARM](https://aka.ms/wsl-ubuntu-1804-arm)

[^A]: CPU 가상화 기술이 지원되어야 합니다. 만약 가상 컴퓨터에서 윈도우 10 또는 윈도우 11을 실행 중인 경우, 중첩 가상화 기능이 설정된 인스턴스에서만 WSL v2를 실행할 수 있습니다. 다만 일부 반기 채널 버전이나 프리뷰 버전을 제외하고 2022년 현재 윈도우 서버에서는 WSL v1만 사용 가능합니다.

[^B]: 윈도우 10 버전 2004 (10.0.19041) 이상의 OS가 필요합니다.

[^C]: 레거시 WSL은 WSL v1 이전에 나온 Bash on Ubuntu on Windows를 말하며, WSL v1으로 업그레이드가 필요합니다.

[^D]: [KB4566116](https://www.catalog.update.microsoft.com/Search.aspx?q=KB4566116) 핫픽스를 설치해야 WSL v2를 사용할 수 있습니다. 특별한 경우가 아니라면, 윈도우 업데이트를 이용하여 모든 업데이트를 설치하면 간편하게 적용이 가능합니다.

[^E]: [KB5004296](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5004296) 핫픽스를 설치해야 WSL v2를 사용할 수 있습니다. 특별한 경우가 아니라면, 윈도우 업데이트를 이용하여 모든 업데이트를 설치하면 간편하게 적용이 가능합니다.

[^F]: 일부 반기 채널 버전이나 프리뷰 버전을 제외하고, 윈도우 서버 2022의 경우 [KB5014021](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5014021) 및 연관되는 업데이트를 설치하면 사용 가능합니다. [자세한 내용 보기](https://techcommunity.microsoft.com/t5/itops-talk-blog/wsl2-now-available-on-windows-server-2022/ba-p/3447570) 단, 현재 WSLg는 사용할 수 없으며, 서버 코어 모드의 경우 `--install` 스위치를 통한 설치가 불가능할 수 있습니다.

[^G]: `--install` 스위치를 이용하여 한 번에 설치할 수 있는 방식을 말합니다.
