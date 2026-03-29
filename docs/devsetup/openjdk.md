# OpenJDK 설치하기

## OpenJDK 설치 방법

Ubuntu의 패키지 매니저를 통해 OpenJDK를 설치할 수 있습니다. 장기 지원(LTS) 버전인 OpenJDK 21을 설치하는 것을 권장합니다.

```bash
sudo apt -y install openjdk-21-jdk
```

OpenJDK 17 LTS 버전을 설치하려는 경우에는 다음과 같이 실행할 수 있습니다.

```bash
sudo apt -y install openjdk-17-jdk
```

> 참고: 여러 JDK 버전을 관리하려면 [SDKMAN](https://sdkman.io/)을 사용하는 것도 좋은 방법입니다.
>
> 다만, `curl ... | bash`와 같이 원격 스크립트를 바로 셸에 파이프로 넘겨 실행하는 방식은 보안상 위험할 수 있습니다. 설치 전에 스크립트 내용을 직접 확인하거나, SDKMAN 공식 문서에서 안내하는 최신 설치/검증 절차를 따르는 것을 권장합니다.
>
> ```bash
> # 설치 스크립트를 먼저 내려받고 내용을 확인한 뒤 실행하는 예시입니다.
> curl -s "https://get.sdkman.io" -o install-sdkman.sh
> less install-sdkman.sh   # 내용 확인 후 실행 여부를 결정하세요.
> bash install-sdkman.sh
> source "$HOME/.sdkman/bin/sdkman-init.sh"
> sdk install java 21.0.2-tem
> ```

## JAVA_HOME 환경 변수 설정

1. 환경 변수를 `~/.bashrc` 또는 `~/.zshrc` 파일에 설정합니다. 아래의 줄을 파일 가장 마지막에 추가합니다. 여기서는 OpenJDK 21 버전을 설치했다고 가정하겠습니다. 다른 버전을 설치한 경우 21 대신 적절한 버전 번호를 대신 지정합니다.

   ```bash
   export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
   export PATH=$PATH:$JAVA_HOME/bin
   ```

   > 참고: 위 명령은 설치된 JDK의 실제 경로를 자동으로 감지합니다. 수동으로 지정하려면 amd64 환경에서는 `/usr/lib/jvm/java-21-openjdk-amd64`, arm64 환경에서는 `/usr/lib/jvm/java-21-openjdk-arm64`를 사용합니다.

1. 환경 변수를 다시 불러오기 위하여 `~/.bashrc` 또는 `~/.zshrc` 파일을 다시 로드하거나, 새로운 터미널 창을 엽니다.

    ```bash
    source ~/.bashrc
    # 또는
    source ~/.zshrc
    ```

1. 제대로 설치되었는지 확인하기 위하여 아래 명령어를 실행합니다.

    ```bash
    java -version
    javac -version
    ```

## Maven 설치하기

복잡한 환경 변수 설정 없이, 우분투의 패키지 관리자로 쉽게 Maven을 설치할 수 있습니다.

```bash
sudo apt -y install maven
```

## Gradle 설치하기

1. 설치하려는 Gradle의 버전을 https://gradle.org/releases/ 페이지에서 먼저 확인합니다.

1. 여기서는 8.12 버전을 설치한다고 가정하고 아래 명령어를 실행하겠습니다.

   ```bash
   sudo apt -y install zip

   pushd /tmp
   wget https://services.gradle.org/distributions/gradle-8.12-bin.zip
   sudo unzip -d /opt/gradle /tmp/gradle-*.zip
   popd
   ```

1. 설치한 Gradle의 정확한 디렉터리를 확인합니다. `8.12` 부분을 정확한 버전 번호로 지정하면 바로 디렉터리를 찾을 수 있습니다.

   ```bash
   ls /opt/gradle/gradle-8.12
   ```

1. `GRADLE_HOME` 환경 변수를 정확하게 설정하기 위해 아래 명령어로 셸 스크립트 파일을 만듭니다.

   ```bash
   sudo mkdir -p /etc/profile.d/
   sudo nano /etc/profile.d/gradle.sh
   ```

1. 다음의 코드를 추가하고 파일을 저장합니다. 만약 기존에 이미 내용이 있다면 버전 번호만 바꾸고 저장합니다.

   ```bash
   export GRADLE_HOME=/opt/gradle/gradle-8.12
   export PATH=${GRADLE_HOME}/bin:${PATH}
   ```

1. 실행 권한을 셸 스크립트에 부여합니다.

   ```bash
   sudo chmod +x /etc/profile.d/gradle.sh
   ```

1. 셸 스크립트 파일을 다시 불러옵니다.

   ```bash
   source /etc/profile.d/gradle.sh
   ```

1. 제대로 설치가 되었는지 다시 확인해봅니다.

   ```bash
   gradle -v
   ```
