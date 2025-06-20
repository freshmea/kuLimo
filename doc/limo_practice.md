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
sudo apt update
sudo apt upgrade

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
