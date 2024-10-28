# docker-compose

## 서론
도커 컴포즈는 단일 서버에서 여러개의 도커 컨테이너를 하나의 서비스로 정의해 컨테이너의 묶음으로 관리할 수 있는 작업 환경을 제공하는 관리 도구

일반적인 배포환경에서, 젠킨스, DB, nginx 컨테이너를 각각 하나씩 생성해 관리하는 것보다 도커 컴포즈를 사용하면 모든 컨테이너들을 하나의 YML 파일로 정의해 간단하게 구성하고 실행할 수 있다.

이를 통해 설정과 의존성을 코드로 관리할 수 있기 떄문에 일관성 있는 환경을 유지하는 데 도움을 준다.

## 설치
### ec2 기준
1. `sudo curl -L "https://github.com/docker/compose/releases/download/v2.29.7/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`: 도커 컴포즈를 설치

2. `sudo chmod +x /usr/local/bin/docker-compose`: 도커 컴포즈에 실행 권한 부여

3. `docker-compose --version`: 설치가 제대로 되었다면, 버전이 출력된다.