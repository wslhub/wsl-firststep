# Windows와 Linux 도구의 상호 운용

2026년 9월 5일 기준으로 WSL은 Linux 셸에서 Windows 실행 파일을 호출하는 기능을 제공합니다. 일부 배포판 설정은 이 기능이나 Windows PATH 추가를 비활성화할 수 있습니다.

실행 파일 호출, 경로 변환, URL 열기, Python 도우미, 설정 확인을 다룹니다.

기본 상호 운용 명령을 먼저 사용한 뒤 필요한 경우에만 별도 도우미를 추가합니다. [Microsoft 상호 운용 문서](https://learn.microsoft.com/en-us/windows/wsl/filesystems#run-windows-tools-from-linux)에 실행 규칙을 설명했습니다.

## Windows 실행 파일 호출

Ubuntu에서 Windows 프로그램은 확장자를 포함해 실행합니다.

```bash
notepad.exe
explorer.exe .
```

## 경로 형식 변환

Linux 경로를 Windows 프로그램에 전달할 때에는 `wslpath`로 변환할 수 있습니다. [WSL 상호 운용 설명](https://wsl.dev/technical-documentation/interop/)에서 실행 경계를 확인할 수 있습니다.

```bash
wslpath -w "$PWD"
```

## Windows 기본 브라우저로 URL 열기

Ubuntu에서 고정 URL을 Windows 셸에 전달하는 예제입니다. PowerShell의 [Start-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process)를 사용합니다.

```bash
powershell.exe -NoProfile -Command "Start-Process 'https://wslhub.com/wsl-firststep/'"
```

임의의 입력을 셸 명령 문자열에 그대로 결합하면 인용 부호와 특수 문자에 따라 다른 명령이 될 수 있습니다.

## Python 도우미의 격리 설치

`xdg-open` 호환 도우미가 필요하면 [xdg-open-wsl 프로젝트](https://github.com/cpbotha/xdg-open-wsl)의 최신 설치와 사용법을 확인할 수 있습니다. 최신 Ubuntu에서는 시스템 Python의 `pip install --user`가 관리 정책에 따라 거부될 수 있습니다.

이어서 Python CLI 도구는 [pipx](https://github.com/pypa/pipx#install-pipx) 또는 별도 가상 환경으로 격리할 수 있습니다. `--break-system-packages`를 기본 설치 방법으로 추가하지 않습니다.

## 상호 운용 설정 확인

[WSL interop 설정](https://learn.microsoft.com/en-us/windows/wsl/wsl-config#interop-settings)은 `/etc/wsl.conf`의 `[interop]`에서 관리합니다. `enabled`는 Windows 프로세스 실행, `appendWindowsPath`는 Windows PATH 추가를 제어합니다.

Ubuntu에서 파일을 확인합니다. 파일이 없으면 기본 설정을 사용합니다.

```bash
cat /etc/wsl.conf
```

## 기본 기능과 추가 도구의 범위

여기까지 정리하면 WSL의 기본 상호 운용으로 편집기, 탐색기, 브라우저를 호출할 수 있습니다. 현재 명령을 찾지 못하는 문제는 PATH와 설정에서 확인하고 장기적으로 사용하는 도우미는 별도 환경에서 관리합니다.

기본 Windows 프로그램 호출로 충분하면 추가 패키지를 생략할 수 있습니다. `xdg-open`을 요구하는 앱에는 호환 도우미의 실제 동작을 확인해 적용합니다.
