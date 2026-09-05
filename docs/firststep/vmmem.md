# WSL 2 메모리 사용량과 회수 설정

2026년 9월 5일 기준으로 WSL 2의 메모리 상한은 기본적으로 Windows 전체 RAM의 50%입니다. Linux 파일 캐시는 사용량에 포함되므로 작업 관리자의 Vmmem 또는 VmmemWSL 표시만으로 메모리 누수를 판단하지 않습니다.

Linux 사용량, Windows 설정, 메모리 상한, 자동 회수, 재시작 검증을 다룹니다.

먼저 실제 작업의 메모리 사용량을 확인한 뒤 제한을 적용합니다. 기본값과 옵션은 [WSL 설정 참조](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)를 기준으로 적었습니다.

## Linux에서 사용 가능한 메모리

Ubuntu에서 메모리와 프로세스 사용량을 확인합니다. `free`의 `available`은 새 작업에 사용할 수 있는 메모리를 추정하며 캐시를 포함한 `used`와 의미가 다릅니다. 세부 열은 [free 매뉴얼](https://manpages.ubuntu.com/manpages/noble/en/man1/free.1.html)에 설명되어 있습니다.

```bash
free -h
ps -eo pid,comm,rss --sort=-rss | head
```

## Windows 사용자별 WSL 설정

설정 위치부터 짚어보겠습니다. `.wslconfig`는 Windows 사용자 프로필에 두며 일반 WSL 2 배포판에 적용하는 가상 머신 설정을 담습니다. 배포판 안의 `/etc/wsl.conf`와 구분합니다. [설정 파일의 범위](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)를 확인할 수 있습니다.

PowerShell에서 파일을 엽니다.

```powershell
notepad.exe "$env:USERPROFILE\.wslconfig"
```

기존 파일이 있으면 복사본을 보관하고 필요한 키만 수정합니다. WSL Settings 앱에서도 해당 설정을 관리할 수 있습니다.

## RAM과 CPU 상한 예제

다음은 메모리 8GB, 논리 프로세서 4개, 스왑 2GB로 제한하는 예제입니다. 호스트 사양과 프로젝트 사용량에 맞게 값을 바꿉니다.

```ini
[wsl2]
memory=8GB
processors=4
swap=2GB
```

[기본값](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#configuration-settings-for-wslconfig)은 메모리 50%, Windows의 논리 프로세서 수, 전체 RAM의 25%를 GB 단위로 올림한 스왑 크기입니다. 예제의 상한이 모든 작업에 적합하지는 않습니다. 제한이 낮으면 대규모 빌드나 컨테이너가 메모리 부족으로 종료될 수 있습니다.

## 자동 메모리 회수 옵션

[자동 메모리 회수](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#experimental-settings)는 `[experimental]`에 설정하며 문서상 기본값은 `dropCache`입니다. `disabled`, `gradual`, `dropCache`를 구분합니다.

완만한 회수를 선택하는 예제는 다음과 같습니다.

```ini
[experimental]
autoMemoryReclaim=gradual
```

이어서 실제 작업을 실행한 뒤 유휴 상태에서 Windows와 Linux의 메모리 사용량을 비교합니다. 회수 시점과 효과는 워크로드에 따라 달라집니다. 최초 도입은 [WSL 2.0.0의 2023년 9월 업데이트](https://devblogs.microsoft.com/commandline/windows-subsystem-for-linux-september-2023-update/)에서 확인할 수 있으며 systemd 최소 버전인 WSL 0.67.6과 구분합니다.

## 재시작과 설정 복원

변경 사항은 WSL 가상 머신을 다시 시작한 뒤 적용합니다. [종료 명령](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#shutdown)은 실행 중인 모든 일반 배포판의 작업을 종료하므로 먼저 저장합니다.

PowerShell에서 종료한 뒤 실제 배포판 이름으로 다시 엽니다.

```powershell
wsl.exe --shutdown
wsl.exe -d Ubuntu-26.04
```

Ubuntu에서 `free -h`와 `nproc`으로 적용 결과를 확인합니다. 작업이 실패하면 변경한 키를 이전 값으로 돌리고 다시 시작합니다. wslc 세션의 자원 관리는 [컨테이너 CLI와 API](wslc.md)에서 별도로 확인합니다.

## 작업량에 맞춘 상한 관리

여기까지 정리하면 WSL 메모리는 사용 중인 프로세스와 캐시, 가상 머신 상한을 함께 비교할 수 있습니다. 변경 직후에는 실제 빌드를 실행하고 장기적으로는 프로젝트 규모가 달라질 때 상한을 조정합니다.

호스트 메모리 부족이 없다면 기본값을 유지할 수 있습니다. 여러 개발 도구를 동시에 실행한다면 상한과 자동 회수를 하나씩 바꾸어 작업 성공 여부를 확인합니다.
