# Vmmem 메모리(RAM) 점유율 이슈 해결하기

WSL 2 환경을 처음 구축 시 WSL 2의 특성과 리눅스의 특성의 결합으로 인해, RAM 점유율 관련 이슈가 발생할 수 있습니다.

- 리눅스: RAM의 한계치까지 파일의 정보를 최대한 캠시로 보존.
- WSL 2: WSL 2에 할당된 RAM이 부족해지면 WSL 2에 추가적인 RAM을 할당.

> 참고: 최근 WSL 버전(2023년 9월 이후)에서는 **자동 메모리 회수(autoMemoryReclaim)** 기능이 실험적으로 제공되며, 이를 활용하면 캐시 메모리를 자동으로 회수하여 vmmem 점유율을 크게 줄일 수 있습니다.

## 램 사용량 보기

wsl 터미널에서 다음 명령어를 입력하면 램 사용량을 볼 수 있다.

```bash
free -h
```

이러한 램 할당을 제한하거나 자동 회수를 설정하려면 `.wslconfig` 파일에 설정을 입력해주어야 합니다.

`C:\Users\사용자이름\.wslconfig` 경로에 파일을 생성합니다. (PowerShell에서는 `$env:USERPROFILE\.wslconfig`)

```powershell
notepad $env:USERPROFILE\.wslconfig
```

그리고 해당 파일에 다음과 같이 입력합니다.

```ini
[wsl2]
memory=4GB
processors=2
swap=1GB
localhostForwarding=true
```

**설정 항목 설명:**

- `[wsl2]`: 설정 섹션의 시작을 나타냅니다.
- `memory=4GB`: WSL 2 가상 머신에 할당된 메모리 양을 설정합니다. (시스템 메모리의 50% 또는 8GB 중 작은 값이 기본값)
- `processors=2`: WSL 2 가상 머신에 할당된 가상 프로세서(코어)의 수를 설정합니다.
- `swap=1GB`: 스왑 파일의 크기를 설정합니다. 스왑 파일은 메모리가 부족한 경우 사용되며 추가 메모리 공간을 제공합니다.
- `localhostForwarding=true`: WSL 2 환경에서 로컬호스트 포트 포워딩을 활성화하는 설정입니다. Windows 호스트의 로컬 포트에 접근할 수 있도록 허용합니다.

해당 설정을 완료하고, WSL을 재시작합니다.

```powershell
wsl.exe --shutdown
```

그 다음 사용하려는 배포판을 다시 시작합니다.

```powershell
wsl.exe -d <배포판 이름>
```

## 자동 메모리 회수 기능 활용하기 (권장)

2023년 9월 업데이트부터 **autoMemoryReclaim** 설정이 도입되어, WSL 2가 사용하지 않는 캐시 메모리를 자동으로 Windows로 반환할 수 있습니다.

`.wslconfig` 파일에 다음과 같이 추가합니다:

```ini
[wsl2]
memory=4GB
processors=2

[experimental]
autoMemoryReclaim=gradual
```

**autoMemoryReclaim 옵션:**

- `gradual`: 점진적으로 메모리를 회수합니다 (권장)
- `dropcache`: 즉시 캐시를 해제합니다 (더 적극적)
- `disabled`: 자동 회수를 비활성화합니다 (기본값)

> 참고:
>
> - 이 기능은 아직 실험적(experimental) 단계이므로 일부 워크로드에서 예상치 못한 동작이 발생할 수 있습니다.
> - Docker Desktop 사용자의 경우 이 기능을 활성화하면 메모리 사용량이 크게 개선됩니다.
> - 자세한 내용: <https://devblogs.microsoft.com/commandline/windows-subsystem-for-linux-september-2023-update/>

설정 후 WSL을 재시작하여 적용합니다:

```powershell
wsl.exe --shutdown
```
