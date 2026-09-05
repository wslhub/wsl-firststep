# Windows Terminal의 WSL 프로필 설정

2026년 9월 5일 기준으로 Windows Terminal은 설치된 WSL 배포판의 프로필을 자동 생성할 수 있습니다. 설정 UI에서 기본 프로필과 표시 옵션을 변경할 수 있습니다.

기본 프로필, 시작 경로, 글꼴, 색 구성표, 화면 분할을 다룹니다.

Terminal을 연 뒤 `Ctrl+,`로 설정 화면에 들어가 순서대로 적용합니다. [공식 설치 안내](https://learn.microsoft.com/en-us/windows/terminal/install)에서 Terminal을 설치할 수 있습니다.

## 기본 프로필 선택

시작 설정에서 사용할 배포판을 기본 프로필로 선택합니다. [시작 설정 참조](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/startup)에 설명한 기본 프로필은 새 탭에서 사용할 셸을 결정합니다.

배포판이 보이지 않으면 PowerShell의 `wsl.exe --list --verbose`에서 등록 이름을 확인하고 Terminal을 다시 엽니다. WSL의 기본 배포판과 Terminal의 기본 프로필은 각각 설정합니다.

## Linux 홈 디렉터리에서 시작

[프로필 일반 설정](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/profile-general)의 시작 디렉터리를 사용하거나 명령줄에 `--cd ~`를 지정할 수 있습니다. 아래 JSON은 새 프로필 객체의 예제이며 기존 프로필에 적용할 때에는 해당 속성만 수정합니다.

```json
{
  "name": "Ubuntu 26.04 Home",
  "commandline": "wsl.exe -d Ubuntu-26.04 --cd ~"
}
```

새 탭의 Ubuntu에서 `pwd`와 `whoami`를 실행해 홈 경로와 사용자를 확인합니다. 배포판 이름은 실제 등록 이름으로 바꿉니다.

## Windows에 설치한 글꼴 선택

글꼴 설정부터 살펴보겠습니다. 프로필의 모양 화면에서 Windows에 설치된 글꼴을 선택합니다. [현재 글꼴 스키마](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/profile-appearance#font)에서는 `font.face`를 사용합니다.

아래 내용은 기존 프로필에 병합할 속성 예제입니다.

```json
{
  "font": {
    "face": "Cascadia Mono",
    "size": 12
  }
}
```

특수 아이콘을 사용하는 테마는 해당 문자를 포함한 글꼴을 별도로 설치할 수 있습니다. Ubuntu 내부의 글꼴 설치는 Windows Terminal 글꼴 선택과 구분합니다.

## 색 구성표와 배경

프로필의 모양 화면에서 내장 색 구성표를 선택할 수 있습니다. JSON에서 사용자 색상을 추가할 때에는 [색 구성표 참조](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes)에 맞는 객체를 `schemes` 배열에 추가하고 프로필의 `colorScheme`으로 이름을 연결합니다.

이어서 투명도와 배경 옵션은 [모양 설정](https://learn.microsoft.com/en-us/windows/terminal/customize-settings/profile-appearance)을 기준으로 지정합니다. 다른 예제의 생략 부호나 전체 `profiles` 배열을 덮어쓰면 기존 프로필을 잃을 수 있으므로 변경할 속성만 병합합니다.

## 화면 분할과 설정 검증

[화면 분할 치트시트](../devsetup/multiplexer.md)에서 좌우 분할과 이동, 크기 조절 키를 확인할 수 있습니다. 공식 동작은 [Terminal 패널 안내](https://learn.microsoft.com/en-us/windows/terminal/panes)에 설명되어 있습니다.

1. 새 탭을 열어 선택한 배포판과 홈 경로를 확인합니다.
2. 한국어와 셸 프롬프트의 글꼴을 확인합니다.
3. `Alt+Shift+-`로 패널을 나누고 `Alt+↓`로 이동합니다.
4. 실습 패널에서 `Ctrl+Shift+W`로 닫기 동작을 확인합니다.

## 프로필 유지와 작업 배치

여기까지 정리하면 Terminal의 프로필과 표시 옵션을 설정할 수 있습니다. 새 탭에서 경로와 문자를 바로 확인할 수 있으며 사용자 키 바인딩과 색 구성표는 이후에도 조정할 수 있습니다.

하나의 WSL 배포판만 사용하면 기본 프로필 설정으로 충분합니다. 여러 프로젝트를 함께 다룬다면 별도 프로필과 화면 분할을 조합할 수 있습니다.
