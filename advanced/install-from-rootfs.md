# RootFS 아카이브로부터 Ubuntu 설치하기

Ubuntu의 경우 공식적으로 WSL에서 사용할 수 있는 미리 구성된 루트 파일 시스템을 제공합니다. 이렇게 만들어진 파일 시스템을 받은 후, `wsl.exe --import` 명령을 사용하여 원하는대로 자유롭게 설치할 수 있는 방법을 소개합니다.

## 원하는 RootFS 이미지 찾기

Canonical은 Ubuntu 16.04부터 최신 버전의 Ubuntu까지 각 버전마다 최신 패키지 구성을 반영하여 보안과 성능을 지속적으로 개선한 버전을 공식 배포 서버에 업로드하고 있습니다. 최신 정보는 [https://wiki.ubuntu.com/WSL#Installing_Ubuntu_on_WSL_via_rootfs](https://wiki.ubuntu.com/WSL#Installing_Ubuntu_on_WSL_via_rootfs)에서 확인하실 수 있으며, 편의를 위하여 이 페이지에도 링크를 추가합니다.

manifest 파일은 RootFS에 들어있는 패키지 구성 및 각 패키지들의 버전 정보가 기재된 파일입니다.

**16.04 LTS (Xenial Xerus)**

- amd64 (64비트를 지원하는 일반 PC)
  - https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-wsl.rootfs.manifest
  - https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-wsl.rootfs.tar.gz
- arm64 (Surface Pro X 등 ARM 프로세서 기반 컴퓨터용)
  - https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-arm64-wsl.rootfs.manifest
  - https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-arm64-wsl.rootfs.tar.gz

**18.04 LTS (Bionic Beaver)**

- amd64 (64비트를 지원하는 일반 PC)
  - https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64-wsl.rootfs.manifest
  - https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64-wsl.rootfs.tar.gz
- arm64 (Surface Pro X 등 ARM 프로세서 기반 컴퓨터용)
  - https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-arm64-wsl.rootfs.manifest
  - https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-arm64-wsl.rootfs.tar.gz

**20.04 LTS (Focal Fossa)**

- amd64 (64비트를 지원하는 일반 PC)
  - https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64-wsl.rootfs.manifest
  - https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64-wsl.rootfs.tar.gz
- arm64 (Surface Pro X 등 ARM 프로세서 기반 컴퓨터용)
  - https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-arm64-wsl.rootfs.manifest
  - https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-arm64-wsl.rootfs.tar.gz

## 설치 명령 실행하기

다음과 같이 명령어를 실행합니다. <...> 부분을 적절하게 변경하도록 합니다.

```powershell
wsl.exe --import <DistributionName> <InstallLocation> <FileName> --version <1|2>
```

예를 들어, WSL 2 기반으로 Ubuntu 18.04를 `MyUbuntu`라는 이름의 배포판을 `C:\Distro\MyUbuntu`에 복원하려면 다음과 같이 명령어를 실행할 수 있습니다.

```powershell
Invoke-WebRequest -UseBasicParsing -Uri 'https://cloud-images.ubuntu.com/focal/current/focal-server-cloudimg-amd64-wsl.rootfs.tar.gz' -OutFile 'ubuntu.tar.gz'
wsl.exe --import MyUbuntu C:\Distro\MyUbuntu ubuntu.tar.gz --version 2
```

백업 파일의 크기, 디스크 입출력 속도, 그리고 WSL 버전에 따라 차이가 있을 수 있으며, 시간이 오래 걸리는 작업이므로 완료될 때까지 기다립니다.

또한 추가 디스크 공간이 필요하므로, 디스크 공간이 여유가 없을 경우 별도의 외부 저장 장치를 사용하여 복원을 진행하는 것을 권장합니다.

정상적으로 복원되었는지 확인하기 위하여 목록 확인 명령어를 실행해보겠습니다.

```powershell
wsl.exe --list --verbose
```

MyUbuntu 라는 항목의 버전이 2로 표시된다면 정상적으로 복원된 것입니다.
