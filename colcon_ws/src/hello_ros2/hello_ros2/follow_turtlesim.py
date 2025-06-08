# sudo apt install ros-humble-tf-transformations
# ros2 run turtlesim turtlesim_node
# ros2 run hello_ros2 follow_turtlesim
# rviz2 -> tf 확인
# ros2 run turtlesim turtle_teleop_key

import math

import rclpy
from geometry_msgs.msg import TransformStamped, Twist
from rclpy import time
from rclpy.node import Node
from tf2_ros.buffer import Buffer
from tf2_ros.transform_broadcaster import TransformBroadcaster
from tf2_ros.transform_listener import TransformListener
from tf_transformations import euler_from_quaternion, quaternion_from_euler
from turtlesim.msg import Pose
from turtlesim.srv import Spawn


class Follow_turtle(Node):
    def __init__(self):
        super().__init__("follow_turtle")  # node name
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(0.1, self.on_timer)
        self.spawner = self.create_client(Spawn, "spawn")
        request = Spawn.Request()
        request.x = 3.0
        request.y = 3.0
        request.theta = 0.0
        self.msg = Pose()
        self.result = self.spawner.call_async(request)
        self.result.add_done_callback(self.spawn_cb)
        self.tf_br = TransformBroadcaster(self)
        self.sub = self.create_subscription(Pose, "/turtle1/pose", self.sub_cb, 10)
        self.sub2 = self.create_subscription(Pose, "/turtle2/pose", self.sub_cb2, 10)
        self.pub = self.create_publisher(Twist, "/turtle2/cmd_vel", 10)

    def spawn_cb(self, future):
        try:
            response = future.result()
            if response.name == "turtle2":
                self.get_logger().info("Turtle2 spawned successfully!")
            else:
                self.get_logger().error("Failed to spawn turtle2.")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

    def sub_cb(self, msg: Pose):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world"
        t.child_frame_id = "turtle1"
        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0
        quat = quaternion_from_euler(0, 0, msg.theta)  # r y p
        t.transform.rotation.x = quat[0]
        t.transform.rotation.y = quat[1]
        t.transform.rotation.z = quat[2]
        t.transform.rotation.w = quat[3]
        self.tf_br.sendTransform(t)

    def sub_cb2(self, msg: Pose):
        self.msg = msg
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world"
        t.child_frame_id = "turtle2"
        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0
        quat = quaternion_from_euler(0, 0, msg.theta)  # r y p
        t.transform.rotation.x = quat[0]
        t.transform.rotation.y = quat[1]
        t.transform.rotation.z = quat[2]
        t.transform.rotation.w = quat[3]
        self.tf_br.sendTransform(t)

    def on_timer(self):
        try:
            transform_to_turtle1 = self.tf_buffer.lookup_transform(
                "turtle2", "turtle1", time.Time()
            )
        except Exception as e:
            self.get_logger().info(f"Lookup transform failed: {e}")
            return

        msg = Twist()
        msg.angular.x = 0.0
        msg.angular.y = 0.0

        angle_error_rad = math.atan2(
            transform_to_turtle1.transform.translation.y,
            transform_to_turtle1.transform.translation.x,
        )

        # 회전 제어 로직
        angular_speed = 2.0
        angle_threshold = 0.1  # 라디안 (약 5.7도)

        if angle_error_rad > angle_threshold:
            msg.angular.z = angular_speed  # 반시계 방향 회전
        elif angle_error_rad < -angle_threshold:
            msg.angular.z = -angular_speed  # 시계 방향 회전
        else:
            msg.angular.z = 0.0  # 목표 방향

        distance_squared = (
            transform_to_turtle1.transform.translation.x**2
            + transform_to_turtle1.transform.translation.y**2
        )

        if distance_squared > 0.2:  # 임계값은 필요에 따라 조정
            msg.linear.x = 3.0
        else:
            msg.linear.x = 0.0  # 목표 근처에 도달하면 정지

        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Follow_turtle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
