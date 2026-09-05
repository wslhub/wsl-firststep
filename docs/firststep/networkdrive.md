# Windows 탐색기에서 WSL 파일 접근

2026년 9월 5일 기준으로 Windows 탐색기는 WSL 네트워크 경로를 통해 배포판의 파일을 표시합니다.

현재 폴더 열기, 배포판 선택, 홈 경로, 즐겨찾기, 파일 편집 범위를 다룹니다.

Ubuntu에서 현재 폴더를 여는 방식부터 시작합니다. [Microsoft 파일 시스템 안내](https://learn.microsoft.com/en-us/windows/wsl/filesystems)를 참고할 수 있습니다.

## Ubuntu의 현재 폴더 열기

Ubuntu 터미널에서 프로젝트 폴더로 이동한 뒤 Windows 탐색기를 실행합니다.

```bash
explorer.exe .
```

명령을 찾을 수 없다면 [Windows 상호 운용 설정](bridge.md)을 확인합니다.

## Windows에서 배포판 목록 열기

탐색기 주소 표시줄에 `\\wsl.localhost\`를 입력합니다. 기존 `\\wsl$\` 경로도 사용할 수 있습니다. [Microsoft WSL 설정 문서](https://learn.microsoft.com/en-us/windows/wsl/wsl-config)는 `\\wsl.localhost` 경로의 예제를 제공합니다.

## 배포판의 사용자 홈 경로

예를 들어 `Ubuntu-26.04`의 `developer` 사용자 홈은 `\\wsl.localhost\Ubuntu-26.04\home\developer`로 접근합니다. 배포판 이름은 PowerShell의 `wsl.exe --list --quiet`에서 확인합니다.

다만 Windows 사용자 이름과 Linux 사용자 이름은 다를 수 있습니다. [WSL 사용자 환경 안내](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password)에 따라 Ubuntu의 `whoami` 결과를 사용합니다.

## 자주 사용하는 경로 보관

홈이나 프로젝트 폴더를 탐색기의 빠른 실행 또는 홈에 고정하면 경로를 다시 입력하지 않아도 됩니다. 드라이브 문자가 필요한 도구라면 탐색기의 네트워크 드라이브 연결에 해당 UNC 경로를 지정할 수 있습니다.

이어서 배포판을 제거하거나 이름을 바꾸면 보관한 경로도 수정합니다. Windows 탐색기의 기본 동작은 [Microsoft 탐색기 안내](https://support.microsoft.com/windows/file-explorer-in-windows-ef370130-1cca-9dc5-e0df-2f7416fe1cb1)를 참고할 수 있습니다.

## Linux 파일 편집과 저장 위치

[파일 저장 안내](https://learn.microsoft.com/en-us/windows/wsl/filesystems#file-storage-and-performance-across-file-systems)에 따라 Linux 도구로 처리할 파일은 Linux 홈 아래에 둘 수 있습니다. Linux 파일 권한과 대소문자를 구분하는 프로젝트는 [VS Code WSL](vscode.md)에서 편집할 수 있습니다.

배포판 저장소의 `ext4.vhdx`를 Windows 편집 도구로 직접 변경하지 않습니다. 등록된 WSL 경로나 `explorer.exe .`를 통해 파일에 접근합니다.

## 파일 접근 경로의 선택

여기까지 정리하면 Windows와 Ubuntu에서 같은 Linux 프로젝트 폴더를 열 수 있습니다. 당장 파일을 찾을 때에는 탐색기 경로를 사용하고 장기적인 개발 작업에는 Linux 파일 시스템의 권한과 대소문자 규칙을 유지합니다.

단발성 파일 이동에는 탐색기를 사용할 수 있습니다. 반복 빌드와 편집에는 WSL에 연결한 개발 도구를 적용합니다.
