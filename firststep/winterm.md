# Windows Terminal 설정하기

Windows Terminal을 처음 설치하면 기본적으로 PowerShell을 사용하도록 설정되어있습니다. PowerShell 대신 WSL을 기본으로 사용하도록 만들려면 약간의 설정이 필요합니다.

## 기본으로 사용할 셸 타입 변경하기

- 시작 메뉴에서 `Windows Terminal` 이나 `wt`를 찾아 실행합니다.

- 설정 메뉴나 `Ctrl + ,` 키로 설정 파일을 엽니다.

- `profiles` -> `list` 항목에서 Ubuntu Linux 또는 사용하려는 WSL 배포판의 GUID 값을 찾습니다.

- 찾은 값을 복사하여 `defaultProfile` 에 붙여넣습니다.

- 파일을 저장하고 새 탭을 띄웠을 때 잘 열리는지 확인합니다.

## 홈 디렉터리를 리눅스 쪽으로 옮기기

- 정확한 경로를 파악하기 위해 우선 폴더 창에서 `\\wsl$\` 을 엽니다. 그 다음, 사용하려는 배포판에 해당하는 폴더에 들어가서 `home` 폴더 -> `사용자 이름` 폴더로 접근한 다음, 주소 창에서 주소를 복사합니다.

- `profiles` -> `list` 항목에서 Ubuntu Linux 또는 사용하려는 WSL 배포판에 해당하는 부분을 찾습니다.

- `startingDirectory` 프로퍼티에 WSL의 네트워크 드라이브 경로를 넣습니다. JSON 문법에 어긋나지 않게 백 슬래시는 두 번씩 써줍니다.

  ```json
  ...
  "startingDirectory": "\\\\wsl$\\Ubuntu-20.04\\home\\Username",
  ...
  ```
- 파일을 저장하고 새 탭을 띄웠을 때 잘 열리는지 확인합니다.

- `pwd` 명령을 실행하여 윈도우 쪽이 아닌 리눅스 쪽 홈 디렉터리로 잘 열리는지 확인합니다.

## Powerline 폰트 설정하기

Oh-my-zsh 등에서 사용하는 꾸밈 폰트가 잘 적용될 수 있도록 Powerline 폰트를 설치합니다. Windows Terminal과 함께 캐스캐디아 코드, 캐스캐디아 모노가 같이 배포되며, 한국어 글꼴과 폭이 맞는 서체를 찾으신다면 네이버의 D2코딩 폰트를 추천합니다.

- `profiles` -> `list` 항목에서 Ubuntu Linux 또는 사용하려는 WSL 배포판에 해당하는 부분을 찾습니다.

- `fontFace` 프로퍼티에 원하는 폰트를 넣습니다. JSON 문법에 어긋나지 않게 백 슬래시는 두 번씩 써줍니다.

  ```json
  ...
  "fontFace": "Cascadia Code PL",
  ...
  ```
- 파일을 저장하고 새 탭을 띄웠을 때 잘 열리는지 확인합니다.
