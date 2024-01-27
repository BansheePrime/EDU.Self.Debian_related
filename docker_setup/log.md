## start container from node latest image, set name and open shell inside container
docker run --name gidra-nodejs -it node /usr/bin/bash

### run as root
apt update
apt install sudo
useradd -m admin
echo -e "123\n123" | passwd admin
usermod -aG sudo admin
su admin