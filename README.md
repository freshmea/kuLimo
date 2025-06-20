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

---

# KU LIMO 로봇 세팅 가이드

이 저장소는 LIMO 로봇의 설치 및 구성 방법에 대한 안내를 제공합니다.

## 목차
1. 하드웨어 설정
2. ROS 설치
3. LIMO 패키지 설치
4. 기본 작동 테스트
5. 문제 해결

각 단계별 상세 설명은 해당 섹션을 참조하세요.
