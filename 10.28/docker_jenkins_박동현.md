# Jenkins

## 서론
대표적인 CI/CD 툴로, 각종 자동화 작업과 pipeline 구축에 사용된다.

## 설치
설치방법은 DooD와 DinD로 나뉜다.
- DinD: Docker in Docker의 약어로, 도커 컨테이너 내부에서 호스트 도커 데몬과 다른 별개의 새로운 도커 데몬을 실행시키는 것
- DooD: Docker out of Docker의 약어로, 호스트 도커 데몬이 사용하는 소켓을 공유하여 도커 클라이언트 컨테이너에서 컨테이너를 실행 

- 선언적: Dockerfile, JenkinsFile, docker-compose.yml 등을 통해 설정

- 명령어: 명령어를 통해 설정

성능적으로는 DinD보다 DooD가 하나의 도커 데몬만을 사용하기에 더 뛰어나지만, WSL 환경에서 문제가 발생할 수 있으므로 DinD로 설치하는 방법을 사용했음
## DinD
- jenkins blue-ocean 버전을 설치. 젠킨스 블루 오션은 기존보다 좀 더 시각화된 대시보드와 파이프라인 편집이 가능하고, 파이프라인이 시각화되어 문제 발생 시 어느 스테이지 또는 스텝에서 문제가 발생했는지 더 쉽게 파악할 수 있음

### 선언형
1. docker-compose.yml 설정
```yml
services:
  jenkins:  # 젠킨스 컨테이너 설정
    build:
      context: .  # Dockerfile이 위치한 현재 디렉토리를 컨텍스트로 지정
      dockerfile: Dockerfile  # 사용할 Dockerfile의 이름을 지정
    container_name: jenkins-blueocean   # 컨테이너 일므을 jenkins-blueocean으로 지정
    restart: on-failure # 컨테이너가 실패할 때 자동 재시작
    networks:
      - jenkins   # jenkins 네트워크에 연결
    environment:
      - DOCKER_HOST=tcp://docker:2376   # Docker의 호스트 주소를 지정 (docker 컨테이너의 2376 포트 사용)
      - DOCKER_CERT_PATH=/certs/client    # Docker 인증서 경로 지정 
      - DOCKER_TLS_VERIFY=1   # Docker TLS 인증 활성화
    volumes:
      - jenkins-data:/var/jenkins_home    # Jenkins 데이터를 영구 저장하는 볼륨
      - jenkins-docker-certs:/certs/client:ro   # Docker 인증서을 읽기 전용으로 연결 ro: read-only
    ports:
      - "9999:8080"   # 로컬 9999 포트를 jenkins의 8080 포트에 연결
      - "50000:50000"   # jenkins 에이전트와의 통신을 위한 50000 포트 매핑

docker:   # Docker in Docker 컨테이너 설정
  image: docker:dind    # Docker-in-Docker 이미지를 사용
  privileged: true    # Docker-in-Docker 사용을 위한 권한 부여
  container_name: jenkins-docker    # 컨테이너 이름을 jenkins-docker로 지정
  restart: unless-stopped   # 컨테이너가 중지될 때만 다시 시작하지 않음
  networks:
    jenkins:
      aliases:
        - docker    # 이 네트워크에서 docker라는 이름으로 접근 가능
  environment:
    - DOCKER_TLS_CERTDIR=/certs   # Docker 인증서 디렉토리 설정
  volumes:
    - jenkins-docker-certs:/certs/client    # Docker 인증서를 위한 볼륨
    - jenkins-data:/var/jenkins_home    # Jenkins 데이터 공유를 위한 볼륨
  ports:
    - "2376:2376"   # Docker 데몬의 2376 포트를 로컬 호스트와 매핑
  command: --storage-driver overlay2    # Docker 저장소 드라이버로 overlay2를 사용

networks:
  jenkins:
    name: jenkins   # 커스텀 네트워크 이름을 jenkins로 설정

volumes:
  jenkins-data:   # Jenkins 데이터를 영구적으로 저장할 볼륨
  jenkins-docker-certs:   # Docker 인증서 데이터를 저장할 볼륨

```

### DooD