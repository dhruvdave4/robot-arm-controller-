# Robot Arm Controller

## Overview

Robot Arm Controller is a robotics development project focused on designing and developing a modular robotic arm control system using ROS 2, C++, Python, Linux, and embedded-system technologies. The main objective of this project is to understand and implement the complete software architecture required to control a multi-joint robotic arm, from high-level system management to future hardware and motor integration.

The project is being developed with a modular architecture in which different responsibilities are separated into individual ROS 2 nodes. The system includes an arm controller, individual joint controllers, and a system-level controller responsible for monitoring and coordinating the robot. ROS 2 communication mechanisms such as publishers, subscribers, timers, services, and actions will be used to provide reliable communication between different parts of the system.

## Current Development

The current stage focuses on understanding ROS 2 architecture and communication. Initial development has been performed using Python and `rclpy` to understand nodes, publishers, subscribers, callbacks, timers, and executors. The next development stage is to implement the main robot-arm architecture using C++ and `rclcpp`.

The project will progressively move toward a C++ based ROS 2 architecture because C++ is highly suitable for robotics, performance-sensitive applications, hardware interfaces, and embedded-system integration.

## Planned Development

Future development will include:

* C++ ROS 2 node architecture
* Multi-joint robot controller
* System monitoring and coordination
* ROS 2 services and actions
* Executor and callback-group design
* Robot simulation
* Hardware interface development
* Motor and sensor communication
* Embedded controller integration
* Communication protocols such as UART, SPI, I2C, and CAN
* Testing and debugging
* Documentation and system design

## Technologies

* C / C++
* Python
* ROS 2
* Linux
* Git and GitHub
* Embedded Systems
* Robot Simulation

## Project Structure

```text
robot-arm-controller/
├── cad/
├── docs/
├── firmware/
├── robot_models/
├── ros2_ws/
└── simulation/
```

This project is continuously evolving as the robot-arm architecture, ROS 2 software, embedded interfaces, and hardware-control concepts are developed and tested.
