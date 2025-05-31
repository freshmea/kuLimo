# kuLimo

---

- limo 수업
  - 1조: 박인규, 정명재, 구찬형, 이현성, 박윤국
  - 2조: 박정우, 차경민, 김학민, 장대진, 이경용
  - 3조: 손건희, 최근호, 김지숙, 이승원
  - 4조: 윤형정, 최용규, 이한솔, 맹진수, 정용태

- Vmware player 파일 다운로드
[링크](https://drive.google.com/file/d/1twlHYAgrWeLSQRO_vHy68lJxr-n1qIWl/view?usp=sharing)

- vscode deb 파일
[링크](https://drive.google.com/file/d/1We4ILpw1NTzpspkflSpvdZikvyApTxn0/view?usp=sharing)

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

# 카토그래퍼 실행
# 1. gazebo 실행 - ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
# 2. 터틀봇3 텔레옵 - ros2 run turtlebot3_teleop teleop_keyboard
# 3. 카토그래퍼 실행 - ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true
# 4. rqt 실행 - rqt -> node graph, tf tree.
# 운용 -> 텔레옵 움직여서 지도가 그려지는것 rviz2 창에서 확인!.

```

```bash
# 31번 라인
if [[ "$TERM" == *color* ]]; then
    color_prompt=yes
fi
# 맨 아래에 추가
source /opt/ros/noetic/setup.bash # ros를 초기화.
source ~/kuLimo/catkin_ws/devel/setup.bash
export XDG_RUNTIME_DIR=/run/user/$(id -u)
mkdir -p /run/user/$(id -u)
chmod 700 /run/user/$(id -u)
```

---

## 파이썬 수업

---

- 수업 일정 (2일)
  - 2025-03-15, 2025-04-05
- 수업 목표
  - VMware 를 이용한 가상환경 운용
  - 리눅스 명령어
  - 파이썬 기초 문법
- [과정 진행 사항](doc/python.md)

---

## ROS1, ROS2 수업

---

- 수업 목표
  - ROS1, ROS2 기초 문법
  - ROS1, ROS2 패키지 만들기
  - ROS1, ROS2 패키지 사용하기
- [과정 진행 사항](doc/ros.md)

---

## 로봇 시뮬레이션 SLAM NAV2 수업

---

- 수업 목표
  - 로봇 시뮬레이션 환경 구축
  - urdf 파일을 이용한 로봇 모델링
  - xacro 파일을 이용한 로봇 모델링
  - SLAM, NAV2 패키지 사용하기
- [과정 진행 사항](doc/simulation.md)
