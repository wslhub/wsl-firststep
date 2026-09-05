# .wsl 이미지와 RootFS 파일 설치

2026년 9월 5일 기준으로 Ubuntu는 WSL용 `.wsl` 이미지를 배포합니다. WSL 2.4.10 이상에서는 이 형식으로 새 배포판을 설치할 수 있습니다.

이미지 선택, 파일 검증, `.wsl` 설치, RootFS 가져오기, 초기 사용자를 다룹니다.

공식 배포 이미지를 설치하는 경로부터 설명한 뒤 직접 만든 RootFS의 차이를 살펴보겠습니다. 이미 사용 중인 배포판은 [복사 가이드](copy-distro.md)를 적용합니다.

## Ubuntu 릴리스와 CPU 아키텍처

[Canonical 설치 문서](https://ubuntu.com/wsl/docs/stable/howto/install-ubuntu-wsl2/#method-2-download-and-install-from-the-ubuntu-archive)에 따라 [Ubuntu 릴리스 아카이브](https://releases.ubuntu.com/)에서 원하는 릴리스의 WSL 이미지를 선택합니다. 일반 서버 ISO나 cloud image를 WSL 이미지로 간주하지 않습니다.

PowerShell에서 현재 Windows 아키텍처를 확인합니다.

```powershell
[System.Runtime.InteropServices.RuntimeInformation]::OSArchitecture
```

x64에는 amd64, Arm64에는 arm64용 이미지를 선택합니다. 파일의 실제 이름과 다운로드 위치는 [공식 배포판 정의](https://github.com/microsoft/WSL/blob/master/distributions/DistributionInfo.json)에서도 확인할 수 있습니다. 이전 문서의 고정 `cloud-images` 파일명이 현재 존재한다고 가정하지 않습니다.

## 다운로드 파일의 무결성 확인

공식 이미지와 같은 릴리스의 체크섬 자료를 준비합니다. [Ubuntu 이미지 검증 안내](https://ubuntu.com/tutorials/how-to-verify-ubuntu)에 따라 체크섬 자료의 출처와 서명을 확인하면 파일 제공자까지 검증할 수 있습니다.

PowerShell에서 다운로드한 파일의 해시를 구합니다. 경로는 실제 파일명으로 바꿉니다.

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath .\ubuntu-image.wsl
```

출력 값을 해당 파일의 공식 SHA256 값과 대조합니다. 자체 생성한 해시와 파일만 함께 받았다면 제공자의 신뢰성까지 확인한 결과로 보지 않습니다.

## .wsl 파일로 배포판 설치

[.wsl 배포 형식](https://learn.microsoft.com/en-us/windows/wsl/build-custom-distro)은 초기 사용자 생성과 같은 배포판 초기화 설정을 포함할 수 있습니다. 이미지를 두 번 클릭하거나 PowerShell에서 설치합니다.

```powershell
wsl.exe --install --from-file .\ubuntu-image.wsl
wsl.exe --list --verbose
```

설치 시 나타나는 사용자 생성 안내를 따릅니다. 실제 등록 이름은 목록에서 확인합니다. 이 방식에는 Microsoft Store 접근이 필요하지 않지만 WSL 구성 요소는 먼저 설치되어 있어야 합니다.

## 일반 RootFS 아카이브 가져오기

직접 만든 Linux 루트 파일 시스템은 [WSL import 기능](https://learn.microsoft.com/en-us/windows/wsl/use-custom-distro)으로 등록할 수 있습니다. Windows용 `.wsl` 초기화 메타데이터를 갖춘 배포 이미지와 일반 tar 아카이브의 동작은 다를 수 있습니다.

PowerShell에서 새 이름과 비어 있는 설치 경로로 가져옵니다. `rootfs.tar`는 Linux 루트 디렉터리 내용이 아카이브 최상위에 있는 파일을 가정합니다.

```powershell
$ImportDir = Join-Path $env:LOCALAPPDATA 'WSL\MyUbuntu'
New-Item -ItemType Directory -Path $ImportDir -ErrorAction Stop | Out-Null
wsl.exe --import MyUbuntu "$ImportDir" .\rootfs.tar --version 2
if ($LASTEXITCODE -ne 0) { throw 'RootFS 가져오기에 실패했습니다.' }
wsl.exe -d MyUbuntu -u root
```

## 최초 사용자와 실행 검증

일반 RootFS에 사용자 계정이 없다면 Ubuntu 안에서 `adduser developer`와 `usermod -aG sudo developer`로 계정을 만들 수 있습니다. sudo 패키지가 없는 최소 이미지라면 패키지 설치도 별도로 진행합니다. [Microsoft의 사용자 구성 예제](https://learn.microsoft.com/en-us/windows/wsl/use-custom-distro#add-wsl-specific-components-like-a-default-user)를 참고할 수 있습니다.

이어서 `/etc/wsl.conf`에 기본 사용자를 지정하고 배포판을 재시작합니다. [복사 가이드의 사용자 설정](copy-distro.md)처럼 기존 파일을 보존하며 수정합니다.

1. 등록 이름과 WSL 2 실행 방식을 확인합니다.
2. 일반 사용자로 로그인해 홈 디렉터리를 확인합니다.
3. Ubuntu의 패키지 저장소와 필요한 개발 도구를 확인합니다.

## 이미지 선택의 기준

여기까지 정리하면 공식 `.wsl` 이미지는 새 설치에 사용하고 RootFS import는 사용자 정의 파일 시스템 등록에 사용할 수 있습니다. 설치 직후에는 초기 계정과 패키지 동작을 확인하고 장기 보관 시에는 원본 이미지의 출처와 체크섬을 함께 관리합니다.

새 Ubuntu 환경에는 공식 WSL 이미지를 선택할 수 있습니다. 기존 환경의 복제에는 내보내기와 가져오기 절차를 적용합니다.
