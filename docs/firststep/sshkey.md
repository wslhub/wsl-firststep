# SSH 키 생성하기

리눅스 환경을 갖추게 되면 가장 먼저 하는 일로 현재 컴퓨터와 사용자를 식별할 수 있는 고유한 SSH 키 페어를 만드는 것입니다.

## ssh-keygen 명령어로 새 키 만들기

```bash
ssh-keygen -t ed25519
```

위의 명령어를 실행한 다음 ED25519 키를 만들 때 필요한 질문에 응답하도록 합니다.

> 참고: ED25519는 RSA보다 더 안전하고 빠른 현대적인 알고리즘입니다. 만약 레거시 시스템과의 호환성이 필요한 경우 `ssh-keygen -t rsa -b 4096`을 사용할 수도 있습니다.

## 만들어진 ssh-key의 공개 키 값 확인하기

```bash
cat ~/.ssh/id_ed25519.pub
```

위의 명령어를 실행한 후 나타나는 파일의 내용을 복사하여 공개 키를 등록하려는 곳에 가져가 등록하면 됩니다.

## 비밀번호를 매번 새로 묻지 않도록 만들기

### 방법 1: Windows의 SSH 에이전트 활용하기 (권장)

Windows 10/11에는 OpenSSH 에이전트가 내장되어 있습니다. WSL에서 Windows의 SSH 에이전트를 활용하면 키 관리를 일원화할 수 있습니다.

먼저 Windows 측에서 SSH 에이전트 서비스를 활성화합니다. 관리자 권한 PowerShell에서 다음을 실행합니다:

```powershell
Set-Service ssh-agent -StartupType Automatic
Start-Service ssh-agent
```

그런 다음 Windows 측에서 키를 등록합니다:

```powershell
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

WSL에서 Windows의 SSH 에이전트를 사용하려면, [npiperelay](https://github.com/jstarks/npiperelay) 또는 [wslu](https://wslutiliti.es/wslu/)와 같은 도구를 활용할 수 있습니다.

### 방법 2: keychain 사용하기

WSL 내에서 직접 SSH 에이전트를 관리하려면 `keychain` 툴을 이용할 수 있습니다.

우선 keychain 패키지를 설치합니다.

```bash
sudo apt -y install keychain
```

그 다음 키 체인에 키를 등록합니다. 비밀 번호가 걸려있는 경우 입력합니다.

```bash
/usr/bin/keychain --nogui $HOME/.ssh/id_ed25519
```

그러면 Bash 셸 시작 시 등록할 수 있는 스크립트 파일이 만들어집니다. 아래 명령어로 확인해봅니다.

```bash
cat ~/.keychain/$(hostname)-sh
```

파일의 내용이 잘 보이면, 셸의 사용자별 설정 파일 (`~/.bashrc` 파일이나 `~/.zshrc` 파일)을 열어 다음 줄을 파일 제일 마지막에 추가합니다.

```bash
source ~/.keychain/$(hostname)-sh
```

이제 새 WSL 창을 열어서 SSH나 git 명령을 호출했을 때 비밀 번호를 묻지 않으면 제대로 작동하는 것입니다.
