# WSL 배포판 복사와 복원

2026년 9월 5일 기준으로 WSL은 기존 배포판을 내보낸 뒤 새 이름으로 가져오는 기능을 제공합니다. 아래 절차는 원본을 유지하면서 같은 컴퓨터에 복사본을 만듭니다.

원본 확인, 내보내기, 해시 대조, 가져오기, 기본 사용자 설정과 복원 검증을 다룹니다.

PowerShell에서 파일 작업을 진행하며 Linux 설정은 대상 배포판 안에서 편집합니다. 다른 컴퓨터로 옮길 때에도 같은 절차를 응용할 수 있습니다.

## 원본과 복사본의 범위

복사할 대상을 먼저 정리하겠습니다. [WSL 내보내기와 가져오기](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#export-a-distribution)는 배포판의 파일 시스템을 다룹니다. Windows의 `.wslconfig`, Windows Terminal 설정, `/mnt/c` 같은 외부 마운트의 데이터는 별도로 보관합니다.

PowerShell에서 배포판 이름을 확인합니다.

```powershell
wsl.exe --list --verbose
```

아래 예제는 `Ubuntu-26.04`에서 `MyUbuntu`를 만듭니다. 이름과 경로는 실제 환경에 맞게 바꿉니다. 데이터베이스 등은 애플리케이션의 백업 또는 정상 종료 절차를 먼저 적용하면 복원 시 불일치를 줄일 수 있습니다. 백업에는 SSH 비밀 키, 토큰, 셸 기록도 포함될 수 있으며 다른 사람과 공유할 이미지라면 별도의 정리된 배포판에서 준비합니다.

## 대상 배포판 종료와 내보내기

원본의 작업을 저장하고 해당 배포판을 종료합니다. `--terminate`는 지정한 배포판을 즉시 종료하므로 저장되지 않은 작업에 영향을 줍니다. [명령 참조](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#terminate)에서 `--shutdown`과의 범위를 비교할 수 있습니다.

아래 예제는 기존 백업을 덮어쓰지 않도록 새 디렉터리를 생성하며 실패한 명령 뒤에는 중단합니다.

```powershell
$ErrorActionPreference = 'Stop'
$BackupDir = Join-Path $env:USERPROFILE 'WSL-Backups\Ubuntu-26.04-copy'
New-Item -ItemType Directory -Path $BackupDir -ErrorAction Stop | Out-Null
$Archive = Join-Path $BackupDir 'Ubuntu-26.04.tar'
wsl.exe --terminate Ubuntu-26.04
if ($LASTEXITCODE -ne 0) { throw '배포판 종료에 실패했습니다.' }
wsl.exe --export Ubuntu-26.04 "$Archive"
if ($LASTEXITCODE -ne 0) { throw '배포판 내보내기에 실패했습니다.' }
(Get-FileHash -Algorithm SHA256 -LiteralPath $Archive).Hash |
    Set-Content -Encoding ascii -LiteralPath "$Archive.sha256"
Get-Item -LiteralPath $Archive
```

원본 데이터, 아카이브, 복사본을 함께 보관할 여유 공간을 확보하면 됩니다. WSL이 내보내는 동안 원본을 다시 실행하지 않습니다.

## 해시 대조와 새 이름으로 가져오기

[Get-FileHash](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/get-filehash)는 파일 변경 여부를 대조하는 데 사용합니다. 해시 일치는 전송 중 변경이 없다는 증거이며 파일 제공자의 신뢰성까지 증명하지는 않습니다.

같은 PowerShell 세션에서 실행합니다. 새 세션이라면 위에서 사용한 `$BackupDir`와 `$Archive`를 다시 지정합니다.

```powershell
$ExpectedHash = (Get-Content -Raw -LiteralPath "$Archive.sha256").Trim()
$ActualHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $Archive).Hash
if ($ExpectedHash -ne $ActualHash) { throw '백업 파일의 해시가 일치하지 않습니다.' }
$InstallDir = Join-Path $env:LOCALAPPDATA 'WSL\MyUbuntu'
New-Item -ItemType Directory -Path $InstallDir -ErrorAction Stop | Out-Null
wsl.exe --import MyUbuntu "$InstallDir" "$Archive" --version 2
if ($LASTEXITCODE -ne 0) { throw '배포판 가져오기에 실패했습니다.' }
wsl.exe --list --verbose
```

기존에 `MyUbuntu`가 있으면 다른 새 이름과 디렉터리를 사용합니다. 다른 컴퓨터로 이전할 때에는 CPU 아키텍처가 호환되는지도 확인합니다.

## 일반 사용자와 기존 설정 보존

[가져온 배포판의 사용자 설정](https://learn.microsoft.com/en-us/windows/wsl/use-custom-distro#add-wsl-specific-components-like-a-default-user)에 따라 복사본의 계정을 확인합니다. 다음 명령으로 root 셸을 열고 `getent passwd`에서 원본의 일반 사용자 이름을 찾은 뒤 `/etc/wsl.conf`를 편집합니다.

```powershell
wsl.exe -d MyUbuntu -u root --cd ~
```

Linux에서 `getent passwd`를 실행하고 `editor /etc/wsl.conf` 또는 설치된 편집기로 파일을 엽니다. 아래 예제의 `developer`를 기존 계정 이름으로 바꾸고 기존 `[user]`가 있다면 그 안의 `default`만 수정합니다. 설정이 계정을 새로 만들지는 않습니다.

### wsl.conf의 기본 사용자

[배포판별 설정 참조](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#user-settings)에 따라 아래 내용을 반영합니다. `[boot]`를 비롯한 기존 설정을 보존합니다.

```ini
[user]
default=developer
```

레지스트리 편집이나 `/etc/wsl.conf` 전체 삭제 없이 설정할 수 있습니다. 최신 WSL의 `wsl.exe --manage MyUbuntu --set-default-user developer` 지원 여부는 설치된 `wsl.exe --help`로 확인할 수 있으며 이 문서는 파일 설정 방식을 사용합니다.

## 복사본 재시작과 데이터 검증

Linux 셸에서 `exit`로 나온 뒤 PowerShell에서 복사본을 재시작합니다. [사용자와 작업 디렉터리 옵션](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#run-a-specific-linux-distribution-from-powershell-or-cmd)으로 실행 결과를 확인합니다.

```powershell
wsl.exe --terminate MyUbuntu
wsl.exe -d MyUbuntu --cd ~ -- whoami
wsl.exe -d MyUbuntu --cd ~ -- pwd
wsl.exe -d MyUbuntu --cd ~
```

일반 사용자, 홈 파일, 개발 도구, 데이터베이스의 실제 데이터를 확인하면 복원 여부를 판단할 수 있습니다. 목록에 이름이 보이는 것만으로 데이터 복원이 모두 검증되지는 않습니다. 서비스 식별자와 SSH 호스트 키도 복제되므로 네트워크 서버로 함께 운용하거나 공유할 때에는 해당 서비스의 식별자 재발급 절차를 적용합니다.

WSL 2는 `--export ... --vhd`와 `--import ... --vhd`, `--import-in-place`도 제공합니다. 특히 `--import-in-place`는 지정한 VHDX 자체를 등록하며 새 복사본을 만들지 않습니다. 세부 형식은 [WSL 명령 참조](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#import-a-distribution)에서 확인할 수 있습니다.

## 복사 결과 점검 항목

1. 원본과 복사본 이름이 각각 등록되어 있는지 확인합니다.
2. 복사본의 일반 사용자와 프로젝트 파일을 확인합니다.
3. 필요한 서비스를 실행해 데이터를 읽을 수 있는지 확인합니다.
4. 백업 아카이브와 해시를 원본과 다른 보관 위치에 복사합니다.

`wsl.exe --unregister`는 해당 배포판의 등록과 데이터를 삭제합니다. 복사 절차에는 이 명령을 포함하지 않았습니다.

## 복사본의 보관과 활용

여기까지 정리하면 원본을 유지한 채 별도 이름의 배포판을 만들고 기본 사용자와 데이터를 검증할 수 있습니다. 복사 직후에는 실제 파일과 서비스를 확인하고 장기 보관 시에는 백업의 접근 권한과 복원 가능 여부를 관리합니다.

개인 실험용 복사본은 기존 설정을 유지할 수 있습니다. 다른 사람에게 전달하거나 여러 서버로 운용할 복사본은 비밀 정보와 서비스 식별자를 정리한 별도 이미지를 사용합니다.
