# limo 실습

---

## limo 세팅

---

### 2.1 ROS 노에틱(Noetic) 설치 수정(Ubuntu 20.04)

```bash

# ROS 패키지 에러 수정
cd /etc/apt/sources.list.d/
sudo rm ros-latest.list
sudo rm ros-latest.list.save

# ROS 저장소 추가
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt upgrade

# domain server 설정
sudo nano /etc/resolv.conf
# nameserver 8.8.8.8 수정
sudo apt update && sudo apt upgrade

```

### 2.2 ROS 의존성 패키지 설치

```bash

# 의존성 설치
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo rosdep init
rosdep update
```

## 3. LIMO 패키지 설치

### 3.1 작업 공간 생성

```bash
cd ~
git clone clone https://github.com/freshmea/kuLimo.git # 본인의 github 주소로 변경
cd kuLimo/catkin_ws/src
git clone https://github.com/agilexrobotics/limo_ros.git
cd ~/kuLimo/catkin_ws
catkin_make
echo "source ~/kuLimo/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### 3.2 의존성 설치

```bash
rosdep install --from-paths src --ignore-src -r -y
```

## 4. LIMO 기본 작동 테스트

### 4.1 시뮬레이션 실행

```bash
# roscore uri 설정
export ROS_MASTER_URI=http://localhost:11311
export ROS_IP=$(hostname -I | awk '{print $1}')
# Gazebo 시뮬레이션 실행
roslaunch limo_gazebo_sim limo_four_diff.launch
roslaunch limo_gazebo_sim limo_four_diff.launch world_name:=$(find limo_gazebo_sim)/worlds/empty.world
```

### 4.2 실제 로봇 구동 - 실제 로봇 ssh에서 실행

```bash
# LIMO 로봇 기본 드라이버 실행
roslaunch limo_bringup limo_start.launch
```