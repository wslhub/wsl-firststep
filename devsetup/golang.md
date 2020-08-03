# Go 개발 환경 설치하기

Go 개발 환경을 설치하기 위해서는 다음의 단계를 따릅니다.

1. Golang 공식 웹 사이트의 [다운로드 페이지](https://golang.org/dl/) 에서 원하는 Golang 버전의 리눅스용 버전을 찾아 주소를 복사합니다. 여기서는 `1.14.6` 버전을 설치한다고 가정하겠습니다.

1. 다음 명령어를 실행합니다.

   ```bash
   pushd /tmp
   wget https://dl.google.com/go/go1.14.6.linux-amd64.tar.gz
   sudo tar -xvf go1.14.6.linux-amd64.tar.gz
   sudo mv ./go/ /usr/local/
   popd
   ```

1. 환경 변수를 `~/.bashrc` 또는 `~/.zhsrc` 파일에 설정합니다. 아래의 줄을 파일 가장 마지막에 추가합니다.

   ```bash
   export GOROOT=/usr/local/go
   export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
   ```

1. 환경 변수를 다시 불러오기 위하여 `~/.bashrc` 또는 `~/.zshrc` 파일을 다시 로드하거나, 새로운 터미널 창을 엽니다.

    ```bash
    source ~/.bashrc
    # 또는
    source ~/.zshrc
    ```

1. 제대로 설치되었는지 확인하기 위하여 아래 명령어를 실행합니다.

    ```bash
    go version
    ```
