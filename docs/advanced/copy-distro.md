# WSL 배포판 복사하기

기본적으로 Microsoft Store를 통하거나 정식 설치 프로그램을 통하여 배포판을 설치하면, 미리 지정된 배포판 이름으로만 고정하여 설치가 가능한 제약 사항이 있습니다. 이런 제약 사항을 피하기 위해서는 배포판을 복사해야하는데, 이 가이드에서는 배포판을 복사하여 설치하는 방법을 설명합니다.

> ⚠️ **경고**
>
> 이 가이드의 내용을 응용하여 다른 컴퓨터로 배포판을 백업하고 복원할 수도 있습니다. 단, 배포판을 복사하여 전송하기 전에 반드시 민감한 정보 (예: SSH 비밀 키, `bash`나 `zsh` 등의 셸이 남기는 명령어 히스토리 파일 등)는 미리 삭제한 후 백업하는 것을 권장합니다.
>
> WSL v1의 경우 확장된 NTFS 파일 시스템을 사용하기 때문에, 여러가지 요인들로 인하여 메타데이터가 손상될 수 있고, 때에 따라서는 WSL 배포판의 데이터가 소실되는 문제가 발생할 수 있습니다. WSL v1을 주로 사용할 경우 배포판을 내보내거나 가져오는 것과는 별개로 중요한 데이터는 실행 가능한 상태일 때 추가로 백업하는 것을 추천합니다.

## 배포판 내보내기

의도하지 않은 입출력 오류로 인하여 배포판이 손상되는 것을 막기 위해, WSL 시스템 전체를 먼저 종료해야 합니다.

```powershell
wsl.exe --shutdown
```

그 다음, 내보내려는 배포판의 이름을 확인합니다.

```powershell
wsl.exe --list --verbose
```

내보내려는 배포판의 이름을 확인한 후, 다음과 같이 명령어를 입력합니다. 여기서는 `Ubuntu-20.04` 배포판을 사용자 홈 디렉터리에 내보내는 것을 가정하겠습니다.

```powershell
wsl.exe --export Ubuntu-20.04 $env:USERPROFILE\Ubuntu-20.04.tar
```

배포판의 크기, 디스크 입출력 속도, 그리고 WSL 버전에 따라 차이가 있을 수 있으며, 시간이 오래 걸리는 작업이므로 완료될 때까지 다른 WSL 배포판을 실행하지 않도록 주의합니다.

또한 기존 배포판이 차지하는 공간만큼 추가 디스크 공간이 필요하므로, 디스크 공간이 여유가 없을 경우 별도의 외부 저장 장치를 사용하여 백업을 진행하는 것을 권장합니다.

백업이 끝나면 파일이 잘 만들어졌는지 확인합니다.

```powershell
dir $env:USERPROFILE\Ubuntu-20.04.tar
```

또한 만들어진 백업 파일이 오염되거나 편집되는 것을 막기 위하여, SHA1SUM을 생성하여 기록해두었다가, 나중에 사용할 때 대조하는 것을 강력히 권장합니다. SHA1SUM을 만들기 위하여 PowerShell에서 다음의 명령어를 입력합니다. (파일 경로는 적절하게 변경합니다.)

```powershell
(Get-FileHash -Algorithm SHA1 -Path $env:USERPROFILE\Ubuntu-20.04.tar).Hash | Out-File -FilePath $env:USERPROFILE\Ubuntu-20.04.tar.txt
Get-Content -Path $env:USERPROFILE\Ubuntu-20.04.tar.txt
```

## 배포판 가져오기

> ⚠️ **경고**
>
> 배포판을 복원하기 전에, 복원하려는 파일이 신뢰할 수 있는 파일인지 다시 한 번 확인합니다. 악성 코드 등으로 오염된 배포판을 사용할 경우 시스템에 치명적인 문제가 발생하거나, 개인 정보나 민감한 정보가 탈취될 수 있습니다.

만들어진 배포판을 다시 복원하기 앞서, SHA1SUM 파일의 내용을 다시 검증합니다.

```powershell
(Get-Content -Path $env:USERPROFILE\Ubuntu-20.04.tar.txt) -eq (Get-FileHash -Algorithm SHA1 -Path $env:USERPROFILE\Ubuntu-20.04.tar).Hash
```

위 명령을 실행했을 때 나오는 결과가 `True`로 표시되면 문제가 없는 것입니다.

그 다음 배포판을 복원하기 위하여 다음과 같이 명령어를 입력합니다. 여기서는 사용자 홈 디렉터리에 만들어진 tar 파일을 `MyUbuntu` 라는 이름으로 `C:\Distro\MyUbuntu` 폴더에 WSL v2로 복원하는 것으로 가정하겠습니다.

