# Ubuntu에서 Go 개발 환경 구성

2026년 9월 5일 기준으로 Ubuntu 패키지와 Go 공식 배포 파일을 통해 Linux용 Go를 설치할 수 있습니다. Ubuntu 패키지 버전이 Go 프로젝트의 최신 릴리스와 같지는 않을 수 있습니다.

요구 버전 확인, 패키지 설치, 공식 배포 선택, 경로 설정, 빌드 검증을 다룹니다.

Ubuntu 터미널에서 프로젝트 요구 조건을 먼저 확인한 뒤 설치 방법을 선택합니다. [Go 공식 설치 안내](https://go.dev/doc/install)를 참고할 수 있습니다.

## 프로젝트 요구 버전 확인

프로젝트의 `go.mod`에 있는 `go`와 `toolchain` 지시문을 확인합니다. [Go toolchain 선택 문서](https://go.dev/doc/toolchain)에 버전 선택과 다운로드 동작을 설명했습니다.

## Ubuntu 패키지 설치

배포판이 제공하는 Go로 시작하려면 패키지 후보를 확인하고 설치합니다. [Ubuntu 패키지 검색](https://packages.ubuntu.com/search?keywords=golang-go)에서 릴리스별 패키지를 볼 수 있습니다.

```bash
sudo apt update
apt-cache policy golang-go
sudo apt install golang-go
go version
```

## 공식 Linux 배포 파일 선택

최신 릴리스나 특정 버전이 필요하면 [Go 다운로드 목록](https://go.dev/dl/)에서 Linux용 아카이브와 SHA256을 선택합니다. Ubuntu의 `uname -m`이 `x86_64`이면 amd64, `aarch64`이면 arm64 파일을 사용합니다.

기존 `/usr/local/go` 위에 덮어 풀지 않고 [공식 설치 절차](https://go.dev/doc/install)에 따라 교체합니다. 삭제 전에 해당 경로가 기존 Go 설치 디렉터리인지 확인합니다. 이 문서는 오래된 패치 버전과 삭제 명령을 묶어 자동 실행하지 않습니다.

## PATH와 도구 설치 경로

수동 설치에서 `/usr/local/go`를 사용했다면 `~/.bashrc` 또는 `~/.zshrc`에 다음 줄을 추가합니다. [Go 설치 문서](https://go.dev/doc/install)에 나온 실행 경로를 사용합니다.

```bash
export PATH="/usr/local/go/bin:$PATH"
```

새 셸에서 `go env GOPATH GOBIN`으로 도구 설치 경로를 확인할 수 있습니다. `GOBIN`이 비어 있으면 일반적으로 GOPATH 아래 `bin`을 사용합니다. `GOROOT`를 수동 지정하지 않아도 Go가 설치 위치를 찾습니다.

## 실제 도구와 프로젝트 검증

Ubuntu의 프로젝트 폴더에서 실행 경로와 테스트 결과를 확인합니다. [Go 명령 참조](https://pkg.go.dev/cmd/go)에 모듈과 테스트 명령을 설명했습니다.

```bash
command -v go
go version
go env GOOS GOARCH GOPATH GOROOT
go test ./...
```

## 버전 관리의 기준

여기까지 정리하면 배포판 패키지 또는 공식 Go 배포로 Linux 개발 환경을 구성할 수 있습니다. 설치 직후에는 프로젝트 테스트를 실행하고 장기적으로는 `go.mod`와 toolchain 정책을 관리합니다.

배포판 버전으로 충분하면 APT를 사용할 수 있습니다. 특정 버전이 필요한 프로젝트는 공식 배포 파일과 체크섬을 기준으로 설치합니다.
