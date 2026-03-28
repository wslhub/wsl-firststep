# 닷넷 개발 환경 설치하기

## 닷넷 SDK 설치하기

최신 .NET SDK를 설치하는 방법입니다. 여기서는 .NET 8 LTS 버전을 기준으로 설명합니다.

### 방법 1: 스크립트를 이용한 설치 (권장)

Microsoft에서 제공하는 설치 스크립트를 이용하면 간편하게 최신 .NET SDK를 설치할 수 있습니다.

```bash
wget https://dot.net/v1/dotnet-install.sh -O dotnet-install.sh
chmod +x dotnet-install.sh
./dotnet-install.sh --channel 8.0
```

설치 후 환경 변수를 설정합니다. `~/.bashrc` 또는 `~/.zshrc` 파일에 아래 내용을 추가합니다.

```bash
export DOTNET_ROOT=$HOME/.dotnet
export PATH=$PATH:$DOTNET_ROOT:$DOTNET_ROOT/tools
```

환경 변수를 다시 불러옵니다.

```bash
source ~/.bashrc
# 또는
source ~/.zshrc
```

### 방법 2: 패키지 매니저를 이용한 설치

Ubuntu 22.04 이상에서는 APT 패키지 매니저를 통해서도 설치할 수 있습니다.

1. 우선 지금 사용하는 우분투의 버전을 아래 명령어로 확인합니다. `NN.NN` 형태의 버전 번호를 확인합니다.

   ```bash
   lsb_release -a
   ```

1. 아래 `wget` 명령어에서 `24.04` 버전 부분을 지금 사용하는 버전과 일치하도록 수정한 후 명령어를 실행합니다. 여기서는 `24.04` 버전을 사용한다고 가정하겠습니다.

    ```bash
    pushd /tmp

    wget https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    
    sudo dpkg -i packages-microsoft-prod.deb
    popd
    ```

1. 패키지 목록을 업데이트하고, 닷넷 SDK를 설치합니다.

   ```bash
   sudo apt-get update && \
   sudo apt-get install -y dotnet-sdk-8.0
   ```

## 설치 확인

설치가 잘되었는지 확인하기 위하여 다음의 명령어를 실행합니다.

```bash
dotnet --list-sdks
```

> 참고: .NET 버전별 지원 기간은 [.NET 지원 정책](https://dotnet.microsoft.com/platform/support/policy)에서 확인할 수 있습니다. LTS 버전(.NET 8 등)은 3년간 지원됩니다.
