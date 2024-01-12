# Simulation

TO install Ros2 humble folllow the link below:
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html

To Install Docker:
https://docs.docker.com/engine/install/ubuntu/

Ensure that DOcker container is correctly installed by running
'''python
sudo docker run hello-world
'''
To build the docker container:
Open the Simulation in Vscode
Navigate to osfr file in terminal and run command "docker compose build"
The Docker container is running with nvidia gpu capabilities, if the system does not have nvidia driver, changes to the docker compose file will need to be made

Installing gazebo:
https://classic.gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros
