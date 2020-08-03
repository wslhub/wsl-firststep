# 닷넷 개발 환경 설치하기

리눅스에서 사용할 수 있는 닷넷 개발 환경은 크게 두 가지입니다. 권장되는 것은 닷넷 코어 또는 닷넷 5 이상의 개발 환경을 설치하는 것이고, 때에 따라 모노를 설치해서 사용해야 할 때도 있습니다.

## 닷넷 코어 SDK 설치하기

1. 우선 지금 사용하는 우분투의 버전을 아래 명령어로 확인합니다. `NN.NN` 형태의 버전 번호를 확인합니다.

   ```bash
   lsb_release -a
   ```

1. 아래 `wget` 명령어에서 `20.04` 버전 부분을 지금 사용하는 버전과 일치하도록 수정한 후 명령어를 실행합니다. 예를 들어 `18.04`로 확인되는 경우 `18.04`로 고쳐씁니다. 여기서는 `20.04` 버전을 사용한다고 가정하겠습니다.

    ```bash
    pushd /tmp

    wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    
    sudo dpkg -i packages-microsoft-prod.deb
    popd
    ```

1. 패키지 목록을 업데이트하고, 필요한 소프트웨어를 설치한 다음, 닷넷 코어 SDK를 설치합니다.

   ```bash
   sudo apt-get update; \
   sudo apt-get install -y apt-transport-https && \
   sudo apt-get update && \
   sudo apt-get install -y dotnet-sdk-3.1
   ```

1. 설치가 잘되었는지 확인하기 위하여 다음의 명령어를 실행합니다.

    ```bash
    dotnet --list-sdks
    ```

## 모노 SDK 설치하기

닷넷 코어와 달리 모노는 닷넷 프레임워크에 대응이 되도록 개발되었으며, 광범위한 패키지들의 설치를 필요로 합니다. 개발 목적으로 사용하는 컴퓨터에만 설치하는 것을 권장합니다.

1. 우선 지금 사용하는 우분투의 버전을 아래 명령어로 확인합니다. `Codename` 항목에 기재된 이름을 찾습니다.

   ```bash
   lsb_release -a
   ```

1. 아래 명령어에서 `stable-focal` 부분을 지금 사용하는 버전과 일치하도록 수정한 후 실행합니다. 예를 들어 `bionic`이 코드명으로 나온 경우 `stable-bionic` 처럼 고쳐씁니다. 여기서는 `stable-focal`로 가정하고 실행하곘습니다.

   ```bash
   sudo apt -y install gnupg ca-certificates
   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
   echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
   sudo apt update
   ```

1. 아래 명령어를 실행합니다.

   ```bash
   sudo apt -y install mono-devel mono-dbg referenceassemblies-pcl ca-certificates-mono nuget
   ```

1. 만약 ASP.NET 개발 환경이 필요하면 아래 명령어도 실행합니다. 모노에서는 IIS를 대신하여 XSP라는 애플리케이션 서버로 ASP.NET을 실행합니다.

    ```bash
    sudo apt -y install mono-xsp4
    ```
