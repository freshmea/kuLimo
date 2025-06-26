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
# 31번 라인
if [[ "$TERM" == *color* ]]; then
    color_prompt=yes
fi
--> color_prompt=yes
# 맨 아래에 추가
source /opt/ros/noetic/setup.bash # ros를 초기화.
source ~/kuLimo/catkin_ws/devel/setup.bash
source /usr/share/gazebo/setup.bash # gazebo를 초기화.
export XDG_RUNTIME_DIR=/run/user/$(id -u)
mkdir -p /run/user/$(id -u)
chmod 700 /run/user/$(id -u)

export ROS_MASTER_URL=http://localhost:11311
export ROS_IP=$(hostname -I | awk '{print $1}')

alias nb='sudo nano ~/.bashrc'
alias sb='source ~/.bashrc'
alias cm='cd ~/kuLimo/catkin_ws && catkin_make'
alias killgazebo='kill -9 gzserver gzclient'

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

---

```limo bashrc
#Limo versions:Emmc_v1
source /opt/ros/melodic/setup.bash
source ~/wego_ws/devel/setup.bash
alias nb='sudo nano ~/.bashrc'
alias sb='source ~/.bashrc'
alias cm='cd ~/wego_ws && catkin_make'

export PATH=/usr/local/cuda-10.2/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH
rosclean purge -y

export ROS_MASTER_URL=http://192.168.1.16:11311
export ROS_IP=192.168.1.16
export LD_LIBRARY_PATH=/usr/lib/aarch64-linux-gnu:$LD_LIBRARY_PATH
```