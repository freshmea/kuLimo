# LIMO 실습

---

## 2025-06-14

---

- 1교시
  - 복습
  - LIMO 하드 웨어 개요
- 2교시
  - LIMO 동작 테스트 - 조정기 사용. chassis 보드 에 직접 연결
- 3교시
  - [실습] LIMO 매카넘 모드, akerman 모드, omni 모드 테스트
- 4교시
  - teleop, teleop_twist_keyboard 패키지 설치
  - LIMO teleop_twist_keyboard 테스트
  - ssh 로 연결해서 LIMO teleop_twist_keyboard 테스트
- 5교시
  - LIMO slam 실습 - gmapping
- 6교시
  - [실습] LIMO slam 으로 교육장 지도 만들기
  - 지도 저장
- 7교시
  - LIMO nav2 실습
  - LIMO nav2 로 교육장 patrol
- 8교시
  - [실습] LIMO nav2 로 교육장 patrol

---

## 2025-06-21

---

- 1교시
  - 복습
  - 노트북 세팅 - ROS1 분산 컴퓨팅을 위한 노트북 세팅
- 2교시
  - ROSMASTER_IP 설정
- 3교시
  - 노트북 에서 ROS1 노드 실행 - teleop 으로 LIMO 조종
- 4교시
  - 노트북 에서 ROS1 토픽 확인한 후에 LIMO로 원을 그리는 노드 작성
- 5교시
  - LIMO_application 패키지 설명
  - stop노드, control 노드, line_detect 노드 실행
- 6교시
  - LIMO_application 패키지 실습
- 7교시
  - 트랙 설치
  - [실습] LIMO_application 패키지 실습 - 잘 움직일 수 있게 수정
- 8교시
  - [실습] LIMO_application 패키지 실습 - 잘 움직일 수 있게 수정

---

## 2025-06-28

---

- 1교시
  - 복습
  - ros1 gazebo 설정
- 2교시
  - limo_gazebo_sim 패키지 설치
- 3교시
  - limo_gazebo_sim urdf 수정 - namespace 적용. limo
- 4교시
  - [실습] limo_gazebo_sim 실행
  - (시뮬레이션) limo_bringup 패키지의 limo_teleop 실행으로 조작하기
    - limo_teleop_keyboard_simul.launch 파일 작성 - namespace 적용
- 5교시
  - limo_gazebo_sim 패키지의 launch 파일 분석
- 6교시
  - turtlebot3_gazebo 패키지에서 월드 파일 및 모델 파일 가져오기
  - [실습] 바닥 그림을 원하는 이미지로 변경하기
  - world 파일 분석 및 수정 - gazebo fuel 에서 모델 가져와서 적용하기
- 7교시
  - limo_application 패키지 수정 - gazebo 에서 동작하도록 수정
  - 수정된 코드를 이용해서 실제 LIMO 로봇에서 동작 테스트
- 8교시
  - [실습] LIMO 로봇에서 gazebo 시뮬레이션 실행

---

## 2025-07-05

---

- 1교시
  - 복습
  - limo SLAM 패키지 설치
  - limo NAV2 패키지 설치
- 2교시
  - willow_garage_world 월드 파일 gazebo 에서 실행
  - teleop_twist_keyboard 패키지로 LIMO 조작
- 3교시
  - simulation 환경에서 LIMO SLAM 실행
    - limo_gmapping_simul.launch 파일 작성
  - 지도 저장
- 4교시
  - [실습] LIMO SLAM 으로 교육장 지도 만들기
- 5교시
  - limo_navigation 패키지 설명
  - limo_navigation 패키지 실행
    - limo_navigation_simul.launch 파일 작성
- 6교시
  - navigation 으로 LIMO gazebo 시뮬레이션 실행
  - hello_ros 패키지에 patrol_limo.py 노드 작성
- 7교시
  - [실습] hello_ros 패키지에 patrol_limo.py - 시뮬레이션
- 8교시
  - [실습] 실제 기체에 patrol_limo.py 노드 실행
