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
roslaunch limo_gazebo_sim limo_four_diff.launch world_name:=$(rospack find limo_gazebo_sim)/worlds/empty.world
roslaunch limo_gazebo_sim limo_four_diff.launch world_name:=$(rospack find turtlebot3_gazebo)/worlds/turtlebot3_stage_1.world
```

### 4.2 limo URDF 변경

- 메쉬 파일이 너무 커서 느림
  - limo_ros 의 limo_description/urdf/limo_four_diff.xacro 수정

```xml

<!-- Base link -->
    <link name="base_link">
        <visual>
            <origin xyz="0 0 -0.07" rpy="0 0 1.57" />
            <geometry>
                <box size="${base_x_size} ${base_y_size} ${base_z_size}"/>
            </geometry>
        </visual>
        <collision>
            <origin xyz="0 0 -0.07" rpy="0 0 1.57" />
            <geometry>
                <box size="${base_x_size} ${base_y_size} ${base_z_size}"/>
            </geometry>
        </collision>
    </link>
```

- 링크 수정 limo_description/urdf/limo_xacro.xacro

```xml
<xacro:macro name="limo_wheel" params="parent_prefix wheel_prefix reflect *joint_pose">
        <link name="${wheel_prefix}_wheel_link">
            <inertial>
                <origin xyz="0 0 0" />
                <mass value="0.5" />
                <inertia ixx="0.01055" ixy="0" ixz="0" iyy="0.00075" iyz="0" izz="0.01055" />
            </inertial>
            <visual>
                <origin xyz="0 0 0" rpy="0 1.57 1.57" />
                <geometry>
                    <cylinder length="${wheel_length}" radius="${wheel_radius}" />
                </geometry>
            </visual>
            <collision>
                <origin xyz="0 ${wheel_length/2} 0" rpy="0 1.57 1.57" />
                <geometry>
                    <cylinder length="${wheel_length}" radius="${wheel_radius}" />
                </geometry>
            </collision>
        </link>
```

- point cloud 제거 및 기타 센서 조절
- limo_description/urdf/limo_gazebo.gazebo

```xml
비쥬얼 제거
<visualize>false</visualize>
주석처리
<!-- <depthImageTopicName>/limo/depth/image_raw</depthImageTopicName>
<depthImageCameraInfoTopicName>/limo/depth/camera_info</depthImageCameraInfoTopicName>
<pointCloudTopicName>/limo/depth/points</pointCloudTopicName> -->
imu hz 조정
100 -> 30
        <update_rate>30</update_rate>
```

### 4.3 launch 파일 수정

- robotname space 변경

```xml
<?xml version="1.0"?>
<launch>
    <arg name="robot_namespace" default="limo"/>
    <arg name="world_name" default="$(find limo_gazebo_sim)/worlds/willowgarage.world"/>

    <include file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="world_name" value="$(arg world_name)"/>
        <arg name="paused" value="false"/>
        <arg name="use_sim_time" value="true"/>
        <arg name="gui" value="true"/>
        <arg name="headless" value="false"/>
        <arg name="debug" value="false"/>
        <arg name="verbose" value="true"/>
    </include>

    <param name="robot_description" command="$(find xacro)/xacro '$(find limo_description)/urdf/limo_four_diff.xacro' robot_namespace:=$(arg robot_namespace)" />

    <!-- initial pose -->
    <arg name="x" default="0.0"/>
    <arg name="y" default="0.0"/>
    <arg name="z" default="0.0"/>
    <arg name="yaw" default="0.0"/>
    <node name="spawn_limo_model" pkg="gazebo_ros" type="spawn_model" args="-x $(arg x)
              -y $(arg y)
              -z $(arg z)
              -Y $(arg yaw)
              -unpause
              -urdf
              -param robot_description
              -model 'limo$(arg robot_namespace)'" />

    <!-- Load joint controller configurations from YAML file to parameter server -->
    <rosparam file="$(find limo_gazebo_sim)/config/limo_four_diff_control.yaml" command="load" ns="$(arg robot_namespace)"/>

    <!-- load the controllers -->
    <node name="controller_spawner" pkg="controller_manager" type="spawner" respawn="false" output="screen" args="limo_state_controller " ns="$(arg robot_namespace)"/>

    <node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" ns="$(arg robot_namespace)"/>

    <node pkg="tf" type="static_transform_publisher" name="base_link_to_laser_link" args="0.105 0.0 0.08 0.0 0.0 0.0 /base_link /laser_link 10" />
    <node pkg="tf" type="static_transform_publisher" name="base_link_to_imu_link" args="0.0 0.0 0.0 0.0 0.0 0.0 /base_link /imu_link 10" />


    <node name="rviz" pkg="rviz" type="rviz" args="-d $(find limo_description)/rviz/model_display.rviz" />
</launch>
```

### 4.4 gazebo 실행 노드 추가

- teleop_key launch 작성

```xml
<?xml version="1.0"?>
<launch>
    <arg name="repeat_rate" value="50.0" />
    <node name="teleop_keybord" pkg="teleop_twist_keyboard" type="teleop_twist_keyboard.py" output="screen">
        <param name="repeat_rate" value="$(arg repeat_rate)" />
        <remap from="cmd_vel" to="/limo/cmd_vel"/>
    </node>
</launch>
```

-track_application_simulation.launch

```xml
<launch>
    <node pkg="limo_application" name="stop" type="stop.py"/>
    <node pkg="limo_application" name="control" type="control.py">
        <remap from="cmd_vel" to="limo/cmd_vel"/>
    </node>
    <node pkg="limo_application" name="Line_detect" type="Line_detect.py">
        <remap from="camera/rgb/image_raw/compressed" to="limo/color/image_raw/compressed"/>
    </node>
</launch>
```

