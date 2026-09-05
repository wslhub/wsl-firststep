# WSL 2 시간 차이 진단과 복구

2026년 9월 5일 기준으로 Ubuntu on WSL은 Hyper-V의 시간 동기화와 배포판의 시간 서비스 구성을 함께 사용합니다. 절전 복귀 후 시간 차이가 발생하면 Windows와 Linux의 실제 시각부터 비교합니다.

UTC 시각 비교, WSL 재시작, systemd 확인, 배포판별 NTP 동작, 오류 기록을 다룹니다.

시간대 표시 차이와 실제 시계 오차를 구분한 뒤 재현되는 조건을 확인합니다. [Canonical 시간 동기화 문서](https://ubuntu.com/wsl/docs/stable/explanation/time-sync/)를 기준으로 작성했습니다.

## Windows와 Linux의 UTC 시각

PowerShell에서 Windows와 대상 배포판의 UTC 시각을 연속으로 출력합니다. 배포판 이름은 실제 이름으로 바꿉니다.

```powershell
[DateTime]::UtcNow.ToString('o')
wsl.exe -d Ubuntu-26.04 -- date -u --iso-8601=seconds
```

[WSL의 Windows 시간대 설정](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#time-settings)은 시간대와 관련된 옵션입니다. 시간대가 같은지와 시계가 동기화되어 있는지는 구분해 판단합니다.

## 업데이트와 배포판 재시작

실제 시계 오차가 크면 Windows의 날짜 및 시간 설정에서 동기화 상태를 확인합니다. 실행 중인 WSL 작업을 저장한 뒤 PowerShell에서 WSL을 업데이트하고 재시작합니다.

```powershell
wsl.exe --update
wsl.exe --shutdown
wsl.exe -d Ubuntu-26.04 -- date -u --iso-8601=seconds
```

[종료 명령](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#shutdown)은 실행 중인 일반 WSL 배포판 전체에 영향을 줍니다. 재시작 후에도 오차가 반복되면 다음 정보를 기록합니다.

## systemd와 시간 서비스 상태

Ubuntu에서 실행 중인 init과 시간 서비스를 확인합니다. [systemd 지원](https://learn.microsoft.com/en-us/windows/wsl/systemd)이 가능하다는 사실만으로 시간 오류가 모두 해결되었다고 판단하지 않습니다.

```bash
ps -p 1 -o comm=
systemctl status chrony.service systemd-timesyncd.service --no-pager
```

설치하지 않은 서비스의 `not found`나 비활성 상태는 그 자체로 시간 오류의 증거가 되지 않습니다. 원인에 맞는 서비스만 진단합니다.

## Ubuntu 릴리스별 동기화 동작

[Canonical 안내](https://ubuntu.com/wsl/docs/stable/explanation/time-sync/#interacting-with-ntp-clients-in-ubuntu-on-wsl)에 따르면 Ubuntu 25.10부터 기본 NTP 클라이언트를 chrony로 전환했습니다. WSL에서는 기본 chrony 구성이 시간 차이를 관찰하더라도 시계를 조정하지 않을 수 있습니다. 이전 릴리스의 systemd-timesyncd 구성과 구분합니다.

다만 Hyper-V 동기화와 다른 NTP 서버를 동시에 사용하면 시계 조정이 충돌할 수 있습니다. 모든 환경에 chrony와 systemd-timesyncd를 함께 켜거나 셸을 열 때마다 root로 시간을 수정하는 명령을 넣지 않습니다. 수동 NTP가 필요한 환경에서는 공식 문서의 컨테이너 동기화 옵션과 조직의 시간 서버를 기준으로 구성합니다.

## 반복 오류에 대한 진단 자료

[WSL 문제 해결 문서](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)와 [시간 오차 추적 이슈](https://github.com/microsoft/WSL/issues/10006)를 참고해 아래 정보를 기록할 수 있습니다.

- Windows 빌드와 WSL 패키지 버전
- Ubuntu 릴리스와 PID 1
- Windows와 Linux의 UTC 시각 차이
- 절전 또는 최대 절전 모드의 복귀 시점
- 재시작 전후 결과와 사용 중인 NTP 서비스

## 복구 결과와 재현 조건

여기까지 정리하면 실제 시각 차이와 배포판 시간 서비스의 동작을 구분해 진단할 수 있습니다. 즉시 복구는 Windows 동기화와 WSL 재시작으로 확인하고 반복 증상은 절전 복귀 조건과 로그로 추적합니다.

기본 동기화가 정상이라면 별도 NTP 설정을 추가하지 않아도 됩니다. 관리형 시간 서버가 필요한 환경은 Windows와 Linux의 시간 공급원을 함께 구성합니다.
