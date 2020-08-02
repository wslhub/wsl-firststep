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
```

## EUC-KR 로캘 만들고 기본 로캘을 한국어 UTF-8로 변경하기

```bash
sudo locale-gen ko_KR.EUC-KR
sudo update-locale LANG=ko_KR.UTF-8 LC_MESSAGES=POSIX
```

## 한국어 글꼴 설치하기

```bash
sudo apt -y install fonts-unfonts-core fonts-unfonts-extra fonts-nanum fonts-nanum-coding fonts-nanum-eco fonts-nanum-extra fonts-noto-cjk
```

## 로그아웃

위의 모든 설정이 반영되려면 로그아웃하고 다시 WSL에 들어와야 합니다.

```bash
logout
```
