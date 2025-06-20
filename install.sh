#!/bin/bash

echo "LIMO 로봇 환경 설정 스크립트를 실행합니다."

# ROS 노에틱 설치 확인
if [ ! -d "/opt/ros/noetic" ]; then
    echo "ROS Noetic 설치 중..."
    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
    sudo apt update
    sudo apt install -y ros-noetic-desktop-full
    
    # ROS 환경 설정
    echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
    source /opt/ros/noetic/setup.bash
    
    # 의존성 도구 설치
    sudo apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
    if [ ! -f "/etc/ros/rosdep/sources.list.d/20-default.list" ]; then
        sudo rosdep init
    fi
    rosdep update
    
    echo "ROS Noetic 설치 완료"
else
    echo "ROS Noetic이 이미 설치되어 있습니다."
fi

# LIMO 작업 공간 생성
if [ ! -d "$HOME/limo_ws" ]; then
    echo "LIMO 작업 공간 생성 중..."
    mkdir -p $HOME/limo_ws/src
    cd $HOME/limo_ws/src
    
    # LIMO 패키지 클론
    git clone https://github.com/AGILEX-ROBOTICS/limo_ros.git
    cd ..
    
    # 의존성 설치
    rosdep install --from-paths src --ignore-src -r -y
    
    # 작업 공간 빌드
    catkin_make
    echo "source $HOME/limo_ws/devel/setup.bash" >> ~/.bashrc
    source $HOME/limo_ws/devel/setup.bash
    
    echo "LIMO 작업 공간 설정 완료"
else
    echo "LIMO 작업 공간이 이미 존재합니다."
fi

echo "LIMO 환경 설정이 완료되었습니다."
echo "터미널을 다시 열거나 'source ~/.bashrc' 명령을 실행하여 변경 사항을 적용하세요."
