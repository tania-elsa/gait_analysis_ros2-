from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'gait_analysis_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),

    ('share/' + package_name,
        ['package.xml']),

    # URDF
    (os.path.join('share', package_name, 'urdf'),
        glob('urdf/*.urdf')),

    # Xacro
    (os.path.join('share', package_name, 'urdf'),
        glob('urdf/*.xacro')),

    # Gazebo
    (os.path.join('share', package_name, 'urdf'),
        glob('urdf/*.gazebo')),

    # ros2_control
    (os.path.join('share', package_name, 'urdf'),
        glob('urdf/*.ros2control')),

    # Meshes
    (os.path.join('share', package_name, 'meshes'),
        glob('meshes/*.stl')),

    (os.path.join('share', package_name, 'meshes'),
        glob('meshes/**/*.stl', recursive=True)),

    # Launch
    (os.path.join('share', package_name, 'launch'),
        glob('launch/*.launch.py')),
    
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stania',
    maintainer_email='stania@todo.todo',
    description='TODO: Package description',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
