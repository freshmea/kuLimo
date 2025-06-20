
## 4. LIMO 기본 작동 테스트

### 4.1 시뮬레이션 실행

```bash
# Gazebo 시뮬레이션 실행
roslaunch limo_gazebo limo_ackermann.launch
```

### 4.2 실제 로봇 구동

```bash
# LIMO 로봇 기본 드라이버 실행
roslaunch limo_bringup limo_start.launch
```

### 4.3 원격 조종

```bash
# 키보드로 제어
roslaunch limo_bringup limo_teleop_keyboard.launch
```

## 5. 주행 모드 설정

LIMO는 네 가지 주행 모드를 지원합니다:
1. 차동 구동(Differential) 모드
2. 아커만(Ackermann) 모드
3. 전방향(Omni-directional) 모드
4. 트랙(Track) 모드

주행 모드 변경 방법:
```bash
rosservice call /limo_driver/set_model_mode "model_mode: 1"  # 0: 차동, 1: 아커만, 2: 전방향, 3: 트랙
```

## 6. 센서 설정

### 6.1 LiDAR 설정

```bash
# LiDAR 구동
roslaunch limo_bringup lidar.launch
```

### 6.2 카메라 설정

```bash
# 카메라 구동
roslaunch limo_bringup camera.launch
```

## 7. 문제 해결

### 통신 오류
- USB 연결 상태 확인
- 전원 상태 확인
- `dmesg` 명령으로 디바이스 인식 여부 확인

### 구동 문제
- 배터리 상태 확인
- 모터 이상 유무 확인
- 주행 모드가 올바르게 설정되었는지 확인

### 소프트웨어 문제
- ROS 패키지 재설치
- 작업 공간 다시 빌드
- 로그 확인: `rosrun rqt_console rqt_console`
