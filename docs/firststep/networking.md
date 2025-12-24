# WSL 2 네트워킹 설정하기

WSL 2는 기본적으로 NAT(Network Address Translation) 네트워크 모드를 사용하지만, 최근 버전에서는 **미러드 네트워킹 모드(Mirrored Networking Mode)** 및 **virtioProxy 모드** 등 향상된 네트워크 기능이 추가되었습니다.

## 네트워킹 모드 비교

| 모드 | 안정성 | 성능 | 호환성 | 권장 사용 |
| --- | --- | --- | --- | --- |
| NAT (기본) | 높음 | 보통 | 보통 | 일반 사용 |
| mirrored | 실험적 | 높음 | 높음 | VPN 사용, IPv6 필요 시 |
| virtioProxy | 실험적 | 매우 높음 | 매우 높음 | 최신 환경, 고성능 필요 시 |

## 기본 네트워킹 모드 (NAT)

WSL 2의 기본 네트워크 모드는 NAT를 사용하여 Windows와 격리된 가상 네트워크 인터페이스를 생성합니다.

**장점:**

- 안정적이고 검증된 방식
- 대부분의 일반적인 사용 사례에 적합

**제약 사항:**

- WSL에서 실행되는 서비스에 Windows 외부에서 직접 접근하기 어려움
- 일부 VPN 소프트웨어와 호환성 문제 발생 가능
- IPv6 지원 제한적

## 미러드 네트워킹 모드 (실험적)

2023년 9월 업데이트에서 도입된 미러드 네트워킹 모드는 Windows의 네트워크 인터페이스를 Linux로 그대로 미러링합니다.

**장점:**

- IPv6 지원 개선
- VPN 호환성 향상
- localhost를 통한 더 나은 네트워크 접근성
- Windows와 WSL 간 네트워크 구성 일관성

**활성화 방법:**

`.wslconfig` 파일(`$env:USERPROFILE\.wslconfig`)에 다음과 같이 추가합니다:

```ini
[wsl2]
networkingMode=mirrored

[experimental]
autoMemoryReclaim=gradual
dnsTunneling=true
firewall=true
autoProxy=true
```

**추가 실험적 네트워크 옵션:**

- `dnsTunneling=true`: DNS 요청 처리 방식 개선
- `firewall=true`: Windows 방화벽 규칙을 WSL에도 적용
- `autoProxy=true`: Windows의 프록시 설정을 WSL에 자동으로 적용

설정 후 WSL을 재시작합니다:

```powershell
wsl.exe --shutdown
```

> 주의: 미러드 네트워킹 모드는 아직 실험적(experimental) 기능이므로 일부 환경에서 예상치 못한 동작이 발생할 수 있습니다.

## virtioProxy 네트워킹 모드 (최신 실험적)

2024년 후반부터 도입된 virtioProxy 모드는 미러드 모드의 개선판으로, virtio 프로토콜을 기반으로 Windows와 WSL 간의 네트워크 통신을 더욱 효율적으로 처리합니다.

**장점:**

- 미러드 모드의 모든 장점 포함
- 더 나은 네트워크 성능 및 처리량
- 낮은 지연 시간 (latency)
- 더 안정적인 네트워크 연결
- 향상된 멀티플렉싱 지원

**활성화 방법:**

`.wslconfig` 파일에 다음과 같이 설정합니다:

```ini
[wsl2]
networkingMode=virtioproxy

[experimental]
autoMemoryReclaim=gradual
dnsTunneling=true
firewall=true
autoProxy=true
```

> 참고: virtioProxy는 mirrored 모드보다 더 최신 기능이므로, 최신 버전의 WSL이 필요합니다. `wsl --version`으로 버전을 확인하세요.

**주의사항:**

- 아직 초기 실험적 단계이므로 프로덕션 환경보다는 테스트 환경에서 먼저 사용을 권장합니다
- 일부 환경에서 호환성 문제가 있을 수 있으며, 문제 발생 시 mirrored 또는 NAT 모드로 전환할 수 있습니다
- WSL GitHub 이슈 트래커를 통해 문제를 보고할 수 있습니다

**모드 변경 시:**

네트워킹 모드를 변경한 후에는 반드시 WSL을 재시작해야 합니다:

```powershell
wsl.exe --shutdown
```

## 컨테이너 런타임 호환성

### Podman Desktop

Podman Desktop을 사용하는 경우 네트워킹 모드 선택 시 주의가 필요합니다:

- ✅ **NAT 모드**: 완전히 지원됨
- ✅ **virtioProxy 모드**: 완전히 지원됨 (권장)
- ⚠️ **mirrored 모드**: 제대로 지원되지 않음

> Podman Desktop 사용자는 mirrored 모드 대신 virtioProxy 또는 NAT 모드를 사용하세요. mirrored 모드에서는 컨테이너 네트워크가 정상적으로 작동하지 않을 수 있습니다.

### Docker Desktop

Docker Desktop의 경우 모든 네트워킹 모드를 지원하지만, 성능을 위해서는 virtioProxy 또는 mirrored 모드를 권장합니다.

## VPN 사용 시 문제 해결

일부 VPN 소프트웨어(특히 Cisco AnyConnect 등)는 WSL의 NAT 네트워크와 충돌할 수 있습니다.

**해결 방법:**

1. **virtioProxy 모드 사용** (최신 WSL이 있는 경우)
   - `.wslconfig`에 `networkingMode=virtioproxy` 설정

2. **미러드 네트워킹 모드 사용**
   - 위에서 설명한 대로 `.wslconfig`에 `networkingMode=mirrored` 설정

3. **VPN 설정 조정**
   - Cisco AnyConnect의 경우: [공식 문서](https://www.cisco.com/c/en/us/support/docs/security/anyconnect-secure-mobility-client/215672-configure-anyconnect-to-work-with-wsl.html) 참고

4. **프록시 자동 미러링 활성화**
   - `.wslconfig`에 `autoProxy=true` 추가

## 추가 리소스

- [Microsoft Learn - WSL 네트워킹](https://learn.microsoft.com/windows/wsl/networking)
- [WSL Troubleshooting - 네트워크 문제](https://learn.microsoft.com/windows/wsl/troubleshooting#networking-issues)
- [WSL .wslconfig 설정 가이드](https://learn.microsoft.com/windows/wsl/wsl-config#wslconfig)
- [WSL September 2023 Update](https://devblogs.microsoft.com/commandline/windows-subsystem-for-linux-september-2023-update/)
- [WSL May 2024 Update](https://devblogs.microsoft.com/commandline/whats-new-in-the-windows-subsystem-for-linux-in-may-2024/)
- [WSL GitHub Releases](https://github.com/microsoft/WSL/releases)
