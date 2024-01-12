# Simulation

# To install Ros2 humble folllow the link below:
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

# To Install Docker:
https://docs.docker.com/engine/install/ubuntu/

Ensure that DOcker container is correctly installed by running
'''python
sudo docker run hello-world
'''
# To build the docker container:
Open the Simulation in Vscode
Navigate to osfr file in terminal and run command "docker compose build"
The Docker container is running with nvidia gpu capabilities, if the system does not have nvidia driver, changes to the docker compose file will need to be made

# Installing gazebo:
https://classic.gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros
# simple_api.py
When the script is run, it allows the user to input the amount of waypoints along with each coordinates in x,y. In addittion if the user presses the 's' key, the robot stops as an emergency stop.
# To build project3:
open terminal and direct towards ros_workspace/src
Then colcon build --symlink-install

To run the urdf in the gazebo run:

# To demonstrate knowledge of waypoint navigaation with capabiility of stopping the robot anytime:
Run:
ros2 launch nav2_bringup tb3_simulation_launch.py headless:=False
This will launch the nav2 basic simulation wiht gazebo. 
Then run the python file called simple_api.py


