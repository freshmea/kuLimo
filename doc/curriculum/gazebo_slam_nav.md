---
title: 고대_빅데이터사물인터넷 과정 강의 계획서
date: 2025-05-24
category: 로봇 시뮬레이션 및 내비게이션
tags: [ROS, Gazebo, SLAM, Navigation, AgileX, LIMO, 로봇 모델링]
---

# 「고대_빅데이터사물인터넷 과정」 로봇 시뮬레이션 및 내비게이션 강의 계획서

## 회차별 강의 계획

### 5월 24일 (토) - Gazebo 시뮬레이션 및 URDF 모델링

| 차시                | 강의 내용                                            |
| ------------------- | ---------------------------------------------------- |
| 1차시 (09:00~09:50) | Gazebo 시뮬레이터 소개 및 ROS1 연동 설정             |
| 2차시 (10:00~10:50) | URDF 기초: XML 구조 및 링크/조인트 개념              |
| 3차시 (11:00~11:50) | URDF 실습: 간단한 로봇 모델 제작 (링크, 조인트 구성) |
| 4차시 (12:00~12:50) | Xacro를 활용한 모듈식 URDF 작성법                    |
| 5차시 (14:00~14:50) | SDF 형식의 이해와 Gazebo World 구성 실습             |
| 6차시 (15:00~15:50) | Gazebo 플러그인 소개: 센서 및 액추에이터 모델링      |
| 7차시 (16:00~16:50) | AgileX LIMO 로봇 URDF 분석 및 Gazebo 시뮬레이션 구축 |
| 8차시 (17:00~17:50) | ROS 토픽을 통한 Gazebo 로봇 제어 및 센서 데이터 수집 |

### 5월 31일 (토) - SLAM(동시적 위치추정 및 지도작성)

| 차시                | 강의 내용                                          |
| ------------------- | -------------------------------------------------- |
| 1차시 (09:00~09:50) | SLAM 기술 개요: 위치 추정과 지도 작성의 원리       |
| 2차시 (10:00~10:50) | 센서 종류 및 특성 비교: LiDAR, 카메라, IMU         |
| 3차시 (11:00~11:50) | LiDAR 기반 ROS1 gmapping 패키지 실습               |
| 4차시 (12:00~12:50) | Gazebo에서 LIMO와 gmapping을 활용한 지도 생성      |
| 5차시 (14:00~14:50) | Google Cartographer 소개 및 설치                   |
| 6차시 (15:00~15:50) | Cartographer 파라미터 튜닝 및 LIMO 적용            |
| 7차시 (16:00~16:50) | 다중 센서 융합 SLAM: 2D/3D LiDAR와 IMU 데이터 활용 |
| 8차시 (17:00~17:50) | 생성된 지도 저장 및 최적화, RViz를 통한 시각화     |

### 6월 7일 (토) - 자율 주행 및 내비게이션

| 차시                | 강의 내용                                            |
| ------------------- | ---------------------------------------------------- |
| 1차시 (09:00~09:50) | 로봇 내비게이션 시스템 구성 요소 및 원리             |
| 2차시 (10:00~10:50) | ROS1 move_base 패키지 구조 및 파라미터 소개          |
| 3차시 (11:00~11:50) | AMCL(Adaptive Monte Carlo Localization) 원리 및 설정 |
| 4차시 (12:00~12:50) | 비용 지도(costmap) 개념 및 설정 방법                 |
| 5차시 (14:00~14:50) | LIMO 로봇 move_base 설정 및 파라미터 튜닝            |
| 6차시 (15:00~15:50) | 경로 계획 알고리즘 비교: DWA, TEB 플래너             |
| 7차시 (16:00~16:50) | LIMO 로봇 자율 주행 실습: 목표점 설정 및 장애물 회피 |
| 8차시 (17:00~17:50) | 복합 미션 구현: LIMO 로봇의 자율 탐색 및 물체 인식   |

## 실습 환경

- **운영체제**: Ubuntu 20.04 LTS
- **ROS 버전**: ROS1 Noetic
- **시뮬레이터**: Gazebo 11
- **로봇 플랫폼**: AgileX Robotics LIMO
- **필수 패키지**:
  - `limo_ros` - AgileX LIMO 기본 드라이버 및 메시지
  - `slam_gmapping` - 2D LiDAR 기반 SLAM
  - `cartographer_ros` - Google Cartographer SLAM
  - `move_base` - ROS 내비게이션 스택
  - `amcl` - 로봇 위치 추정
  - `rviz` - 시각화 도구

## 참고 자료

- AgileX Robotics LIMO 사용자 매뉴얼
- ROS Wiki (http://wiki.ros.org/)
- Gazebo 튜토리얼 (http://gazebosim.org/tutorials)
- 「Programming Robots with ROS」 - Morgan Quigley, Brian Gerkey, and William D. Smart
