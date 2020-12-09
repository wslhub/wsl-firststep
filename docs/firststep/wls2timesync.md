# WSL2 시간 동기화 문제 임시발편 조치하기

WSL2의 경우, WSL1과 달리 컴퓨터를 절전모드에 두었다가 깨우면 그 시간만큼 시간이 느려지는 문제가 있습니다.
그래서 이로 인해 패키지 저장소 업데이트 중 오류가 발생하거나, SSL 인증서 검증 오류, Git 커밋 생성시 시간 꼬이는 등 다양한 문제가 
발생할 수 있습니다.

2019년 부터 관련 이슈가 여러번 제기되었지만, 아직까지는 해결되지 않은 상태입니다. 본 문서를 통해 임시방편으로 조치하는 방법을 알아봅니다.

* [WSL2: Clock skewed? #4677](https://github.com/microsoft/WSL/issues/4677)
* [WSL2 - clock problems during build #4975](https://github.com/microsoft/WSL/issues/4975)
* [WSL2 Ubuntu, time stopped. #5184](https://github.com/microsoft/WSL/issues/5184)
* [WSL2 date incorrect after waking from sleep #5324](https://github.com/microsoft/WSL/issues/5324)

## 시간 동기화 명령 실행하기

### 하드웨어 시간과 동기화
하드웨어 시간을 시스템에 적용하려면 `hwclock`명령을 사용합니다. 하드웨어 시간(`h`)를 시스템(`sys`) 에 적용할 것이므로, `--htosys` 인자를 사용합니다. 축약된 인자인 `-s` 를 대신 사용할 수도 있습니다.

```bash
sudo hwclock --htosys
# sudo hwclock -s
```

### 타임 서버와 동기화
`chrony` 를 이용하여 시간 서버와 동기화 하는 방법도 있습니다. 아래 명령으로 `chrony` 를 설치합니다.

```bash
sudo apt -y install chrony
```

`upstart`를 이용하여 `chrony` 서비스를 켭니다. `chrony` 에 의해 주기적으로 시간이 동기화 됩니다.

```bash
sudo service chrony start
```

## 시간 동기화 명령 자동 실행
시간 동기화를 한번 실행한 후에도, 절전모드 전환할 일은 계속 있기 때문에 그 때 마다 시간 동기화를 수행해야 합니다.
매번 직접 실행하는 것은 번거로우므로, 자동으로 실행되도록 설정합시다. 또한 앞서 `upstart` 를 이용해 `chrony` 를 시작했다 해도,
WSL 환경에서는 `upstart`가 서비스를 자동 시작 하는 것을 지원하지 않아, 서비스 시작 명령을 자동 실행하도록 별도의 설정이 필요합니다.

### `.bashrc`, `.zshrc` 등 셸 프로필 파일 수정
가장 쉬운 방법은 각 CLI 셸이 사용하는 `.*rc` 파일(`bash`->`.bashrc`, `zsh`->`.zshrc`, `fish`->`.fishrc`) 을 수정하여 가장 마지막 줄에 명령줄을 추가하는 방법입니다.

아래와 같이 루트 권한 상승이 필요한 명령을 그대로 넣으면, 매번 셀을 새로 열 때 마다 암호를 입력해야 해서 번거롭습니다.
WSL 에서는 Windows 의 명령이나 셸을 뒤에 `.exe` 를 붙여 바로 실행이 가능합니다. 이를 활용하여 Windows에서 사용하는 명령인 `wsl`을 
`wsl.exe` 로 실행합니다. `wsl` 로 명령 실행시 WSl 환경에서 실행할 명령과 명령을 실행할 계정을 지정하여 해당 계정 암호 입력 없이 바로 실행이 가능합니다.

그러므로, 아래와 같이 루트 계정으로 암호 입력 없이 원하는 명령을 실행할 수 있습니다.

```bash
wsl.exe -u root -e <실행할 명령>
```

이제 이를 이용하여 아래와 같은 내용을 `.bashrc`, `.zshrc` 등 파일의 마지막 줄에 추가합니다.

```bash
# hwclock 명령 사용시
wsl.exe -u root -e hwclock -s

# chrony 사용시
wsl.exe -u root -e service chrony start
```

### Windows 작업 스케줄러 활용
Windows 작업 스케줄러를 설정하여 잠금 해제 할 때 마다 명령을 실행하도록 설정도 가능합니다.
다만 명령 실행을 위해 명령 프롬프트 창이 잠깐 나왔다 사라져서 조금 거슬릴 수 있습니다.

- 시작 메뉴에서 *작업 스케줄러* 를 검색하여 실행합니다.
- *작업* 에서 *작업 만들기...* 를 클릭하여 새 작업을 생성합니다.
- *트리거* 탭으로 가서 *새로 만들기...* 를 누릅니다.
    - *작업 시작* 조건을 *워크스테이션 잠금 해제 시* 로 선택하고 *확인* 을 누릅니다.
- *동작* 탭으로 가서 *새로 만들기...* 를 누릅니다.
    - *동작* 을 *프로그램 시작으로 설정합니다.
    - `hwclock` 명령을 실행하도록 하려면 다음과 같이 합니다.
        - *프로그램/스크립트*에 `wsl` 입력
        - *인수 추가(옵션)*에 `-u root -e hwclock -s` 를 입력
    - `chrony` 데몬이 시작되도록 하려면 다음과 같이 합니다.
        - *프로그램/스크립트*에 `wsl` 입력
        - *인수 추가(옵션)*에 `-u root -e service chrony start` 를 입력
    - 다 입력했다면 *확인* 을 누릅니다.
- *확인* 을 눌러 저장합니다.
- 이제 잠금 해제 할 때 마다 시간 동기화 명령이 실행됩니다.