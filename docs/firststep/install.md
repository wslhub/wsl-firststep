# 커맨드라인으로 WSL 2 설치하기

커맨드라인으로 WSL 2를 설치하면 간단하고 빠르게 WSL 2를 시작할 수 있습니다.

## 지원되는 윈도우 버전 확인하기

내가 실행하는 윈도우 10 버전이 정확히 어떻게 되는지 확인하려면 PowerShell에서 다음과 같이 실행합니다.

```powershell
cmd.exe /c ver
```

그 후 나타나는 버전 번호에 따라 WSL 2 지원 여부를 판단할 수 있습니다.

- x64 프로세서를 사용하는 컴퓨터에서는 윈도우 10 버전 1903 (빌드 번호 18362) 또는 버전 1909 (빌드 번호 18363)으로 업그레이드하고, 버전 번호 마지막 자릿수가 1049 이상인지 확인하여 이보다 낮으면 윈도우 업데이트를 끝까지 진행합니다.
- Surface Pro X 같은 ARM 프로세서를 사용하는 컴퓨터에서는 윈도우 10 2004 버전 (빌드 번호 19041) 이상으로 업데이트합니다.

위의 조건에 해당하는 OS를 가지고 있으면 WSL 2를 실행할 수 있는 OS를 가지고 있는 것입니다.

## Windows Terminal 설치하기

WSL 2를 사용하면서 기존의 내장 터미널을 사용해도 문제 없지만, 좀 더 풍부하고 다양한 기능을 사용하려면 Windows Terminal을 설치해서 사용하는 것이 좋습니다.

PowerShell을 열고 아래 명령어를 붙여넣으세요.

```powershell
Start-Process 'https://aka.ms/terminal'
```

그러면 Windows Terminal을 설치할 수 있는 스토어 페이지로 접근할 수 있고, 바로 설치를 시작할 수 있습니다.

## WSL, HCS 옵션 켜기

**NOTE: 윈도우, 리눅스, 맥, 그리고 퍼블릭 클라우드 환경에서 가상 컴퓨터 안에서 WSL을 사용하려고 Windows 10이나 Windows Server 2019 이상의 OS를 설치한 경우, 사용하는 가상 컴퓨터가 중첩 가상화 기능을 제공하는지 확인한 다음 이 단계를 따라하세요. 중첩 가상화가 작동하지 않는 가상 컴퓨터 상에 설치된 Windows 10에서는 WSL v1만 사용할 수 있습니다.**

WSL 1과 2를 모두 사용하려면 관리자 모드로 PowerShell을 열고 아래 명령어를 붙여넣으세요. 컴퓨터가 재부팅될 수 있습니다.

```powershell
If ((Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform, Microsoft-Windows-Subsystem-Linux).RestartNeeded) { Restart-Computer -Force }
```

설치가 끝난 다음에는 아래 명령어를 붙여넣으세요. 재부팅이 되었다면 다시 한 번 관리자 모드로 PowerShell을 열고 아래 명령어를 붙여넣으세요.

```powershell
wsl --set-default-version 2
```

## WSL 2용 최신 리눅스 커널 업데이트하기

WSL 2를 실행하려면 마이크로소프트가 배포하는 최신 버전의 리눅스 커널 패키지를 설치해야 합니다. 이 커널 패키지는 HCS 위에서 실행되는 WSL 2를 위한 전용 리눅스 커널입니다.

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

## Ubuntu 20.04 설치하기

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

## 다른 리눅스 패키지 찾아보기

- Ubuntu 18.04: https://aka.ms/wsl-ubuntu-1804
- Ubuntu 16.04: https://aka.ms/wsl-ubuntu-1604
- Debian/GNU Linux: https://aka.ms/wsl-debian-gnulinux
- Kali Linux: https://aka.ms/wsl-kali-linux-new
- OpenSUSE LEAP: https://aka.ms/wsl-opensuse-42
- SUSE Linux Enterprise: https://aka.ms/wsl-sles-12

Fedora Remix는 아래 Github 리포지터리 다운로드 페이지에서 받을 수 있습니다.

- https://github.com/WhitewaterFoundry/Fedora-Remix-for-WSL/releases

 Surface Pro X를 쓰시는 분들은 아래 패키지만 공식적으로 제공됩니다.
 
 - Ubuntu 20.04 ARM: https://aka.ms/wslubuntu2004arm
 - Ubuntu 18.04 ARM: https://aka.ms/wsl-ubuntu-1804-arm
 
