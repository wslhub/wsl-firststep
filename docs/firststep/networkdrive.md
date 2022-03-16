# Windows 파일탐색기로 WSL 파일시스템 확인하는 방법

Windows 파일탐색기를 통해 WSL 디렉토리나 파일시스템을 확인하고 싶을 때 사용할 수 있는 방법들은 여러가지가 있습니다. 그 중 몇가지에 대해 소개하고자 합니다.
1. Windows 파일탐색기 주소란 직접 기입
2. 네트워크 드라이브 추가하기

## Windows 파일탐색기 주소란 직접 기입

파일탐색기 주소란에 `\\wsl$`을 입력하면, 보유하고 있는 WSL 배포판들이 나열됩니다.

![image](https://user-images.githubusercontent.com/37402072/139535893-ea400a99-fc3a-4b20-bd18-ca4a1456652c.png)

## 네트워크 드라이브 추가하기

위 과정이 번거롭다면, `내 컴퓨터`에서 C드라이브, D드라이브처럼 확인할 수 있도록 바로가기 형식의 네트워크 드라이브를 추가할 수 있습니다.

![image](https://user-images.githubusercontent.com/37402072/139535881-30d38176-f71c-49f0-90e1-85dad64703d3.png)

네트워크 드라이브로 생성하고 싶은 배포판의 폴더를 우클릭하여 `네트워크 드라이브(M) 연결...`을 선택합니다.

![image](https://user-images.githubusercontent.com/37402072/139535972-3e809bc1-b4ab-4d98-8cb5-4e035a0c76b0.png)

여기서 원하는 드라이브 명을 선택한 후 마칩니다.

![image](https://user-images.githubusercontent.com/37402072/139536051-5cfb7ae1-cd1a-42ad-910c-962a957ec42f.png)

Z 드라이브에 마운트한 결과입니다. 조금 더 편하고 쉽게 `내 컴퓨터` 상에서도 WSL의 Ubuntu 파일시스템 접근이 가능합니다.
