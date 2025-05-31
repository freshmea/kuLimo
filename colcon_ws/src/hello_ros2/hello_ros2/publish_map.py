import rclpy
from nav_msgs.msg import OccupancyGrid
from rclpy.node import Node


class PublishMap(Node):
    def __init__(self):
        super().__init__("publish_map")  # node name
        self.create_timer(0.01, self.pub_cb)
        self.pub = self.create_publisher(OccupancyGrid, "/map", 10)
        self.msg = OccupancyGrid()
        self.msg.header.frame_id = "test map"
        self.msg.info.resolution = 0.1
        self.msg.info.width = 200
        self.msg.info.height = 100
        self.msg.info.origin.position.x = 0.0
        self.msg.info.origin.position.y = 0.0
        self.msg.info.origin.position.z = 0.0
        self.msg.info.origin.orientation.x = 0.0
        self.msg.info.origin.orientation.y = 0.0
        self.msg.info.origin.orientation.z = 0.0
        self.msg.info.origin.orientation.w = 1.0

        self.msg.data = [-1 for _ in range(20_000)]

    def pub_cb(self):
        self.msg.header.stamp = self.get_clock().now().to_msg()
        self.pub.publish(self.msg)


def main():
    rclpy.init()
    node = PublishMap()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()


if __name__ == "__main__":
    main()
