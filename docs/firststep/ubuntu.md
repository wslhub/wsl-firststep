# Ubuntu 설치 후에 처음 할 일

항상 처음 시스템을 설치하면 밀려있는 보안 업데이트 등을 모두 설치하여 모든 보안 취약점을 최대한 예방하는 것이 좋습니다.

## 패키지 미러 주소 변경하기

2020년 여름 현재 통신사가 대역폭 제한을 설정하여 정상적으로 해외 CDN 서버에서 빠른 속도로 파일을 다운로드할 수 없는 경우가 발생하고 있습니다. 이럴 때는 한국의 미러 서버를 사용하도록 고쳐주는 것이 좋습니다.

카카오의 미러 서버로 변경하여 패키지를 업데이트하도록 아래와 같이 명령어를 붙여넣습니다.

```bash
sudo sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list
```

## 패키지 업데이트, 업그레이드, 불필요한 패키지 자동 제거

```bash
sudo apt update && sudo apt -y upgrade && sudo apt -y autoremove
```

## ZSH 설치하기

```bash
sudo apt -y install zsh
```

## Oh-My-ZSH 설치하기

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

## 기본 셸 변경하기

자동 설치 스크립트에서 기본 셸을 바꾸지 않았다면 아래 명령어를 붙여넣습니다.

```bash
chsh -s $(which zsh)
```

## 한국어 언어 팩 설치하기

```bash
sudo apt -y install language-pack-ko

sudo locale-gen ko_KR.EUC-KR
sudo update-locale LANG=ko_KR.UTF-8 LC_MESSAGES=POSIX

sudo apt -y install fonts-unfonts-core fonts-unfonts-extra fonts-nanum fonts-nanum-coding fonts-nanum-eco fonts-nanum-extra fonts-noto-cjk
```

위의 모든 설정이 반영되려면 로그아웃하고 다시 WSL에 들어와야 합니다.

```bash
logout
```

## Fuzzy Search 추가하기

터미널을 사용하면서 많이 사용하는 기능 중에 전에 입력했던 명령어를 다시 실행하는 기능을 많이 사용합니다. 그 외에도 파일 이름 등을 자동 완성하기 위하여 일부분만 입력하고 Tab 키를 누르는 기능도 많이 사용합니다.

이처럼 텍스트 검색을 할 때 완전히 동일한 시작 순서와 문자를 입력하지 않아도 적절하게 검색 결과를 찾아 제안하는 Fuzzy Search 기능이 개발자들 사이에서 많이 사용됩니다. Fuzzy Search를 사용하기 위해서는 fzf 라는 도구를 설치하여 사용해야 합니다.

1. 다음의 명령어를 입력합니다.

    ```bash
    sudo apt -y install git

    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
    ```

1. 설치가 끝나면, 현재 사용 중인 셸과 연동하기 위하여 아래 명령어를 입력합니다.

    ```bash
    ~/.fzf/install
    ```

1. 몇 가지 질문에 모두 `Y` 키를 눌러 답을 합니다.

1. 변경된 터미널 설정이 반영될 수 있도록, 현재 사용 중인 터미널 창을 닫았다가 새 창을 엽니다.

1. 설치가 끝난 후, 잘 설치가 되었는지 확인하기 위하여 `Ctrl` 키를 누른채로 `R` 키를 누릅니다. 그러면 다음과 같이 fzf가 입력했던 명령어들을 검색하고 후보를 추천해주는 기능이 잘 작동하는 것을 알 수 있습니다.
