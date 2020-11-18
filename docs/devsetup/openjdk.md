# OpenJDK 설치하기

## OpenJDK 치 방법

오랫동안 널리 사용되었기 때문에 OpenJDK 8 버전은 우분투 패키지 매니저에 계속 포함되어있어서 아래 명령어로 쉽게 설치할 수 있습니다.

```bash
sudo apt -y install openjdk-8-jdk
```

OpenJDK 9 버전 이상을 설치하려는 경우에도 다음과 같이 실행할 수 있습니다.

```bash
sudo apt -y install openjdk-9-jdk
```

## JAVA_HOME 환경 변수 설정

1. 환경 변수를 `~/.bashrc` 또는 `~/.zhsrc` 파일에 설정합니다. 아래의 줄을 파일 가장 마지막에 추가합니다. 여기서는 OpenJDK 9 버전을 설치했다고 가정하겠습니다. 다른 버전을 설치한 경우 9 대신 적절한 버전 번호를 대신 지정합니다.

   ```bash
   export JAVA_HOME=/usr/lib/jvm/openjdk-9-jdk
   export PATH=$PATH:$JAVA_HOME/bin
   ```

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

1. 여기서는 6.5.1 버전을 설치한다고 가정하고 아래 명령어를 실행하겠습니다.

   ```bash
   sudo apt -y install zip

   pushd /tmp
   wget https://services.gradle.org/distributions/gradle-6.5.1-bin.zip
   sudo unzip -d /opt/gradle /tmp/gradle-*.zip
   popd
   ```

1. 설치한 Gradle의 정확한 디렉터리를 확인합니다. `6.5.1` 부분을 정확한 버전 번호로 지정하면 바로 디렉터리를 찾을 수 있습니다.

   ```bash
   ls /opt/gradle/gradle-6.5.1
   ```

1. `GRADLE_HOME` 환경 변수를 정확하게 설정하기 위해 아래 명령어로 셸 스크립트 파일을 만듭니다.

   ```bash
   sudo mkdir -p /etc/profile.d/
   sudo nano /etc/profile.d/gradle.sh
   ```

1. 다음의 코드를 추가하고 파일을 저장합니다. 만약 기존에 이미 내용이 있다면 버전 번호만 바꾸고 저장합니다.

   ```bash
   export GRADLE_HOME=/opt/gradle/gradle-6.5.1
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
