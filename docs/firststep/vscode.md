# Visual Studio Code 설정하기

## Visual Studio Code - WSL 확장 설치

Visual Studio Code에서도 WSL 연동 기능을 제공합니다. Visual Studio Code를 설치한 다음 아래 확장을 설치해주세요.

[https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

> 참고: 이 확장은 이전에 "Remote - WSL"이라는 이름이었으나, 현재는 "WSL"로 이름이 변경되었습니다.

이미지 출처: [https://microsoft.github.io/vscode-remote-release/images/wsl-readme.gif](https://microsoft.github.io/vscode-remote-release/images/wsl-readme.gif)

![Visual Studio Code용 WSL 확장 동작 예시](images/wsl-readme.gif)

## WSL 배포판에서 Visual Studio Code 프로젝트 열기

WSL에서 프로젝트를 Visual Studio Code로 열고자한다면, 해당 프로젝트 디렉토리에 이동하여 아래 명령어를 사용할 수 있습니다. VS Code Server가 설치되며, WSL 내 프로젝트를 Visual Studio Code에서 작업할 수 있습니다.

```bash
code .
```

이미지 출처: [https://learn.microsoft.com/windows/wsl/tutorials/wsl-vscode](https://learn.microsoft.com/windows/wsl/tutorials/wsl-vscode)

![code . 동작 예시](https://learn.microsoft.com/windows/wsl/media/wsl-open-vs-code.gif)
