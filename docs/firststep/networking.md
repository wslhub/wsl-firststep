# WSL 2 네트워크 모드와 연결 진단

2026년 9월 5일 기준으로 Microsoft의 일반 WSL 설정 문서는 NAT를 기본 네트워크 모드로 안내합니다. Windows 11 버전 22H2 이상에서는 mirrored 모드와 DNS 터널링을 사용할 수 있습니다.

네트워크 모드, 설정 파일, 호스트 연결, VPN 진단, 컨테이너와의 범위를 다룹니다.

먼저 현재 연결을 확인하고 필요한 설정만 바꾼 뒤 같은 연결을 다시 시험합니다. [공식 네트워킹 안내](https://learn.microsoft.com/en-us/windows/wsl/networking)를 기준으로 작성했습니다.

## 모드별 적용 조건

[설정 참조](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#configuration-settings-for-wslconfig)에 명시한 차이를 정리하겠습니다. 모드 이름만으로 성능이나 모든 VPN의 호환성을 판단하지 않습니다.

| 모드 | 적용 조건 또는 동작 | 사용 시 확인할 항목 |
| --- | --- | --- |
| `nat` | 일반 WSL의 기본값 | Windows와 WSL의 IP 구분 |
| `mirrored` | Windows 11 버전 22H2 이상 | IPv6, VPN, Hyper-V 방화벽 |
| `virtioproxy` | WSL 2.3.25부터 NAT 실패 시 대체 경로 | 설치 버전과 실제 연결 |
| `bridged` | WSL 2.4.5부터 사용 중단 대상으로 지정 | 기존 설정의 이전 |

VirtioProxy를 mirrored의 상위 호환 모드로 설명하지 않습니다. 네트워크 요구 조건과 문제 재현 결과를 기준으로 선택합니다.

## mirrored와 DNS 설정

Windows 사용자 프로필의 `.wslconfig`에서 기존 `[wsl2]` 섹션에 필요한 키를 병합합니다. [DNS와 프록시 옵션](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)은 `[experimental]`에 두지 않습니다.

아래 예제는 Windows 11 버전 22H2 이상의 mirrored 구성을 보여 줍니다.

```ini
[wsl2]
networkingMode=mirrored
dnsTunneling=true
firewall=true
autoProxy=true
```

실행 중인 모든 WSL 작업을 저장한 뒤 PowerShell에서 `wsl.exe --shutdown`을 실행하고 배포판을 다시 엽니다. DNS 터널링을 사용할 때에는 배포판의 `/etc/wsl.conf`에서 `generateResolvConf=false`로 자동 생성을 막았는지도 확인합니다. 관련 조건은 [WSL 문제 해결](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)에 설명되어 있습니다.

## Windows와 Linux 서비스 연결

Windows 브라우저에서는 WSL 개발 서버의 `http://localhost:포트`로 접속할 수 있습니다. 반대로 WSL에서 Windows 서버로 연결할 때 NAT에서는 호스트 IP를 사용하고 mirrored에서는 IPv4 `127.0.0.1` 연결을 사용할 수 있습니다. [접속 방향별 안내](https://learn.microsoft.com/en-us/windows/wsl/networking)를 기준으로 구분합니다.

Ubuntu에서 NAT 기본 경로의 호스트 주소를 확인합니다.

```bash
ip route show default
```

LAN의 다른 컴퓨터에서 접속하려면 서버의 수신 주소, 포트 공개, Windows와 Hyper-V 방화벽을 함께 구성합니다. 방화벽 전체를 비활성화하는 방법을 기본 절차로 사용하지 않습니다.

## VPN과 프록시 문제 진단

이어서 DNS 해석과 HTTPS 연결을 나누어 확인합니다. Ubuntu에서 다음 명령을 실행한 뒤 VPN 연결 전후의 결과를 비교합니다.

```bash
getent ahosts learn.microsoft.com
curl -I https://learn.microsoft.com/
```

DNS만 실패하면 터널링과 `/etc/resolv.conf` 생성 설정을 확인합니다. DNS는 성공하지만 HTTPS가 실패하면 프록시, 신뢰 인증서, 방화벽을 확인합니다. 적용한 키만 이전 값으로 복원하고 WSL을 재시작하면 변경 전후를 비교할 수 있습니다. [공식 문제 해결 문서](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)에 알려진 VPN 제약을 정리했습니다.

## Docker와 wslc의 구분

[Docker Desktop의 WSL 백엔드](https://docs.docker.com/desktop/features/wsl/)는 제품 자체의 네트워크 설정도 사용합니다. Podman이나 Docker가 모든 WSL 모드에서 같은 방식으로 동작한다고 단정하지 않습니다.

다만 [WSL 컨테이너 공개 미리 보기](https://devblogs.microsoft.com/commandline/wsl-container-is-now-available-for-public-preview/)의 consomme 기본 네트워킹은 컨테이너에 대해 발표한 변경입니다. 일반 배포판의 모드를 바꾸는 절차와 [wslc 실습](wslc.md)을 구분해 적용합니다.

## 연결 변경 후 점검

1. DNS 해석과 HTTPS 접속을 각각 확인합니다.
2. Windows에서 WSL 개발 서버로 접속합니다.
3. 필요한 경우 WSL에서 Windows 서버로 접속합니다.
4. VPN을 사용하는 상태에서 같은 작업을 반복합니다.

## 환경별 네트워크 선택

여기까지 정리하면 WSL 네트워크는 접속 방향과 Windows 버전에 따라 설정이 달라집니다. 변경 직후에는 실제 개발 서버와 VPN 연결을 확인하고 장기적으로는 사용 중인 컨테이너 도구의 지원 조건을 함께 관리합니다.

현재 NAT에서 문제가 없다면 그 구성을 유지할 수 있습니다. IPv6나 호스트 연결 요구가 있는 Windows 11 환경에서는 mirrored를 적용한 뒤 실제 연결 결과로 판단합니다.
