# docker

## 서론 

### 그래서 도커가 뭔데
- 컨테이너 기반 가상화 플랫폼.
- 일단, 서버 배포를 위해 VMware나 가상화 머신을 통해 독립적인 계층을 생성해 운영체제, 커널, 드라이버 등을 올리는 경우 자원 소비가 엄청남.
- Docker 컨테이너는 운영체제의 커널을 공유하여 격리된 환경을 생성해 가볍고, 효율적.
- 이를 통해 독립적이고 격리된 환경을 보장함으로써 효율적인 배포가 가능해진다.

## 설치

### 로컬 서버에서 구성하는 경우
- 그냥 설치하면 된다. [공식 문서](https://www.docker.com)

### ec2 서버 위에서 구동시키는 경우 (초기 설정)
1. `sudo apt-get update` : 현재 ec2 서버의 기존 패키지를 업데이트 한다.
2. `sudo apt-get install ca-certificates curl gnupg lsb-release`: 도커 설치를 위한 필수 종속성 패키지를 설치한다.

            1. ca-certificates: HTTPS 연결을 통해 인증서 검증을 지원, 보안이 필요한 패키지 다운로드가 가능해짐
            2. curl: Docker 레포지토리와 GPG키를 다운로드할 때 사용
            3. gnupg: Docker 패키지의 GPG키를 통해 진위성을 확인하여, 신뢰할 수 있는 Docker 소프트웨어만 설치되도록 함
            4. lsb-release: 현재 시스템의 배포판 정보를 확인하여, Docker가 사용하는 레포지토리ㅗ아 패키지가 운영체제에 맞도록 설정

3. `sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg-dearmor -o /etc/apt/keyrings/docker.gpg`
: Docker의 GPG키를 추가한다.
4. `echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null` : Docker 패키지 레포지토리를 추가
5. `sudo apt-get update`: 위에서 추가했던 Docker관련 패키지를 다시 업데이트
6. `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`: Docker와 관련 패키지들을 모두 설치

7. `sudo systemctl enable docker`: 서버가 재부팅될 때 Docker가 자동으로 시작되도록 함