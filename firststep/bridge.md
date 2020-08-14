# 리눅스 환경과 격차 줄이기

WSL은 실제 리눅스 환경과 동일하게 작동하는 부분도 있지만, Windows가 메인 OS이기 때문에 발생하는 환경 상의 격차도 있습니다. 이런 부분에 의존하는 기능을 사용할 경우 사용이 불편할 수 있습니다. 이 문서에서는 필요에 따라 추가로 설치하거나 구성할 수 있는 부분들에 대해 정리하였습니다.

## xdg-open의 WSL 버전 설치하기

여러 가지 xdg-open의 WSL 버전에 대한 구현체가 존재하지만, 가장 추천할 만한 구현체는 Python 기반으로 작성된 `xdg-open-wsl` 도우미입니다.

```bash
pip3 install --user git+https://github.com/cpbotha/xdg-open-wsl.git
```
