# Ubuntu 설치 후 초기 설정

2026년 9월 5일 기준으로 Ubuntu 26.04 LTS와 Ubuntu 24.04 LTS의 WSL 환경을 다룹니다. Ubuntu 릴리스에 따라 패키지 버전과 기본 서비스 구성이 달라집니다.

패키지 갱신, APT 저장소, 한국어 로캘, 선택형 셸 도구, systemd 상태를 설명합니다.

Ubuntu 터미널에서 기본 설정을 진행한 뒤 필요한 도구를 추가합니다. PowerShell 명령은 별도로 표시했습니다.

## 패키지 목록과 설치 상태 갱신

현재 배포판 정보와 기본 패키지부터 살펴보겠습니다. [Ubuntu 패키지 관리 문서](https://ubuntu.com/server/docs/how-to/software/package-management/)에 따라 목록을 갱신한 뒤 업그레이드 변경 내역을 확인합니다.

```bash
cat /etc/os-release
sudo apt update
sudo apt upgrade
sudo apt install ca-certificates curl git build-essential
```

사용하지 않는 의존성은 `sudo apt autoremove`가 제시하는 삭제 목록을 확인한 뒤 정리할 수 있습니다. 패키지 업그레이드는 Ubuntu의 다음 릴리스로 전환하는 명령과 구분합니다.

## APT 저장소 주소와 아키텍처

Ubuntu 24.04 이상은 주로 `/etc/apt/sources.list.d/ubuntu.sources`의 deb822 형식을 사용합니다. 기존 이미지에는 `/etc/apt/sources.list`가 남아 있을 수도 있습니다. [APT 저장소 형식](https://manpages.ubuntu.com/manpages/noble/en/man5/sources.list.5.html)에 맞추어 실제 파일부터 확인합니다.

```bash
dpkg --print-architecture
grep -R -E '^(URIs:|Suites:|Components:|deb )' \
  /etc/apt/sources.list /etc/apt/sources.list.d/ 2>/dev/null
```

다운로드 속도 문제가 있을 때에만 해당 파일을 백업하고 편집합니다. amd64용 아카이브와 Arm64용 `ports.ubuntu.com/ubuntu-ports`는 취급하는 패키지가 다르므로 호스트 이름을 일괄 치환하지 않습니다. 미러의 지원 아키텍처와 릴리스, 보안 업데이트 경로를 [Ubuntu 공식 미러 목록](https://launchpad.net/ubuntu/+archivemirrors)에서 확인할 수 있습니다.

## 한국어 UTF-8 로캘

한국어 메시지나 문자 처리가 필요하면 [Ubuntu 로캘 설정](https://help.ubuntu.com/community/Locale)에 따라 UTF-8 로캘을 구성합니다. 아래 명령은 Linux 앱의 메시지는 영어로 유지하면서 기본 로캘을 한국어로 지정합니다.

```bash
sudo apt install language-pack-ko
sudo locale-gen ko_KR.UTF-8
sudo update-locale LANG=ko_KR.UTF-8 LC_MESSAGES=C
```

이어서 터미널을 닫고 다시 연 뒤 `locale`로 결과를 확인합니다. Windows Terminal의 글꼴은 Windows에서 설정하며 Linux GUI 앱용 글꼴은 Ubuntu의 `fonts-noto-cjk` 패키지로 추가할 수 있습니다.

## Zsh와 fzf 선택 설치

Bash를 계속 사용해도 개발 환경 구성에는 지장이 없습니다. Zsh와 fzf가 필요하면 Ubuntu 패키지로 설치할 수 있습니다. [fzf 공식 설치 문서](https://github.com/junegunn/fzf)는 패키지 설치와 Git 설치를 모두 안내합니다.

1. Ubuntu에서 선택 도구를 설치합니다.

    ```bash
    sudo apt install zsh fzf
    ```

2. Zsh를 기본 셸로 사용하려면 셸을 변경합니다.

    ```bash
    chsh -s "$(command -v zsh)"
    ```

3. 터미널을 다시 연 뒤 `echo "$SHELL"`과 `fzf --version`으로 결과를 확인합니다.

fzf의 `Ctrl+R` 연동 방식은 설치된 버전에 따라 달라집니다. `fzf --help`와 배포판 패키지의 `/usr/share/doc/fzf/` 안내를 기준으로 구성합니다. [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh)는 선택 사항이며 기존 `.zshrc` 설정을 백업한 뒤 공식 설치 절차를 적용할 수 있습니다.

## systemd 실행 상태

[Microsoft systemd 안내](https://learn.microsoft.com/en-us/windows/wsl/systemd)에 따르면 WSL 0.67.6 이상에서 systemd를 지원합니다. Ubuntu 터미널에서 실제 PID 1과 서비스 상태를 확인합니다.

```bash
ps -p 1 -o comm=
systemctl status
```

PID 1이 `systemd`가 아니라면 기존 `/etc/wsl.conf`를 `sudoedit /etc/wsl.conf`로 열고 `[boot]` 섹션의 `systemd=true`를 설정합니다. 기존 섹션과 다른 설정은 보존합니다. 변경 뒤 실행 중인 작업을 저장하고 PowerShell에서 `wsl.exe --terminate Ubuntu-26.04`로 대상 배포판을 종료합니다. 실제 배포판 이름에 맞게 바꾼 뒤 다시 실행합니다.

`systemctl status`가 `degraded`를 표시하면 `systemctl --failed`로 실패한 서비스를 확인합니다. WSL 2는 가상 머신 종료와 재시작의 영향을 받으므로 서비스가 항상 실행되는 서버와 운영 방식이 다릅니다.

## 초기 설정 점검 항목

1. `sudo apt update`가 저장소 오류 없이 끝나는지 확인합니다.
2. 새 터미널에서 `whoami`, `locale`, `echo "$SHELL"`을 실행합니다.
3. 필요한 서비스가 있다면 PID 1과 해당 서비스 상태를 확인합니다.
4. [Visual Studio Code](vscode.md) 또는 [컨테이너 도구](docker.md) 설정으로 진행합니다.

## 개발 도구 추가의 기준

여기까지 정리하면 Ubuntu의 패키지 갱신과 사용자 환경 설정을 마쳤습니다. 설치 직후에는 저장소 오류와 로캘을 확인하고 장기적으로는 프로젝트가 요구하는 패키지 버전을 관리합니다.

기본 Bash 환경으로도 개발을 시작할 수 있습니다. 셸 꾸미기와 추가 서비스는 실제 작업에서 필요한 범위만 선택합니다.
