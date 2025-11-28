# Vmmem 메모리(RAM) 점유율 이슈 해결하기

WSL2 환경을 처음 구축 시 WSL2의 특성과 리눅스의 특성의 결합으로 인해, RAM 점유율 관련 이슈가 발생한다.

-   리눅스 : RAM의 한계치까지 파일의 정보를 최대한 캐시로 보존.
-   WSL2 : WSL2에 할당된 RAM이 부족해지면 WSL2에 추가적인 RAM을 할당.

## 램 사용량 보기

wsl 터미널에서 다음 명령어를 입력하면 램 사용량을 볼 수 있다.

```
free -h
```

이러한 램 할당을 임의로 제한해주려면 wslconfig라는 파일에 설정을 입력해주어야한다.

따라서 c\\users\\사용자이름\\.wslconfig 경로에 파일을 생성해준다.

```
vi .wslconfig
```

그리고 해당 파일에 다음과 같이 입력한다.

```
[wsl2]
memory=4GB
processors=2
swap=1GB
localhostForwarding=true
```

\[wsl2\]: 설정 섹션의 시작을 나타냄.

-   memory=4GB: WSL 2 가상 머신에 할당된 메모리 양을 설정.
-   processors=2: WSL 2 가상 머신에 할당된 가상 프로세서(코어)의 수를 설정.
-   swap=1GB: 스왑 파일의 크기를 설정한다. 스왑 파일은 메모리가 부족한 경우 사용되며 추가 메모리 공간을 제공. 여기서는 1GB의 스왑 파일을 사용하도록 구성한다.
-   localhostForwarding=true: WSL 2 환경에서 로컬호스트 포트 포워딩을 활성화하는 설정이다. 이것은 WSL 2에서 실행 중인 Linux 애플리케이션에서 Windows 호스트의 로컬 포트에 액세스하도록 허용한다.

해당 설정을 완료하고, wsl을 리부팅해준다.

```
wsl.exe --shutdown
wsl.exe -d <배포판 이름>
```

## 최신 업데이트++

23년 9월자로 wsl이 새로 업데이트되며 autoMemoryReclaim이라는 램을 조절하는 기능이 새로 추가되었다.

다음 사이트에서 해당 내용을 살펴볼 수 있다.

https://devblogs.microsoft.com/commandline/windows-subsystem-for-linux-september-2023-update/?fbclid=IwAR1uZTuF15VEONgSWReYgzpkRwC6djTo85l7Bd6q94dugbdy0PJRAONuWVE

그러나 다음 페이지에서 볼 수 있듯 아직 오류가 많고, 안정화가 필요해보인다.

https://github.com/ddev/ddev/issues/5356
