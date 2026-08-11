#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 
from std_msgs.msg import String 
from rclpy.executors import MultiThreadedExecutor


class arm_controller_node(Node):
    def __init__(self):
     super().__init__("arm_controller_node")
     self.get_logger().info("Arm controller node is ready.")     
     self.joint1_publisher = self.create_publisher(String, "joint1_topic", 10)  
    #  self.timer = self.create_timer(5.0, self.timer_callback)
    # def timer_callback(self): 
     msg = String()
     msg.data = "BaseJoint is ready."
     self.joint1_publisher.publish(msg)     
     self.get_logger().info(f"Published message: {msg.data}") 


  
 
# class jointnode1(Node): 
#     def __init__(self):
#      super().__init__("BaseJoint") 
#      self.subscription = self.create_subscription(String, 'joint1_topic', self.listener_callback, 10)   
#     def listener_callback(self, msg):
#       self.get_logger().info(f"Received: {msg.data}")
 
   
class JointNode2(Node): 
    def __init__(self):
        super().__init__("ShoulderJoint")   
        self.get_logger().info("ShoulderJoint is ready.")   
      

class jointnode3(Node): 
    def __init__(self):
        super().__init__("BaseJoint") 
        self.subscription = self.create_subscription(String, 'joint1_topic', self.listener_callback, 10)   
    def listener_callback(self, msg):
        self.get_logger().info(f"Received on joint1_topic: {msg.data}") 
       


class jointnode4(Node):   
    def __init__(self):
        super().__init__("ElbowJoint") 
        self.get_logger().info("ElbowJoint is ready.")


class system_ready(Node): 
    def __init__(self): 
        super().__init__("system_ready")  
        self.get_logger().info( "========================== \n"
                                     "Robot Arm Controller\n"
                                     "Robot Name : ARM-01\n"
                                     "Joints : 4\n"
                                     "Status READY\n"
                                     "========================== ")   
   
# class HeartbeatNode(Node):
#     def __init__(self):
#         super().__init__("HeartbeatNode")
#         self.counter = 0
#         self.timer = self.create_timer(1.0, self.timer_callback)

#     def timer_callback(self): 
#         self.counter += 1
#         self.get_logger().info(f" :) Heartbeat:{self.counter}")

def main(args=None):
    rclpy.init(args=args)
    arm_node = arm_controller_node()   
    # joint_node1 = jointnode1()
    joint_node2 = JointNode2()
    joint_node3 = jointnode3()  
    joint_node4 = jointnode4()  
    system_ready_node = system_ready()  
    # heartbeat_node = HeartbeatNode()    

    # rclpy.spin_once(arm_node, timeout_sec=1) 
    # rclpy.spin_once(joint_node2, timeout_sec=1) 
    # rclpy.spin_once(joint_node3, timeout_sec=1)  
    # rclpy.spin_once(joint_node4, timeout_sec=1)
    # rclpy.spin_once(system_ready_node, timeout_sec=1)   
    # # rclpy.spin_once(joint_node1, timeout_sec=1)  # Spin joint_node1 to allow its timer callback to execute

    # # rclpy.spin(heartbeat_node)  # Keep the heartbeat node running   

    # arm_node.destroy_node()
    # joint_node2.destroy_node()
    # joint_node3.destroy_node()
    # joint_node4.destroy_node()
    # system_ready_node.destroy_node() 
    # # joint_node1.destroy_node()  # Destroy joint_node1 after its timer callback has been executed
    # # heartbeat_node.destroy_node()
    # rclpy.shutdown()  
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(arm_node)
    executor.add_node(joint_node2)
    executor.add_node(joint_node3)
    executor.add_node(joint_node4)
    executor.add_node(system_ready_node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()

        arm_node.destroy_node()
        joint_node2.destroy_node()
        joint_node3.destroy_node()
        joint_node4.destroy_node()
        system_ready_node.destroy_node()

    rclpy.shutdown() 



if __name__ == "__main__":
    main()