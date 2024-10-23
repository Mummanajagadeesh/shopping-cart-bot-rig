from setuptools import find_packages, setup

package_name = 'joycomm'

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
    maintainer='jagadeesh97',
    maintainer_email='jagadeesh97@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "joy_controller = joycomm.joy_controller:main",
            "joy_ctrl_esp32 = joycomm.joy_ctrl_esp32:main"
        ],
    },
)

