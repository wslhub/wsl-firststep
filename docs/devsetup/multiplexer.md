# Windows Terminal 화면 분할 단축키

2026년 9월 5일에 Microsoft의 Windows Terminal 기본 단축키 안내를 확인했습니다. 키 바인딩을 변경했다면 설치된 Terminal의 설정이 우선합니다.

화면 분할, 포커스 이동, 크기 조절, 닫기, 명령 팔레트 사용을 다룹니다.

기본 프로필은 [Windows Terminal 설정](../firststep/winterm.md)에서 구성한 뒤 아래 키를 사용할 수 있습니다.

## 좌우와 위아래 화면 분할

[패널 생성 안내](https://learn.microsoft.com/en-us/windows/terminal/panes#creating-a-new-pane)에 따른 기본 키부터 정리하겠습니다.

| 작업 | 기본 단축키 | 결과 |
| --- | --- | --- |
| 좌우 분할 | `Alt+Shift++` | 오른쪽에 새 패널 |
| 위아래 분할 | `Alt+Shift+-` | 아래쪽에 새 패널 |
| 프로필을 골라 분할 | `Alt`를 누른 채 프로필 메뉴 클릭 | 선택한 프로필로 새 패널 |

키보드 배열에 따라 `+` 입력 위치가 다를 수 있습니다. 설정의 작업 화면에서 `splitPane`에 연결한 키를 확인할 수 있습니다.

## 인접 패널로 포커스 이동

[포커스 이동](https://learn.microsoft.com/en-us/windows/terminal/panes#switching-between-panes)은 `Alt`와 방향키를 사용합니다.

- 위쪽 패널: `Alt+↑`
- 아래쪽 패널: `Alt+↓`
- 왼쪽 패널: `Alt+←`
- 오른쪽 패널: `Alt+→`

입력 대상 패널은 테두리 강조로 구분합니다.

## 패널 크기 조절

[크기 조절](https://learn.microsoft.com/en-us/windows/terminal/panes#resizing-a-pane)은 `Alt+Shift`와 방향키를 사용합니다. 포커스가 있는 패널과 인접 패널 사이의 경계를 이동합니다.

- 높이 조절: `Alt+Shift+↑`, `Alt+Shift+↓`
- 너비 조절: `Alt+Shift+←`, `Alt+Shift+→`

## 패널과 탭 닫기

[닫기 단축키](https://learn.microsoft.com/en-us/windows/terminal/panes#closing-a-pane)는 `Ctrl+Shift+W`입니다. 현재 패널을 닫으며 패널이 하나라면 탭을 닫습니다. 마지막 탭을 닫으면 창도 닫힙니다.

다만 패널 닫기는 실행 중인 셸과 프로세스에 영향을 줄 수 있습니다. 장시간 작업의 분리와 재접속은 [tmux](https://github.com/tmux/tmux/wiki)의 세션 기능으로 구성할 수 있습니다. Terminal의 화면 분할만으로 tmux의 세션 유지 기능까지 제공하지는 않습니다.

## 명령 팔레트와 사용자 키 바인딩

`Ctrl+Shift+P`로 [명령 팔레트](https://learn.microsoft.com/en-us/windows/terminal/command-palette)를 엽니다. 패널 확대와 복원은 `togglePaneZoom` 작업으로 실행할 수 있으며 기본 전용 단축키는 없습니다.

이어서 `Ctrl+,`로 설정을 열고 작업 화면에서 원하는 키를 등록할 수 있습니다. JSON을 직접 편집한다면 [작업 설정 참조](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/actions)에 따라 기존 `actions`와 `keybindings`를 보존합니다.

## 단축키 적용 결과

여기까지 정리하면 Windows Terminal에서 여러 셸을 한 탭에 배치하고 이동할 수 있습니다. 당장 필요한 화면 구성에는 기본 단축키를 사용하고 장시간 실행 작업에는 세션 유지 여부를 별도로 판단합니다.

기본 키가 동작하지 않으면 Terminal 설정과 실행 중인 프로그램의 키 처리를 확인합니다. WSL 배포판마다 다른 셸을 사용해도 Terminal이 처리하는 분할 단축키는 같은 방식으로 적용합니다.
