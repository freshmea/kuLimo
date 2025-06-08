# ROS2 시뮬레이션 수업

---

## 2025-05-24

---

- 1교시
  - 복습
  - rviz2, gazebo 작동 원리
  - ku_description 패키지 생성
    - myfirst.urdf 작성
- 2교시
  - urdf_launch 패키지 설치
  - display.launch.py 작성
  - urdf 실습 예제 작성
    - origin.urdf 작성
- 3교시
  - urdf 작성(link, visual, joint tag)
    - visual.urdf 작성
  - urdf 체크 (check_urdf, rqt(tf-tree)) 확인
- 4교시
  - urdf 작성(joint, collision, inertial tag)
    - physics.urdf 작성
  - xacro 작성
    - model.xacro 작성(변수 및 매크로 사용 실습)
- 5교시
  - limo_ros2 description 패키지 설치 및 실습
  - gazebo 모델링 (sdf) - limo_ros2 패키지 분석
- 6교시
  - move_limo 노드 작성 (gazebo와 move_limo 연동)
  - limo xacro 파일 분석 및 tf tf_static 분석
- 7교시
  - turtlebot3_simulation 패키지 설치
  - gazebo에서 환경을 꾸미기
    - world 파일 작성
    - world 파일과 spawn.py로 로봇 배치
- 8교시
  - world 파일에 모델 추가(stop traffic sign 모델 추가)

---

## 2025-05-31

---

- 1교시
  - 복습
  - 슬램 개념 학습
- 2교시
  - gazebo 시뮬레이션 설정 - 복습
    - turtlebot3_simulation 패키지 설치
    - limo_ros2 패키지 설치
    - gazebo 설치
- 3교시
  - turtlebot3 패키지 설치
  - turtlebot3_gazebo 실습
- 4교시
  - cartographer 패키지 설치
  - turtlebot3_cartographer 패키지 설치
- 5교시
  - map_server 패키지 설치(nav2)
  - 지도 그리기 실습 - map.pgm, map.yaml 파일 생성
  - SLAM 파인 튜닝 방법 lua 변경 및 옵션 찾기 - thread, resolution, imu 설정
- 6교시
  - OccupancyGrid 메시지 이해
  - rviz2에서 OccupancyGrid 메시지 시각화
- 7교시
  - publish_map 노드 작성
- 8교시
  - scan 메시지 이해
  - scan 메시지와 map 메시지 연결 노드 작성

```bash
# 필요한 환경 변수
export TURTLEBOT3_MODEL=burger
source /usr/share/gazebo/setup.bash
export SVGA_VGPU10=0
alias killgazebo='pkill -9 gzserver; pkill -9 gzclient; pkill -9 gzweb; pkill -9 gzbridge'
# sudo apt install ros-humble-gazebo-*
# sudo apt install ros-humble-turtlebot3-msgs
# sudo apt install ros-humble-turtlebot3-teleop
# cd ~/kuLimo/colcon_ws/src
# git clone https://github.com/agilexrobotics/limo_ros2.git
# git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
# cd ~/kuLimo/colcon_ws/src/limo_ros2/limo_car
# mkdir log
# mkdir worlds
# mkdir src
# cb
# ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
# sudo apt install ros-humble-rqt-tf-tree
# ros2 run rqt_tf_tree rqt_tf_tree --force-discover
# ros2 run turtlebot3_teleop teleop_keyboard
# sudo apt install ros-humble-cartographer
# sudo apt install ros-humble-cartographer-ros
# git clone -b humble https://github.com/ROBOTIS-GIT/DynamixelSDK.git
# git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3.git
# sudo apt install ros-humble-navigation2
# sudo apt install ros-humble-nav2-bringup
# ros2 run nav2_map_server map_saver_cli -f map

# 카토그래퍼 실행
# 1. gazebo 실행 - ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
# 2. 터틀봇3 텔레옵 - ros2 run turtlebot3_teleop teleop_keyboard
# 3. 카토그래퍼 실행 - ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true
# 4. rqt 실행 - rqt -> node graph, tf tree.
# 운용 -> 텔레옵 움직여서 지도가 그려지는것 rviz2 창에서 확인!.

```

---

## 2025-06-07

---

- 1교시
  - 복습
  - Navigation2 개념 학습
- 2교시
  - 지도 그리기 실습 - nav2 를 위한 지도 저장
- 3교시
  - nav2 실행 - rviz2 에서 실습
- 4교시
  - follow_waypoints 노드 작성
- 5교시
  - patrol 노드 작성 (turtlebot3 가 gazebo에서 patrol)
  - dynamic tf 노드 작성
- 6교시
  - tf_listener 노드 작성
- 7교시
  - follow_turtlesim 노드 작성
- 8교시
  - follow_turtlesim 노드 수정

```bash
# SLAM 지도 그리기
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true
ros2 run turtlebot3_teleop teleop_keyboard
cd ~/kuLimo
ros2 run nav2_map_server map_saver_cli -f map

# Nav2 실행
# cartographer 는 종료한다.
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=/home/${USER}/kuLimo/map.yaml
# 2d pose estimate 실행
# nav2 goal 실행 -> 움직임 확인
# nav2 goal 실행 후 path 가 정해진다음 이동 경로에 장애물 설치 실습
```
