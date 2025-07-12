---
title: 「고대_Limo ros 과정」 LIMO 로봇 강의 계획서
date: 2025-06-14
category: LIMO 로봇 프로그래밍
tags: [LIMO, ROS, 로봇제어, SLAM, Navigation, Gazebo, 시뮬레이션]
---

## 회차별 강의 계획

### 6월 14일 (토) - LIMO 하드웨어 및 기본 제어

| 차시                | 강의 내용                                                |
| ------------------- | -------------------------------------------------------- |
| 1차시 (09:00~09:50) | 복습 및 LIMO 하드웨어 개요                               |
| 2차시 (10:00~10:50) | LIMO 동작 테스트 - 조정기 사용 및 chassis 보드 직접 연결 |
| 3차시 (11:00~11:50) | LIMO 매카넘 모드, akerman 모드, omni 모드 테스트 실습    |
| 4차시 (12:00~12:50) | teleop, teleop_twist_keyboard 패키지 설치 및 테스트      |
| 5차시 (14:00~14:50) | SSH 연결을 통한 LIMO teleop_twist_keyboard 원격 제어     |
| 6차시 (15:00~15:50) | LIMO SLAM 실습 - gmapping을 이용한 교육장 지도 만들기    |
| 7차시 (16:00~16:50) | 생성된 지도 저장 및 LIMO nav2 실습                       |
| 8차시 (17:00~17:50) | LIMO nav2를 이용한 교육장 patrol 실습                    |

### 6월 21일 (토) - ROS 분산 컴퓨팅 및 LIMO 응용

| 차시                | 강의 내용                                                      |
| ------------------- | -------------------------------------------------------------- |
| 1차시 (09:00~09:50) | 복습 및 ROS1 분산 컴퓨팅을 위한 노트북 환경 설정               |
| 2차시 (10:00~10:50) | ROSMASTER_IP 설정 및 네트워크 구성                             |
| 3차시 (11:00~11:50) | 노트북에서 ROS1 노드 실행 - teleop으로 LIMO 원격 조종          |
| 4차시 (12:00~12:50) | ROS1 토픽 분석 및 LIMO 원형 주행 노드 작성                     |
| 5차시 (14:00~14:50) | LIMO_application 패키지 소개 - stop, control, line_detect 노드 |
| 6차시 (15:00~15:50) | LIMO_application 패키지 실습 및 동작 테스트                    |
| 7차시 (16:00~16:50) | 트랙 설치 및 LIMO_application 패키지 최적화 실습               |
| 8차시 (17:00~17:50) | LIMO_application 패키지 성능 개선 및 안정화 실습               |

### 6월 28일 (토) - Gazebo 시뮬레이션 및 환경 구성

| 차시                | 강의 내용                                                      |
| ------------------- | -------------------------------------------------------------- |
| 1차시 (09:00~09:50) | 복습 및 ROS1 Gazebo 환경 설정                                  |
| 2차시 (10:00~10:50) | limo_gazebo_sim 패키지 설치 및 구성                            |
| 3차시 (11:00~11:50) | limo_gazebo_sim URDF 수정 - namespace 적용                     |
| 4차시 (12:00~12:50) | limo_gazebo_sim 실행 및 limo_teleop_keyboard_simul.launch 작성 |
| 5차시 (14:00~14:50) | limo_gazebo_sim 패키지 launch 파일 분석                        |
| 6차시 (15:00~15:50) | turtlebot3_gazebo 월드/모델 파일 활용 및 바닥 텍스처 변경 실습 |
| 7차시 (16:00~16:50) | Gazebo Fuel 모델 적용 및 limo_application 시뮬레이션 수정      |
| 8차시 (17:00~17:50) | 실제 LIMO 로봇과 Gazebo 시뮬레이션 통합 테스트 실습            |

### 7월 5일 (토) - SLAM 및 Navigation 시뮬레이션

| 차시                | 강의 내용                                                         |
| ------------------- | ----------------------------------------------------------------- |
| 1차시 (09:00~09:50) | 복습, LIMO SLAM 패키지 및 NAV2 패키지 설치                        |
| 2차시 (10:00~10:50) | willow_garage_world 환경에서 teleop_twist_keyboard로 LIMO 조작    |
| 3차시 (11:00~11:50) | 시뮬레이션 환경에서 LIMO SLAM 실행 - limo_gmapping_simul.launch   |
| 4차시 (12:00~12:50) | LIMO SLAM을 이용한 교육장 지도 생성 실습                          |
| 5차시 (14:00~14:50) | limo_navigation 패키지 소개 및 limo_navigation_simul.launch 작성  |
| 6차시 (15:00~15:50) | Navigation을 이용한 LIMO Gazebo 시뮬레이션 및 patrol_limo.py 작성 |
| 7차시 (16:00~16:50) | hello_ros 패키지에 patrol_limo.py 노드 시뮬레이션 실습            |
| 8차시 (17:00~17:50) | 실제 LIMO 기체에 patrol_limo.py 노드 적용 및 통합 테스트          |
