# WSL 컨테이너와 wslc 시작하기

2026년 9월 5일 기준으로 Microsoft는 WSL 컨테이너를 공개 미리 보기로 제공합니다. WSL 2.9.3 이상이 필요하며 확인한 최신 사전 릴리스는 WSL 2.9.10입니다.

이 문서에서는 설치와 확인, 컨테이너 실행, 이미지 빌드, 로그와 정리, Windows 앱용 API와 호환성 범위를 다룹니다.

실습은 Windows PowerShell에서 진행합니다. Ubuntu 셸에서 Windows 명령을 호출하는 경우에는 `wslc.exe`처럼 확장자를 붙입니다.

미리 보기 적용 범위는 다음과 같습니다.

> 2026년 9월 5일에 [Microsoft의 컨테이너 안내](https://learn.microsoft.com/en-us/windows/wsl/wsl-container)를 확인했습니다. `wsl.exe --update --pre-release`로 참여하며 정식 출시 시 CLI와 API가 달라질 수 있습니다. 이 문서의 명령은 공식 자료와 대조했으며 Windows에서의 실행 검증은 별도로 진행할 수 있습니다.

## 사전 릴리스 설치와 CLI 확인

설치 절차부터 살펴보겠습니다. [공식 시작 가이드](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers)는 별도 컨테이너 엔진 설치 없이 WSL에 포함된 `wslc.exe`를 사용합니다. 기존 배포판의 [백업](../advanced/copy-distro.md)을 준비한 뒤 PowerShell에서 실행합니다.

```powershell
wsl.exe --update --pre-release
wsl.exe --version
Get-Command wslc.exe
wslc.exe version
wslc.exe --help
wslc.exe run --rm hello-world
```

`hello-world`는 이미지 다운로드와 컨테이너 실행을 함께 확인합니다. 명령을 찾을 수 없다면 Windows Terminal을 다시 열고 WSL 버전을 확인합니다. 회사 환경에서는 프록시와 허용된 레지스트리 정책도 다운로드에 영향을 줍니다.

## 웹 컨테이너 실행과 포트 연결

[컨테이너 실행 예제](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers#run-your-first-containers)를 바탕으로 nginx를 실행합니다. 로컬 포트 8080을 사용하므로 기존 서버와 충돌하지 않는 포트를 선택합니다.

```powershell
wslc.exe run -d --rm -p 8080:80 --name firststep-web nginx:stable
Invoke-WebRequest -UseBasicParsing http://localhost:8080/
wslc.exe container list
wslc.exe exec firststep-web cat /etc/os-release
```

웹 컨테이너는 로그 확인 단계까지 실행 상태로 둡니다. `--rm`으로 시작했으므로 정지할 때 자동 제거됩니다. 포트 공개 범위는 호스트 네트워크와 방화벽의 영향을 받습니다. 이 예제에는 비밀 정보나 외부 공개용 애플리케이션을 넣지 않습니다.

## Containerfile로 자체 이미지 빌드

이미지 빌드 입력과 실행 결과를 분리해 확인하겠습니다. 새 실습 폴더에서 `Containerfile`을 만들고 다음 내용을 저장합니다. [WSL 이미지 빌드 안내](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers#build-and-run-your-own-container-image)에 설명한 형식을 사용합니다.

```dockerfile
FROM alpine:3
CMD ["sh", "-c", "printf 'WSL container build OK\n'; uname -s"]
```

### 빌드한 이미지 실행

`Containerfile`이 있는 폴더의 PowerShell에서 아래 명령을 실행합니다. `-f`로 빌드 파일을 지정해 파일 이름에 따른 자동 탐색 차이를 피합니다.

```powershell
wslc.exe build -f Containerfile -t firststep-check:local .
wslc.exe image list
wslc.exe run --rm firststep-check:local
```

`WSL container build OK`와 `Linux` 출력을 확인하면 됩니다. `alpine:3` 같은 태그는 이후 다른 이미지를 가리킬 수 있습니다. 팀에서 빌드를 재현할 때에는 검증한 이미지 digest를 고정할 수 있습니다. 세부 옵션은 `wslc.exe build --help`에 표시합니다.

## 로그 확인과 선택한 자원 정리

[WSL 컨테이너 문제 해결](https://learn.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers#troubleshooting)의 `inspect`와 `logs` 명령으로 상태를 확인합니다. 다음 예제는 앞의 웹 컨테이너를 조회한 뒤 마지막 명령으로 정지합니다.

```powershell
wslc.exe container logs firststep-web
wslc.exe container inspect firststep-web
wslc.exe image inspect nginx:stable
wslc.exe container list --all
wslc.exe system info
wslc.exe container stop firststep-web
```

`wslc.exe system info`는 [WSL 2.9.10 릴리스](https://github.com/microsoft/WSL/releases/tag/2.9.10)에 추가되었습니다. 이전 버전에서는 해당 명령이 없을 수 있습니다. 종료한 실습 컨테이너는 `--rm`에 따라 제거되며 이미지 삭제는 `wslc.exe image rm firststep-check:local`처럼 대상을 지정합니다. `container prune`과 `image prune`은 여러 미사용 자원을 삭제하므로 정리 범위가 더 넓습니다.

## Windows 앱용 API와 도구 호환성

[공식 API 개요](https://learn.microsoft.com/en-us/windows/wsl/wsl-container#wsl-container-api)는 C, C++, C#에서 컨테이너를 사용할 수 있는 진입점을 제공합니다. `Microsoft.WSL.Containers` NuGet 패키지와 [공식 API 참조 및 예제](https://wsl.dev/api-reference/)에서 대상 프레임워크, 세션 수명, 입출력 처리 방법을 확인할 수 있습니다.

다만 친숙한 명령 형태가 Docker Engine API나 모든 Compose 기능의 동일한 동작을 보장하지는 않습니다. [Microsoft의 공개 미리 보기 발표](https://devblogs.microsoft.com/commandline/wsl-container-is-now-available-for-public-preview/)는 Dev Containers의 `0.462.0-pre-release`에서 Docker Path를 `wslc`로 설정하는 연동을 소개합니다. 설치한 확장 버전과 프로젝트 구성의 동작은 별도로 확인합니다. 기존 Docker Compose 작업은 [Docker Desktop 경로](docker.md)로 유지할 수 있습니다.

또한 컨테이너의 virtiofs와 consomme 도입 범위는 [발표의 플랫폼 변경 설명](https://devblogs.microsoft.com/commandline/wsl-container-is-now-available-for-public-preview/)을 따릅니다. 해당 설명을 일반 배포판의 `.wslconfig` 기본값으로 옮기지 않습니다.

## 실습 결과 점검 항목

1. WSL 2.9.3 이상과 `wslc.exe version` 출력을 기록합니다.
2. `hello-world`의 정상 종료를 확인합니다.
3. nginx의 HTTP 응답과 컨테이너 종료를 확인합니다.
4. 직접 빌드한 이미지의 메시지와 Linux 커널 출력을 확인합니다.
5. 실습 자원만 종료하거나 제거합니다.

## 도입 범위와 후속 확인

여기까지 정리하면 wslc는 Windows에서 Linux 컨테이너를 빌드하고 실행할 수 있는 내장 CLI와 API를 제공합니다. 지금은 실습 명령과 프로젝트 호환성을 확인할 수 있으며 정식 지원 범위는 이후 릴리스에서 다시 판단합니다.

단일 컨테이너 실습은 이 문서의 예제로 시작할 수 있습니다. Compose, Dev Containers, Windows 앱 배포에 의존하는 작업은 각 기능의 실제 지원 상태와 실행 결과를 기준으로 전환 범위를 정합니다.
