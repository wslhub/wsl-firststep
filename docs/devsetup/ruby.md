# Ruby 개발 환경 설치하기

Ruby 개발 환경을 설치하는 방법은 크게 4가지가 있습니다.

* 시스템 패키지 매니저를 통해 설치하는 방법 (이 경우 설치된 버전이 최신 버전이 아닐 수 있습니다.)
* 인스톨러를 통해 설치하는 방법
* 매니저를 통해 여러 버전을 설치하는 방법
* 소스를 빌드하여 설치하는 방법

## 시스템 패키지 매니저를 통해 설치하기

패키지 관리 시스템을 통해 설치하는 방법은 가장 쉬운 방법입니다.
그러나 설치된 패키지 버전이 최신 버전이 아닐 수 있습니다.

1. 다음 명령어를 실행해 Ruby를 설치합니다

    ```bash
    sudo apt install ruby-full
    ```

1. 다음 명령어를 통해 루비가 설치 됨과 버전을 확인합니다.

    ```bash
    ruby -v
    ```

## 인스톨러를 통해 설치하는 방법

인스톨러를 통해 설치하는 방법은 원하는 Ruby 버전을 설치할 수 있으며 여러 버전 또한 함께 설치할 수 있습니다.

여러 인스톨러 중 `ruby-install` 을 이용하여 최신 버전을 설치해보겠습니다.

1. 다음 명령어를 통해 `ruby-install`을 설치합니다

    ```bash
    sudo apt install ruby-install
    ```

1. 최신 버전을 설치합니다.

    ```bash
    ruby-install --latest
    ```

## 매니저를 통해 여러 버전을 설치하는 방법

매니저를 이용하면 시스템에 설치된 루비 여러 버전을 전환할 수 있습니다. 

여러 매니저 중 asdf-vm 을 통해 설치해보겠습니다.

1. 의존성 패키지를 설치합니다.

    ```bash
    sudo apt install curl git
    ```

1. asdf를 다운로드합니다

    ```bash
    git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.8.1
    ```

1. 쉘에서 명령어를 실행할 수 있도록 합니다

    bash를 사용한다면 아래와 같이 실행합니다.

    ```bash
    echo -e ". $HOME/.asdf/asdf.sh" >> ~/.bashrc
    ```

1. Ruby를 사용할 수 있도록 [asdf-ruby](https://github.com/asdf-vm/asdf-ruby) 플러그인을 추가합니다.

    ```bash
    asdf plugin add ruby https://github.com/asdf-vm/asdf-ruby.git
    ```

1. 설치할 수 있는 Ruby 버전을 확인하고 설치합니다.

    ```bash
    asdf list ruby
    ```

    위의 명령어를 실행했을 때 나타나는 버전 목록 중 원하는 버전을 선택합니다. 여기서는 3.0.2 버전을 사용하여 설치한다고 가정하겠습니다.

    ```bash
    asdf install ruby 3.0.2
    ```

1. 프로젝트 내에서 사용할 Ruby 버전을 지정합니다.

    ```bash
    asdf local ruby 3.0.2
    ```

    전역으로 설치를 원한다면 아래 명령어를 실행합니다.

    ```bash
    asdf global ruby 3.0.2
    ```

## 소스를 빌드하여 설치하는 방법

1. [Ruby 다운로드](https://www.ruby-lang.org/en/downloads/)를 통해서 원하는 버전을 다운로드합니다. 3.0.2 버전을 예로 들어 진행하겠습니다.

1. 다운로드 받은 파일의 압축을 해제합니다.

    ```bash
    tar -xf ruby-3.0.2.tar.gz
    ```

1. 압축 해제된 폴더에 들어가 빌드합니다.

    ```bash
    ./configure
    make
    sudo make install
    ```
