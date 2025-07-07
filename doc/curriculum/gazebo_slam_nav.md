---
title: 「고대_Limo ros2 과정」 로봇 시뮬레이션 및 내비게이션 강의 계획서
date: 2025-05-24
category: 로봇 시뮬레이션 및 내비게이션
tags: [ROS2, Humble, Gazebo, SLAM, Navigation2, AgileX, LIMO, 로봇 모델링, URDF, Xacro, Cartographer]
---

## 회차별 강의 계획

### 5월 24일 (토) - Gazebo 시뮬레이션 및 URDF 모델링 (ROS2 Humble)

| 차시                | 강의 내용                                                                    |
| ------------------- | ---------------------------------------------------------------------------- |
| 1차시 (09:00~09:50) | Gazebo 시뮬레이터 소개 및 ROS2 연동, RViz2, ku_description 패키지 생성       |
| 2차시 (10:00~10:50) | URDF 기초: XML 구조, 링크/조인트 개념, urdf_launch 패키지, display.launch.py |
| 3차시 (11:00~11:50) | URDF 실습: 간단한 로봇 모델 제작 (link, visual, joint 태그), URDF 체크       |
| 4차시 (12:00~12:50) | URDF 고급: collision, inertial 태그, Xacro를 활용한 모듈식 URDF 작성법       |
| 5차시 (14:00~14:50) | SDF 형식 이해, Gazebo World 구성, limo_ros2 description 패키지 분석          |
| 6차시 (15:00~15:50) | Gazebo 플러그인, LIMO xacro 분석, TF 및 TF_static, move_limo 노드 작성       |
| 7차시 (16:00~16:50) | turtlebot3_simulation 패키지, Gazebo 환경 구성 (world 파일 작성)             |
| 8차시 (17:00~17:50) | Gazebo World에 모델 추가 (spawn.py 활용), ROS 토픽을 통한 로봇 제어          |

### 5월 31일 (토) - SLAM(동시적 위치추정 및 지도작성) (ROS2 Humble)

| 차시                | 강의 내용                                                                        |
| ------------------- | -------------------------------------------------------------------------------- |
| 1차시 (09:00~09:50) | SLAM 기술 개요: 위치 추정과 지도 작성의 원리, 센서 종류 및 특성                  |
| 2차시 (10:00~10:50) | Gazebo 시뮬레이션 설정 복습 (turtlebot3_simulation, limo_ros2)                   |
| 3차시 (11:00~11:50) | turtlebot3_gazebo 실습 및 ROS2 Cartographer 패키지 소개 및 설치                  |
| 4차시 (12:00~12:50) | Gazebo에서 LIMO/TurtleBot3와 Cartographer를 활용한 지도 생성 (실습)              |
| 5차시 (14:00~14:50) | Cartographer 파라미터 튜닝 (lua 파일 수정, 옵션 탐색: thread, resolution, IMU)   |
| 6차시 (15:00~15:50) | 생성된 지도 저장 (map_server 활용: map.pgm, map.yaml), OccupancyGrid 메시지 이해 |
| 7차시 (16:00~16:50) | RViz2에서 OccupancyGrid 시각화, publish_map 노드 작성 (개념)                     |
| 8차시 (17:00~17:50) | LaserScan 메시지 이해, Scan 메시지와 Map 메시지 연동 (개념)                      |

### 6월 7일 (토) - 자율 주행 및 내비게이션 (ROS2 Humble)

| 차시                | 강의 내용                                                                    |
| ------------------- | ---------------------------------------------------------------------------- |
| 1차시 (09:00~09:50) | 로봇 내비게이션 시스템(Navigation2) 구성 요소 및 원리                        |
| 2차시 (10:00~10:50) | ROS2 Navigation2 스택 구조 및 주요 파라미터 소개 (nav2_bringup)              |
| 3차시 (11:00~11:50) | AMCL(Adaptive Monte Carlo Localization) 원리 및 설정 (Nav2)                  |
| 4차시 (12:00~12:50) | 비용 지도(costmap) 개념 및 설정 방법 (Nav2), Nav2를 위한 지도 저장 실습      |
| 5차시 (14:00~14:50) | LIMO/TurtleBot3 로봇 Nav2 설정 및 파라미터 튜닝, RViz2에서 Nav2 실행         |
| 6차시 (15:00~15:50) | 경로 계획 알고리즘 (Nav2 플래너), follow_waypoints 노드 작성 및 실습         |
| 7차시 (16:00~16:50) | LIMO/TurtleBot3 로봇 자율 주행 실습: 목표점 설정, 장애물 회피, patrol 노드   |
| 8차시 (17:00~17:50) | TF 동적 변환 노드 작성, TF 리스너 노드 작성, follow_turtlesim 노드 실습/수정 |

## 실습 환경

- **운영체제**: Ubuntu 20.04 LTS (또는 22.04 LTS 권장)
- **ROS 버전**: ROS2 Humble Hawksbill
- **시뮬레이터**: Gazebo (Gazebo 11 또는 최신 호환 버전)
- **로봇 플랫폼**: AgileX Robotics LIMO, TurtleBot3
- **필수 패키지**:
  - `limo_ros2` - AgileX LIMO ROS2 드라이버 및 메시지
  - `turtlebot3_simulations` - TurtleBot3 시뮬레이션 패키지
  - `cartographer_ros` - Google Cartographer SLAM (ROS2 버전)
  - `navigation2`, `nav2_bringup` - ROS2 내비게이션 스택
  - `slam_toolbox` (선택적 SLAM 옵션)
  - `rviz2` - ROS2 시각화 도구
  - `tf_transformations`, `tf2_ros`

## 참고 자료

- AgileX Robotics LIMO 사용자 매뉴얼 (ROS2 버전 확인)
- [ROS2 공식 문서](https://docs.ros.org/en/humble/)
- [Gazebo 튜토리얼](http://gazebosim.org/tutorials)
- [Navigation2 공식 문서](https://navigation.ros.org/)
- [Cartographer ROS 문서](https://google-cartographer-ros.readthedocs.io/)
