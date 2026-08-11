from setuptools import find_packages, setup

package_name = 'robot_arm_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dhruv',
    maintainer_email='dhruv@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        # 'console_scripts': [ 'arm_node = robot_arm_controller.arm_node:main', 'joint_node2 = robot_arm_controller.joint_node2:main', 'joint_node3 = robot_arm_controller.joint_node3:main', 'joint_node4 = robot_arm_controller.joint_node4:main', 'system_ready_node = robot_arm_controller.system_ready_node:main', 'heartbeat_node = robot_arm_controller.heartbeat_node:main'
        'console_scripts': [ 'arm_node = robot_arm_controller.arm_node:main', 'joint_node2 = robot_arm_controller.joint_node2:main', 'joint_node3 = robot_arm_controller.joint_node3:main', 'joint_node4 = robot_arm_controller.joint_node4:main', 'system_ready_node = robot_arm_controller.system_ready_node:main'

         ],
    },
)