```powershell
mkdir C:\Distro\MyUbuntu
wsl.exe --import MyUbuntu C:\Distro\MyUbuntu $env:USERPROFILE\Ubuntu-20.04.tar --version 2
```

백업 파일의 크기, 디스크 입출력 속도, 그리고 WSL 버전에 따라 차이가 있을 수 있으며, 시간이 오래 걸리는 작업이므로 완료될 때까지 기다립니다.

또한 추가 디스크 공간이 필요하므로, 디스크 공간이 여유가 없을 경우 별도의 외부 저장 장치를 사용하여 복원을 진행하는 것을 권장합니다.

정상적으로 복원되었는지 확인하기 위하여 목록 확인 명령어를 실행해보겠습니다.

```powershell
wsl.exe --list --verbose
```

`MyUbuntu` 라는 항목의 버전이 `2`로 표시된다면 정상적으로 복원된 것입니다.

## 기본 사용자 변경하기

> ⚠️ **경고**
>
> 이 작업은 레지스트리 설정 변경을 동반하는 작업입니다. 예기치 않은 사고를 방지하기 위하여 시스템 백업을 먼저 진행하시는 것을 권장합니다.

공식 WSL 설치 진입점을 이용할 경우, 맨 처음에는 기본으로 사용할 사용자 계정의 이름과 비밀 번호를 입력받는 것을 본 적이 있을 것입니다. 이 과정은 내부적으로 `root` 계정이 배포판 내에 처음부터 들어있기 때문에 가능한 동작이며, 가져오기 기능을 통해서 배포판을 다시 설치한 경우에도 `root` 사용자 계정을 기본으로 사용하게 됩니다.

따라서 이전처럼 원래 사용하던 계정으로 돌아가려면 배포판 안에 어떤 계정이 들어있는지 다시 한 번 확인하여 정확한 UID 값을 레지스트리에 지정해야 합니다.

사용자 이름을 정확히 안다면 이 단계를 건너뛰고, 그렇지 않다면 등록된 사용자들의 목록을 확인하기 위하여 다음의 명령어를 실행합니다. 여기서는 `MyUbuntu` 배포판을 사용하는 것을 가정하겠습니다.

```powershell
wsl.exe --distribution MyUbuntu --user root -- cat /etc/passwd
```

원하는 사용자 이름이 표시되거나, 정확한 사용자 이름을 알고 있다면 다음엔 아래의 명령어를 실행합니다.

```powershell
wsl.exe --distribution MyUbuntu --user rkttu -- id -u
```

확인한 사용자 ID 값을 레지스트리에 설정해야 합니다. 관리자 권한으로 권한 상승한 PowerShell 프롬프트에서 다음의 명령어를 입력합니다. `$DistroName`과 `$UserId` 환경 변수만 적절하게 변경합니다.

```
$DistroName='MyUbuntu'
$UserId='rkttu'
$DefaultUid=(wsl.exe --distribution $DistroName --user $UserId -- id -u)
Get-ItemProperty Registry::HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Lxss\*\ DistributionName | Where-Object -Property DistributionName -eq $DistroName | Set-ItemProperty -Name DefaultUid -Value $DefaultUid
```

이제 해당 배포판을 실행 중이었다면 종료하고 다시 실행합니다.

### 트러블슈팅

만약 기본 사용자 변경이 제대로 동작하지 않는다면, `root` 사용자 계정 앞으로 `/etc/wsl.conf` 파일에 기본 사용자 설정이 들어가 있기 때문일 수 있습니다. 다음의 명령어를 실행하여 `[user]` 섹션과 함께 `default=` 설정이 들어있는지 확인합니다.

```powershell
wsl.exe --distribution 'MyUbuntu' --user root -- cat /etc/wsl.conf
```

이 때에는 해당 파일의 설정이 더 우선시되므로, 파일을 삭제하거나 해당되는 설정을 제거하여 저장합니다.

그 다음 아래 명령어를 사용하여 WSL 전체를 Shutdown하고 다시 해당 배포판을 시작합니다. 이렇게 하는 이유는, `/etc/wsl.conf`의 설정은 레지스트리와는 별개로 WSL의 코어 시스템인 `LxssManager`에 직접 적용되는 설정이고, 해당 서비스를 다시 시작하기 전까지는 설정이 유지되기 때문입니다.

```poweshell
wsl.exe --shutdown
wsl.exe --distribution 'MyUbuntu'
```

