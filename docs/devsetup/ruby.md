# Ubuntu에서 Ruby 설치와 버전 관리

2026년 9월 5일 기준으로 Ubuntu 패키지 또는 별도 버전 관리 도구로 Ruby를 설치할 수 있습니다. asdf는 현재 바이너리 설치와 `asdf set` 명령을 사용합니다.

패키지 설치, asdf 준비, 설치 가능 버전, 프로젝트 버전 선택, 실행 검증을 다룹니다.

Ubuntu에서 기본 설치를 시작한 뒤 여러 버전이 필요한 경우에만 버전 관리 도구를 추가합니다. [Ruby 공식 설치 안내](https://www.ruby-lang.org/en/documentation/installation/)를 기준으로 선택할 수 있습니다.

## Ubuntu 패키지로 Ruby 설치

배포판 버전으로 충분하면 Ruby 전체 패키지를 설치합니다.

```bash
sudo apt update
sudo apt install ruby-full build-essential
ruby -v
```

[공식 패키지 설치 안내](https://www.ruby-lang.org/en/documentation/installation/)는 패키지 버전과 최신 Ruby 릴리스가 다를 수 있음을 설명합니다.

## 현재 asdf 설치 방식

[asdf 시작 안내](https://asdf-vm.com/guide/getting-started.html)에 따라 Linux 아키텍처에 맞는 바이너리를 설치하고 shims 경로를 PATH에 추가합니다. 구형 `v0.14.1` 저장소 복제와 `asdf.sh` 로딩 절차를 현재 버전에 적용하지 않습니다.

Ubuntu 셸에서 asdf가 실행되는지 확인합니다.

```bash
asdf version
```

## Ruby 플러그인과 설치 가능 버전

[asdf-ruby](https://github.com/asdf-vm/asdf-ruby)의 빌드 의존성을 먼저 설치합니다. 그다음 플러그인을 추가하고 설치 가능한 버전을 확인합니다. 이미 플러그인이 있으면 추가 명령은 생략합니다.

```bash
asdf plugin add ruby https://github.com/asdf-vm/asdf-ruby.git
asdf list all ruby
```

`asdf list ruby`는 설치된 버전을 보여 주므로 설치 가능한 전체 목록과 구분합니다.

## 프로젝트 Ruby 버전 지정

[asdf 버전 관리](https://asdf-vm.com/manage/versions.html)에 따라 프로젝트가 요구하는 정확한 버전을 설치하고 지정합니다. 다음은 구문 예제이며 `X.Y.Z`를 선택한 버전으로 바꿉니다.

```bash
asdf install ruby X.Y.Z
asdf set ruby X.Y.Z
```

기존 `asdf local`과 `asdf global` 대신 현재 명령을 사용합니다. 홈 기준 버전은 `asdf set -u ruby X.Y.Z`로 설정할 수 있습니다. 프로젝트의 `.tool-versions`, `.ruby-version`, Gemfile이 요구하는 버전도 함께 확인합니다.

## 실행 파일과 Gem 환경 검증

프로젝트 폴더에서 Ruby 실행 경로와 패키지 환경을 확인합니다. [RubyGems 안내](https://guides.rubygems.org/command-reference/#gem-environment)에 `gem environment`의 출력을 설명했습니다.

```bash
command -v ruby
ruby -v
gem environment
```

Gemfile과 lock 파일이 있는 프로젝트는 [Bundler](https://bundler.io/guides/using_bundler_in_applications.html)에 따라 의존성을 설치하고 테스트를 실행합니다.

## 설치 방식과 프로젝트 유지

여기까지 정리하면 Ubuntu 패키지로 Ruby를 시작하거나 asdf로 프로젝트 버전을 지정할 수 있습니다. 설치 직후에는 실행 파일과 의존성 설치를 확인하고 장기적으로는 프로젝트의 Ruby 버전과 lock 파일을 관리합니다.

단일 실습 환경에는 APT를 사용할 수 있습니다. 여러 버전의 프로젝트를 함께 다룬다면 asdf 같은 버전 관리 도구를 적용합니다.
