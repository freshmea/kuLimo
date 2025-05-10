# ROS 수업

---

## 2025-04-12

---

- 1교시
  - ros1 설명
  - docker 설명
- 2교시
  - docker 설치
- 3교시
  - VsCode 에서 docker 사용하기 - dev container, docker extension
  - ros1 컨테이너 만들기 - ros:noetic-desktop-full
- 4교시
  - ubuntu22.04 의 display 설정
  - xhost 설정 : x11 : x org로 실행 및 x11 권한 설정
- 5교시
  - turtlesim 설명
  - ros1 cli 설명
- 6교시
  - ros1 package 만들기 - catkin_make -> hello_ros
  - Twist 메세지 사용 터틀심 움직이기
  - ros1 cli 분석 - rospack, rosnode, rosrun, rostopic
- 7교시
  - ros2 설명
- 8교시
  - ros2 package 만들기 - colcon build -> hello_ros2

---

## 2025-04-19

---

- 1교시
  - 복습
  - docker 설명
- 2교시
  - ros2 hello_ros class 만들기
  - rqt 활용 - topic publisher 사용
- 3교시
  - ros2 simple_sub 노드 만들기
- 4교시
  - ros2 simple_pub 노드 만들기
  - ros2 launch 파일 설명
- 5교시
  - message.launch.py 작성
- 6교시
  - ros1 docker 설정 - 복습
  - [docker 설정](/doc/docker/docker%20설정.md)
- 7교시
  - hello.py 코드 객체지향으로 변경
- 8교시
  - launch/message.launch 작성 (ros1 launch)
  - ros1 launch 로 hello.py 실행

---

## 2025-04-26

---

- 1교시
  - 복습
  - python setup.py 추가
  - ros1 mtpub 작성
- 2교시
  - ros1 mtsub 작성
- 3교시
  - ros1 launch 작성
- 4교시
  - [과제] 노드 5개 연결 통합 과제
- 5교시
  - 과제 풀이 - mtpub, mtsub, mpub, msub, msub2, launch
- 6교시
  - ros1 service 설명
  - ros1 simpleServiceServer 작성
  - ros1 simpleServiceServer 수정 - thread 코드 추가
- 7교시
  - ros1 simpleServiceClient 작성
  - ros1 asyncio 로 Serviceclient2 작성
- 8교시
  - ros2 service server 작성

---

## 2025-05-10

---

- 1교시
  - 복습
  - ros2 service server 테스트
- 2교시
  - ros2 service server2 비동기 서버 작성
- 3교시
  - ros2 service client 작성
- 4교시
  - ros2 파라미터 설명
- 5교시
  - ros2 param 명령어 - list, get, set, dump
  - simple_parameter.py 작성
  - launch 파일에 yaml 파일 사용(param dump turtlesim.yaml)
- 6교시
  - 터틀심 파라미터 실습
  - change_color_client.py 과제
- 7교시
  - ros1 parameter
- 8교시
  - ros1 parameter simple_parameter.py 작성
  - launch 파일 작성
