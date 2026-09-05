# WSL에서 SSH 키 생성과 에이전트 사용

2026년 9월 5일 기준으로 Ubuntu의 OpenSSH 클라이언트는 키 생성과 에이전트 기능을 제공합니다. 이 문서는 WSL 내부에서 사용하는 키를 다룹니다.

기존 키 확인, 키 생성, 공개 키 등록, 에이전트 사용, Windows와의 경계를 설명합니다.

Ubuntu 터미널에서 진행하며 서버에 전달할 공개 키와 개인 보관용 비밀 키를 구분합니다. [GitHub SSH 안내](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)를 참고할 수 있습니다.

## 기존 키와 클라이언트 확인

새 키를 만들기 전에 기존 파일과 OpenSSH 설치 상태를 확인합니다.

```bash
ls -la ~/.ssh
ssh -V
```

`.ssh`가 없으면 첫 키를 생성할 때 디렉터리를 만들 수 있습니다. 필요한 경우 `sudo apt install openssh-client`로 클라이언트를 설치합니다. [기존 키 확인 안내](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)에서 파일명을 확인할 수 있습니다.

## Ed25519 키 생성

[키 생성 안내](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)에 따라 새 키를 생성합니다. 예제 이메일을 자신의 식별용 설명으로 바꿉니다.

```bash
ssh-keygen -t ed25519 -C 'developer@example.com'
```

저장 경로에 기존 키가 있다면 덮어쓰기 대신 별도 파일명을 선택합니다. 서버가 요구하는 알고리즘이 다르면 해당 서버의 정책을 기준으로 선택합니다.

## 공개 키 등록

Ubuntu에서 생성한 공개 키를 출력합니다.

```bash
cat ~/.ssh/id_ed25519.pub
```

출력 내용을 [서버의 SSH 키 등록 화면](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)에 등록합니다. `.pub`가 없는 `id_ed25519`는 비밀 키이므로 등록란이나 이슈에 붙여넣지 않습니다.

## 현재 셸에서 ssh-agent 사용

키의 암호를 매번 입력하지 않으려면 현재 셸에서 에이전트를 시작하고 키를 추가합니다. [ssh-agent 매뉴얼](https://man.openbsd.org/ssh-agent)에 소켓과 환경 변수 동작을 설명했습니다.

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
ssh-add -l
```

이어서 다른 터미널에서도 공유하려면 셸과 세션에 맞는 에이전트 관리 구성을 사용합니다. 위 명령을 무조건 `.bashrc`에 추가하면 터미널마다 에이전트를 생성할 수 있습니다.

## Windows 에이전트와의 경계

WSL의 Linux OpenSSH가 Windows `ssh-agent` 서비스에 자동 연결되지는 않습니다. [npiperelay](https://github.com/jstarks/npiperelay)는 Windows named pipe를 연결하는 별도 도구이며 추가 설정이 필요합니다.

Windows 키를 공유할 이유가 없다면 WSL 내부에서 생성한 키와 에이전트를 사용할 수 있습니다. Windows 공유 구성을 선택하는 경우에는 비밀 키 복사, Windows 파일 권한, 에이전트 소켓 전달을 각각 검토합니다.

## 키 관리와 연결 확인

여기까지 정리하면 WSL에서 키를 생성하고 공개 키를 등록한 뒤 에이전트로 사용할 수 있습니다. 등록 직후에는 실제 대상 서버로 인증을 시험하고 장기적으로는 키 사용 범위와 폐기 절차를 관리합니다.

WSL 작업에는 Linux 에이전트를 사용할 수 있습니다. Windows와 공유하는 경우에는 별도의 연결 구성이 실제로 동작하는지 확인합니다.
