# Ubuntu에서 OpenJDK와 Java 빌드 도구 설치

2026년 9월 5일 기준으로 Ubuntu는 기본 JDK와 버전별 OpenJDK 패키지를 제공합니다. 프로젝트마다 요구하는 Java 버전이 다를 수 있습니다.

JDK 선택, 설치 확인, JAVA_HOME, Maven, Gradle Wrapper를 설명합니다.

Ubuntu 터미널에서 프로젝트 설정을 확인한 뒤 필요한 JDK를 설치합니다. [Ubuntu Java 안내](https://help.ubuntu.com/community/Java)를 참고할 수 있습니다.

## 프로젝트에 맞는 JDK 선택

별도 버전 요구가 없다면 Ubuntu의 `default-jdk`를 설치할 수 있습니다. JDK 21이 필요한 프로젝트는 `openjdk-21-jdk`의 설치 후보를 확인해 선택합니다. [Ubuntu 패키지 목록](https://packages.ubuntu.com/search?keywords=openjdk)에서 지원하는 릴리스를 확인합니다.

```bash
sudo apt update
apt-cache policy default-jdk openjdk-21-jdk
sudo apt install default-jdk
```

## java와 javac 버전 확인

Ubuntu에서 런타임과 컴파일러가 의도한 버전을 사용하는지 확인합니다. 여러 버전을 설치한 경우 [Ubuntu alternatives](https://manpages.ubuntu.com/manpages/noble/en/man1/update-alternatives.1.html)로 선택을 관리할 수 있습니다.

```bash
java -version
javac -version
readlink -f "$(command -v javac)"
```

## JAVA_HOME 설정

도구가 JAVA_HOME을 요구하면 실제 컴파일러 경로를 기준으로 설정합니다. 아래 내용은 Ubuntu 패키지로 설치한 JDK를 가정하며 셸 설정 파일에 추가할 수 있습니다. [Maven 설치 안내](https://maven.apache.org/install.html)에 JDK 환경 조건을 설명했습니다.

```bash
export JAVA_HOME="$(dirname "$(dirname "$(readlink -f "$(command -v javac)")")")"
export PATH="$JAVA_HOME/bin:$PATH"
```

## Maven 설치 또는 프로젝트 Wrapper

[Maven](https://maven.apache.org/install.html)을 Ubuntu 패키지로 설치하고 버전을 확인합니다. 프로젝트에 `mvnw`가 있다면 해당 Wrapper의 사용 절차를 적용할 수 있습니다.

```bash
sudo apt install maven
mvn -version
```

## Gradle Wrapper로 프로젝트 실행

[Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html)가 있는 프로젝트는 지정한 Gradle 버전을 사용합니다. 오래된 전역 Gradle ZIP 설치 예제를 그대로 적용할 필요 없이 프로젝트가 선언한 버전을 확인할 수 있습니다.

신뢰하는 프로젝트의 루트에서 Wrapper 설정과 실행 결과를 확인합니다.

```bash
cat gradle/wrapper/gradle-wrapper.properties
./gradlew --version
./gradlew build
```

Wrapper가 없다면 [Gradle 설치 안내](https://docs.gradle.org/current/userguide/installation.html)에 따라 프로젝트와 JDK가 지원하는 버전을 설치합니다.

## Java 도구 선택의 기준

여기까지 정리하면 JDK 설치와 실제 컴파일러 경로를 확인하고 프로젝트의 빌드 도구를 실행할 수 있습니다. 설치 직후에는 빌드 성공 여부를 확인하고 장기적으로는 JDK와 Wrapper 버전의 호환성을 관리합니다.

새 실습에는 Ubuntu 기본 JDK를 사용할 수 있습니다. 기존 프로젝트에는 해당 프로젝트가 요구하는 JDK와 빌드 도구 버전을 적용합니다.
