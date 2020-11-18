# SSH 키 생성하기

리눅스 환경을 갖추게되면 가장 먼저 하는 일로 현재 컴퓨터와 사용자를 식별할 수 있는 고유한 SSH 키 페어를 만드는 것입니다.

## ssh-keygen 명령어로 새 키 만들기

```bash
ssh-keygen -t rsa
```

위의 명령어를 실행한 다음 RSA 키를 만들 때 필요한 질문에 응답하도록 합니다.

## 만들어진 ssh-key의 공개 키 값 확인하기

```bash
cat ~/.ssh/id_rsa.pub
```

위의 명령어를 실행한 후 나타나는 파일의 내용을 복사하여 공개 키를 등록하려는 곳에 가져가 등록하면 됩니다.

## 비밀번호를 매번 새로 묻지 않도록 만들기

팁 출처: https://medium.com/@pscheit/use-an-ssh-agent-in-wsl-with-your-ssh-setup-in-windows-10-41756755993e

WSL은 실제 리눅스 머신과는 달라서 서비스라는 컨셉이 따로 없고 곧바로 셸로 진입하는 아키텍처를 가지고 있습니다. 이 때문에 `ssh-add` 명령을 쓰는 방식으로는 키에 대한 비밀 번호를 묻지 않도록 자동화할 수 없습니다. 이럴 때 `keychain` 툴을 이용하면 편리합니다.

우선 keychain 패키지를 설치합니다.

```bash
sudo apt -y install keychain
```

그 다음 키 체인에 키를 등록합니다. 비밀 번호가 걸려있는 경우 입력합니다.

```bash
/usr/bin/keychain --nogui $HOME/.ssh/id_rsa
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
